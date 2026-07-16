---
id: PAS-001-IC-INTEGRATION-001
title: Integrações Funcionais da Capacidade de Intervenções Contextuais
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-16
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-IC-FOUNDATION-001
  - PAS-001-IC-LIFECYCLE-001
  - PAS-001-IC-VIEW-001
  - PAS-001-IC-EVENT-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-IC-INTEGRATION-001 — Integrações Funcionais da Capacidade de Intervenções Contextuais

## 1. Autoridade e vínculo

Este documento é a **quinta extensão normativa da Capacidade 07 — Intervenções Contextuais** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser interpretado como continuidade das quatro extensões normativas anteriores de Intervenções Contextuais, do `PAS-001 0.5.0`, das seções 1 a 3164, dos contratos finais das Capacidades 02 a 06, da `GLPA-001` e da `GIA-000`.

Esta extensão mantém a Capacidade 07 como `In progress` e eleva o progresso editorial de referência de `80%` para `90%`.

As Capacidades 02, 03, 04, 05 e 06 permanecem `Functionally complete`. A Capacidade 08 — Experiências permanece `Planned`.

# 3165. Finalidade das integrações

As integrações deverão governar como Intervenções Contextuais troca informações, sinais, comandos, propostas, eventos, decisões, confirmações e resultados com outras capacidades, produtos, organizações, profissionais, canais e sistemas externos.

A integração deverá preservar:

- finalidade;
- titularidade;
- autoridade;
- temporalidade;
- sensibilidade;
- autonomia;
- neutralidade comercial;
- rastreabilidade;
- revogação;
- falha segura.

# 3166. Definição de integração funcional

Integração funcional é uma relação governada entre produtor e consumidor para troca limitada de elementos necessários a uma finalidade específica.

A integração não deverá ser tratada como acesso irrestrito ao participante, à jornada ou ao histórico completo.

# 3167. Singularidade

A singularidade das integrações será:

> **Permitir que a decisão de manifestação utilize contexto e produza efeitos coordenados sem transferir titularidade, ampliar autoridade ou transformar integração técnica em vigilância.**

# 3168. Titularidade e responsabilidade

Cada capacidade ou produto deverá continuar responsável por seu próprio domínio.

Intervenções Contextuais poderá decidir:

- se uma manifestação é adequada;
- quando ela poderá ocorrer;
- por qual canal;
- com qual intensidade;
- com qual conteúdo mínimo.

Ela não deverá assumir a autoridade funcional do produtor original ou do executor externo.

# 3169. Princípios gerais

As integrações deverão obedecer a:

1. finalidade específica;
2. autoridade limitada;
3. minimização;
4. proveniência;
5. temporalidade explícita;
6. sensibilidade;
7. neutralidade comercial;
8. revogabilidade;
9. explicabilidade;
10. auditabilidade;
11. idempotência;
12. ordenação;
13. prevenção de ciclos;
14. proteção de terceiros;
15. falha segura.

# 3170. Tipos de integração

As integrações poderão ser:

- informativas;
- consultivas;
- transacionais;
- eventuais;
- contínuas;
- temporárias;
- pessoais;
- organizacionais;
- profissionais;
- públicas;
- comerciais;
- institucionais;
- coletivas.

# 3171. Modos de integração

Modos possíveis:

- consulta;
- resposta;
- comando;
- evento;
- callback;
- assinatura;
- sincronização;
- lote;
- fluxo contínuo;
- confirmação;
- encaminhamento humano;
- atualização manual.

# 3172. Contrato comum

Toda integração deverá declarar:

- produtor;
- consumidor;
- participante;
- destinatário;
- finalidade;
- modo;
- autoridade;
- escopo de dados;
- sensibilidade;
- fonte;
- proveniência;
- temporalidades;
- qualidade;
- confiança;
- retenção;
- permissões;
- relação comercial;
- estado de sincronização;
- estado de revogação;
- comportamento diante de falha.

# 3173. Produtor

O produtor será responsável por:

- declarar fatos dentro de sua autoridade;
- fornecer versão;
- informar validade;
- indicar sensibilidade;
- preservar proveniência;
- minimizar o payload;
- reconhecer correções;
- propagar revogações aplicáveis.

# 3174. Consumidor

O consumidor deverá:

- validar finalidade;
- respeitar autoridade;
- aplicar minimização adicional;
- preservar significado;
- verificar versão;
- tratar duplicidade;
- aplicar revogações;
- não ampliar o escopo recebido;
- registrar efeitos materiais.

