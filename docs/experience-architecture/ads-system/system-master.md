---
id: GKR-ADS-SYSTEM-MASTER-001
title: Guivos ADS — Sistema Autenticado — Documento Mestre de Superfícies e Fluxos
status: candidate_for_review
version: 0.1.1
owner: Guivos Ads / Experience Architecture
last_updated: 2026-11-02
normative: false
---

# Guivos ADS — Sistema Autenticado — Documento Mestre

## 1. Propósito e fronteiras

Especificação candidata da experiência funcional do **Guivos ADS**, para orientar projeto de interface e futura construção em ambiente Replit após gate de autorização. **Não altera a Home Pública Guivos Ads**. GPA-007 continua como autoridade de produto. A Home pública introduz o Ads; esta coleção descreve o **sistema autenticado** de gestão comercial.

### Frentes integradas, não confundidas

- **Publicidade no ecossistema**: criação, gestão e mensuração de campanhas autorizadas em superfícies do Journey, Mall, Travel, Media e demais produtos, quando houver inventário e autoridade da superfície anfitriã.
- **Anúncio e patrocínio de oportunidades**: exploração de oportunidades explicitamente abertas à modalidade comercial, negociação com organizador, contrapartidas e comprovação.
- **Opportunity Boost**: contratação opcional pelo organizador ao final do cadastro ou posteriormente em Minhas oportunidades, ou por patrocinador formalmente autorizado. Não é sinônimo de patrocínio nem de publicidade geral.

A relação bilateral entre Organizações e Coletivos continua em ferramenta independente. Identidade institucional é reutilizada, sem duplicação automática de entidades.

## 2. Entrada e identidade

Entrada única **Guivos ADS**, sem obrigar escolha antecipada ou persistente de intenção comercial. Todas as modalidades elegíveis permanecem disponíveis no painel; a escolha ocorre **por ação**, ao criar campanha, explorar oportunidade, propor patrocínio ou solicitar impulsionamento. O cadastro captura representação e entidade responsável, dados institucionais, marca(s), responsabilidades e autorizações. Contas existentes habilitam um papel Ads; múltiplas marcas/entidades são segregadas por permissões. O sistema deve proporcionar **Cadastrar** e **Acessar**, de forma alinhada à experiência de entrada de Organização/Coletivo; o anexo de referência mostra o padrão de escolha e continuidade, não autoriza sua cópia literal.

Fluxo: entrada única Guivos ADS → identificação/cadastro ou acesso → verificação/termos aplicáveis → painel com todas as ferramentas → escolha de modalidade na ação específica. Uma marca poderá executar múltiplas campanhas e patrocinar várias oportunidades, inclusive por modalidades diferentes, sem seleção global exclusiva. O usuário não tem acesso às capacidades comerciais antes de elegibilidade, permissões e controles correspondentes.

## 3. Navegação autenticada proposta

1. **Visão geral** — compromissos, andamento e indicadores separados por frente.
2. **Minha marca / entidades** — identidade, marcas, representantes e comprovação; **não** determina nem bloqueia modalidades comerciais do painel.
3. **Campanhas no ecossistema** — campanhas, criativos, formatos, orçamentos, superfícies e períodos.
4. **Explorar oportunidades** — apenas oportunidades ativas, aprovadas e habilitadas para anúncios/patrocínios; filtros **Anúncios / Patrocínios / Ambos**, localização, período, categoria, disponibilidade e tipo de contribuição.
5. **Propostas e contratos** — enviadas, recebidas, em negociação, aceitas, recusadas, em execução, concluídas e contestadas.
6. **Patrocínios e Pontos** — obrigações, contribuições, reservas, contrapartidas, comprovações e situação dos Pontos Guivos.
7. **Opportunity Boost** — campanhas de impulsionamento sob titularidade/autorização.
8. **Analytics** — exposição contratada x entregue x validada, custos, resultados sem inflar impressões e separação por frente.
9. **Financeiro** — cobrança, reservas, reconciliação, reembolsos e histórico autorizado.
10. **Equipe e permissões** — identidade operante, funções, segregação e auditoria.

As entradas são **superfícies candidatas**, não afirmação de disponibilidade operacional.

## 4. Publicidade no ecossistema

