---
id: PAS-001-OA-LIFECYCLE-001
title: Regras do Ciclo de Vida das Oportunidades Ativas
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-14
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-OA-FOUNDATION-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - GLPA-001
  - GIA-000
  - GE2-SYNC-006
  - GE2-SYNC-007
---

# PAS-001-OA-LIFECYCLE-001 — Regras do Ciclo de Vida das Oportunidades Ativas

## 1. Autoridade e vínculo

Este documento é a **segunda extensão normativa da Capacidade 06 — Oportunidades Ativas** do `PAS-001 — Guivos Journey Product Architecture Specification`.

Seu conteúdo deve ser lido como continuidade do `PAS-001-OA-FOUNDATION-001 1.0.0`, das seções 2061 a 2138 e do `PAS-001 0.5.0`.

Esta extensão mantém a capacidade no estado `In progress` e eleva o progresso editorial de referência de `20%` para `40%`.

# 2139. Finalidade do ciclo de vida

O ciclo de vida deverá governar como uma possibilidade externa ou interna passa por identificação, avaliação, ativação, apresentação, atualização e encerramento.

O ciclo deverá impedir que:

- qualquer item disponível seja tratado como relevante;
- publicidade seja tratada como oportunidade funcional;
- interesse seja presumido;
- disponibilidade desatualizada permaneça ativa;
- elegibilidade seja confundida com aprovação;
- contratação seja confundida com benefício recebido;
- comissão, patrocínio ou estoque alterem relevância;
- uma oportunidade encerrada continue produzindo intervenções.

# 2140. Fluxo funcional geral

```text
sinal ou fonte
→ oportunidade identificada
→ oportunidade candidata
→ validação da identidade e da fonte
→ avaliação de autoridade
→ avaliação de completude
→ avaliação de disponibilidade
→ avaliação de elegibilidade
→ avaliação de relevância
→ avaliação de risco e sensibilidade
→ verificação comercial
→ ativação funcional
→ decisão de apresentação
→ relação do participante
→ eventual vínculo com Próximo Passo
→ atualização, pausa, expiração ou encerramento
→ arquivamento
```

# 2141. Dimensões independentes

O ciclo deverá preservar separadamente:

1. estado funcional da oportunidade;
2. estado da informação;
3. disponibilidade;
4. elegibilidade;
5. relevância;
6. risco;
7. sensibilidade;
8. relação comercial;
9. relação individual do participante;
10. decisão de apresentação;
11. vínculo com Próximo Passo;
12. situação transacional externa.

Nenhuma dessas dimensões deverá substituir automaticamente as demais.

# 2142. Estado funcional da oportunidade

Os estados funcionais serão:

- Identificada;
- Candidata;
- Em avaliação;
- Ativa;
- Pausada;
- Indisponível;
- Encerrada;
- Expirada;
- Cancelada;
- Contestada;
- Corrigida;
- Arquivada.

# 2143. Estado da informação

O estado da informação poderá ser:

- completo;
- parcialmente completo;
- insuficiente;
- pendente de verificação;
- atualizado;
- potencialmente desatualizado;
- desatualizado;
- divergente;
- contestado;
- corrigido;
- indisponível.

Uma oportunidade poderá estar funcionalmente ativa e possuir informação parcialmente desatualizada, desde que os efeitos sejam limitados e a condição seja apresentada com transparência.

# 2144. Estado de disponibilidade

A disponibilidade deverá possuir ciclo próprio:

- não avaliada;
- prevista;
- disponível;
- limitada;
- sob consulta;
- lista de espera;
- abertura futura;
- temporariamente indisponível;
- esgotada;
- encerrada;
- cancelada;
- expirada;
- desconhecida;
- contestada.

# 2145. Estado de elegibilidade

A elegibilidade deverá possuir ciclo próprio:

- não avaliada;
- informação insuficiente;
- possivelmente elegível;
- elegível;
- elegível com condição;
- exige verificação;
- possivelmente não elegível;
- não elegível;
- contestada;
- expirada.

# 2146. Estado de relevância

A relevância poderá ser:

- não avaliada;
- insuficiente;
- baixa;
- moderada;
- alta;
- condicionada;
- temporariamente reduzida;
- desatualizada;
- contestada;
- não aplicável.

Relevância não deverá representar recomendação definitiva.

# 2147. Relação individual do participante

A relação do participante deverá permanecer separada do estado da oportunidade.

Estados possíveis:

- não apresentada;
- apresentada;
- visualizada;
- salva;
- interesse declarado;
- descartada;
- ocultada;
- inscrição iniciada;
- inscrição enviada;
- aceita externamente;
- recusada externamente;
- contratada;
- cancelada pelo participante;
- participação iniciada;
- participação concluída;
- relação encerrada.

# 2148. Situação transacional externa

A situação transacional poderá registrar fatos como:

- carrinho iniciado;
- reserva iniciada;
- pagamento pendente;
- pagamento confirmado;
- contratação confirmada;
- inscrição enviada;
- inscrição aprovada;
- inscrição rejeitada;
- entrega pendente;
- entrega concluída;
- serviço agendado;
- serviço realizado;
- cancelamento solicitado;
- reembolso pendente;
- reembolso concluído.

