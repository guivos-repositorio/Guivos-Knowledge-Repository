---
id: UXA-064
title: Wireframes Móveis da Revisão e Solicitação de Participação em Coletivos
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-005
depends_on:
  - UXA-001
  - UXA-003
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-014
  - UXA-019
  - UXA-056
  - UXA-058
  - UXA-059
  - UXA-062
  - UXA-063
related:
  - UXA-065
  - UXA-066
  - M7.67
normative: false
---

# Wireframes Móveis da Revisão e Solicitação de Participação em Coletivos

## 1. Finalidade

Este documento governa a quarta referência P0A definida pela UXA-059: a revisão e a Solicitação de Participação móvel.

A versão 0.2.0 incorpora as reformulações validadas pela UXA-065. A família permite que uma pessoa:

- compreenda o significado do vínculo antes da ação;
- diferencie entrada aberta, aprovação e convite protegido;
- revise regras, dados, autoridade e consequências;
- confirme conscientemente sem opções previamente selecionadas;
- cancele antes do envio;
- compreenda o resultado imediato sem confundi-lo com acompanhamento contínuo.

Os artefatos permanecem wireframes móveis de baixa fidelidade. Não representam design final, base jurídica, tecnologia de consentimento, protótipo ou Engenharia de Produto.

## 2. Continuidade validada

```text
Perfil Público validado
→ revisar vínculo, regras, dados e consequências
→ confirmar entrada aberta ou enviar solicitação
→ receber confirmação imediata ou comprovante transitório
→ futura Solicitação Pendente, mediante pacote e autorização separados
```

Para convite protegido:

```text
apresentação protegida validada
→ revisar remetente, autoridade, motivo, validade e alegações
→ revisar ou contestar dados mínimos
→ recusar, denunciar ou enviar dados mínimos para análise
```

## 3. Artefatos

| Estado | Arquivo | Situação |
|---|---|---|
| revisão para entrada aberta | `uxa-064-collective-participation-open-entry-review-mobile.svg` | reformulado e validado |
| entrada aberta confirmada | `uxa-064-collective-participation-open-entry-confirmed-mobile.svg` | reformulado e validado |
| revisão mediante aprovação | `uxa-064-collective-participation-approval-request-review-mobile.svg` | reformulado e validado |
| comprovante transitório | `uxa-064-collective-participation-approval-request-receipt-mobile.svg` | reformulado e validado |
| revisão protegida de convite | `uxa-064-collective-participation-protected-invite-review-mobile.svg` | reformulado e validado |

Os cinco SVGs possuem 390 × 844 pixels, `title`, `desc`, estados textuais e decisões que não dependem apenas de cor.

## 4. Hierarquia comum

```text
retorno ou cancelamento
→ Coletivo e modelo de entrada
→ significado do vínculo ou da solicitação
→ dados enviados e dados protegidos
→ autoridade, prazo e consequência
→ permissões separadas
→ confirmações inicialmente vazias
→ ação principal condicionada
→ cancelamento sem envio
```

Estados protegidos acrescentam remetente, motivo, validade, alegação não verificada, confidencialidade condicionada e denúncia.

## 5. Entrada aberta

A entrada aberta exige confirmação consciente mesmo sem análise do responsável.

A revisão informa que a participação:

- cria vínculo de participante somente após confirmação;
- permite acesso interno conforme permissões;
- não cria função, autoridade ou obrigação de presença;
- não autoriza contato privado ou marketing;
- começa sem aparição na lista nominal;
- permite mudança posterior de visibilidade em controle próprio;
- permite pausa ou saída conforme regras e consequências revisadas.

A ação `Confirmar participação` permanece indisponível enquanto as confirmações necessárias estiverem vazias.

## 6. Confirmação da entrada aberta

A confirmação demonstra:

- vínculo ativo e horário do registro;
- acesso ao ambiente interno existente;
- visibilidade inicial como `não aparecer`;
- notificações não ativadas automaticamente;
- contato privado não autorizado;
- ausência de papel e autoridade automáticos;
- identificador do registro e possibilidade de salvar a confirmação;
- retorno ao Perfil Público sem antecipar uma superfície de gestão pessoal.

Pausa e saída não são executadas nesta tela. Uma superfície futura deverá explicar consequências antes da confirmação.

