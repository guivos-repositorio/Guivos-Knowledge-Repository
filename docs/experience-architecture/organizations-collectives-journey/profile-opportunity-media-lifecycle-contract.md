---
id: GKR-UX-ORGCOL-PROFILE-OPPORTUNITY-MEDIA-001
title: Organizações e Coletivos — Perfis, Oportunidades, Galeria e Vigência
status: proposed
version: 0.1.0
owner: Experience Architecture
last_updated: 2026-10-17
normative: false
depends_on:
  - GKR-UX-ORGCOL-AUTH-SURFACE-MAP-001
  - GKR-PLANS-ORGANIZATION-001
  - GKR-PLANS-COLLECTIVE-001
---

# Organizações e Coletivos — Perfis, Oportunidades, Galeria e Vigência

## 1. Origem e situação

Direção explícita do fundador em 17/10/2026, a incorporar à experiência em desenvolvimento no Replit e a reconciliar nas autoridades do GKR. Este contrato reúne exigências funcionais candidatas e limites de materialização, **sem substituir** o Surface Registry, Transition Registry, decisões sobre autenticação, privacidade, aprovação, cobrança ou publicação produtiva. Alteração de política comercial definitiva requer ratificação própria; este documento não reivindica maturidade global ou homologação de engenharia.

## 2. Dois cadastros distintos por participante

**Organização:** (A) cadastro completo e manutenção do perfil institucional, com dados pertinentes, representação, contatos, localização/abrangência, descrição e galeria institucional; (B) cadastro, revisão, envio e administração de cada oportunidade/programa oferecido, com conteúdo, preço, prazo e galeria daquela oportunidade.

**Coletivo:** (A) cadastro completo e manutenção do perfil do Coletivo, com identidade, propósito, responsáveis, área de atuação, contatos e galeria contextual; (B) criação e gestão de atividades/oportunidades (curso, encontro, pedalada, evento etc.), com dados, preço, prazo e galeria própria; **não** confundir cadastro de oportunidade com consultas ou decisões nem criar novo SURF/TRN por simetria. Usar responsabilidade/fluxo especializado existente conforme autoridade do Coletivo.

A UI deve ter entrada inequívoca de **Criar Organização**, **Criar Coletivo**, **Editar perfil** e **Criar oportunidade**, condicionadas ao contexto e à autoridade correspondente. Cadastro de perfil não implica autenticação, verificação, representação legal ou publicação aprovada. Nenhuma parte pode editar identidade, galeria ou oportunidades da outra por estar relacionada.

## 3. Perfil e galeria institucional

Fotos institucionais de Organização ou Coletivo podem ilustrar fachada, recepção, instalações/ambientes internos, equipe, atividades e eventos anteriores, desde que o remetente possua direitos e fundamento adequado de publicação e exposição de pessoas. O campo **logo** deve ser tratado separadamente da galeria fotográfica: não confundir identidade gráfica com fotos de eventos; sua regra de quantidade e validação de marca depende de contrato próprio, e **não** contar automaticamente como foto da galeria.

Contrato funcional candidato: seleção de múltiplas imagens, pré-visualização, ordem, capa, substituição, exclusão, formatos permitidos, limite técnico por arquivo sob validação, metadados alternativos e explicação de erros. Não presumir autorização de exposição de imagens de crianças, participantes ou terceiros; exigir proteção e base jurídica específica onde aplicável. A validação de autorização/proveniência é obrigatória antes de publicação real.

## 4. Oportunidades/atividades — cadastro completo, preço e vigência

Dados materiais de cada oportunidade: responsável publicador, título, descrição, categoria/tipo, público e condições pertinentes, lugar ou modalidade, data/hora inicial e final quando aplicáveis, prazo de inscrição separado quando aplicável, vagas/capacidade caso governadas, estado, preço ou indicação explícita **Gratuita**, galeria própria e revisão antes do envio.

**Preço:** permitir escolha mutuamente exclusiva `Gratuita` (`preço = 0`, exibir claramente "Gratuito") ou `Paga` (preço positivo em moeda e condições/obrigações aplicáveis); não inventar checkout, taxas ou processamento financeiro. Coletivo `Livre` não pode publicar oportunidade com cobrança obrigatória. `Mobiliza`, `Impacta`, `Rede` podem propor oportunidades gratuitas ou pagas conforme autoridade e capacidades; Organizações `Conecta`, `Eleva`, `Transforma` igualmente conforme baseline. Eventos podem ocorrer depois do encerramento da inscrição: são datas diferentes.

