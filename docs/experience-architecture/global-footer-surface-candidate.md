---
id: GKR-UX-GLOBAL-FOOTER-SURFACE-001
title: Superfície Transversal — Rodapé Global da Guivos
status: proposed
version: 0.2.1
owner: Experience Architecture
last_updated: 2026-10-16
normative: false
maturity: design_candidate
depends_on:
  - GKR-STATE-001
  - GKR-UX-HOMES-DESIGN-DELIVERY-001
  - GKR-UX-HOMES-DESIGN-HANDOFF-001
  - GKR-UX-HOME-MASTER-001
  - GKR-UX-GLOBAL-FOOTER-001
---

# Rodapé Global — superfície transversal da Guivos

> **Superfície de projeto candidata.** Este documento define uma arquitetura editorial e de experiência a ser validada para o rodapé de todas as Homes públicas e páginas elegíveis da Guivos. Não substitui a autoridade de cada produto, não aprova novos destinos, não cria páginas jurídicas e não equivale à implementação.

## 0. Precedência sobre a referência visual validada (reconciliação de 16/10/2026)

**Autoridade corrente já existente na `main`:** [Rodapé Institucional Global — Referência Validada](global-institutional-footer.md), `GKR-UX-GLOBAL-FOOTER-001 v1.0.0`, `status: validated-visual-reference`, `normative: true`, baseada na composição aprovada pelo fundador em 14/10/2026. Esta PR não é autorização para redesenhar a composição, suprimir conteúdo aprovado ou substituir seus textos. Os módulos R01–R06 abaixo são **um mapa lógico de responsabilidades** para implementação transversal, e não um novo copywriting, wireframe de substituição ou revisão do Design validado.

**Elementos já fixados e que deverão ser preservados em qualquer composição conforme a referência:**
- assinatura de marca: **Possibility, lived.**;
- posicionamento: **Conectamos pessoas a possibilidades que podem transformar suas vidas.**;
- seções: **Explore o ecossistema**, **Guivos**, **Ajuda** e **Receba novidades**;
- descrição do bloco de novidades: **Acompanhe novas oportunidades, experiências e possibilidades que surgem e evoluem no ecossistema Guivos.**;
- chamada final: **Descubra. Viva. Evolua.**, com destaque cromático em **Evolua.**;
- fundo `#FFFFFF`, paleta oficial, família Goldplay conforme autoridade tipográfica e respiros da referência visual;
- navegação institucional e jurídica, campo voluntário de novidades e canais sociais conforme a referência, **sem presumir destinos ou integração ativos**.

**Complementos em exame neste documento:** `Mapa do Ecossistema` como responsabilidade de navegação referida pela autoridade da Home, aplicação em outras Homes, estados responsivos, ajuda e variações por contexto. O item `Mapa do Ecossistema` não substitui os grupos/itens aprovados no rodapé nem vira link clicável sem destino autorizado. Para qualquer diferença entre o wireframe lógico da §4 e a referência validada, **prevalece a referência validada**, sujeita às autoridades legais, de marca e acessibilidade pertinentes.

**Lacunas de implantação:** a referência corrente não comprova ativo vetorial, links, captação de novidades, publicação, mobile ou integração. O botão/QR de obtenção do app, se proposto em iteração visual posterior, exige registro de conteúdo e destino oficiais antes de integrar a superfície de produção; não presumir que já esteja contemplado pela referência normativa de 14/10. Nenhuma implementação é autorizada por esta reconciliação.

## 1. Papel e princípios

O Rodapé é uma **superfície transversal de orientação, confiança, continuidade e compreensão do ecossistema**, não uma nona Home, uma vitrine extensa de serviços ou um funil compulsório. Sua função é permitir que a Pessoa, Organização ou Coletivo compreenda a Guivos, transite entre superfícies, encontre assistência e acesse informações institucionais e legais verificadas.

- Preservar sensação de ecossistema único, global e territorialmente relevante, sem alegar presença efetiva em países não atendidos.
- Respeitar a liberdade criativa de Design definida pelas autoridades comuns do GKR; esta especificação fixa **funções, agrupamentos, prioridades e limites**, não grade visual, cor, dimensão ou tecnologia.
- Manter consistência estrutural nas oito Homes e páginas internas, com adaptação contextual limitada e rastreável.
- Não antecipar acesso, serviço, recurso social, programa ou página inexistente.
- Preservar a autonomia de navegação e o acesso por teclado, leitura assistiva e dispositivos móveis.