## 7. Entrada mediante aprovação

Antes do envio, a revisão apresenta:

- ausência de vínculo e acesso interno;
- dados declarados editáveis;
- responsável e papel autorizado;
- prazo estimado sem promessa;
- cancelamento atual sem compartilhamento;
- cancelamento posterior reservado à futura Solicitação Pendente;
- Organização apoiadora sem recebimento automático;
- acessibilidade como recurso separado das confirmações obrigatórias.

A ação `Enviar solicitação` não equivale a aprovação, participação ou presença em lista nominal.

## 8. Comprovante transitório

O comprovante registra somente:

- recebimento do envio;
- ausência de vínculo;
- dados enviados;
- responsável e prazo estimado;
- identificador do comprovante;
- eventos futuros possíveis.

Ele não cria ação para uma superfície inexistente. O acompanhamento contínuo aparece como não materializado e permanece reservado à UXA-066.

O comprovante não materializa fila, histórico contínuo, informação adicional, decisão, contestação ou cancelamento operacional.

## 9. Convite protegido

A revisão protegida apresenta:

- remetente, autoridade, motivo e validade;
- acesso individual e não encaminhável;
- alegação do remetente identificada como não verificada;
- possibilidade de revisar ou contestar a alegação antes do envio;
- dados mínimos e dados protegidos;
- confidencialidade como condição explicada, não garantia absoluta;
- recusa e denúncia sem penalidade automática;
- ausência de vínculo, acesso ou visibilidade automática.

A ação `Enviar dados mínimos para análise` inicia análise especializada e não ativa participação.

## 10. Dados e permissões

Poderão ser enviados, conforme necessidade legítima e revisão:

- nome de exibição;
- identificador da participação, solicitação ou convite;
- confirmações registradas;
- data e horário;
- experiência e disponibilidade declaradas;
- respostas necessárias a processo protegido;
- preferência inicial de visibilidade.

Não serão enviados automaticamente:

- telefone ou e-mail pessoal;
- endereço ou localização exata;
- conteúdo protegido da Jornada;
- outros Coletivos;
- contatos pessoais;
- histórico comercial;
- denúncias ou recusas anteriores;
- informações sensíveis não relacionadas;
- inferências não autorizadas.

Participação não concede automaticamente lista pública, perfil público, notificações, mensagem privada, comunicação comercial, função, disponibilidade ou autoridade.

## 11. Confirmações

As caixas começam vazias e cobrem somente elementos necessários à decisão apresentada.

A redação utiliza `Confirmo que desejo enviar` em vez de declarar uma base jurídica específica. A UXA-064 e a UXA-065 não definem consentimento técnico, retenção ou fundamento jurídico de produção.

Leitura, rolagem, silêncio, acompanhamento ou abertura do perfil não equivalem a confirmação.

## 12. Acessibilidade

Acessibilidade permanece disponível como recurso próprio e não como condição obrigatória de participação.

Os artefatos utilizam:

- títulos e descrições acessíveis;
- ações nomeadas;
- estados textuais;
- ordem linear;
- caixas vazias visíveis;
- consequências explícitas;
- ausência de significado dependente apenas de cor.

Teste com tecnologia assistiva e conformidade técnica final permanecem posteriores.

## 13. Cobertura após validação

| Família | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Coletivos — descoberta e busca | 5 | 5 | 0 |
| Coletivos — Perfil Público | 4 | 4 | 0 |
| Coletivos — revisão e solicitação | 5 | 5 | 0 |
| Opportunity Boost | 46 | 36 | 10 |

Total de Coletivos: 14 SVGs materializados e 14 validados.

## 14. Limites

Não são iniciados:

- Solicitação Pendente;
- informação adicional;
- recusa, expiração ou contestação após envio;
- cancelamento operacional após envio;
- gestão de solicitações;
- `Meus Coletivos`;
- Central de Atualizações;
- reformulação do Início do Participante;
- gestão do responsável;
- política jurídica;
- protótipo, teste ou identidade visual;
- Engenharia de Produto.

## 15. Próxima transição recomendada

**UXA-066 — Wireframes Móveis da Solicitação Pendente em Coletivos.**

A UXA-066 dependerá de autorização separada e não é iniciada por esta validação.
