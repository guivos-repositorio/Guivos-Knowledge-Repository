---
id: GKR-LIVED-POSSIBILITIES-IDENTITY-MEDIA-CANDIDATE-001
title: Possibilidades Vividas — G05 Contrato Candidato de Identidade e Mídia
status: proposed
version: 0.1.0
owner: Guivos
last_updated: 2026-11-22
normative: false
---

# G05 — Identidade, CAPA e fotografias

Especificação funcional documental candidata ao protótipo isolado de Possibilidades Vividas. Reutilizar autoridades existentes; não autoriza Replit, alteração do cadastro, publicação de perfis ou uso de fotos reais.

## 1. Fontes de verdade e objetos distintos

| Elemento | Fonte competente | Uso no grafo | Limite |
|---|---|---|---|
| Identidade e nome da oportunidade | Cadastro autoritativo da oportunidade e edição | Nome do nó central e contexto | Grafo não duplica cadastro nem corrige nome na origem |
| CAPA da oportunidade | Mídia oficial designada no cadastro | Imagem circular do nó central | Não usar foto do ofertador/responsável |
| Identidade e identificação pública da Pessoa | Identidade oficial e regras públicas aplicáveis | Apenas identidade contextual autorizada | Não criar pessoa ou perfil paralelo |
| Fotografia de perfil da Pessoa | Fonte competente de foto/perfil, com direitos aplicáveis | Nó individual autorizado | Foto existente não equivale à permissão de exibição |
| Perfil Público de Experiências da Pessoa | Perfil público candidato e respectivas autoridades | Navegação opcional autorizada | Perfil público não autoriza vínculo com a oportunidade |
| Relação Pessoa–manifestação | Projeção válida de R1/P1 e autorizações | Aresta de participação identificada | Não revelar R1, trajetória privada ou presença sem autorização |

A primeira imagem da galeria designada no cadastro é a **CAPA inicial** conforme deliberação da Direção; isso ainda requer reconciliação com o contrato de cadastro oficial. Após uma troca válida da CAPA, o grafo usa a **CAPA oficial atual**, e não assume que a primeira posição física da galeria ainda controla a seleção. Reordenação não altera automaticamente uma designação explícita sem regra do cadastro. Preservar versão histórica e contexto da oportunidade quando materialmente relevantes à vivência e à avaliação.

## 2. Atualizações e fallback

A alteração autorizada de nome ou CAPA é refletida na página da oportunidade e no nó central pelo mecanismo compartilhado que vier a ser contratado, sem cópias divergentes. A mesma mudança visual não modifica objeto/edição/etapa, identidade lógica da avaliação, relatos, evidências ou contagens. Se a mídia estiver ausente, retirada, inválida, expirada, indisponível ou sem direitos válidos, apresentar fallback **neutro** e nome oficial quando permitido; jamais substituir por foto do ofertador, imagem inventada de vivência ou participante. O fallback não concede autoridade para usar outro ativo.

Alteração de nome, foto de perfil ou estado de perfil da Pessoa requer revalidação da autorização contextual. Se a foto foi retirada, deixar de exibi-la; a existência da identificação textual permanece condicionada à sua permissão específica. Tornar perfil privado impede navegação pública ao perfil; demais autorizações independentes não são automaticamente presumidas revogadas ou mantidas sem analisar suas dependências. Retirar identificação da manifestação exige ocultar nome, foto, vínculo e metadados capazes de reidentificar; somente agregação ainda autorizada e suficientemente protegida pode permanecer. Retirada da autorização de agregação atualiza também os derivados correspondentes. Não permitir ressurgimento por cache, exportação, replay ou restauração.

Atualizações sincronizadas deverão ter revalidação de autorização, versão, escopo e recuperação em falhas. Não definir tecnologia, API, serviço, webhooks, prazo de sincronização ou garantia de instantaneidade sem contrato competente. Para o protótipo isolado, usar **fixtures sintéticas** capazes de simular essas mudanças e proibições, sem conectar sistemas de produção.

## 3. Pessoas e imagem na apresentação inicial

O grafo pode mostrar algumas fotografias **reais apenas quando efetivamente autorizado no futuro ambiente de produção**, associadas a participantes efetivos elegíveis e às manifestações correspondentes. Para o protótipo, usar avatares e imagens sintéticos, sem retratar pessoas reais como participantes verificados. A seleção fotográfica deve contemplar diferentes manifestações, sem privilegiar impactos positivos, prestígio, popularidade ou renda; nenhuma inferência sensível para fabricar diversidade. Não apresentar fotografias apenas por existirem em perfis públicos.

Quantidade visível limitada pela legibilidade e espaço, não por número fixo universal. Estabilidade durante exploração e eventual rotatividade entre visitas, sem trocar fotos enquanto usuário investiga relação. Foto indisponível não exclui contribuição agregada legítima; pode restringir apenas presença fotográfica inicial. Identificação alternativa (p. ex. nome reduzido) exige contrato próprio e não pode servir para reidentificar quem preferiu não se expor.

## 4. Permissões e fronteiras

