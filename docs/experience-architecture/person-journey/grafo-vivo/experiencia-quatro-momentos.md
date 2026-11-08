---
title: Grafo Vivo — Experiência Conceitual nos Quatro Momentos
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: exploratory_non_operational
---

# Grafo Vivo — Experiência Conceitual nos Quatro Momentos

> Estudo **não normativo** para aprofundamento. Não cria telas, PER-IDs, ações oficiais, transições, autorizações, direitos de acesso, implementações, testes ou critérios de aceite normativos.

## 1. Confronto com autoridades da Jornada

A hipótese de um **Dashboard Vivo** deve ser examinada como experiência articulada com superfícies existentes, não como tela nova presumida.

| Autoridade existente | Papel vigente | Fronteira que a proposta deve respeitar |
| --- | --- | --- |
| PER-007 — Compreensão Inicial Revisável | Revisar origem, inferências, contestações; escolher **separadamente** persistência e personalização | Grafo não pode absorver nem dispensar a confirmação e escolhas de PER-007 |
| TRN-007 | Continuidade governada PER-007 → PER-008 | Nenhum acesso ao Grafo Vivo pode assumir bypass |
| PER-008 — Hoje | Síntese contextual na primeira entrada e no retorno | Não transformar Hoje em dashboard de performance humana, catálogo obrigatório ou feed |
| PER-010 — Meus Objetivos | Acompanhamento e revisão de objetivos | Grafo não cria, aceita, altera ou prioriza objetivos sozinho |
| PER-011 — Meus Próximos Passos | Organização e controle de próximos passos | Sugestões no grafo não se tornam passos assumidos |
| PER-012 — Minha Evolução | Trajetórias, baseline, evidência, interpretação e controle | Mudança de nó não comprova progresso ou evolução |
| GIA-COG-001 e GPA-006 | Responsabilidade de compreensão governada da Intelligence | Interface e provedor de áudio não assumem autoridade cognitiva |
| PAS-001 + Surface/Transition Registries | Ontologia, responsabilidades e transições | Não criar entidade de domínio nem navegação por inferência |

**Hipótese prioritária para exame posterior:** descobrir se perspectivas do Grafo Vivo podem funcionar como modos/estados legítimos em PER-008 e/ou aprofundamentos de PER-010/011/012. **Não adjudicado**: localização funcional do diálogo contínuo, da escuta e de eventuais visões expandidas. A ausência de autorização não é convite para implantar modalidades dentro da tela.

## 2. Momento A — Primeiro acesso ao contexto

**Pré-condição:** a Pessoa percorreu o processamento, revisão e escolhas legítimas pertinentes e chegou a PER-008 pelo fluxo governado.

### Experiência candidata

1. Hoje apresenta uma síntese simples, com ausência de histórico tratada legitimamente.
2. Quando existir compreensão apropriada e autorizada para a finalidade, a Pessoa pode conhecer as alternativas **Explorar visualmente, Escutar ou Conversar**.
3. A Pessoa escolhe livremente uma modalidade ou segue a Jornada sem usá-las.
4. Grafo: exibe somente elementos sustentados pelo contexto permitido, com progressão de complexidade.
5. Narração: explica o que a Intelligence compreendeu, o que permanece aberto e as possibilidades de aprofundar, sem fingir conhecer trajetória anterior.
6. Conversa: responde perguntas e pode pedir esclarecimentos sem pressupor memória duradoura ou personalização.

**Estados a estudar:** primeira entrada sem contexto elegível, compreensão parcial, personalização recusada, áudio indisponível, sem relações suficientes para grafo, ausência de histórico.

**Proibição:** geração automática de objetivos, experiências comprovadas, próximos passos ou evolução apenas para preencher o dashboard.

## 3. Momento B — Retorno à Jornada

**Pré-condição:** sessão autenticada e consulta ao estado canônico autorizado para a finalidade atual.

1. Recuperar referências ao contexto vigente conforme persistência e personalização autorizadas.
2. Apresentar síntese contextual sem alegar mudanças inexistentes.
3. Quando houver base temporal verificável, informar **o que foi alterado desde uma referência temporal identificável**; a ausência de mudança é legítima.
4. Oferecer retomada de exploração, escuta ou conversa, com versão apropriada e preservação de autonomia.
5. Informar se uma narração anterior está desatualizada; não substituir seu conteúdo silenciosamente.
6. Se uma permissão tiver sido revogada, não reutilizar conteúdo antigo por caches do grafo, transcrições ou áudio.

**Exemplo sintético:** uma informação de disponibilidade de tempo foi corrigida pela Pessoa. A interface pode explicar que determinadas relações foram reavaliadas, sem afirmar que a Pessoa evoluiu por essa correção.

## 4. Momento C — Conversa que introduz nova informação

**Exemplo:** "Comecei um curso de programação há dois meses".

1. Receber texto ou transcrição revisável e compreender a intenção comunicativa.
2. Identificar afirmação factual **declarada**, sem inferir conclusão do curso ou proficiência.
3. Consultar os limites de finalidade, persistência, personalização, sensibilidade e revisão existentes.
4. Se houver autorização apropriada, classificar e propor atualização contextual; resolver contradições/ambiguidades relevantes por confirmação.
5. Somente após a etapa governada de consolidação, atualizar a projeção relacional e reavaliar análises afetadas.
6. Opcionalmente mostrar "Nova informação considerada" e explicar o impacto; nunca usar aviso como consentimento presumido.
7. Permitir correção/contestação pelos caminhos governados.
8. Eventualmente oferecer nova síntese e narração, preservando versão de análise anterior.