**Fluxo candidato:** objetivo comercial → seleção de contexto/produto anfitrião → campanha/criativo → orçamento/período → política e disponibilidade → contratação → revisão e ativação → entrega identificada → mensuração e fechamento. Criativos não podem interferir na recomendação orgânica, no Próximo Passo da Pessoa, na autoridade editorial do Media, nas buscas orgânicas do Mall ou nas decisões operacionais do Travel.

Diferenciar **inventário controlado pela Guivos** de espaços e contrapartidas que pertencem ao organizador de uma oportunidade.

## 5. Oportunidades comerciais exploráveis

O organizador declara separadamente `bilateral_enabled`, `ads_enabled` e `sponsorship_enabled`. Uma oportunidade poderá habilitar nenhuma, uma ou ambas as modalidades Ads, e a bilateral de forma independente. Somente oportunidades válidas, aprovadas, dentro do período, com vagas comerciais e autorização expressa entram na descoberta correspondente. O modo “aberta a patrocínios” **não é selo público**.

**Cartão/lista candidata:** identificação do evento, organizador verificado quando aplicável, local/período, categoria, tipo de publicidade aceito, pacotes, número de cotas disponíveis, faixa comercial e contrapartidas de alto nível. Estimativas de público não são impressões observadas e não dão acesso a dados pessoais de participantes.

**Propostas:** cada proposta registra anunciante, oportunidade, modalidade, valor e unidade, contrapartidas, condicionantes, responsável, prazo, versão e estado. Propostas bilaterais não entram neste fluxo Ads.

## 6. Patrocínios e controle do organizador

Permitir por oportunidade:
- mínimo por contribuição (por exemplo R$ 100 sem teto);
- faixa mínima/máxima por contribuição;
- valor fixo;
- pacotes de patrocínio personalizados com contrapartidas e quantidade de cotas;
- limite máximo de patrocinadores, limite financeiro agregado, exclusividade ou conflitos de categoria;
- habilitação separada para propostas personalizadas.

Não confundir número de contratos, valores propostos, contratados, garantidos e entregues. Reservas de cotas têm validade; não bloqueiam o catálogo indefinidamente. O que o organizador não controla (inventário do Ads) exige contrato e autorização da Guivos.

**Festival Cultural ilustrativo:** anúncio de campanha associado à oportunidade versus patrocínio de evento com contrapartidas comerciais; recursos podem ser financeiros, produtos, serviços ou pontos mediante critérios próprios. Apoio cultural não é necessariamente publicidade.

## 7. Pontos Guivos

Pontos patrocinados são Pontos Guivos comuns da Pessoa, utilizáveis conforme elegibilidade de Mall e Travel. Financiamentos dos patrocinadores precisam de origem rastreável e garantia antes da concessão. A soma de múltiplos patrocinadores pode formar **saldo restrito vinculado à oportunidade, administrado pelo organizador**, nunca saldo livre. O organizador registra elegibilidade e premiação, e a distribuição ocorre mediante prova, controles e auditoria. Não exigir acesso a anúncios, consentimento comercial ou visita ao patrocinador para receber pontos legitimamente atribuídos.

Premiações somente quando **proporcionais e justificáveis** (por exemplo colocação em corrida), não de modo automático por inscrição, presença, visualização ou conclusão. Prever prevenção a eventos fictícios, autoconcessão, participantes simulados e contrapartidas não entregues; disputa comercial do patrocinador não elimina automaticamente prêmio legítimo da Pessoa.

## 8. Opportunity Boost — após cadastro da oportunidade

Na etapa final do cadastro aprovado para continuidade, apresentar escolha clara e não coercitiva:

- **Concluir sem impulsionamento** — cadastro segue fluxo de revisão/aprovação sem ônus publicitário;
- **Continuar com Opportunity Boost** — consultar planos elegíveis, período, orçamento, limites, termos, pagamento, revisão e confirmação.

Não usar “Continuar com patrocínio” para a contratação de Boost: o organizador **compra mídia**, não recebe patrocínio. O Boost só entra em distribuição após aprovação e elegibilidade da oportunidade. Pode ser contratado posteriormente no painel **Minhas oportunidades**. Terceiro patrocinador só pode custear Boost quando formalmente autorizado; separar verba de Boost de contribuição ao organizador. Manter inventário patrocinado rotulado, limites de frequência/orçamento, eventos válidos e reconciliação.