Esses fatos não deverão redefinir automaticamente relevância, experiência, resultado ou evolução.

# 2149. Transições fundamentais

O fluxo principal poderá seguir:

```text
Identificada
→ Candidata
→ Em avaliação
→ Ativa
```

Após a ativação, a oportunidade poderá transitar para:

```text
Ativa
→ Pausada
→ Ativa
```

```text
Ativa
→ Indisponível
→ Ativa
```

```text
Ativa
→ Expirada
→ Arquivada
```

```text
Ativa
→ Encerrada
→ Arquivada
```

```text
Ativa
→ Cancelada
→ Arquivada
```

```text
qualquer estado material
→ Contestada
→ Corrigida
→ estado funcional aplicável
```

# 2150. Transições proibidas

Não deverão ocorrer diretamente:

- Identificada → interesse declarado;
- Candidata → contratada;
- Em avaliação → inscrição enviada;
- Ativa → participação concluída;
- visualizada → interesse declarado;
- salva → inscrição iniciada;
- inscrição enviada → aceita sem fonte autorizada;
- compra confirmada → experiência concluída;
- oportunidade expirada → ativa sem nova avaliação;
- oportunidade corrigida → estado anterior sem registro da correção.

# 2151. Identificação

Uma oportunidade poderá ser identificada por:

- participante;
- fornecedor;
- organização;
- curadoria;
- busca;
- catálogo;
- integração;
- fonte pública;
- Guivos Intelligence;
- produto especializado;
- parceiro;
- patrocinador;
- profissional.

A identificação não representa admissão nem relevância.

# 2152. Identificação por sinal

Sinais poderão indicar a possível existência de uma oportunidade.

Exemplos:

- publicação;
- anúncio;
- vaga;
- evento;
- programa;
- benefício;
- produto;
- serviço;
- convite;
- edital;
- campanha;
- disponibilidade informada.

Sinais não deverão produzir ativação diretamente.

# 2153. Criação da candidatura

Uma oportunidade deverá tornar-se `Candidata` quando possuir:

- identidade mínima;
- natureza compreensível;
- fonte identificável;
- possível participante ou público;
- finalidade de avaliação;
- ausência de proibição imediata.

# 2154. Rejeição antes da avaliação

Uma candidata poderá ser rejeitada antes da avaliação quando:

- a fonte for fraudulenta;
- a identidade não puder ser estabelecida;
- a finalidade for ilegítima;
- a oportunidade for proibida;
- houver exploração explícita de vulnerabilidade;
- o conteúdo for publicidade disfarçada;
- não houver condições mínimas;
- a relação comercial for deliberadamente ocultada.

A rejeição deverá ser registrada sem criar Oportunidade Ativa.

# 2155. Início da avaliação

A candidata deverá entrar em `Em avaliação` quando o sistema iniciar verificações de:

- fonte;
- autoridade;
- disponibilidade;
- elegibilidade;
- relevância;
- risco;
- sensibilidade;
- temporalidade;
- custo;
- relação comercial;
- permissões.

# 2156. Validação da fonte

A fonte deverá ser avaliada quanto a:

- identidade;
- autenticidade;
- autoridade;
- atualidade;
- histórico;
- escopo;
- confiabilidade;
- conflitos de interesse;
- capacidade de correção;
- disponibilidade para auditoria.

# 2157. Limite da autoridade

A fonte somente poderá confirmar fatos dentro de seu escopo.

Exemplos:

- fornecedor confirma características próprias;
- organização confirma regras de seu programa;
- plataforma comercial confirma estoque registrado;
- instituição pública confirma edital publicado;
- profissional confirma orientação dentro de sua competência;
- patrocinador confirma patrocínio;
- Guivos Intelligence estima compatibilidade, mas não confirma fatos externos sem fonte.

# 2158. Avaliação de completude

A completude deverá verificar se existem informações suficientes sobre:

- natureza;
- fornecedor;
- condições;
- disponibilidade;
- elegibilidade;
- temporalidade;
- custo;
- localização;
- risco;
- relação comercial;
- forma de acesso;
- limitações.

Informação insuficiente poderá manter a oportunidade em avaliação ou limitar sua apresentação.

# 2159. Avaliação de disponibilidade

A disponibilidade deverá considerar:

- estoque;
- vagas;
- inscrições;
- período;
- capacidade;
- localização;
- atendimento;
- modalidade;
- restrições;
- confirmação da fonte;
- última atualização.

# 2160. Disponibilidade presumida

Disponibilidade não deverá ser presumida apenas porque a oportunidade:

- aparece em busca;
- permanece publicada;
- foi anteriormente utilizada;
- existe em catálogo;
- possui preço;
- possui página ativa;
- foi indicada por outro participante.

# 2161. Disponibilidade futura

Uma oportunidade com abertura futura poderá permanecer candidata ou ativa de forma condicionada quando:

- a previsão for suficientemente confiável;
- a data ou condição estiver clara;
- não for apresentada como disponível no presente;
- o participante puder controlar notificações;
- a informação possuir validade definida.

# 2162. Disponibilidade limitada

A condição limitada deverá apresentar:

- natureza da limitação;
- quantidade conhecida ou estimada;
- fonte;
- momento da verificação;
- possibilidade de alteração;
- ausência de garantia.

Escassez não deverá produzir urgência pessoal automática.

# 2163. Lista de espera

A lista de espera deverá ser distinguida de disponibilidade imediata.

A oportunidade poderá permanecer ativa quando a lista de espera representar uma alternativa legítima e compreensível.

# 2164. Avaliação de elegibilidade

A elegibilidade deverá considerar apenas critérios necessários e autorizados.

Poderão ser avaliados:

- idade;
- localização;
- formação;
- experiência;
- vínculo institucional;
- renda;
- condição documental;
- disponibilidade;
- requisitos técnicos;
- critérios públicos;
- regras do programa.

# 2165. Elegibilidade sensível

Critérios sensíveis somente poderão ser avaliados quando:

- necessários;
- explícitos;
- autorizados;
- limitados à finalidade;
- protegidos;
- sujeitos a contestação;
- baseados em fonte legítima.

# 2166. Elegibilidade condicionada

Uma oportunidade poderá ser `elegível com condição` quando depender de:

- documento;
- aprovação;
- pagamento;
- avaliação;
- inscrição;
- entrevista;
- exame;
- vaga;
- autorização;
- conclusão prévia;
- requisito futuro.

A condição deverá permanecer visível.

# 2167. Elegibilidade não confirmada

`Possivelmente elegível` não deverá ser apresentada como elegibilidade confirmada.

`Provavelmente não elegível` não deverá bloquear a apresentação quando:

- houver incerteza significativa;
- a decisão final pertencer a terceiro;
- existir possibilidade legítima de exceção;
- o participante puder corrigir dados.

# 2168. Avaliação de relevância

A relevância deverá considerar a relação entre oportunidade e:

- contexto autorizado;
- objetivo;
- Próximo Passo;
- Evento de Vida;
- necessidade;
- preferência;
- restrição;
- capacidade;
- custo;
- risco;
- localização;
- temporalidade;
- elegibilidade;
- disponibilidade;
- alternativas.

# 2169. Relevância condicionada

A relevância poderá depender de:

- confirmação do participante;
- conclusão de dependência;
- mudança de contexto;
- disponibilidade futura;
- redução de risco;
- obtenção de recurso;
- aprovação institucional;
- condição temporal.

# 2170. Relevância desatualizada

A relevância deverá ser revisada quando ocorrer:

- mudança de objetivo;
- mudança de Próximo Passo;
- Evento de Vida;
- alteração de localização;
- mudança de orçamento;
- alteração de preferência;
- restrição nova;
- mudança de disponibilidade;
- alteração de risco;
- correção de informação.

# 2171. Avaliação de risco

O risco deverá ser avaliado de forma proporcional.

A avaliação poderá resultar em:

- risco não material;
- risco baixo;
- risco moderado;
- risco elevado;
- exige análise especializada;
- apresentação limitada;
- apresentação proibida;
- avaliação pendente.

# 2172. Risco elevado

Uma oportunidade de risco elevado somente poderá ser ativada quando:

- sua apresentação for legítima;
- os riscos estiverem explicitados;
- houver autoridade adequada;
- não existir exploração de vulnerabilidade;
- a decisão permanecer com o participante;
- orientações profissionais forem preservadas;
- os efeitos automáticos forem limitados.

# 2173. Avaliação de sensibilidade

A sensibilidade deverá controlar:

- uso de contexto;
- indexação;
- busca;
- notificações;
- títulos;
- compartilhamento;
- retenção;
- publicidade;
- auditoria;
- acesso organizacional.

# 2174. Verificação comercial

Antes da ativação, deverão ser identificados:

- fornecedor;
- comissão;
- afiliação;
- patrocínio;
- promoção paga;
- exclusividade;
- participação na receita;
- vantagem comercial da Guivos;
- financiamento;
- relação indireta relevante.

# 2175. Alteração comercial durante o ciclo

Mudanças de patrocínio, comissão ou relação contratual deverão:

- atualizar o registro;
- preservar histórico;
- reavaliar transparência;
- reavaliar ordenação;
- não alterar relevância funcional por si mesmas;
- não ocultar alternativas.

# 2176. Ativação funcional

Uma oportunidade poderá tornar-se `Ativa` quando atender ao limiar de ativação definido nos fundamentos.

A ativação deverá registrar:

- momento;
- versão;
- critérios atendidos;
- critérios pendentes;
- confiança;
- fonte;
- validade;
- limitações;
- relação comercial;
- participante ou público aplicável.

# 2177. Ativação condicionada

Uma oportunidade poderá ser ativada de forma condicionada quando:

- a condição estiver explícita;
- a informação pendente não representar risco crítico;
- a apresentação puder ser proporcional;
- a ausência da condição não for ocultada;
- não houver garantia indevida.