# 3175. Participante e titular

O participante titular deverá permanecer distinguido de:

- organização;
- profissional;
- responsável legal;
- familiar;
- equipe;
- comunidade;
- fornecedor;
- sistema executor.

A relação com uma organização não transfere automaticamente titularidade sobre a jornada individual.

# 3176. Finalidade da integração

A finalidade deverá ser:

- específica;
- compreensível;
- proporcional;
- compatível com a autoridade;
- limitada no tempo;
- passível de explicação ao participante.

Finalidades genéricas de engajamento, retenção ou conversão não serão suficientes.

# 3177. Escopo de dados

O escopo deverá declarar:

- campos;
- categorias;
- período;
- granularidade;
- frequência;
- origem;
- consumidores;
- usos permitidos;
- usos proibidos.

# 3178. Sensibilidade

A sensibilidade deverá governar:

- autenticação;
- criptografia;
- conteúdo;
- logs;
- canais;
- retenção;
- consumidores;
- notificações;
- visualização;
- compartilhamento.

# 3179. Fonte e proveniência

A integração deverá preservar a cadeia:

> fonte original → validação → transformação → produtor → integração → consumidor → decisão → efeito

Transformações intermediárias deverão permanecer identificáveis.

# 3180. Temporalidades

Deverão permanecer distintas:

- momento do fato;
- momento da observação;
- momento do conhecimento;
- momento do envio;
- momento do recebimento;
- momento da aplicação;
- momento da manifestação;
- momento da resposta;
- momento da correção;
- momento da revogação.

# 3181. Correlação e causalidade

Correlação deverá conectar elementos do mesmo fluxo.

Causalidade somente deverá ser declarada quando existir relação funcional demonstrável.

Proximidade temporal não será prova suficiente de causalidade.

# 3182. Versão e compatibilidade

A integração deverá declarar:

- versão do contrato;
- versões compatíveis;
- campos obrigatórios;
- campos opcionais;
- comportamento diante de versão desconhecida;
- política de migração;
- possibilidade de reprocessamento.

# 3183. Idempotência

Operações materiais deverão possuir chave de idempotência.

Reprocessamento não deverá duplicar:

- avaliação;
- admissão;
- programação;
- apresentação;
- entrega;
- resposta;
- execução;
- correção;
- revogação.

# 3184. Permissões

Permissões deverão especificar:

- quem pode produzir;
- quem pode consumir;
- quais campos podem ser utilizados;
- por qual finalidade;
- durante qual período;
- por quais canais;
- com quais restrições.

# 3185. Retenção

A retenção deverá ser proporcional a:

- finalidade;
- sensibilidade;
- auditoria;
- segurança;
- obrigação legítima;
- contestação;
- correção;
- revogação.

# 3186. Relação comercial

A integração deverá declarar:

- patrocínio;
- comissão;
- publicidade;
- afiliação;
- exclusividade;
- participação na receita;
- vantagem indireta.

Relações comerciais não deverão aumentar relevância ou urgência funcional.

# 3187. Requisitos de admissão

Uma integração somente deverá ser admitida quando possuir:

- finalidade legítima;
- produtor identificado;
- consumidor identificado;
- autoridade suficiente;
- escopo minimizado;
- proteção compatível;
- versionamento;
- política de revogação;
- comportamento de falha;
- observabilidade;
- possibilidade de auditoria.

# 3188. Integrações rejeitadas

Deverão ser rejeitadas integrações que:

- forneçam acesso irrestrito à jornada;
- ocultem finalidade;
- ocultem relação comercial;
- utilizem contexto sensível para publicidade;
- não permitam revogação;
- não preservem proveniência;
- ampliem autoridade;
- formem perfis paralelos;
- produzam manifestações sem avaliação;
- dependam de vigilância contínua sem fundamento.

# 3189. Identidade

A associação entre participante e registro externo deverá utilizar identidade suficientemente confiável.

A integração não deverá utilizar apenas:

- nome semelhante;
- dispositivo compartilhado;
- endereço;
- localização;
- vínculo organizacional;
- conta familiar;

como prova definitiva de identidade.

# 3190. Associação incerta

Associações incertas deverão:

- permanecer marcadas;
- limitar efeitos;
- impedir manifestações sensíveis;
- solicitar confirmação quando necessário;
- permitir correção;
- evitar retenção excessiva.

# 3191. Associação incorreta

Quando uma associação incorreta for reconhecida:

- novos efeitos deverão ser bloqueados;
- consumidores deverão ser informados;
- manifestações derivadas deverão ser reavaliadas;
- dados deverão ser recompostos;
- o histórico deverá preservar a correção.