**Nomes, preços, períodos e benefícios finais dos pacotes não estão aprovados.** A imagem OLX é referência de padrão de escolha, não fonte de identidade, condições comerciais ou cópia de interface.

## 9. Estados operacionais candidatos

- **Identidade**: em cadastro → aguardando validação → habilitada → restrita/suspensa.
- **Disponibilidade de oportunidade**: não habilitada → aberta → temporariamente indisponível → encerrada/suspensa; bilateral independente.
- **Proposta**: rascunho → enviada → recebida → negociação/contraproposta → aceita/recusada/expirada → execução → concluída/contestada/cancelada.
- **Campanha**: rascunho → revisão → elegível → aguardando financiamento → programada → ativa/pausada → encerrada → reconciliada.
- **Pontos**: prometidos → financiados → reservados → atribuídos após evidência → transferidos → reconciliados/contestados.

Cada transição exige responsável autorizado, registro temporal e histórico, além de política de estorno específica.

## 10. Proteção, mensuração e critérios de aceite do handoff

Interface: fundo branco, identidade oficial, tipografia Goldplay (ou fallback técnico autorizado), itens de navegação com ícones, dashboards prioritariamente numéricos, calendário flexível quando período for necessário. **O laranja solicitado nesta tarefa pertence ao título da seção no menu do GKR**, não define automaticamente uma paleta de marca para todas as telas Ads.

Critérios de handoff:
- entrada própria de Ads, sem duplicar cadastro de O/C;
- as três frentes aparecem sem confusão;
- oportunidade fechada para as modalidades não é explorável;
- status administrativos não viram selos na Journey;
- bilateral e Ads permanecem sistemas distintos;
- Boost preserva saída gratuita e não compra relevância orgânica;
- patrocinador não obtém dados pessoais ou direito ao direcionamento individual;
- valores de pontos com lastro, motivação, responsabilização e trilha;
- dashboard diferencia entregas previstas, observadas e validadas;
- não exibir rótulos artificiais de prototipação em telas de produto (sem declarar dados reais falsamente).

## 11. Dependências, entregáveis e limites de autorização

Para um futuro Replit: derivar inventário de telas, mapa de rotas, componentes, contratos de API, esquemas de dados, permissões, cenários de falha e matriz de testes; manter sincronização com autoridades do GKR e sistema de pagamentos próprio. Nenhuma dessas entregas equivale a implementar nesta etapa.

**Gates em aberto:** direitos de inventário e contrapartidas, política de anúncios, precificação de Boost, captação e remuneração, contratos jurídicos, financiamento/conciliação de pontos, antifraude operacional, integração de pagamentos, proteção de dados, validação humana e liberação de engenharia.

**Estado:** conceito documentado para avaliação e posterior handoff; sem aprovação de implementação, deploy ou funcionamento comercial.

## 12. Decisão posterior — modalidades por ação e cenários de avaliação (2026-11-02)

A direção esclareceu que não há etapa obrigatória de **escolha de modalidades de participação** no cadastro nem bloqueio global por preferência. O anunciante pode combinar publicidade de ecossistema, publicidade de oportunidade, patrocínio e Boost autorizado em quantos contratos independentes for elegível, respeitando cotas, orçamento, riscos, direitos de inventário e termos de cada oportunidade. Cada proposta ou campanha registra sua modalidade própria.

A experiência Replit pode apresentar **cenários locais com dados de ensaio** de oportunidades, pacotes, anúncios, contratos, pontos e indicadores para avaliação de layout e fluxo. A interface não precisa conter rótulos repetitivos de prototipação, mas não poderá representar transações, aprovações, pessoas verificadas ou saldos financeiros simulados como verdadeiros. Operações reais e integrações permanecem bloqueadas até gates específicos. Cenários não autorizados para anúncio/patrocínio não devem surgir no explorador, mesmo na simulação.

**Prevalência:** esta decisão substitui qualquer orientação anterior de seleção de intenção antes do cadastro ou de ativação exclusiva de modalidade no perfil.
