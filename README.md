# Guivos Knowledge Repository (GKR)

O Guivos Knowledge Repository representa a Guivos em seu estado de maturidade institucional, reunindo fundamentos, arquiteturas, modelos, decisões, especificações e patrimônio intelectual.

## Status atual

- **Era vigente:** GE-2 — Knowledge
- **Marco vigente:** M5.6 — Journey Operational Philosophy Consolidated
- **Frente operacional:** Product Engineering
- **Sincronização vigente:** GE2-SYNC-005
- **Especificação ativa:** PAS-001 — Guivos Journey 0.3.0
- **Arquitetura funcional:** GLPA-001
- **Guia Oficial:** GOG-001 4.0.0
- **GKA-000:** Parte V pendente
- **A2-R02:** em espera operacional
- **Guivos Economic Model:** planejado

## Ponto exato de retomada

Retomar no `PAS-001 — Guivos Journey` pela especificação funcional detalhada da **Captura de Contexto**.

A próxima entrega deverá cobrir:

- primeira conversa por voz ou texto;
- escuta e interpretação;
- reflexão da compreensão;
- confirmação, correção e limitação;
- consentimento e privacidade;
- exceções;
- transição para objetivos, prioridades e primeiras oportunidades.

## Filosofia operacional do Journey

O Journey opera por cinco responsabilidades permanentes:

1. compreender;
2. acompanhar;
3. ativar;
4. orquestrar;
5. aprender.

Sequência comportamental:

```text
Escutar
  -> Compreender
  -> Refletir
  -> Confirmar
  -> Recomendar ou agir
```

## Conceitos funcionais consolidados no PAS-001

- Captura Multimodal de Contexto;
- voz como canal prioritário, mas não exclusivo;
- relação contínua com a vida real;
- Estado e Eventos de Vida;
- Oportunidades Ativas;
- Intervenções Contextuais;
- Orquestração de Intervenções;
- Distância para Evolução como conceito interno de produto;
- LPM e CIE preservados como candidatos, não como componentes técnicos obrigatórios.

## Decisão de foco

O Architecture Engineering Sprint não é mais a atividade imediata.

GTF, GCM, GPMA, GLS, GDP, GDF e GAME permanecem preservados como candidatos, mas não serão desenvolvidos antes da conclusão suficiente das especificações funcionais dos produtos oficiais.

## Acesso rápido

- [PAS-001 — Guivos Journey](docs/product-architecture/pas-001-guivos-journey.md)
- [GE2-SYNC-005 — Journey Operational Philosophy and Product Engineering](docs/project/GE2-SYNC-005-journey-operational-philosophy-and-product-engineering.md)
- [GLPA-001 — Guivos Layered Product Architecture](docs/product-architecture/layered-product-architecture.md)
- [Guia Oficial da Guivos](docs/public/guia-oficial-da-guivos.md)
- [Roadmap Arquitetural](docs/roadmap.md)
- [Knowledge Board](docs/project/knowledge-board.md)
- [Guivos Intelligence Architecture](docs/intelligence-architecture/index.md)
- [Guivos Economic Model](docs/economic-model/index.md)

## Princípios centrais

> A Guivos é concebida em sua capacidade máxima. A implementação realiza progressivamente essa visão.

> O participante permanece soberano sobre as informações utilizadas para compreender e personalizar sua jornada.

> O Journey não maximiza quantidade de oportunidades; ele busca ativar as oportunidades certas no momento certo.

> Cada sessão de trabalho deve produzir incremento funcional concreto enquanto houver produto oficial sem especificação suficiente.

## Pipeline de publicação

```text
GitHub -> Markdown -> Mermaid -> Site -> PDF
```

O Markdown versionado no GitHub é a fonte oficial.