# 2178. Ativação não representa apresentação

Uma oportunidade ativa poderá permanecer não apresentada.

A decisão de apresentação pertence à Capacidade de Intervenções Contextuais e deverá considerar:

- momento;
- atenção;
- sensibilidade;
- urgência real;
- preferência;
- fadiga;
- canal;
- necessidade de silêncio;
- alternativas.

# 2179. Ativação não representa recomendação

A oportunidade ativa poderá ser:

- uma alternativa;
- uma possibilidade;
- uma opção secundária;
- uma opção condicionada;
- uma opção de reserva;
- uma oportunidade informativa.

Ela não deverá ser apresentada como melhor escolha sem fundamento comparativo suficiente.

# 2180. Manutenção do estado ativo

Uma oportunidade ativa deverá permanecer sujeita a revisão de:

- disponibilidade;
- validade;
- elegibilidade;
- relevância;
- risco;
- custo;
- condições;
- relação comercial;
- fonte;
- permissões.

# 2181. Horizonte de revisão

A frequência de revisão deverá considerar:

- volatilidade;
- sensibilidade;
- prazo;
- tipo de oportunidade;
- autoridade da fonte;
- risco;
- disponibilidade;
- importância da decisão;
- histórico de mudanças.

# 2182. Atualização silenciosa

Atualizações poderão ocorrer sem interromper o participante quando:

- não alterarem materialmente a decisão;
- não aumentarem risco;
- não reduzirem direitos;
- não alterarem custo relevante;
- não modificarem elegibilidade;
- não alterarem relação comercial;
- permanecerem auditáveis.

# 2183. Atualização material

Mudanças materiais deverão ser apresentadas quando afetarem:

- preço;
- elegibilidade;
- disponibilidade;
- prazo;
- localização;
- risco;
- fornecedor;
- patrocínio;
- condições;
- cancelamento;
- alternativa escolhida;
- compromisso já iniciado.

# 2184. Pausa

Uma oportunidade poderá ser pausada quando:

- a fonte estiver temporariamente indisponível;
- a revisão estiver pendente;
- houver conflito;
- o participante limitar seu uso;
- a relação comercial estiver sob análise;
- o risco precisar de reavaliação;
- houver suspensão temporária do programa.

# 2185. Efeitos da pausa

Durante a pausa:

- novas apresentações deverão ser suspensas;
- recomendações dependentes deverão ser revistas;
- notificações deverão ser limitadas;
- relações históricas deverão ser preservadas;
- transações externas existentes não deverão ser apagadas;
- o participante deverá ser informado quando houver impacto material.

# 2186. Retomada

A oportunidade pausada poderá retornar a `Ativa` após:

- resolução da causa;
- revalidação;
- atualização;
- análise de risco;
- confirmação de disponibilidade;
- recomposição de permissões;
- nova versão funcional.

# 2187. Indisponibilidade

A oportunidade deverá tornar-se `Indisponível` quando não puder ser utilizada no momento, mas sua retomada permanecer possível.

A indisponibilidade deverá registrar:

- causa;
- início;
- expectativa de retorno;
- fonte;
- alternativas;
- impactos sobre interessados;
- revisão futura.

# 2188. Indisponibilidade não representa encerramento

Uma oportunidade indisponível poderá retornar a ativa.

Ela não deverá:

- ser apresentada como disponível;
- manter urgência;
- iniciar novas inscrições;
- gerar contratação;
- permanecer na ordem principal sem justificativa.

# 2189. Expiração

A oportunidade deverá expirar quando:

- sua janela terminar;
- a validade da informação vencer;
- a condição temporal deixar de existir;
- a elegibilidade depender de período encerrado;
- o evento relacionado já tiver ocorrido;
- a oferta perder validade.

# 2190. Expiração e relação do participante

A expiração não deverá apagar:

- visualizações;
- salvamentos;
- interesse declarado;
- inscrições;
- contratações;
- participação;
- histórico;
- evidências de comunicação.

# 2191. Encerramento

A oportunidade deverá ser encerrada quando:

- o programa terminar;
- a ação for concluída;
- o fornecedor encerrar a oferta;
- o benefício deixar de existir;
- a oportunidade cumprir sua finalidade;
- não houver previsão de retorno.

# 2192. Cancelamento

A oportunidade deverá ser cancelada quando sua interrupção decorrer de decisão explícita do responsável.

O cancelamento deverá ser distinguido de:

- expiração;
- encerramento regular;
- indisponibilidade;
- esgotamento;
- pausa;
- contestação.

# 2193. Contestação

Poderão ser contestados:

- identidade;
- fonte;
- disponibilidade;
- elegibilidade;
- custo;
- risco;
- patrocínio;
- relação comercial;
- relevância;
- descrição;
- localização;
- condições;
- tratamento de dados.

# 2194. Efeitos da contestação

Uma contestação material deverá:

- limitar apresentação;
- suspender automações;
- impedir afirmações definitivas;
- preservar versões;
- registrar o contestante;
- encaminhar avaliação;
- proteger o participante;
- evitar exclusão silenciosa.