# 3192. Autoridade da fonte

Cada fonte deverá declarar sua autoridade sobre:

- fato;
- disponibilidade;
- prazo;
- risco;
- elegibilidade;
- resultado;
- obrigação;
- recomendação;
- transação;
- correção.

A fonte não deverá declarar além do que pode legitimamente confirmar.

# 3193. Qualidade, confiança e autoridade

Deverão permanecer separadas:

- **qualidade técnica**;
- **confiança funcional**;
- **autoridade da fonte**.

Uma fonte tecnicamente confiável poderá não possuir autoridade para determinada afirmação.

# 3194. Transformações permitidas

Poderão ser realizadas transformações como:

- normalização;
- tradução;
- sumarização;
- classificação funcional;
- redução de granularidade;
- extração de campos;
- anonimização;
- pseudonimização;
- agregação;
- conversão de formato.

# 3195. Transformações proibidas

A integração não deverá fabricar:

- disponibilidade;
- urgência;
- elegibilidade;
- aprovação;
- intenção;
- interesse;
- prioridade;
- compromisso;
- causalidade;
- resultado;
- progresso;
- transformação;
- diagnóstico;
- precisão inexistente.

# 3196. Limitação de finalidade

Dados recebidos para uma intervenção não deverão ser reutilizados automaticamente para:

- publicidade;
- precificação;
- perfil comercial;
- avaliação de crédito;
- ranking;
- produtividade;
- seleção;
- exclusão;
- inferência moral;
- recomendação incompatível.

# 3197. Minimização

A integração deverá utilizar o menor conjunto de dados capaz de sustentar a decisão.

Sempre que possível, deverá utilizar:

- sinal em vez de narrativa;
- categoria em vez de detalhe;
- faixa em vez de valor exato;
- disponibilidade em vez de agenda integral;
- confirmação em vez de histórico completo.

# 3198. Recortes funcionais

Um recorte deverá declarar:

- finalidade;
- campos;
- validade;
- consumidor;
- sensibilidade;
- permissão;
- retenção;
- condição de descarte.

# 3199. Consentimento

Quando aplicável, o consentimento deverá ser:

- específico;
- informado;
- granular;
- revogável;
- separado de termos gerais;
- proporcional ao impacto.

Consentimento para uma integração não autoriza outras finalidades.

# 3200. Pausa

Uma integração poderá ser pausada sem ser desconectada.

A pausa deverá:

- interromper novos fluxos;
- preservar estado;
- indicar motivo;
- definir efeitos;
- permitir retomada segura;
- não representar revogação completa.

# 3201. Desconexão

A desconexão deverá:

- bloquear novas trocas;
- cancelar assinaturas;
- interromper callbacks;
- preservar evidências mínimas;
- identificar pendências;
- informar consumidores dependentes.

# 3202. Revogação

A revogação deverá impedir:

- novas consultas;
- novas avaliações;
- novas manifestações;
- novos compartilhamentos;
- novos processamentos incompatíveis.

# 3203. Propagação da revogação

A revogação deverá ser propagada a:

- consumidores;
- canais;
- filas;
- caches;
- produtos;
- integrações derivadas;
- sistemas externos aplicáveis.

# 3204. Retenção após revogação

Após revogação, somente poderão permanecer dados necessários para:

- obrigação legítima;
- segurança;
- contestação;
- auditoria;
- prevenção de fraude;
- comprovação da própria revogação.

# 3205. Estados de sincronização

A sincronização poderá estar:

- não iniciada;
- em preparação;
- em andamento;
- concluída;
- parcial;
- pendente;
- divergente;
- pausada;
- bloqueada;
- falha;
- reconciliada;
- revogada.

# 3206. Divergência

Divergências deverão registrar:

- fontes;
- versões;
- temporalidades;
- autoridade;
- efeitos;
- estado provisório;
- necessidade de confirmação;
- decisão de reconciliação.

# 3207. Ordenação

A integração deverá considerar:

- versão;
- sequência;
- causalidade;
- temporalidade;
- dependências;
- correções;
- revogações;
- estado atual.

# 3208. Concorrência

Alterações concorrentes deverão exigir:

- versão esperada;
- detecção de conflito;
- preservação das propostas;
- decisão explícita;
- ausência de sobrescrita silenciosa.

# 3209. Reconciliação

A reconciliação deverá:

- preservar as versões recebidas;
- identificar autoridade;
- considerar temporalidades;
- limitar efeitos provisórios;
- registrar a decisão;
- permitir auditoria.