## 2. Estrutura conceitual da superfície

### R01 — Identidade e continuidade

Identidade Guivos, frase curta de posicionamento vinculada ao significado institucional corrente e, **quando adequado ao contexto e autoridade de marca**, assinatura `Possibility, lived.`. Uma mensagem de encerramento não deve substituir o conteúdo narrativo próprio de cada Home.

### R02 — Explore o ecossistema

Área de orientação para os destinos publicamente disponíveis do ecossistema. Candidatos à arquitetura de informação:

- Pessoa e Journey;
- Organizações e Coletivos;
- Mall;
- Travel;
- Business;
- Media;
- Intelligence;
- Ads.

**Regra de presença:** destino só vira link clicável quando URL, finalidade pública e disponibilidade real forem confirmadas. Para superfícies ainda sem página, não usar `#`, links quebrados nem simular lançamento. A relação entre nome de produto, navegação e disponibilidade não autoriza promessa operacional.

### R03 — Mapa do Ecossistema — item obrigatório

**Obrigatório no rodapé:** link textual com nome exato **`Mapa do Ecossistema`**, conforme seção 31 de `GKR-UX-HOME-MASTER-001 v1.0.8`.

O destino, conteúdo e comportamento da futura página **não estão definidos por esta seção**. Antes de ativar o link em produção, resolver URL e arquitetura dessa página por decisão própria. Durante prototipação, o componente pode apresentar estado explicitamente rotulado como demonstração e não deve navegar a destino fictício.

### R04 — Sobre a Guivos

Entrada institucional de entendimento da plataforma, propósito, marca e informações corporativas que estiverem publicadas e aprovadas. A existência de `Sobre`, `Carreiras`, `Imprensa`, `Contato` ou redes sociais é **candidata**, não um inventário de páginas já existentes.

### R05 — Ajuda, confiança e direitos

Acesso simples às rotas efetivamente disponibilizadas de suporte, acessibilidade, privacidade, termos, preferências e canais de reporte. Não inventar canais de suporte, garantias legais, promessas de resposta, telefones, endereços ou contatos.

Os links legais definitivos, jurisdição, entidade editorial, cookies e meios de exercer direitos exigem validação por Legal/Privacidade e disponibilidade real.

### R05A — Receba novidades — função preservada da referência aprovada

O bloco **Receba novidades** é parte do rodapé validado em `GKR-UX-GLOBAL-FOOTER-001`, não uma opção editorial a ser omitida pelo wireframe lógico desta PR. Deve preservar título, descrição oficial, campo de e-mail, botão de envio e canais sociais conforme a referência, com adaptação responsiva sem exclusão de função.

Esse bloco é **distinto** de Ajuda e da faixa institucional inferior. A presença visual aprovada não comprova captação real, consentimento, integração, assinatura concluída, destinos ou contas oficiais das redes. Não ativar o formulário nem links sem validação de finalidade, privacidade e comportamento.

A designação R05A é **submódulo editorial desta proposta**, não ID de superfície nem alteração de `GKR-SURF` ou `GKR-TRN`.

### R06 — Faixa institucional inferior

Conjunto de informações factuais e revisadas que podem incluir identificação corporativa apropriada, direitos de marca, ano, políticas e controles de idioma/região quando estes existirem e forem operacionais. Não exibir país, moeda, seletor, número de CNPJ, símbolo de certificação ou texto de conformidade como adorno ou suposição.

## 3. Tratamento por tipo de página

| Superfície | Aplicação do rodapé |
|---|---|
| Home Pessoa | Completo, após a narrativa e o Movimento 11, sem repetir nem enfraquecer o CTA da Home |
| Home Organizações e Coletivos | Mesmo esqueleto, sem insinuar que selos pendentes estão concedidos |
| Homes Mall e Travel | Mesmo esqueleto; não prometer liquidação, parceiros, estoque ou disponibilidade não contratados |
| Homes Business, Media, Intelligence e Ads | Mesma arquitetura; não transformar itens de navegação em claims de operação |
| Páginas públicas internas | Rodapé completo ou condensado conforme extensão, mantendo `Mapa do Ecossistema` quando o contexto permitir |
| Formulários e fluxos autenticados sensíveis | Variante compacta de confiança e links legais, sem distrações e sem vazamento de estado privado; requisitos próprios devem ser validados |
| Telas de erro e indisponibilidade | Acesso mínimo a ajuda verificada, navegação e políticas quando possível |