# 2195. Correção

A correção deverá ocorrer por registro compensatório.

Ela deverá preservar:

- valor anterior;
- valor corrigido;
- fonte;
- motivo;
- momento;
- efeitos aplicados;
- consumidores notificados;
- necessidade de reavaliação.

# 2196. Reativação após correção

Uma oportunidade corrigida poderá retornar a:

- Em avaliação;
- Ativa;
- Pausada;
- Indisponível;
- Expirada;
- Encerrada.

O retorno deverá depender do conteúdo corrigido.

# 2197. Arquivamento

O arquivamento deverá retirar a oportunidade do uso operacional corrente sem apagar seu histórico.

Poderão ser arquivadas oportunidades:

- encerradas;
- expiradas;
- canceladas;
- rejeitadas;
- substituídas;
- sem relevância atual;
- duplicadas;
- descontinuadas.

# 2198. Reabertura

Uma oportunidade arquivada somente deverá ser reaberta quando:

- a mesma oportunidade retornar legitimamente;
- a fonte confirmar nova janela;
- as condições forem renovadas;
- houver correção relevante;
- o ciclo anterior puder ser preservado;
- não se tratar de oportunidade materialmente nova.

# 2199. Nova oportunidade ou reabertura

Deverá ser criado novo registro quando houver mudança material de:

- fornecedor;
- natureza;
- finalidade;
- público;
- condições centrais;
- risco;
- programa;
- identidade;
- obrigação contratual.

Uma nova edição periódica poderá preservar relação com a anterior sem reutilizar indevidamente o mesmo ciclo.

# 2200. Duplicidade

Duas oportunidades deverão ser avaliadas como duplicadas quando representarem o mesmo meio funcional com:

- mesmo fornecedor;
- mesmas condições;
- mesma janela;
- mesmo público;
- mesma finalidade;
- mesma identidade operacional.

# 2201. Unificação

A unificação deverá:

- preservar registros originais;
- escolher identidade canônica;
- consolidar fontes;
- preservar diferenças;
- recompor relações;
- impedir perda de interesse ou histórico;
- evitar duplicidade de apresentação.

# 2202. Oportunidades semelhantes

Oportunidades semelhantes não deverão ser unificadas quando diferirem materialmente em:

- custo;
- fornecedor;
- localização;
- risco;
- elegibilidade;
- qualidade;
- prazo;
- modalidade;
- condições;
- relação comercial.

# 2203. Substituição

Uma oportunidade poderá substituir outra como alternativa funcional.

A substituição não deverá:

- apagar a anterior;
- transferir interesse automaticamente;
- iniciar inscrição;
- criar compromisso;
- ocultar diferenças;
- preservar artificialmente prioridade.

# 2204. Alternativas

Alternativas deverão apresentar, quando possível:

- benefícios;
- limitações;
- custo;
- risco;
- elegibilidade;
- disponibilidade;
- distância;
- temporalidade;
- relação comercial;
- confiança da fonte.

# 2205. Comparação

A comparação deverá ser explicável e não poderá reduzir opções complexas a uma pontuação única sem fundamento suficiente.

Critérios de comparação deverão permanecer visíveis e ajustáveis quando apropriado.

# 2206. Ordem de apresentação

A ordem poderá considerar:

- compatibilidade;
- disponibilidade;
- elegibilidade;
- temporalidade;
- custo;
- risco;
- preferência;
- localização;
- qualidade;
- confiança;
- diversidade de alternativas.

Não poderá considerar como fator funcional positivo:

- comissão;
- patrocínio;
- estoque patrocinado;
- valor da transação;
- probabilidade de clique;
- tempo de tela.

# 2207. Apresentação

A apresentação deverá registrar:

- oportunidade;
- participante;
- canal;
- momento;
- finalidade;
- justificativa;
- versão;
- sensibilidade;
- relação comercial;
- alternativas mostradas;
- decisão da Intervenção Contextual.

# 2208. Visualização

A visualização representa acesso ao conteúdo.

Ela não deverá produzir automaticamente:

- interesse;
- prioridade;
- salvamento;
- inscrição;
- contratação;
- compartilhamento;
- recomendação futura mais intensa.

# 2209. Salvamento

Salvar representa intenção de preservar a oportunidade para consulta posterior.

Não representa:

- interesse definitivo;
- compromisso;
- prioridade;
- elegibilidade;
- inscrição;
- contratação.

# 2210. Interesse declarado

O interesse deverá depender de ação ou declaração suficientemente clara.

Ele poderá gerar:

- comparação;
- solicitação de detalhes;
- vínculo potencial com Próximo Passo;
- preparação;
- contato autorizado;
- início consciente de inscrição.

# 2211. Descarte

Descartar deverá permitir:

- remover da atenção;
- informar incompatibilidade;
- limitar reapresentação;
- registrar motivo opcional;
- preservar alternativas;
- não gerar penalidade.

# 2212. Ocultação

Ocultar deverá impedir reapresentação conforme escopo escolhido:

