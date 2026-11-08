---
title: Grafo Vivo — Matriz de Gatilhos de Revalidação e Impacto Contextual
status: conceptual_study
version: 0.1.0
owner: Concepção de Produto / Jornada da Pessoa
last_updated: 2026-11-07
normative: false
maturity: diagnostic_non_operational
---

# Grafo Vivo — Matriz de Gatilhos de Revalidação e Impacto Contextual

> **Diagnóstico conceitual condicionado, não normativo.** O modelo de gatilhos não define algoritmo, thresholds, políticas de consentimento, retenção, identidade de objetos, eventos/APIs ou comportamentos já implementáveis. Não cria IDs oficiais. Autorizações e contratos vigentes têm precedência sobre este estudo.

## 1. Pergunta arquitetural

Quando uma informação nova em texto, voz ou anexo deve:
- permanecer apenas como fala/hipótese de sessão;
- ser interpretada sem atualização;
- exigir esclarecimento;
- ser candidata a consolidação em contexto autorizado;
- acionar reavaliação seletiva de relações, possibilidades e relatórios;
- suspender usos por correção, revogação ou conflito?

**Princípio:** a intensidade da revalidação deve responder ao risco, à natureza, à origem, à autorização e ao efeito da informação — **não somente à confiança numérica declarada pelo modelo**.

## 2. Autoridades e fronteiras preservadas

- `PER-007`: a compreensão inicial é revisável. Persistência e personalização exigem escolhas **independentes**; o direito de usar a sessão não permite memória duradoura.
- `PER-008`: Hoje é síntese contextual, sem score humano, diagnóstico ou implicação de avanço.
- `PER-010`: objetivos continuam sob autoria, revisão e decisão da Pessoa.
- `PER-011`: próximos passos não são aceitos, iniciados ou concluídos por inferência.
- `PER-012`: mudanças temporais não equivalem a evolução reconhecida.
- `PAS-001`, `GPA-006`, `GIA-COG-001`, `Surface Registry` e `Transition Registry`: preservados, sem extrapolação de competência.
- Privacidade/Dados/Segurança e políticas aplicáveis devem decidir formalmente coleta, retenção, compartilhamento e finalidades.

**Gatilhos são hipóteses de desenho, não permissões.** Nenhuma mudança é persistida sem autoridade e finalidade válidas, mesmo que seja explícita e pareça trivial.

## 3. Eixos que influenciam o tratamento (candidatos)

| Eixo | Pergunta |
| --- | --- |
| Natureza | Declaração explícita, inferência, pergunta, hipótese, objetivo, correção, negação ou evidência? |
| Fonte | Texto da Pessoa, transcrição incerta, arquivo, registro oficial, terceiro, IA? |
| Autoridade | Quem pode confirmar ou alterar o objeto de domínio correspondente? |
| Temporalidade | Refere-se ao presente, passado, futuro desejado ou cenário contrafactual? |
| Sensibilidade | Exige proteção adicional por intimidade, saúde, finanças ou outros contextos protegidos? |
| Conflito | Contradiz informação vigente ou apenas complementa histórico? |
| Consequência | Pode mudar orientação, oportunidade, elegibilidade, privacidade ou interpretação de trajetória? |
| Permissão | Há finalidade e autorização vigentes para uso na sessão, persistência e personalização separadamente? |
| Reversibilidade | A correção pode propagar a derivados sem efeitos irreversíveis em terceiros? |

Não criar “pontuação de risco da Pessoa”. A avaliação de impacto diz respeito **à operação de tratamento**, não ao valor ou mérito da Pessoa.

## 4. Matriz principal de gatilhos