A variação contextual altera **densidade e prioridade**, nunca o conteúdo normativo ou a existência de produtos.

## 4. Wireframe lógico — não visual final

```text
┌────────────────────────────────────────────────────────────────────┐
│ GUIVOS          Explore o ecossistema  Sobre  Ajuda  Receba novidades│
│ Posicionamento Destinos ativos        Guivos Apoio  E-mail / canais│
│                 Mapa do Ecossistema (destino a validar)             │
├────────────────────────────────────────────────────────────────────┤
│ Identificação factual  •  Privacidade/Termos aprovados  •  Controles│
└────────────────────────────────────────────────────────────────────┘
```

**Mobile:** módulos em sequência sem colunas comprimidas; agrupamentos expansíveis são opcionais, desde que nomeados e operáveis por teclado, sem ocultar links legais essenciais. **Desktop:** design pode usar distribuição em colunas, hierarquia editorial e presença imagética discreta. **Acessibilidade:** landmark de rodapé, títulos, links com propósito identificável, foco visível, contraste, leitura linear, movimento reduzido e alvos de toque adequados.

## 5. Arquitetura de dados e implementação

- **Única fonte de configuração de links**, com `id`, rótulo, finalidade, rota absoluta/interna, idioma, mercado, `available`, `approved` e versão de origem. Não inferir publicação a partir da existência de um Master.
- **Componente compartilhado** para todas as Homes, evitando oito rodapés divergentes; variações `full`, `compact` e `minimal` somente quando justificadas por contexto.
- Nenhum link deve existir funcionalmente sem URL validada; navegação externa deve identificar destino e observar boas práticas de segurança.
- Idioma e região devem refletir suporte real, não dropdowns demonstrativos apresentados como funcionalidade ativa.
- Pode usar fotografia, iconografia e visualização, mas os elementos não podem eclipsar navegação e informações de confiança.

## 6. Gates e critérios de aceite

| Gate | Necessário para declarar concluído |
|---|---|
| FTR-01 | Ratificação humana da arquitetura de informação e módulos |
| FTR-02 | Destinos e URLs ativas verificadas, sobretudo `Mapa do Ecossistema` |
| FTR-03 | Revisão Brand e coerência das oito Homes |
| FTR-04 | Revisão Legal/Privacidade de elementos legais e institucionais |
| FTR-05 | Design responsivo e validação de acessibilidade, inclusive teclado/leitor de tela |
| FTR-06 | Implementação de componente compartilhado e cobertura de rotas públicas elegíveis |
| FTR-07 | Testes de links, estados indisponíveis, mobile, regressão e navegação assistiva |
| FTR-08 | Aprovação de publicação e evidência de deploy real |

**Estado inicial:** `FTR-01..08 = NOT_ADJUDICATED`. A estrutura é uma proposta documentada para deliberação, não autorização de implantação ou anúncio de disponibilidade.

## 7. Fronteiras com trabalhos em andamento

- **Gráfico Vivo:** permanece parte da experiência e narrativa específica, não métrica de rodapé nem painel de contadores.
- **Selos:** não usar selo de reconhecimento como rodapé institucional ou sinal de certificação.
- **Pontos:** não incluir saldo, valor, câmbio ou resgate no rodapé público.
- **Replit:** executar implantação apenas após compatibilização de rotas reais e decisão de Design, sem interromper atualização atual de Organizações e Coletivos.
- **MENU do GKR:** eventual entrada de descoberta documental para esta superfície precisa de aprovação e publicação separadas; o item `Mapa do Ecossistema` é um **link do produto**, não um item do MENU do repositório.

## 8. Decisões de arquitetura pendentes

- Nomes finais e ordem dos grupos, variante compacta e peso editorial da assinatura da marca.
- Página de destino de `Mapa do Ecossistema` e seus critérios de publicação.
- Canais de ajuda e contato efetivamente mantidos.
- Conteúdos legais, informação institucional obrigatória e mercados/idiomas ativos.

Estas decisões devem ser resolvidas com responsáveis pertinentes e evidências, sem preencher lacunas com textos ou URLs fictícios.