# 3210. Prevenção de ciclos

Integrações deverão impedir ciclos automáticos como:

> contexto → intervenção → resposta inferida → alteração de contexto → nova intervenção equivalente

A prevenção deverá utilizar:

- correlação;
- causalidade;
- identificador da decisão;
- limite de repetição;
- janela temporal;
- estado do participante;
- deduplicação semântica.

# 3211. Tempo real

Integração em tempo real somente deverá ser utilizada quando a utilidade depender efetivamente de baixa latência.

Tempo real não deverá justificar:

- coleta contínua;
- rastreamento permanente;
- notificações imediatas;
- aumento de frequência;
- vigilância.

# 3212. Processamento em lote

O processamento em lote poderá ser utilizado para:

- resumos;
- reconciliação;
- atualização de estados;
- análise de falhas;
- auditoria;
- expiração;
- limpeza;
- propagação.

# 3213. Retentativas

Retentativas deverão possuir:

- limite;
- intervalo;
- idempotência;
- condição de interrupção;
- observabilidade;
- prevenção de duplicidade;
- escalonamento controlado.

# 3214. Falha segura

Em falha, a integração deverá:

- preservar o último estado válido;
- impedir falsa manifestação;
- bloquear efeitos críticos;
- evitar duplicidade;
- reduzir automação;
- identificar impacto;
- permitir recuperação.

# 3215. Degradação controlada

A capacidade poderá degradar para:

- canal passivo;
- conteúdo reduzido;
- pergunta de confirmação;
- espera;
- encaminhamento humano;
- silêncio.

Degradação não deverá fabricar certeza ou sucesso.

# 3216. Integração com Captura de Contexto

Intervenções Contextuais poderá solicitar informação adicional quando:

- o contexto atual for insuficiente;
- a finalidade estiver explícita;
- a pergunta for mínima;
- a resposta puder ser recusada;
- não houver coleta automática equivalente.

# 3217. Integração com Contexto Vivo

Contexto Vivo poderá fornecer recortes sobre:

- momento;
- restrições;
- preferências;
- disponibilidade;
- localização autorizada;
- relacionamentos;
- condições atuais;
- horários protegidos.

Intervenções Contextuais não deverá copiar o Contexto Vivo integral.

# 3218. Integração com Objetivos

Objetivos poderá fornecer:

- direção;
- prioridade declarada;
- horizonte;
- estado;
- critérios;
- sensibilidade.

A intervenção não poderá criar, ativar, concluir ou repriorizar Objetivos.

# 3219. Integração com Eventos de Vida

Eventos de Vida poderá solicitar avaliação diante de mudança relevante.

A integração deverá impedir:

- exploração comercial;
- exposição prematura;
- interpretação emocional automática;
- comunicação sem momento adequado;
- causalidade presumida.

# 3220. Integração com Próximos Passos

Próximos Passos poderá solicitar:

- pergunta;
- lembrete;
- alerta;
- confirmação;
- apresentação de alternativa;
- espera.

A intervenção não deverá confirmar ou concluir o Próximo Passo.

# 3221. Integração com Oportunidades Ativas

Oportunidades Ativas deverá fornecer:

- relevância;
- disponibilidade;
- elegibilidade;
- prazo;
- custo;
- risco;
- sensibilidade;
- relação comercial;
- alternativas.

Intervenções Contextuais decidirá se, quando e como a oportunidade será apresentada.

# 3222. Integração com Experiências

Uma intervenção poderá:

- preparar;
- acompanhar;
- apoiar;
- revisar;
- solicitar registro posterior.

Ela não deverá declarar que uma experiência foi vivida, compreendida ou transformadora.

# 3223. Integração com Evolução Contínua

Evolução Contínua poderá fornecer sinais agregados e autorizados para adequar futuras intervenções.

Não deverá fornecer classificações determinísticas ou utilizar evolução humana para segmentação comercial.

# 3224. Integração com Guivos Intelligence

Guivos Intelligence poderá:

- identificar candidaturas;
- estimar relevância;
- avaliar temporalidade;
- identificar fadiga;
- sugerir canal;
- resumir conteúdo;
- detectar conflito;
- propor silêncio;
- produzir justificativas.

# 3225. Limites da Guivos Intelligence

Guivos Intelligence não deverá:

- impor manifestação;
- ignorar preferências;
- fabricar urgência;
- presumir consentimento;
- declarar intenção;
- executar ação material sem contrato;
- ampliar autoridade;
- utilizar vulnerabilidade comercialmente.