| Tipo de entrada / gatilho | Exemplo sintético | Resposta conceitual | Revalidação requerida | Propagação candidata |
| --- | --- | --- | --- | --- |
| T1 — Complemento explícito de baixo impacto | “Agora tenho aulas às terças” | Classificar como declaração contextual; uso/persistência somente se elegível | Confirmar apenas se ambíguo ou necessário à finalidade | Relações de disponibilidade pertinentes; evitar recalcular todo o contexto |
| T2 — Informação ausente, mas ambígua | “Estou pensando em mudar” | Perguntar o que a Pessoa quis dizer quando material | Esclarecimento direcionado antes de afirmar objetivo | Nenhum objeto oficial até resolver |
| T3 — Contradição de estado presente | “Tenho quatro horas livres”, antes eram seis | Identificar possível atualização temporal ou erro; não substituir sem checagem quando relevante | Confirmar novo valor e período, conforme autoridade | Invalidar conclusões dependentes e verificar relatório |
| T4 — Mudança material de orientação | “Não quero mais trabalhar nessa área” | Distinguir nova preferência de revogação de objetivo oficial | Revisar intenção e efeitos antes de alterar objeto canônico | Reavaliar possibilidades sem cancelar objetivo por inferência |
| T5 — Potencialmente sensível | Informação sobre saúde ou crença | Minimizar, não inferir categoria sensível nem gravar automaticamente | Aplicar gates específicos de finalidade, privacidade e segurança | Somente projeções estritamente permitidas; possivelmente nenhuma |
| T6 — Transcrição de voz incerta | STT interpretou incorretamente número ou negação | Evidenciar incerteza da transcrição, solicitar correção quando material | Confirmar conteúdo original antes de consolidar | Bloquear projeções e relatos derivados do trecho duvidoso |
| T7 — Hipótese “e se...” | “E se eu tivesse R$ 5 mil?” | Isolar simulação, sem alterar renda ou recursos reais | Sem confirmação como fato; apenas limites de sessão | Cenário temporário, identificável e descartável |
| T8 — Fonte externa em conflito | Cadastro diz curso concluído; fala diz que está em andamento | Preservar status e proveniência de cada origem | Encaminhar divergência à autoridade do domínio; não decidir pelo LLM | Suspender conclusões derivadas da alegação conflitante |
| T9 — Evidência nova relevante | Comprovante legítimo de experiência | Distinguir evidência recebida de comprovação formal | Aplicar contrato de validação da autoridade competente | Atualizar dependentes somente após decisão reconhecida |
| T10 — Correção ou contestação explícita | “Você entendeu errado” | Abrir revisão e indicar elemento contestado | Não reiterar a interpretação como fato | Invalidar relações/explicações afetadas |
| T11 — Revogação ou exclusão | “Não quero mais que use essa informação” | Restringir usos conforme escopo e processar solicitação pelas regras aplicáveis | Examinar direitos, retenção legal, cópias e provedores | Grafos, caches, sessões, relatórios/áudio sujeitos a tratamento |
| T12 — Informação antiga/expirada | Horário informado há meses | Marcar como possivelmente desatualizado | Renovação contextual quando necessário à decisão | Evitar recomendação baseada em dado presumido atual |
| T13 — Alteração não material | Preferência de forma de escuta da sessão | Aplicar somente ao escopo permitido | Não exigir confirmação intrusiva se decisão clara e autorizada | Ajuste de apresentação, não de memória pessoal por padrão |
| T14 — Mudança de autorização durante conversa | Pessoa desativa personalização | Interromper usos incompatíveis e limitar contexto futuro | Reconsultar autorização vigente | Atualizar sessão, projeções, caches e narração conforme política |
| T15 — Duplicidade/replay | Mensagem repetida após reconexão | Detectar possibilidade de processamento repetido | Verificar versão/idempotência na autoridade técnica futura | Não criar nós, eventos ou atualizações duplicados |

**T1–T15 são rótulos locais deste diagnóstico, não IDs oficiais.** A coluna de propagação descreve consequências possíveis, não autorização de escrita.

## 5. Intensidade de revalidação — quatro níveis candidatos

