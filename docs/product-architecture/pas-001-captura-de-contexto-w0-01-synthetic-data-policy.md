---
id: PAS-001-CC-W0-01-SYNTHETIC-DATA-001
title: Política de Dados Sintéticos do W0-01
status: draft
version: 0.1.0
owner: Guivos
last_updated: 2026-07-20
normative: true
parent: PAS-001-CC-W0-01-CHARTER-001
related:
  - PAS-001-CC-W0-ENV-001
  - PAS-001-CC-W0-RISK-001
  - PAS-001-CC-W0-01-PIPELINE-001
---

# PAS-001-CC-W0-01-SYNTHETIC-DATA-001 — Política de Dados Sintéticos

## 1. Regra principal

Nenhum dado pessoal real, dado de pesquisa, conteúdo de participante ou material de terceiro poderá ser usado no W0-01, no repositório de implementação ou nos ambientes Local e Test.

## 2. Definição

Dado sintético válido é produzido especificamente para teste e não deriva de registro real de forma reidentificável.

Ele deverá ser:

- fictício;
- explicitamente marcado como sintético;
- reproduzível por seed ou gerador versionado;
- descartável;
- independente de bases reais;
- adequado ao cenário de teste;
- revisável;
- livre de segredo;
- incapaz de contactar pessoa real.

## 3. Proibições

É proibido:

- copiar base real e remover apenas nomes;
- usar CPF, CNPJ, telefone ou e-mail real;
- importar respostas da VAL-002;
- copiar conversa, documento, foto, vídeo ou áudio pessoal;
- utilizar produção como fonte de fixtures;
- usar dado anonimizado sem avaliação formal específica;
- gerar identificador que possa pertencer a uma pessoa real;
- incluir endereço, coordenada ou combinação reidentificável;
- manter dado suspeito enquanto se decide sua origem.

Dado de origem incerta deverá ser tratado como real e removido do fluxo.

## 4. Padrões permitidos

| Categoria | Padrão |
|---|---|
| identidade | UUID gerado para teste |
| nome | nome fictício de catálogo controlado |
| e-mail | domínio `.invalid` |
| telefone | faixa não roteável ou máscara deliberadamente inválida |
| documento | formato propositalmente inválido e marcado |
| endereço | localidade fictícia ou genérica |
| data | cenário artificial |
| mídia | arquivo criado exclusivamente para teste |
| texto | conteúdo inventado e sem referência a pessoa real |
| organização | entidade fictícia claramente identificada |

## 5. Catálogo mínimo de cenários

O catálogo deverá cobrir:

- participante individual;
- ator diferente do participante;
- representação válida, expirada e revogada;
- menor e terceiro;
- dispositivo compartilhado;
- sessão abandonada;
- hipótese, interpretação e fato confirmado;
- confirmação, rejeição e contestação;
- autorização válida, expirada e revogada;
- correção simples e encadeada;
- retenção temporária e residual;
- consumidor online, atrasado, offline e comprometido;
- mensagem duplicada, incompatível e fora de ordem;
- replay;
- conteúdo textual;
- documento sintético;
- uma mídia sintética mínima;
- tentativa de prompt injection fictícia;
- tentativa de enumeração;
- segredo canário não funcional.

## 6. Estrutura do catálogo

```yaml
fixture_id: string
scenario_ids: string[]
classification: synthetic
seed: string
generator_version: string
created_at: datetime
owner: string
reviewer: string
contains_media: boolean
expected_behaviors: string[]
prohibited_uses: string[]
integrity_hash: string
```

## 7. Geração e revisão

- geradores deverão estar versionados;
- mesma seed deverá reproduzir o conjunto esperado;
- mudança material exige nova versão;
- fixture manual deverá registrar autor e justificativa;
- Security & Privacy Owner revisará padrões de risco;
- Quality & Evidence Owner validará cobertura e reprodução;
- fixtures não deverão representar grupos reais de forma discriminatória ou estigmatizante;
- cenários adversariais deverão ser limitados à finalidade de teste.

## 8. Varredura automatizada

O pipeline deverá verificar, no mínimo:

- padrões de CPF/CNPJ potencialmente válidos;
- e-mails fora de domínios aprovados;
- telefones potencialmente roteáveis;
- chaves, tokens e segredos;
- arquivos binários não catalogados;
- metadados EXIF ou equivalentes;
- nomes de clientes, parceiros ou participantes conhecidos;
- referências à VAL-002 ou bases de pesquisa como fonte de fixture;
- payload sem marcação `synthetic`.

A varredura não substitui revisão humana.

## 9. Mídia sintética

Toda mídia deverá:

- ser criada para teste;
- não conter pessoa real identificável sem autorização específica futura;
- remover metadados desnecessários;
- possuir hash;
- registrar tipo, tamanho e origem;
- ser limitada ao menor conjunto necessário;
- permanecer fora de publicação pública;
- passar pelo mesmo fluxo de quarentena planejado para a Onda 0.

## 10. Incidente de dado real

Ao detectar dado real ou suspeito:

1. interromper o fluxo (`Stop-L3` quando houver exposição material);
2. bloquear acesso ao artefato;
3. remover de branches e artefatos ativos sem apagar a trilha mínima do incidente;
4. revogar credenciais quando aplicável;
5. registrar `W0-R-020`;
6. avaliar necessidade de limpeza do histórico;
7. revalidar scanners e controles;
8. produzir evidência da contenção;
9. obter autorização para retomada.

## 11. Relação com evidências

Evidência não deverá conter o conteúdo completo da fixture quando um hash, referência ou resultado agregado for suficiente.

Todo manifesto deverá registrar:

- dataset sintético;
- versão do gerador;
- seed;
- hash;
- ambiente;
- finalidade;
- owner;
- aprovação.

## 12. Critérios de aceite

A política estará executada quando:

- catálogo mínimo existir;
- fixtures forem versionadas e reproduzíveis;
- scanner estiver obrigatório;
- teste deliberado de dado proibido for bloqueado;
- mídia estiver catalogada;
- nenhum dado da VAL-002 for utilizado;
- owners aprovarem o conjunto;
- EV-017 registrar política e resultado.

## 13. Limites

Esta política não autoriza dado anonimizado, pseudonimizado ou real. Qualquer ensaio com pessoa exige decisão posterior, finalidade específica, base apropriada e controles adicionais.