- oportunidade específica;
- fornecedor;
- categoria;
- tema;
- campanha;
- período;
- origem.

# 2213. Início de inscrição

A inscrição somente deverá ser iniciada por ação consciente ou autorização previamente delimitada.

O início deverá apresentar:

- destinatário;
- dados necessários;
- finalidade;
- termos;
- custos;
- possibilidade de cancelamento;
- responsabilidade externa.

# 2214. Envio de inscrição

O envio deverá exigir confirmação proporcional ao impacto.

O evento deverá registrar:

- conteúdo enviado;
- versão;
- destinatário;
- momento;
- autorização;
- protocolo;
- limitações;
- próximos estados externos possíveis.

# 2215. Aceitação externa

A aceitação por fornecedor ou organização não deverá representar:

- conclusão de Próximo Passo;
- experiência realizada;
- resultado;
- benefício recebido;
- evolução;
- aprovação global do participante.

# 2216. Contratação

A contratação pertence ao produto ou serviço responsável pela transação.

Oportunidades Ativas deverá receber somente o recorte necessário para atualizar a relação do participante.

# 2217. Participação

A participação poderá ser informada por:

- participante;
- organização;
- integração;
- presença objetiva;
- prestação do serviço;
- evento externo.

Participação não deverá confirmar resultado ou transformação.

# 2218. Vínculo com Próximo Passo

Uma oportunidade poderá ser vinculada como:

- meio principal;
- alternativa;
- recurso;
- fornecedor;
- local;
- serviço;
- conteúdo;
- experiência;
- apoio financeiro;
- apoio institucional.

# 2219. Efeitos sobre Próximos Passos

A alteração da oportunidade poderá solicitar reavaliação de:

- prontidão;
- dependência;
- bloqueio;
- custo;
- risco;
- agenda;
- alternativa;
- execução.

A oportunidade não deverá cancelar ou concluir o Próximo Passo diretamente.

# 2220. Efeitos sobre Intervenções Contextuais

Mudanças poderão solicitar revisão da decisão de:

- apresentar;
- lembrar;
- alertar;
- perguntar;
- aguardar;
- silenciar.

A capacidade de Oportunidades Ativas não deverá decidir sozinha o momento da interrupção.

# 2221. Efeitos sobre Objetivos

A oportunidade poderá apoiar um objetivo, mas suas alterações não deverão:

- redefinir direção;
- alterar prioridade estratégica;
- confirmar progresso;
- concluir objetivo;
- criar objetivo pessoal.

# 2222. Efeitos de Eventos de Vida

Um Evento de Vida poderá exigir reavaliação individual das oportunidades afetadas.

Exemplos:

- mudança de cidade;
- perda de renda;
- novo emprego;
- condição de saúde;
- mudança familiar;
- início de curso;
- alteração jurídica;
- mudança de disponibilidade.

# 2223. Oportunidades recorrentes

Oportunidades recorrentes deverão possuir:

- série;
- ocorrências;
- regras de repetição;
- disponibilidade por ocorrência;
- elegibilidade por período;
- capacidade;
- cancelamento individual;
- encerramento da série.

# 2224. Oportunidades coletivas

Uma oportunidade coletiva deverá distinguir:

- oportunidade global;
- capacidade total;
- participantes;
- elegibilidade individual;
- inscrições individuais;
- responsabilidades;
- conteúdos privados;
- estado coletivo;
- estado individual.

# 2225. Oportunidades institucionais

Organizações poderão apresentar oportunidades dentro de sua autoridade.

Elas não deverão:

- acessar o contexto pessoal integral;
- definir relevância pessoal absoluta;
- transformar obrigação em interesse;
- utilizar dados fora da finalidade;
- impedir contestação;
- ocultar relações comerciais.

# 2226. Oportunidades patrocinadas

O patrocínio poderá financiar:

- gratuidade;
- desconto;
- benefício;
- evento;
- conteúdo;
- programa;
- premiação;
- acesso.

O patrocínio deverá permanecer visível e não poderá elevar relevância funcional.

# 2227. Mudança de preço

Mudanças materiais de preço deverão:

- preservar o valor anterior;
- informar nova condição;
- registrar momento;
- reavaliar custo total;
- reavaliar relevância;
- notificar interessados quando necessário;
- permitir desistência sem penalidade indevida.

# 2228. Mudança de fornecedor

A mudança de fornecedor deverá provocar nova avaliação de:

- identidade;
- autoridade;
- qualidade;
- risco;
- condições;
- relação comercial;
- privacidade;
- responsabilidade.

# 2229. Mudança de risco

A elevação de risco poderá produzir:

- pausa;
- retirada de apresentação;
- alerta;
- solicitação de confirmação;
- análise especializada;
- cancelamento;
- arquivamento.

# 2230. Fonte indisponível

Quando a fonte ficar indisponível, a capacidade deverá:

- marcar desatualização;
- reduzir confiança;
- suspender atualizações automáticas;
- preservar último estado válido;
- limitar apresentação;
- buscar fonte alternativa legítima;
- não fabricar disponibilidade.