Separar, sem dedução entre si: (a) agregação, (b) identificação pública, (c) fotografia no nó, (d) vínculo Pessoa–manifestação, (e) consulta ao perfil público, (f) relato público e (g) relevância/impacto individuais. A seleção preferencial de compartilhamento solicitada pela Direção permanece **condicionada ao G06**, não autoriza qualquer campo por default e não deve ser confundida com consentimento afirmativo. Não expor localização, objetivos, condições, contatos, Contexto Vivo ou relações privadas. Visibilidade do perfil e participação na oportunidade são decisões distintas. Dados de terceiros e fotos do ofertador não substituem identidade de participante.

## 5. Critérios de aceite documental e teste sintético posterior

| ID local | Cenário | Resultado esperado |
|---|---|---|
| G05-T01 | Cadastro atribui CAPA inicial à primeira foto da galeria | Nó central utiliza designação oficial sem criar cópia autoritativa |
| G05-T02 | Ordem da galeria muda com CAPA explicitamente preservada | Nó mantém CAPA oficialmente designada, não muda por suposição |
| G05-T03 | CAPA é substituída por decisão autorizada | Nó central e página consumidora refletem fonte oficial; histórico protegido intacto |
| G05-T04 | CAPA não carrega ou é retirada | Fallback neutro, nunca foto do ofertador |
| G05-T05 | Nome da oportunidade é alterado | Atualiza rótulo autorizado; avaliação e editionamento preservados |
| G05-T06 | Nova edição com CAPA e nome próprios | Identidade da edição e avaliações antigas não são misturadas |
| G05-T07 | Foto da Pessoa existe mas exibição não foi autorizada | Nenhum nó fotográfico identificável |
| G05-T08 | Foto e identificação autorizadas para a manifestação | Nó público usa fonte oficial somente no escopo autorizado |
| G05-T09 | Nome público muda | Projeções permitidas se atualizam; autoria de R1 não muda |
| G05-T10 | Foto é retirada, agregação continua permitida | Foto retirada; agregação preservada se legítima e protegida |
| G05-T11 | Perfil da Pessoa torna-se privado | Link público desabilitado; demais autorizações revalidadas |
| G05-T12 | Pessoa retira identificação mas mantém agregação | Ocultar nome, foto e arestas identificáveis; só agregação autorizada permanece |
| G05-T13 | Pessoa retira autorização de agregação | Recalcular derivados; impedir ressurreição |
| G05-T14 | Perfil público existe mas vínculo com vivência não foi autorizado | Não publicar vínculo/aresta nem permitir inferência identificável |
| G05-T15 | Pessoa sem foto participa de manifestação elegível | Não excluir contagem agregada por ausência de foto |
| G05-T16 | Visitante seleciona nó de participante | Priorizar experiência autorizada; link para perfil somente com permissão distinta |
| G05-T17 | Pessoa tem várias expressões | Mesma identidade contextual autorizada, sem multiplicar pessoa |
| G05-T18 | Foto inicial de diferentes manifestações | Não usar popularidade ou positividade como critério de mérito |
| G05-T19 | Mudança de autorização ocorre durante exibição | Revalidar e ocultar conteúdo afetado sem estados públicos obsoletos |
| G05-T20 | Cache antigo reaparece após retirada | Estado removido não é republicado |
| G05-T21 | Foto ou URL de mídia viola direitos ou se torna inválida | Bloquear mídia, aplicar fallback, registrar problema para autoridade competente |
| G05-T22 | Protótipo sem integrações reais | Todas as imagens e identidades são sintéticas, sem alegar participantes reais |

Todos os 22 cenários são especificações **não executadas**.

## 6. Dependências explícitas

- **Cadastro de oportunidades:** regra efetiva da CAPA inicial, substituição, reordenação, direitos de mídia, versionamento e identidade de edição; a referência de cadastro de Organização inspecionada não comprova essa regra.
- **Perfil Público de Experiências:** modelo e fronteiras candidatos; titularidade e propriedade arquitetural ainda não adjudicadas.
- **UXA-057 e PAS-001:** elegibilidade, prova, identidade lógica e R1/P1, sem nova autoridade.
- **G06:** fundamento legítimo de divulgação, consentimento quando aplicável, proteção contra reidentificação, revogação, menores e experiências sensíveis.
- **G07/G08:** acessibilidade visual e futuras integrações compartilhadas, mediante autorização específica.

Referências verificadas: [Grafo Público](public-graph-belonging-and-continuity.md); [G04](graph-projection-and-counting-acceptance-candidate.md); [Perfil Público](../experience-architecture/perfil-publico-experiencias-pessoa/modelo-funcional.md); [Fronteiras](../experience-architecture/perfil-publico-experiencias-pessoa/fronteiras-arquiteturais.md); [Cadastro de Organização](../experience-architecture/organizations-collectives-journey/organization-opportunity-registration-master.md).

**Estado G05:** documentação candidata e 22 cenários disponíveis para aceite humano. Não equivale à reconciliação canônica de mídia e perfis, testes executados ou autorização de implantação. Replit bloqueado.