**Caso de teste essencial:** "E se eu fizesse um curso?" deve gerar um cenário hipotético, não um curso iniciado na memória persistente.

**Caso sem persistência:** o diálogo pode utilizar informação temporalmente na sessão se isso estiver autorizado; não pode reter nem usar para personalização futura por inferência.

## 5. Momento D — Relatório narrado e interrupção

**Arquitetura de experiência candidata, sem seleção de provedor:** a Intelligence prepara uma representação narrativa derivada de um snapshot contextual com referência temporal e proveniência. Um adaptador de voz realiza síntese; interface de conversa pode receber perguntas durante a escuta.

Sequência candidata:
1. A Pessoa escolhe voluntariamente ouvir a análise.
2. A interface informa o escopo do relatório e a data/contexto utilizado; existe equivalente textual.
3. Inicia reprodução. Se desejado, o grafo acompanha por destaques explicativos, sem exigir acompanhamento visual.
4. A Pessoa pausa ou interrompe para perguntar por voz ou texto.
5. O serviço de conversa recebe somente o contexto mínimo necessário e a referência ao trecho narrado.
6. A resposta preserva incertezas e não transforma pergunta hipotética em fato.
7. A Pessoa decide retomar o relatório ou continuar conversando.
8. Se a conversa mudar materialmente o contexto consolidado, a interface sinaliza que o relatório anterior representa uma versão e pode oferecer uma nova análise; não reescreve áudio já gerado sem indicação.

**Grok/xAI:** candidato prioritário para Text-to-Speech e Speech-to-Speech; demais alternativas e arquitetura STT → modelo → TTS não estão excluídas. Guivos Intelligence permanece responsável por interpretação, autorizações e política de memória.

**Estados a estudar:** falha de microfone, interrupção de conexão, transcrição incerta, falha de síntese, atrasos, retomada após navegação, falta de áudio, perda de autorização, mudança de versão durante a narração.

## 6. Continuidade transversal

**Unidade conceitual de continuidade (não contrato técnico):**
- Identidade autorizada da Pessoa e escopos de finalidade;
- Referência à versão vigente da compreensão;
- Modalidade selecionada;
- Elemento ou conjunto focal do grafo;
- Versão de relatório e trecho de reprodução, quando houver;
- Sessão conversacional autorizada e hipótese temporária associada, quando aplicável;
- Estado de confirmação/correção/revogação;
- Preferências de acessibilidade e ritmo sem confundi-las com consentimento de retenção.

**Invariantes:**
- Trocar de modalidade não autoriza persistência nem personalização;
- Escutar não equivale a confirmar conclusões;
- Clique em nó não equivale a escolher próximo passo;
- Conversar não substitui governança de objetivos, oportunidades ou experiências;
- A visão visual e a narração devem explicar a mesma versão de contexto quando declaradas sincronizadas;
- Nenhuma modalidade pode ser a única forma de acessar informação essencial.

## 7. Integrações por momento — candidatos

| Momento | Integrações potencialmente envolvidas | Verificações antes de engenharia |
| --- | --- | --- |
| Primeiro acesso | Jornada/PER-007/008, Intelligence, fonte contextual, visualização e TTS opcional | Eleição legítima de persistência/personalização e conteúdo elegível |
| Retorno | Autenticação, memória governada, fonte canônica, grafo, armazenamento de versões | Autorizações vigentes, invalidação de caches, baseline temporal |
| Nova informação | Texto/voz, STT (Gemini ou alternativa), Intelligence/modelos, consentimento, armazenamento e grafo | Classificação, correção de transcrição, idempotência, confirmação e revogação |
| Narração e diálogo | Intelligence, roteiro/snapshot, Grok TTS/Voice ou alternativas, controle de reprodução, transcrição | Latência, custo, segurança, dados enviados, interrupções e coerência temporal |

## 8. Questões em aberto para a direção e autoridades

1. O acesso às três modalidades aparece diretamente em Hoje ou em aprofundamentos já reconhecidos? Exige exame do Surface Registry.
2. Há uma entrada discreta para relatório narrado quando não existe material suficiente para um grafo?
3. Que informação pode ser adicionada ao contexto em sessão e qual depende de autorização de persistência/permissão de personalização?
4. A atualização das relações será sinalizada em tempo real, por resumo de alterações ou por ação da Pessoa?
5. Qual comportamento quando uma análise deixa de ser atual durante a narração?
6. Que experiências equivalentes são necessárias para acessibilidade e modo sem áudio?
7. Como preservar interrupção/retomada sem manter áudio/transcrições além da finalidade autorizada?
8. Que capacidade de IA e voz poderá ser vinculada a planos, caso exista autorização comercial futura? Não inventar quotas nem preços.

## 9. Próximo exame recomendado

Elaborar **Matriz de Responsabilidades e Fronteiras Funcionais** com entradas/saídas, autoridades, dados/estados, eventos e lacunas para PER-007, PER-008, PER-010, PER-011, PER-012 e Intelligence. O estudo não deve selecionar uma nova tela nem adjudicar transições.

**Estado: estudo conceitual sujeito a revisão; sem alteração normativa, implementação, teste, Design operacional, integração real ou publicação de produto.**
