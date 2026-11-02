"""Guardas do Susano: deteccao de segredos, dados pessoais e do travessao no momento da escrita.

Usado pelos hooks guarda_conteudo.py (PreToolUse) e guarda_prompt.py (UserPromptSubmit).
Somente biblioteca padrao (Python 3.9+). E a trava de tempo real; a trava final de merge
continua sendo o `scripts/brain.py validate` no CI do repositorio.

Niveis:
- bloquear: segredo, cartao (Luhn), CPF valido, travessao. A escrita e recusada.
- perguntar: telefone e e-mail. A pessoa confirma que e contato profissional necessario.
  Endereco de sistema sem caixa de pessoa (noreply@, no-reply@) e dominios de exemplo nao perguntam.
  Linha com o marcador [PUBLICO] (ou [PÚBLICO]) e contato que o dono decidiu publicar: nao pergunta.
  O marcador nunca libera um bloqueio (segredo, cartao, CPF, travessao).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List

BLOQUEAR = "bloquear"
PERGUNTAR = "perguntar"

# U+2014 gerado com chr(): este arquivo nao contem o proprio caractere.
TRAVESSAO = chr(0x2014)


@dataclass(frozen=True)
class Achado:
    tipo: str
    nivel: str
    linha: int
    trecho: str

    def texto(self) -> str:
        return f"{self.tipo} (linha {self.linha}: {self.trecho})"


def _mascara(valor: str) -> str:
    valor = valor.strip()
    if len(valor) <= 6:
        return "***"
    return valor[:4] + "***"


_SEGREDOS = [
    ("chave Anthropic", r"sk-ant-[A-Za-z0-9_\-]{20,}"),
    ("chave OpenAI", r"(?<![A-Za-z0-9])sk-(?!ant-)(?:proj-|svcacct-)?[A-Za-z0-9_\-]{20,}"),
    ("token GitHub", r"(?<![A-Za-z0-9])(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,}"),
    ("chave AWS", r"(?<![A-Z0-9])(?:AKIA|ASIA)[0-9A-Z]{16}(?![A-Z0-9])"),
    ("chave Google", r"AIza[0-9A-Za-z_\-]{35}"),
    ("token Slack", r"xox[abposr]-[A-Za-z0-9\-]{10,}"),
    ("token Meta", r"(?<![A-Za-z0-9])EAA[A-Za-z0-9]{30,}"),
    ("chave Stripe", r"(?:sk|rk)_live_[A-Za-z0-9]{16,}"),
    ("token HubSpot", r"pat-(?:na1|na2|eu1|ap1)-[0-9a-f\-]{30,}"),
    ("chave privada", "-----BEGIN " + r"(?:[A-Z0-9]+ )*PRIVATE KEY-----"),
    ("JWT", r"eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),
    ("URL com senha", r"[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s@]{3,}@[^\s/]+"),
    (
        "credencial atribuida",
        r"(?i)\b(?:senha|password|passwd|api[_-]?key|client[_-]?secret|secret[_-]?key|access[_-]?token)"
        r"\s*[:=]\s*['\"]?(?![$<{*\[(])[^\s'\"]{8,}",
    ),
]
_SEGREDOS_RX = [(tipo, re.compile(padrao)) for tipo, padrao in _SEGREDOS]

_CARTAO = re.compile(r"(?<![\w.])(?:\d[ \-]?){12,18}\d(?![\w])")
_CPF_FMT = re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)")
_CPF_CRU = re.compile(r"(?i)\bcpf\b[^\d\n]{0,20}(\d{11})(?!\d)")
_TELEFONE = re.compile(
    r"(?:\+55\s?)?\(\d{2}\)\s?9?\d{4}[-\s]?\d{4}(?!\d)"
    r"|\+55\s?\d{2}\s?9?\d{4}[-\s]?\d{4}(?!\d)"
    r"|(?<![\d\-])\d{2}\s9\d{4}-\d{4}(?!\d)"
)
_EMAIL = re.compile(r"(?<![\w.+\-])[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
_EMAIL_PERMITIDOS = ("example.com", "example.org", "exemplo.com", "exemplo.com.br", "users.noreply.github.com")
_EMAIL_SEM_CAIXA = ("noreply", "no-reply", "donotreply", "do-not-reply")
_PUBLICO = ("[PUBLICO]", "[P\u00daBLICO]")


def luhn_valido(digitos: str) -> bool:
    total = 0
    for i, ch in enumerate(reversed(digitos)):
        n = int(ch)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def _parece_cartao(d: str) -> bool:
    if not 13 <= len(d) <= 19:
        return False
    if d[0] not in "3456":
        return False
    if len(set(d)) == 1:
        return False
    return luhn_valido(d)


def cpf_valido(valor: str) -> bool:
    d = re.sub(r"\D", "", valor)
    if len(d) != 11 or d == d[0] * 11:
        return False
    for pos in (9, 10):
        soma = sum(int(d[i]) * ((pos + 1) - i) for i in range(pos))
        dig = (soma * 10) % 11
        if dig == 10:
            dig = 0
        if dig != int(d[pos]):
            return False
    return True


def analisar(texto: str, caminho: str = "") -> List[Achado]:
    """Achados de um texto. `caminho` fica disponivel para regras futuras por pasta."""
    achados: List[Achado] = []
    linhas = texto.splitlines() or [texto]
    for i, linha in enumerate(linhas, start=1):
        for tipo, rx in _SEGREDOS_RX:
            for m in rx.finditer(linha):
                achados.append(Achado(tipo, BLOQUEAR, i, _mascara(m.group(0))))
        for m in _CARTAO.finditer(linha):
            digitos = re.sub(r"\D", "", m.group(0))
            if _parece_cartao(digitos):
                achados.append(Achado("numero de cartao", BLOQUEAR, i, _mascara(digitos)))
        for m in _CPF_FMT.finditer(linha):
            if cpf_valido(m.group(0)):
                achados.append(Achado("CPF", BLOQUEAR, i, _mascara(m.group(0))))
        for m in _CPF_CRU.finditer(linha):
            if cpf_valido(m.group(1)):
                achados.append(Achado("CPF", BLOQUEAR, i, _mascara(m.group(1))))
        publico = any(marca in linha for marca in _PUBLICO)
        if not publico:
            for m in _TELEFONE.finditer(linha):
                achados.append(Achado("telefone", PERGUNTAR, i, _mascara(m.group(0))))
            for m in _EMAIL.finditer(linha):
                local, dominio = m.group(0).lower().rsplit("@", 1)
                if local in _EMAIL_SEM_CAIXA:
                    continue  # endereço de sistema (noreply), não é de pessoa
                if not any(dominio == d or dominio.endswith("." + d) for d in _EMAIL_PERMITIDOS):
                    achados.append(Achado("e-mail", PERGUNTAR, i, _mascara(m.group(0))))
        if TRAVESSAO in linha:
            achados.append(Achado("travessao (troque por virgula, dois-pontos ou seta)", BLOQUEAR, i, "U+2014"))
    return achados


def bloqueios(achados: List[Achado]) -> List[Achado]:
    return [a for a in achados if a.nivel == BLOQUEAR]


def avisos(achados: List[Achado]) -> List[Achado]:
    return [a for a in achados if a.nivel == PERGUNTAR]