**Prazo e visibilidade:** oportunidade com ocorrência temporal determinada deve registrar horário e fuso coerentes, e o instante efetivo de término da oportunidade; enquanto aprovada/ativa e dentro da janela de visibilidade, pode constar nas superfícies de descoberta da Pessoa. **Ao atingir a data/hora de término, tornar indisponível para novas manifestações/inscrições e removê-la automaticamente de listagens de oportunidades futuras/ativas da Pessoa, sem precisar de ação manual do publicador.** A verificação deve acontecer também ao consultar/filtrar dados (e não só por tarefa agendada), para impedir reaparição de registros expirados. A página/histórico e evidências podem permanecer disponíveis nos contextos legitimamente autorizados, sem representar a oportunidade como ativa; obrigações, inscrições prévias, cancelamentos, recursos e registros não são apagados. O prazo de inscrição pode fechar antes do evento e não deve ser confundido com a data final de ocorrência. Caso não haja data de encerramento comprovável, **não inventar data automática**: exigir um prazo real antes da publicação de oportunidade de duração determinada ou manter rascunho/bloqueio contextual; programas contínuos exigem contrato próprio para janela de validade/renovação, não expiração arbitrária.

Estados `Rascunho`, `Em revisão`, `Aprovada/ativa`, `Pausada`, `Encerrada/expirada` e `Cancelada` são semanticamente distintos. O protótipo pode demonstrar essa regra localmente; estado real persistido, auditoria, scheduler, API e sincronização multicanal requerem implementação e testes próprios. Não usar timestamp de navegador como prova de publicação real.

## 5. Galeria por plano — decisão solicitada, contrato candidato

| Contexto | Plano vigente | Quantidade máxima de fotos da galeria do PERFIL | Quantidade máxima de fotos POR oportunidade |
|---|---|---:|---:|
| Coletivo | Livre (gratuito) | 3 | 3 |
| Coletivo | Mobiliza, Impacta, Rede (pagos) | 9 | 9 |
| Organização | Conecta, Eleva, Transforma (pagos) | 9 | 9 |
| Organização | Eventual plano gratuito formalmente aprovado no futuro | 3 | 3 |

O limite é **por entidade para a galeria de perfil e por oportunidade para a galeria daquele objeto**, não cota mensal e não número global compartilhado. Logo institucional é campo próprio, sujeito a decisão de contabilização específica (não presumir consumo da quota fotográfica). O contrato deve informar limite restante antes do upload, bloquear inserção excedente sem descartar arquivos válidos, preservar histórico, respeitar acessibilidade e permitir exclusão ou substituição com autoridade. Mudança de plano não apaga automaticamente mídias válidas já existentes; novas inclusões devem obedecer à capacidade atual e regras de exibição e regularização a serem homologadas.

**Escopo de autoridade:** percentuais de preço por mídia, limites em MB, formatos finais, política de armazenamento/retenção, direitos de imagem, moderação, redimensionamento/crop, faturamento e assinatura real exigem decisão/evidência específica. A diferença 3/9 está recebida como direção expressa do fundador e registrada **como proposta para ratificação comercial**, sem alteração tácita na baseline econômica consolidada. Não criar plano gratuito de Organização.

## 6. Jornadas e responsabilidades preservadas

- Cadastro do perfil é uma responsabilidade contextual de identidade do participante; deve ser tratada sem multiplicar `GKR-SURF-*` ou `GKR-TRN-*` até verificação de necessidade de identificador estável.
- Cadastro de oportunidade de Organização continua `ORG-002` e vida da ativa `ORG-003`; manter revisão, autoridade e `TRN-201..203` conforme registry, sem promover transições.
- Coletivo mantém atividades em `COL-006` e encaminha oportunidades a fluxo especializado quando existente. Não criar falsa simetria com `ORG-002`.
- Descoberta da Pessoa deve consumir **apenas oportunidades elegíveis, publicadas e temporalmente ativas** na listagem de oportunidades futuras, sem falsificar relevância, prova, participação ou privilégios.
- A implementação no Replit será prototipação funcional até testes e gates específicos de Engenharia, privacidade, marca, disponibilidade, moderação, acessibilidade e publicação real.

## 7. Critérios de aceite da implementação de protótipo

1. Entradas distintas de perfil e oportunidade para cada participante; criação, revisão e edição acessíveis e coerentes.
2. Galerias de perfil e oportunidade independentes, seleção real local de fotos, preview, capa, reordenação, remoção, limites 3/9 e erro contextual.
3. Escolha `Gratuita` ou `Paga` sujeita ao plano; `Livre` proíbe cobrança obrigatória.
4. Início/fim e inscrição separados; oportunidade vencida some imediatamente das listas futuras da Pessoa, sem apagar histórico ou compromissos.
5. Registro de estados sem divulgação de dados de terceiros, falsa operação de pagamentos ou falsa publicação real.
6. Desktop/mobile e acessibilidade, com aparência final Guivos e sem textos técnicos do GKR na interface.

**Estado:** `FOUNDER_DIRECTION_RECORDED / CROSS_DOMAIN_RATIFICATION_PENDING / REPLIT_PROTOTYPE_AUTHORIZED / PRODUCTION_NOT_AUTHORIZED`.