| Nível local | Condição ilustrativa | Tratamento pretendido | Limite |
| --- | --- | --- | --- |
| R0 — Somente interpretar | Hipótese, conversa casual ou ausência de permissão de persistência | Resposta durante sessão autorizada; nenhuma consolidação | Uso temporário também depende de finalidade legítima |
| R1 — Conferência proporcional | Declaração explícita, sem conflito e baixo impacto | Poderá não exigir pergunta adicional **se** a governança permitir | Dispensa de pergunta não dispensa autorização de persistência |
| R2 — Confirmação direcionada | Ambiguidade, contradição, transcrição duvidosa, mudança significativa | Pergunta contextual específica, sem interrogatório repetitivo | Não tomar silêncio como confirmação |
| R3 — Revisão pela autoridade competente | Dado sensível, revogação, efeito sobre objetivo/passos/evolução, evidência oficial | Suspender automatismo e consultar contrato/domínio apropriado | Não usar o motor de IA como adjudicador |

**Não aplicar níveis como uma pontuação automática.** Eles servem para comparar políticas que ainda precisam de aprovação da direção e das autoridades.

## 6. Impacto contextual — matriz de dependências

| Objeto afetado | Baixo impacto | Médio impacto | Alto impacto / bloqueio |
| --- | --- | --- | --- |
| Grafo | Adicionar ou ajustar relação candidata elegível | Recalcular subgrafo e explicar alteração | Suspender conexão sem base/proveniência ou revogada |
| Síntese de Hoje | Nenhuma mudança visível se irrelevante | Atualizar elemento contextual legitimamente relevante | Não mostrar urgência/evolução não reconhecida |
| Objetivos | Apenas contextualizar intenção | Sugerir revisão consciente, se aplicável | Nunca alterar objetivo assumido sem PER-010/autoridade |
| Próximos Passos | Refinar explicação de condição | Indicar possível reavaliação | Nunca aceitar/concluir passo automaticamente |
| Minha Evolução | Contextualizar informação nova | Reexaminar temporalidade/baseline | Reconhecimento pertence a PER-012/PAS-001 |
| Oportunidades | Reexaminar pertinência contextual | Atualizar motivos de correspondência | Não inventar elegibilidade ou oportunidade ativa |
| Relatório narrado | Nenhuma atualização se irrelevante | Sinalizar versão anterior e oferecer nova síntese | Bloquear reuso indevido se contém informação revogada |
| Conversa por voz | Ajustar resposta no escopo da sessão | Solicitar confirmação e limitar contexto | Interromper uso de dado sem autorização |

**Materialidade** não é apenas número de nós alterados: depende do risco de orientar inadequadamente a Pessoa ou de violar autoridade/privacidade.

## 7. Sequências exemplificativas

### A. Atualização de disponibilidade sem interrupção excessiva

1. A Pessoa declara informação clara de rotina durante conversa.
2. A Intelligence classifica a declaração e consulta finalidade/permissões.
3. Caso haja autorização válida e baixo impacto, a governança candidata pode permitir registro sem uma pergunta extra.
4. Projeções afetadas são atualizadas com origem/tempo.
5. A Pessoa pode inspecionar/corrigir a informação; a plataforma não presume progresso.

**Gate crítico:** fluidez da conversa não substitui escolha consciente de persistência/personalização.

### B. Contradição que altera recomendações

1. A Pessoa declara mudança de disponibilidade que conflita com o contexto vigente.
2. A Intelligence pergunta se o novo valor substitui o antigo ou descreve período diferente.
3. Se resolvido e autorizado, consolida-se por autoridade competente.
4. Relações dependentes e explicações são reavaliadas.
5. Relatório anterior permanece identificado por versão; nova narração pode ser oferecida.

### C. Informação sensível na conversa com Grok

1. Grok transmite à Guivos Intelligence somente conteúdo necessário à interação autorizada.
2. A Intelligence não presume consentimento para persistir dado sensível.
3. O sistema restringe uso e encaminha necessidade de decisão ao domínio de privacidade/dados.
4. Não expõe a informação automaticamente no grafo ou em narração futura.

### D. Revogação durante um relatório