# 3226. Integração com Platform Layer

A Platform Layer poderá sustentar:

- identidade;
- autorização;
- filas;
- eventos;
- agendamento;
- canais;
- entrega;
- confirmação;
- preferências;
- observabilidade;
- idempotência;
- auditoria.

Ela não deverá definir relevância humana ou urgência funcional.

# 3227. Integração com Guivos Mall

Mall poderá:

- fornecer fatos sobre produtos, serviços, estoque, preço e pedidos;
- executar ações comerciais autorizadas;
- devolver resultados transacionais.

Mall não deverá transformar promoção, estoque ou margem em urgência funcional.

# 3228. Integração com Guivos Travel

Travel poderá fornecer:

- itinerários;
- reservas;
- alterações;
- cancelamentos;
- requisitos;
- riscos;
- prazos reais;
- localização autorizada.

Intervenções deverão distinguir sugestão de viagem, reserva e obrigação externa.

# 3229. Integração com Guivos Business

Business poderá originar:

- comunicações organizacionais;
- solicitações;
- obrigações;
- benefícios;
- convites;
- alertas institucionais.

A organização não deverá acessar a jornada pessoal além do escopo autorizado.

# 3230. Integração com Guivos Media

Media poderá fornecer:

- conteúdo relacionado;
- explicações;
- materiais educativos;
- histórias;
- atualizações editoriais.

Consumo de conteúdo não deverá ser convertido automaticamente em interesse ou necessidade.

# 3231. Integração com Guivos Ads

Guivos Ads deverá permanecer separado das intervenções funcionais.

Publicidade deverá:

- ser identificada;
- possuir contrato próprio;
- respeitar bloqueios;
- não utilizar contexto sensível;
- não assumir aparência de alerta;
- não interferir na ordenação funcional.

# 3232. Integração com organizações

Organizações poderão fornecer fatos dentro de sua autoridade.

A integração deverá distinguir:

- obrigação;
- política;
- benefício;
- convite;
- oportunidade;
- comunicação geral;
- alerta institucional.

# 3233. Integração com profissionais

Profissionais poderão:

- confirmar atendimento;
- fornecer orientação dentro de sua competência;
- solicitar informação;
- registrar resultado autorizado;
- receber respostas minimizadas.

A Guivos não deverá ampliar a autoridade profissional.

# 3234. Integração com saúde

Integrações de saúde deverão:

- limitar automação;
- preservar confidencialidade;
- identificar autoridade;
- evitar diagnóstico fabricado;
- impedir publicidade derivada;
- utilizar canais protegidos;
- permitir encaminhamento humano.

# 3235. Integração com finanças

Integrações financeiras deverão:

- indicar instituição;
- apresentar custos e riscos;
- distinguir estimativa de aprovação;
- exigir confirmação para efeitos materiais;
- limitar dados compartilhados;
- impedir promessas de retorno.

# 3236. Integração jurídica

Integrações jurídicas deverão:

- identificar jurisdição;
- preservar confidencialidade;
- distinguir informação e aconselhamento;
- evitar promessa de resultado;
- limitar automação;
- indicar autoridade profissional.

# 3237. Integração com educação

Integrações educacionais poderão fornecer:

- cursos;
- inscrições;
- frequência;
- prazos;
- avaliações;
- certificados;
- resultados.

Resultados educacionais não deverão ser convertidos automaticamente em valor humano ou evolução.

# 3238. Integração com trabalho

Integrações profissionais poderão tratar:

- vagas;
- processos seletivos;
- compromissos;
- escalas;
- treinamentos;
- avaliações formais;
- obrigações contratuais.

A integração não deverá permitir vigilância ocupacional irrestrita.

# 3239. Integração religiosa e espiritual

Integrações religiosas deverão preservar:

- liberdade de crença;
- liberdade de não participação;
- privacidade;
- pluralidade;
- ausência de julgamento;
- possibilidade de desconexão integral.

# 3240. Integração social e de voluntariado

Integrações sociais poderão tratar:

- causas;
- ações;
- necessidades;
- inscrições;
- presença;
- horas voluntárias;
- recompensas;
- patrocinadores.

A integração não deverá medir bondade, mérito ou valor moral.

# 3241. Integração com serviços públicos

Serviços públicos poderão fornecer:

- prazos;
- requisitos;
- protocolos;
- benefícios;
- obrigações;
- alertas;
- resultados.

A fonte pública deverá permanecer identificada e temporalmente validada.