# 2231. Revogação de contexto

Quando o participante revogar o uso de contexto:

- novas avaliações dependentes deverão parar;
- novos recortes não deverão ser produzidos;
- oportunidades poderão permanecer salvas sem personalização;
- relações históricas legítimas poderão ser preservadas;
- publicidade não deverá assumir o lugar da personalização revogada.

# 2232. Propagação da revogação

A revogação somente deverá ser considerada concluída após:

- identificação dos consumidores;
- bloqueio de novos usos;
- recomposição de recortes;
- confirmação de processamento;
- registro de falhas;
- validação da propagação.

# 2233. Retroatividade

Informações recebidas posteriormente deverão distinguir:

- momento real do fato;
- momento do registro externo;
- momento do conhecimento;
- momento do processamento;
- momento da aplicação;
- efeitos reconstruíveis;
- efeitos não reversíveis.

# 2234. Idempotência

O reprocessamento não poderá duplicar:

- oportunidade;
- ativação;
- apresentação;
- interesse;
- salvamento;
- inscrição;
- notificação;
- vínculo;
- cancelamento;
- arquivamento.

# 2235. Ordenação

Eventos fora de ordem não poderão gerar:

- ativação após encerramento sem reabertura;
- apresentação após revogação;
- disponibilidade após expiração sem nova versão;
- aceitação antes do envio;
- contratação antes da confirmação externa;
- correção anterior à informação corrigida.

# 2236. Concorrência

Alterações concorrentes deverão utilizar:

- versão esperada;
- detecção de conflito;
- preservação das versões;
- reconciliação;
- ausência de sobrescrita silenciosa;
- auditoria.

# 2237. Falha segura

Em falha, a capacidade deverá:

- preservar último estado válido;
- impedir falsa disponibilidade;
- impedir falsa elegibilidade;
- impedir falsa ativação;
- suspender apresentação quando necessário;
- marcar pendência;
- evitar duplicidade;
- permitir recuperação;
- informar impacto material.

# 2238. Falha parcial

Uma operação parcialmente concluída deverá informar:

- o que foi processado;
- o que falhou;
- quais consumidores receberam atualização;
- quais ações permanecem pendentes;
- se existe risco de duplicidade;
- se o participante precisa agir.

# 2239. Eventos funcionais do ciclo

Deverão ser previstos, entre outros:

- `OportunidadeIdentificada`;
- `CandidaturaDeOportunidadeCriada`;
- `AvaliacaoDeOportunidadeIniciada`;
- `FonteDeOportunidadeValidada`;
- `FonteDeOportunidadeRejeitada`;
- `DisponibilidadeDeOportunidadeAvaliada`;
- `ElegibilidadeDeOportunidadeAvaliada`;
- `RelevanciaDeOportunidadeAvaliada`;
- `RiscoDeOportunidadeAvaliado`;
- `SensibilidadeDeOportunidadeClassificada`;
- `RelacaoComercialDeOportunidadeDeclarada`;
- `OportunidadeAtivada`;
- `OportunidadeAtivadaComCondicao`;
- `OportunidadePausada`;
- `OportunidadeRetomada`;
- `OportunidadeTornadaIndisponivel`;
- `OportunidadeDisponibilizadaNovamente`;
- `OportunidadeExpirada`;
- `OportunidadeEncerrada`;
- `OportunidadeCancelada`;
- `OportunidadeContestada`;
- `ContestacaoDeOportunidadeResolvida`;
- `OportunidadeCorrigida`;
- `OportunidadeArquivada`;
- `OportunidadeReaberta`;
- `OportunidadesDuplicadasIdentificadas`;
- `OportunidadesUnificadas`;
- `OportunidadeSubstitutaRegistrada`;
- `OportunidadeApresentada`;
- `OportunidadeVisualizada`;
- `OportunidadeSalva`;
- `InteresseEmOportunidadeDeclarado`;
- `OportunidadeDescartada`;
- `OportunidadeOcultada`;
- `InscricaoEmOportunidadeIniciada`;
- `InscricaoEmOportunidadeEnviada`;
- `AceitacaoExternaDeOportunidadeRegistrada`;
- `RecusaExternaDeOportunidadeRegistrada`;
- `ContratacaoRelacionadaRegistrada`;
- `ParticipacaoRelacionadaRegistrada`;
- `VinculoComProximoPassoRegistrado`;
- `VinculoComProximoPassoRemovido`;
- `PermissaoDeContextoRevogada`;
- `RevogacaoDeContextoPropagada`;
- `ProcessamentoDeOportunidadeFalhou`;
- `EstadoDeOportunidadeReconstruido`.

# 2240. Responsabilidades do ciclo

O ciclo será responsável por:

1. controlar identificação e candidatura;
2. validar fonte e autoridade;
3. avaliar completude;
4. governar disponibilidade;
5. governar elegibilidade;
6. governar relevância;
7. avaliar risco;
8. proteger sensibilidade;
9. declarar relações comerciais;
10. controlar ativação;
11. preservar estados independentes;
12. controlar apresentação;
13. registrar relação do participante;
14. governar pausa e retomada;
15. tratar indisponibilidade;
16. controlar expiração e encerramento;
17. permitir contestação e correção;
18. controlar duplicidade e unificação;
19. integrar Próximos Passos;
20. operar com falha segura.