1. Pessoa solicita a retirada de informação da personalização enquanto um áudio a utiliza.
2. A experiência interrompe novos usos incompatíveis e verifica o escopo da solicitação.
3. A autoridade competente decide tratamento de memória, snapshots, caches e provedores.
4. O sistema não promete eliminação absoluta sem fundamento, nem segue narrando conteúdo que deixou de poder utilizar.

## 8. Gate de explicabilidade

Para uma relação alterada ou uma nova sugestão, a Pessoa deve poder saber, de maneira acessível:
- **o que** mudou na compreensão apresentada;
- **por que** a alteração é sugerida (origem e significado, sem revelar raciocínio interno do modelo);
- **quando** a informação foi obtida ou é válida;
- **se** se trata de declaração, evidência, inferência ou hipótese;
- **como** revisar ou contestar conforme autoridade vigente.

O modo narrado e a conversa por voz devem conseguir explicar esse mesmo impacto, quando pertinente, sem exigir leitura do grafo.

## 9. Limites de integrações candidatas

- **Grok/xAI**: candidato para Text-to-Speech e diálogo por voz; não controla gatilhos de persistência, alterações de domínio ou autorização.
- **Gemini STT e alternativas**: representação de fala com possibilidade de erro; não atribuir caráter de fato à transcrição automaticamente.
- **GPT/Claude/Gemini**: interpretação assistiva e classificação de candidatas, sob Guivos Intelligence; resultados não são decisões oficiais.
- **Neo4j Aura**: memória/projeção relacional candidata; não se torna fonte única de verdade nem guarda irrestrita.
- **Journey/PAS-001**: fontes governadas de objetivos, passos, evolução, oportunidades e experiências.
- **Logs/observabilidade**: minimizar dados, remover conteúdo indevido e respeitar escopos; não transformar telemetria em memória pessoal.

## 10. Lacunas de adjudicação

| Lacuna | Pergunta a resolver | Autoridades a consultar |
| --- | --- | --- |
| V-01 — Materialidade | Quando uma mudança exige confirmação adicional? | Produto/UX, GIA, dados/privacidade |
| V-02 — Persistência posterior | Como capturar fatos declarados após PER-007 sem novas autorizações presumidas? | Jornada, PER-007, privacidade |
| V-03 — Evidência | Quando fala, arquivo e estado externo possuem autoridades diferentes? | PAS-001 e domínios |
| V-04 — Memória/versão | Como preservar substituições temporais e evitar eventos duplicados? | Dados/Engenharia, GIA |
| V-05 — Voz | Como verificar transcrições críticas e impedir uso indevido em Grok? | Segurança, GIA, UX, fornecedor |
| V-06 — Relatórios | Quando uma nova versão é necessária e quem decide gerá-la? | Intelligence, Journey, UX |
| V-07 — Revogação | Como bloquear derivados e comunicar limites de eliminação? | Jurídico, Privacidade, Dados |
| V-08 — Acessibilidade | Como a Pessoa compreende a revisão sem grafo ou áudio? | UX e acessibilidade |
| V-09 — Planos | Há diferença legitimamente contratada de capacidades/limites? | Autoridades de Planos, sem inventar entitlements |

Identificadores V-xx são referências locais e não constituem novos IDs GKR.

## 11. Parecer e próximo exame

**Parecer condicionado:** adotar como hipótese de UX uma validação proporcional ao risco e impacto, para evitar perguntas desnecessárias, **sem reduzir as exigências de autorização**. Atualizações de baixo impacto podem ser discretas somente quando a finalidade e a persistência já forem legítimas. Conflitos relevantes, incerteza material, dados sensíveis, mudanças com efeitos de domínio e revogação exigem tratamento elevado ou autoridade específica.

Próximo exame sugerido: **Contrato Conceitual de Sincronização e Versionamento entre Contexto, Grafo, Conversa e Narração**, com foco em mudanças concorrentes, falhas e integridade temporal, sem especificar APIs operacionais.

**Estado:** documento diagnóstico candidato, sem alteração normativa, novas superfícies/IDs, testes, integrações reais, implementação, Design operacional ou publicação.
