---
id: UXA-007
title: Wireframe de Baixa Fidelidade do Detalhe de Oportunidade
status: draft
version: 0.2.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-26
parent: UXA-005
related:
  - UXA-002
  - UXA-004
  - UXA-006
  - UXA-009
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-OA-LIFECYCLE-001
  - PAS-001-OA-VIEW-001
normative: false
---

# Wireframe de Baixa Fidelidade do Detalhe de Oportunidade (identificador UXA-007)

O identificador técnico `UXA-007` serve somente para rastreabilidade. O nome de leitura desta superfície é **Detalhe de Oportunidade**.

## 1. Pergunta da superfície

> **O que preciso compreender sobre esta oportunidade antes de decidir se desejo salvá-la, compará-la ou iniciar um processo?**

A superfície deverá explicar valor, condições, limites, relevância, elegibilidade, fonte e relação comercial antes de enfatizar conversão.

## 2. Wireframe

![Wireframe móvel do Detalhe de Oportunidade](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg)

[Visualizar o arquivo gráfico vetorial escalável (SVG)](../assets/wireframes/uxa-007-opportunity-detail-mobile.svg)

## 3. Hierarquia proposta

| Ordem | Bloco | Responsabilidade |
|---:|---|---|
| 1 | identidade e preço | identificar oportunidade, responsável, custo e validade |
| 2 | relevância explicada | demonstrar por que pode apoiar a jornada atual |
| 3 | informações principais | mostrar disponibilidade, modalidade, horário e acessibilidade |
| 4 | elegibilidade | distinguir estimativa da decisão final de terceiro |
| 5 | Organização responsável | permitir avaliar fonte, identidade e suporte |
| 6 | transparência comercial | revelar comissão, patrocínio ou outra relação material |
| 7 | ações persistentes | iniciar, salvar ou localizar sem ocultar alternativas |

## 4. Identidade, custo e temporalidade

O topo deverá apresentar:

- tipo da oportunidade;
- modalidade;
- estado de disponibilidade;
- título;
- Organização ou Coletivo responsável;
- preço principal;
- custo total conhecido ou estimado;
- número de parcelas ou recorrência;
- validade do preço;
- prazo material.

### 4.1 O que significa validade do preço

**Validade do preço** é a data ou o período até o qual a Organização declara que o valor informado permanece vigente para uma nova inscrição, contratação ou compra.

Exemplo:

> R$ 79,90 por mês, válido para novas inscrições realizadas até 31/08/2026.

A validade do preço não representa:

- duração do serviço;
- vencimento da parcela;
- prazo de inscrição;
- período do contrato;
- prazo de cancelamento;
- prazo de reembolso.

Após a validade, o preço deverá ser confirmado novamente. Caso o valor mude durante um processo já iniciado, a nova condição deverá ser apresentada para confirmação consciente antes da continuidade.

Regras adicionais:

- `grátis` não poderá ser utilizado quando existirem custos obrigatórios;
- `a partir de` deverá indicar o que pode alterar o valor;
- preço sob consulta deverá limitar a apresentação e comparação;
- mudança de preço após processo iniciado deverá produzir nova confirmação.

## 5. Por que pode ser relevante

A explicação resumida poderá utilizar:

- objetivo confirmado;
- Próximo Passo;
- preferência declarada;
- busca realizada;
- localização autorizada;
- disponibilidade compatível;
- necessidade explicitamente informada.

O participante deverá poder:

- abrir `Por que estou vendo isto?`;
- ajustar relevância;
- impedir uso de determinada informação;
- corrigir contexto;
- ocultar categoria ou fonte;
- contestar a avaliação.

Inferência sensível não deverá ser revelada desnecessariamente.

## 6. Informações principais

O primeiro nível deverá permitir decisão inicial sem leitura de todo o documento.

Informações propostas:

- disponibilidade;
- modalidade;
- data e horário;
- local ou abrangência;
- acessibilidade;
- requisitos principais;
- cancelamento;
- última atualização.

Detalhes, políticas e documentos deverão permanecer em níveis progressivos.

## 7. Elegibilidade

A tela deverá distinguir:

- não avaliada;
- possivelmente elegível;
- elegível;
- elegível com condição;
- exige verificação;
- possivelmente não elegível;
- não elegível;
- contestada.

Quando a decisão final pertencer a terceiro, isso deverá ser declarado. A Guivos não poderá apresentar probabilidade como aprovação.

## 8. Organização responsável

O bloco deverá permitir verificar:

- nome e identidade;
- estado de verificação;
- unidade responsável;
- canal de suporte;
- atualização e histórico relevantes;
- outras oportunidades;
- perfil institucional;
- meios de contestação ou denúncia.

Verificação institucional não representa garantia de resultado.

## 9. Transparência comercial

A tela deverá declarar, quando aplicável:

- comissão;
- afiliação;
- patrocínio;
- exclusividade;
- promoção paga;
- participação da Guivos na receita;
- financiamento;
- relação indireta relevante.

A declaração deverá informar que a relação comercial não aumenta relevância funcional.

## 10. Ações persistentes

A barra inferior do wireframe contém:

- ação principal: iniciar inscrição;
- ação secundária: salvar;
- ação contextual: abrir no mapa.

Outras ações possíveis:

- comparar;
- compartilhar;
- declarar interesse;
- ocultar;
- mostrar menos como isto;
- contestar informação;
- denunciar;
- entrar em lista de espera;
- solicitar aviso de abertura futura.

O início da inscrição deverá abrir confirmação de executor, compartilhamento de dados, custos, destinatário e reversibilidade.

## 11. Estados alternativos que ainda exigem wireframe

- oportunidade gratuita com custos externos;
- preço variável ou sob consulta;
- lista de espera;
- abertura futura;
- elegibilidade insuficiente;
- risco elevado;
- oportunidade patrocinada;
- oportunidade criada por Coletivo;
- oportunidade presencial com localização protegida;
- oportunidade expirada;
- informação contestada;
- falha de sincronização com fonte externa.

## 12. Perguntas para validação humana

1. O preço deve aparecer antes da explicação de relevância?
2. O custo total estimado está suficientemente destacado?
3. A validade do preço está clara e não se confunde com prazo de inscrição ou duração do serviço?
4. A diferença entre `possivelmente elegível` e `elegível` é compreensível?
5. A relação comercial está clara sem dominar a tela?
6. O perfil da Organização precisa de maior destaque?
7. `Iniciar inscrição` é a ação principal correta para todos os tipos?
8. Salvar e comparar deveriam ocupar a mesma hierarquia?
9. O participante compreende que a Guivos não garante disponibilidade ou resultado?

## 13. Critérios de aceite do wireframe

O wireframe poderá avançar quando:

- preço e custo total forem compreendidos;
- validade do preço, prazo de inscrição e duração do serviço forem distinguidos;
- prazo e disponibilidade não forem confundidos;
- relevância for explicável e ajustável;
- elegibilidade não for interpretada como aprovação;
- fonte e relação comercial forem identificáveis;
- ação principal não ocultar condições ou riscos;
- o participante puder desistir, salvar ou comparar sem pressão;
- a leitura não depender do conhecimento do identificador técnico.