# 3242. Canais internos

Superfícies internas deverão preservar:

- identidade da intervenção;
- estado;
- justificativa;
- sensibilidade;
- controles;
- histórico;
- relação comercial.

# 3243. Canais conversacionais

Canais conversacionais deverão interpretar comandos como:

- adiar;
- silenciar;
- contestar;
- mostrar detalhes;
- alterar canal;
- bloquear fonte;
- confirmar.

Ambiguidade deverá impedir efeitos materiais.

# 3244. Notificações móveis

Notificações deverão aplicar:

- minimização;
- título neutro;
- horário protegido;
- controle de frequência;
- autenticação proporcional;
- ausência de publicidade disfarçada.

# 3245. E-mail

E-mails deverão:

- identificar finalidade;
- distinguir comunicação funcional e comercial;
- evitar assunto sensível;
- direcionar para ambiente protegido;
- permitir controle de frequência;
- preservar rastreabilidade.

# 3246. Calendários

Integrações com calendário deverão distinguir:

- compromisso confirmado;
- sugestão;
- lembrete;
- prazo;
- reserva;
- evento coletivo.

Inserção automática deverá exigir autorização aplicável.

# 3247. Localização

Localização somente deverá ser utilizada quando:

- necessária;
- autorizada;
- temporalmente relevante;
- minimizada;
- protegida;
- limitada à finalidade.

Localização não deverá representar intenção ou interesse.

# 3248. Fontes públicas

Fontes públicas deverão ser avaliadas quanto a:

- autenticidade;
- atualização;
- jurisdição;
- autoridade;
- estabilidade;
- termos de uso;
- sensibilidade;
- risco de associação incorreta.

# 3249. Sistemas externos

Sistemas externos deverão devolver fatos sobre suas próprias operações.

Intervenções Contextuais não deverá presumir:

- conclusão;
- aceitação;
- pagamento;
- contratação;
- entrega;
- participação;
- resultado;

sem retorno autorizado.

# 3250. Informações de terceiros

Informações sobre terceiros somente poderão ser utilizadas quando:

- necessárias;
- autorizadas ou legitimamente aplicáveis;
- minimizadas;
- protegidas;
- relacionadas à finalidade.

Não deverá ser criado perfil independente do terceiro.

# 3251. Intervenções coletivas

Integrações coletivas deverão distinguir:

- contexto coletivo;
- participante individual;
- responsabilidade coletiva;
- decisão individual;
- conteúdo público;
- conteúdo privado;
- respostas compartilháveis.

# 3252. Integrações entre organizações

Integrações entre organizações deverão declarar:

- papéis;
- autoridade;
- responsabilidade;
- escopo;
- finalidade;
- retenção;
- compartilhamentos posteriores;
- mecanismo de revogação.

# 3253. Dispositivos compartilhados

Em dispositivos compartilhados, a integração deverá:

- reduzir prévias;
- ocultar categorias sensíveis;
- exigir autenticação;
- limitar ações rápidas;
- evitar persistência desnecessária;
- preservar identidade individual.

# 3254. Integrações temporárias e pessoais

Uma integração temporária deverá possuir:

- início;
- finalidade;
- validade;
- campos;
- término;
- descarte;
- possibilidade de renovação;
- revogação.

# 3255. Integrações com oportunidades compartilhadas

Oportunidades destinadas a grupos deverão distinguir:

- elegibilidade coletiva;
- elegibilidade individual;
- disponibilidade;
- quantidade;
- responsabilidade;
- decisão pessoal;
- efeitos sobre terceiros.

# 3256. Eventos funcionais de integração

Deverão ser previstos, entre outros:

- `IntegracaoDeIntervencaoProposta`;
- `IntegracaoDeIntervencaoAdmitida`;
- `IntegracaoDeIntervencaoRejeitada`;
- `IntegracaoDeIntervencaoConectada`;
- `IntegracaoDeIntervencaoPausada`;
- `IntegracaoDeIntervencaoRetomada`;
- `IntegracaoDeIntervencaoDesconectada`;
- `SincronizacaoDeIntervencaoIniciada`;
- `SincronizacaoDeIntervencaoConcluida`;
- `SincronizacaoDeIntervencaoPendente`;
- `DivergenciaDeIntervencaoReconhecida`;
- `IntegracaoDeIntervencaoReconciliada`;
- `RevogacaoDeIntegracaoSolicitada`;
- `RevogacaoDeIntegracaoPropagada`;
- `FalhaDeIntegracaoDeIntervencaoReconhecida`.