# 2241. Limites do ciclo

O ciclo não será responsável por:

1. decidir objetivos;
2. criar compromissos pessoais;
3. determinar prioridade estratégica;
4. executar publicidade;
5. concluir transações;
6. prestar serviços;
7. garantir elegibilidade;
8. garantir disponibilidade;
9. garantir aprovação;
10. garantir benefício;
11. concluir Próximos Passos;
12. confirmar progresso;
13. medir evolução;
14. diagnosticar;
15. substituir profissionais;
16. definir valor humano;
17. utilizar vulnerabilidade;
18. criar urgência artificial;
19. impor participação;
20. ocultar interesses comerciais.

# 2242. Critérios de aceite

A extensão será considerada consolidada quando:

1. definir todas as dimensões independentes;
2. definir estados funcionais;
3. definir estados de informação;
4. definir disponibilidade;
5. definir elegibilidade;
6. definir relevância;
7. definir relação do participante;
8. definir situação transacional externa;
9. formalizar transições válidas;
10. bloquear transições indevidas;
11. governar identificação;
12. governar candidatura;
13. governar avaliação;
14. limitar autoridade;
15. governar ativação;
16. separar ativação de apresentação;
17. governar atualizações;
18. governar pausa e retomada;
19. governar indisponibilidade;
20. governar expiração;
21. governar encerramento e cancelamento;
22. permitir contestação e correção;
23. governar arquivamento e reabertura;
24. tratar duplicidade e unificação;
25. governar alternativas e comparação;
26. governar interação do participante;
27. governar inscrições e contratações sem absorvê-las;
28. integrar Próximos Passos e Intervenções;
29. aplicar revogação;
30. operar com idempotência, ordenação, concorrência e falha segura.

# 2243. Regras fundamentais

1. Identificação não representa candidatura.
2. Candidatura não representa ativação.
3. Avaliação não representa recomendação.
4. Ativação não representa apresentação.
5. Apresentação não representa visualização.
6. Visualização não representa interesse.
7. Salvamento não representa prioridade.
8. Interesse não representa compromisso.
9. Inscrição iniciada não representa inscrição enviada.
10. Inscrição enviada não representa aceitação.
11. Aceitação não representa contratação.
12. Contratação não representa participação.
13. Participação não representa resultado.
14. Resultado não representa evolução.
15. Disponibilidade não representa elegibilidade.
16. Elegibilidade não representa aprovação.
17. Relevância não representa obrigação.
18. Relação comercial não define relevância.
19. Patrocínio não altera prioridade funcional.
20. Escassez não fabrica urgência pessoal.
21. Estado funcional e estado da informação permanecem separados.
22. Estado da oportunidade e relação do participante permanecem separados.
23. A situação transacional não redefine a jornada.
24. Fonte somente confirma fatos dentro de sua autoridade.
25. Informação desatualizada reduz automação.
26. Oportunidade ativa pode permanecer não apresentada.
27. Oportunidade indisponível não deve ser apresentada como disponível.
28. Expiração não apaga histórico.
29. Cancelamento não equivale a fracasso.
30. Contestação limita efeitos materiais.
31. Correção não reescreve o histórico.
32. Reabertura exige nova avaliação.
33. Duplicidade não pode gerar múltiplas apresentações equivalentes.
34. Alternativas não patrocinadas não podem ser ocultadas.
35. Mudança comercial exige transparência.
36. Mudança de risco exige reavaliação.
37. Revogação interrompe novos usos.
38. Reprocessamento não duplica efeitos.
39. Falha parcial não representa sucesso integral.
40. O participante permanece no controle.

# 2244. Continuidade normativa

`PAS-001-OA-LIFECYCLE-001 1.0.0` deverá ser registrado como a **segunda extensão normativa da Capacidade 06 — Oportunidades Ativas**.

A extensão deverá:

- preservar o `PAS-001-OA-FOUNDATION-001 1.0.0`;
- manter as Capacidades 02, 03, 04 e 05 como `Functionally complete`;
- manter a Capacidade 06 como `In progress`;
- elevar o progresso editorial de `20%` para `40%`;
- consolidar os ciclos da oportunidade, da informação, da disponibilidade, da elegibilidade e da relação individual;
- separar ativação, apresentação, interesse, inscrição, aceitação, contratação e participação;
- preservar neutralidade comercial;
- garantir contestação, correção, revogação, idempotência e falha segura;
- definir a visualização e o controle como próxima etapa.

O bloco seguinte será:

> **Comportamentos funcionais da visualização e do controle das Oportunidades Ativas, incluindo descoberta, busca, filtros, cartões, detalhamento, comparação, alternativas, transparência comercial, elegibilidade, disponibilidade, custos, riscos, oportunidades sensíveis, controles do participante e consistência entre canais.**