# 3257. Falha parcial

Falha parcial deverá identificar:

- produtores afetados;
- consumidores afetados;
- dados entregues;
- dados pendentes;
- efeitos aplicados;
- efeitos não aplicados;
- risco de duplicidade;
- ação de recuperação.

# 3258. Falha externa

Falha de sistema externo deverá:

- preservar estado interno válido;
- impedir falsa conclusão;
- limitar repetição;
- informar dependências;
- permitir canal alternativo;
- registrar indisponibilidade.

# 3259. Correções e retroatividade

Correções deverão distinguir:

- momento do fato;
- momento do conhecimento;
- momento da correção;
- consumidores já afetados;
- efeitos reversíveis;
- efeitos irreversíveis;
- necessidade de nova intervenção.

# 3260. Reconstrução

O fluxo deverá ser reconstruível por:

- contratos;
- versões;
- eventos;
- decisões;
- permissões;
- sincronizações;
- correções;
- revogações;
- falhas;
- efeitos.

# 3261. Observabilidade

A integração deverá permitir observar:

- disponibilidade;
- latência;
- falhas;
- duplicidades;
- divergências;
- filas;
- revogações pendentes;
- consumidores incompatíveis;
- exposição indevida;
- ciclos.

# 3262. Explicabilidade

O participante deverá poder compreender:

- qual integração foi utilizada;
- por qual finalidade;
- quais dados foram recebidos;
- qual fonte originou;
- por que a manifestação ocorreu;
- quais consumidores receberam;
- como pausar;
- como desconectar;
- como revogar.

# 3263. Auditoria

A auditoria deverá reconstruir:

> fonte → integração → recorte → avaliação → decisão → manifestação → resposta → efeito → correção ou revogação

# 3264. Métricas

Métricas futuras poderão avaliar:

- integrações sem finalidade;
- excesso de dados;
- autoridade incompatível;
- relações comerciais omitidas;
- divergências não resolvidas;
- falhas de idempotência;
- eventos fora de ordem;
- revogações não propagadas;
- ciclos automáticos;
- falhas parciais ocultadas;
- tempo de recuperação;
- capacidade de reconstrução.

As métricas deverão avaliar o sistema.

# 3265. Responsabilidades dos produtores

Produtores deverão:

1. validar identidade;
2. declarar autoridade;
3. declarar finalidade;
4. preservar proveniência;
5. classificar sensibilidade;
6. minimizar dados;
7. versionar contratos;
8. garantir idempotência;
9. reconhecer correções;
10. propagar revogações.

# 3266. Responsabilidades dos consumidores

Consumidores deverão:

1. validar versão;
2. validar finalidade;
3. respeitar autoridade;
4. limitar escopo;
5. preservar significado;
6. aplicar permissões;
7. tratar duplicidade;
8. respeitar ordenação;
9. aplicar revogações;
10. registrar efeitos.

# 3267. Responsabilidades dos executores e canais

Executores e canais deverão:

- confirmar somente efeitos próprios;
- diferenciar envio e entrega;
- preservar sensibilidade;
- respeitar preferências;
- aplicar horários protegidos;
- evitar repetição indevida;
- informar falhas;
- não ampliar conteúdo.

# 3268. Comportamentos proibidos

As integrações não deverão:

1. transferir titularidade da jornada;
2. ampliar autoridade;
3. permitir acesso irrestrito;
4. ocultar finalidade;
5. ocultar relação comercial;
6. utilizar contexto sensível para publicidade;
7. fabricar urgência;
8. inferir intenção por comportamento técnico;
9. inferir consentimento por atenção;
10. transformar visualização em interesse;
11. transformar resposta em progresso;
12. copiar histórico integral sem necessidade;
13. formar perfil paralelo de terceiro;
14. reter dados indefinidamente;
15. impedir revogação;
16. declarar revogação antes da propagação;
17. sobrescrever conflitos;
18. duplicar efeitos;
19. criar ciclos automáticos;
20. declarar sucesso após falha parcial;
21. concluir operação externa sem retorno;
22. utilizar localização como intenção;
23. utilizar vínculo organizacional como titularidade;
24. produzir ranking moral;
25. substituir decisão do participante.

# 3269. Critérios de aceite

A extensão será considerada consolidada quando:

1. definir integração funcional;
2. preservar titularidade;
3. definir princípios;
4. definir tipos e modos;
5. definir contrato comum;
6. definir produtores e consumidores;
7. governar finalidade;
8. governar escopo;
9. governar sensibilidade;
10. governar proveniência;
11. governar temporalidades;
12. separar correlação e causalidade;
13. governar versão;
14. governar idempotência;
15. governar permissões;
16. governar retenção;
17. governar relações comerciais;
18. governar admissão e rejeição;
19. governar identidade;
20. governar autoridade;
21. separar qualidade, confiança e autoridade;
22. governar transformações;
23. limitar finalidade;
24. assegurar minimização;
25. governar consentimento;
26. governar pausa e desconexão;
27. governar revogação e propagação;
28. governar sincronização;
29. governar divergência;
30. governar concorrência;
31. impedir ciclos;
32. governar tempo real e lote;
33. assegurar falha segura;
34. integrar todas as capacidades do Journey;
35. limitar Guivos Intelligence;
36. limitar Platform Layer;
37. integrar os produtos especializados;
38. proteger organizações e profissionais;
39. proteger setores sensíveis;
40. governar canais;
41. proteger terceiros;
42. assegurar observabilidade;
43. assegurar explicabilidade;
44. assegurar auditoria;
45. manter o participante no controle.

# 3270. Regras fundamentais

1. Integração não transfere titularidade.
2. Integração não amplia autoridade.
3. Acesso técnico não representa legitimidade funcional.
4. Finalidade deve ser específica.
5. Dados devem ser minimizados.
6. Fonte e proveniência devem permanecer identificáveis.
7. Momento do fato e momento do registro permanecem distintos.
8. Correlação não representa causalidade.
9. Qualidade técnica não representa autoridade.
10. Confiança funcional não representa certeza.
11. Relação comercial não eleva relevância.
12. Patrocínio não aumenta prioridade.
13. Comissão não cria urgência.
14. Integração sensível não alimenta publicidade.
15. Consentimento é granular e revogável.
16. Pausa não representa desconexão.
17. Desconexão não representa apagamento integral.
18. Revogação interrompe novos usos.
19. Revogação somente termina após propagação suficiente.
20. Retenção pós-revogação deve possuir fundamento.
21. Sincronização parcial não representa conclusão.
22. Divergências permanecem visíveis.
23. Conflitos não são sobrescritos silenciosamente.
24. Reprocessamento não duplica efeitos.
25. Eventos fora de ordem não criam estados impossíveis.
26. Alterações concorrentes exigem reconciliação.
27. Ciclos automáticos devem ser impedidos.
28. Tempo real não autoriza vigilância.
29. Localização não representa intenção.
30. Visualização não representa interesse.
31. Atenção não representa consentimento.
32. Resposta não representa progresso.
33. Produto executor confirma suas próprias operações.
34. Intervenções Contextuais decide a manifestação, não a transação.
35. Contexto Vivo fornece recortes, não acesso integral.
36. Objetivos não são criados por integração.
37. Próximos Passos não são confirmados por integração.
38. Oportunidades não são apresentadas apenas por existirem.
39. Experiências não são declaradas automaticamente.
40. Evolução humana não deve alimentar segmentação comercial.
41. Guivos Intelligence pode sugerir, mas não impor.
42. Platform Layer transporta, mas não define relevância humana.
43. Falha parcial não representa sucesso integral.
44. Métricas avaliam o sistema.
45. O participante permanece no controle.

# 3271. Continuidade normativa

`PAS-001-IC-INTEGRATION-001 1.0.0` é registrado como a **quinta extensão normativa da Capacidade 07 — Intervenções Contextuais**.

A extensão:

- preserva as quatro extensões normativas anteriores;
- preserva o `PAS-001 0.5.0`;
- mantém as Capacidades 02 a 06 como `Functionally complete`;
- mantém a Capacidade 07 como `In progress`;
- eleva o progresso editorial de `80%` para `90%`;
- preserva a Capacidade 08 como `Planned`;
- consolida os contratos das integrações;
- governa finalidade, autoridade, minimização, proveniência e sensibilidade;
- governa sincronização, divergência, revogação e propagação;
- integra capacidades, produtos, organizações, profissionais, canais e sistemas externos;
- impede ciclos, vigilância e interferência comercial;
- assegura observabilidade, explicabilidade, auditoria e falha segura;
- estabelece o contrato final da capacidade como próxima etapa normativa.

O próximo bloco será:

> **KPIs, guardrails, baseline funcional, painel de saúde, níveis de desempenho, cenários funcionalmente ideal, alternativo e limite, critérios de conclusão, lacunas bloqueantes e não bloqueantes, critérios de reabertura e contrato final da Capacidade de Intervenções Contextuais.**
