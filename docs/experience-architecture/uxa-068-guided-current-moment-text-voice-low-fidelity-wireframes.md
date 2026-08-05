---
id: UXA-068
title: Wireframes Móveis da Expressão Guiada do Momento Atual por Texto e Voz
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-04
parent: UXA-034
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-020
  - UXA-023
  - UXA-034
  - UXA-035
  - UXA-036
  - UXA-037
related:
  - UXA-069
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
  - M7.70
normative: false
---

# Wireframes Móveis da Expressão Guiada do Momento Atual por Texto e Voz

## 1. Finalidade

Este documento materializa a família móvel que ajuda a Pessoa a expressar seu **Momento Atual** de forma clara, útil, proporcional e revisável antes da compreensão inicial da Guivos.

A UXA-034 já permitia escolher `Escrever`, `Falar`, `Enviar arquivo` ou `Perguntas opcionais`, mas sua tela de escolha não demonstrava como o relato seria orientado depois da seleção.

A UXA-068 preenche essa lacuna sem transformar o início da jornada em entrevista obrigatória, diagnóstico, questionário fixo ou coleta excessiva.

A família deverá permitir responder:

> **A Pessoa compreende o que a Guivos precisa saber para ajudá-la neste momento, consegue contar por texto ou voz com orientação suficiente, separar assuntos, preencher apenas lacunas úteis e revisar uma síntese estruturada antes de qualquer processamento?**

## 2. Decisão estrutural

A Guivos não deverá apenas perguntar:

> `O que você quer contar?`

Ela deverá explicar:

> `O que precisamos compreender para preparar uma leitura inicial útil e corrigível deste momento.`

Isso não significa limitar o relato. Significa evitar que a experiência dependa de volume, eloquência, familiaridade com tecnologia ou capacidade da Pessoa de adivinhar quais informações serão relevantes.

O relato livre continua legítimo. A orientação existe para:

- tornar a finalidade compreensível;
- reduzir lacunas materiais;
- evitar exposição desnecessária;
- distinguir assuntos diferentes;
- reconhecer incerteza;
- preparar revisão consciente;
- impedir sugestões pessoais sem base suficiente.

## 3. Posição na experiência

```text
Home pública
→ início protegido
→ escolha de modalidade na UXA-034
→ orientação comum da UXA-068
→ texto guiado ou voz guiada
→ pergunta adaptativa, somente quando útil
→ separação de focos, quando necessária
→ síntese estruturada e revisável
→ inventário e autorização específica da UXA-034
→ processamento visível da UXA-036
→ compreensão inicial revisável
```

A UXA-068 não substitui:

- a escolha de modalidade da UXA-034;
- o inventário de conteúdos recebidos;
- a autorização específica de processamento;
- o processamento visível da UXA-036;
- a compreensão inicial e suas decisões.

## 4. Dimensões de referência

A orientação busca compreender, de forma progressiva, cinco dimensões.

| Dimensão | Pergunta de referência | Regra |
|---|---|---|
| situação | o que está acontecendo agora? | não exigir biografia completa |
| impacto | o que isso dificulta, causa ou modifica? | não pressupor sofrimento ou problema |
| prioridade | o que mais importa compreender ou tratar agora? | aceitar múltiplas prioridades e incerteza |
| direção | o que a Pessoa gostaria que mudasse, fosse decidido ou construído? | aceitar `não sei ainda` |
| contexto | quais prazos, limites, recursos ou tentativas anteriores são relevantes? | solicitar somente quando reduzir incerteza material |

Nenhuma dimensão é obrigatória por padrão.

Uma síntese poderá permanecer incompleta quando isso estiver visível e não gerar recomendação artificial.

## 5. Inventário visual

Foram materializados oito SVGs móveis.

| Estado | Arquivo | Função principal |
|---|---|---|
| orientação comum | `uxa-068-guided-current-moment-orientation-mobile.svg` | explicar o que a Guivos precisa compreender e oferecer texto ou voz |
| rascunho por texto | `uxa-068-guided-current-moment-text-draft-mobile.svg` | permitir texto livre com apoio progressivo |
| preparação para voz | `uxa-068-guided-current-moment-voice-preparation-mobile.svg` | explicar gravação, transcrição, áudio e proteção antes do microfone |
| gravação em andamento | `uxa-068-guided-current-moment-voice-recording-mobile.svg` | manter estado evidente, pausa, conclusão e descarte |
| revisão da transcrição | `uxa-068-guided-current-moment-voice-transcription-review-mobile.svg` | separar áudio, transcrição e declaração revisada |
| esclarecimento adaptativo | `uxa-068-guided-current-moment-adaptive-clarification-mobile.svg` | preencher uma lacuna material com razão explícita e resposta opcional |
| separação de focos | `uxa-068-guided-current-moment-focus-separation-mobile.svg` | organizar assuntos diferentes sem descarte silencioso |
| síntese estruturada | `uxa-068-guided-current-moment-structured-summary-mobile.svg` | revisar situação, impacto, prioridade, direção, contexto e desconhecidos |

## 6. Artefatos visuais

### 6.1 Orientação comum

![Orientação para expressar o Momento Atual](../assets/wireframes/uxa-068-guided-current-moment-orientation-mobile.svg)

### 6.2 Rascunho guiado por texto

![Rascunho guiado por texto](../assets/wireframes/uxa-068-guided-current-moment-text-draft-mobile.svg)

### 6.3 Preparação para voz

![Preparação anterior à gravação](../assets/wireframes/uxa-068-guided-current-moment-voice-preparation-mobile.svg)

### 6.4 Gravação em andamento

![Gravação guiada do Momento Atual](../assets/wireframes/uxa-068-guided-current-moment-voice-recording-mobile.svg)

### 6.5 Revisão da transcrição

![Revisão da transcrição](../assets/wireframes/uxa-068-guided-current-moment-voice-transcription-review-mobile.svg)

### 6.6 Pergunta adaptativa

![Pergunta adaptativa](../assets/wireframes/uxa-068-guided-current-moment-adaptive-clarification-mobile.svg)

### 6.7 Separação de focos

![Separação de focos](../assets/wireframes/uxa-068-guided-current-moment-focus-separation-mobile.svg)

### 6.8 Síntese estruturada

![Síntese estruturada do Momento Atual](../assets/wireframes/uxa-068-guided-current-moment-structured-summary-mobile.svg)

Dimensão de referência dos oito arquivos:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- orientação: retrato;
- fidelidade: baixa;
- processamento: ainda não autorizado.

## 7. Orientação anterior ao relato

Antes de escrever ou falar, a Pessoa conhece:

- a finalidade atual;
- as cinco dimensões que podem ajudar;
- que não precisa contar toda a vida;
- que poderá começar com uma frase;
- que perguntas poderão ser puladas;
- que texto e voz são equivalentes;
- que poderá trocar de modalidade;
- que nada será processado antes de revisão e autorização;
- que poderá continuar sem personalização.

A orientação não deverá prometer que um relato completo produzirá a melhor solução.

## 8. Relato guiado por texto

O estado de texto preserva simultaneamente:

- campo livre;
- apoio com perguntas de referência;
- edição e remoção de trechos;
- salvamento e pausa explícitos;
- troca para voz;
- organização provisória do que já aparece;
- indicação do que ainda permanece em aberto;
- continuidade sem exigir o preenchimento de todas as dimensões.

A organização exibida durante o rascunho é provisória. Ela não poderá ser tratada como interpretação confirmada, fato ou compreensão inicial.

Digitar não autoriza processamento, persistência de compreensão ou personalização.

## 9. Relato guiado por voz

### 9.1 Preparação

Antes de ativar o microfone, a tela informa:

- o que pode ajudar a contar;
- que não é necessário responder a tudo;
- quando a gravação começa e termina;
- que haverá transcrição;
- que a transcrição poderá conter erros;
- que áudio e transcrição são distintos;
- que será possível corrigir, remover ou regravar;
- que informações de terceiros devem ser evitadas quando desnecessárias;
- que gravar não autoriza análise.

A decisão sobre manter temporariamente o áudio ou descartá-lo após a transcrição começa desmarcada.

### 9.2 Gravação

Durante a gravação, o estado deverá ser anunciado visual e semanticamente.

A Pessoa poderá:

- pausar;
- concluir uma parte;
- descartar;
- trocar para texto sem usar o áudio;
- acessar ajuda;
- voltar com interrupção conhecida.

A orientação permanece disponível, mas não deverá interromper, avaliar ou conduzir o relato em tempo real de forma invasiva.

### 9.3 Revisão da transcrição

Depois da gravação, a experiência distingue:

- áudio original;
- transcrição automática;
- correções da Pessoa;
- trechos incertos;
- versão revisada que poderá entrar no rascunho.

A Pessoa poderá:

- ouvir o áudio;
- remover o áudio;
- corrigir a transcrição;
- remover um trecho;
- marcar palavra incerta;
- regravar uma parte;
- descartar áudio e transcrição;
- gravar outra parte.

Falhas de transcrição não poderão ser elevadas a declarações da Pessoa.

## 10. Perguntas adaptativas

Perguntas adicionais não formam questionário fixo.

Uma pergunta somente deverá aparecer quando:

- houver uma lacuna material identificável;
- a razão estiver explicada;
- a resposta puder reduzir incerteza relevante;
- a Pessoa puder pular;
- existirem alternativas como `não sei ainda`, `prefiro não informar` ou texto livre;
- nenhuma resposta vier pré-selecionada;
- a ausência de resposta não bloquear exploração geral.

A pergunta não deverá sugerir que a Guivos já conhece a melhor direção.

## 11. Relevância e separação de assuntos

A Guivos não deverá classificar silenciosamente um trecho como `irrelevante`.

Quando houver assuntos diferentes ou relação ainda incerta, a interface deverá dizer que:

- mais de um assunto foi identificado;
- a relação entre eles ainda não está confirmada;
- nada será removido sem decisão da Pessoa.

A Pessoa poderá:

- manter os assuntos juntos;
- escolher um foco principal;
- tratar um segundo assunto como condição;
- criar um assunto separado;
- deixar um trecho fora desta compreensão;
- editar o conteúdo;
- manter o rascunho como está.

Deixar um trecho fora da compreensão não equivale automaticamente a excluí-lo do rascunho ou do armazenamento aplicável.

## 12. Síntese estruturada

Antes do inventário e da autorização da UXA-034, a Pessoa recebe uma síntese provisória organizada por:

1. situação atual;
2. impacto principal;
3. prioridade atual;
4. direção desejada;
5. contexto e pontos em aberto.

Cada bloco permite correção própria.

A superfície declara que:

- a síntese é organização provisória;
- não é diagnóstico;
- não é compreensão final da Guivos;
- desconhecidos permanecem identificados;
- pontos em aberto não são fatos;
- continuar não inicia processamento.

A saída principal conduz à revisão dos conteúdos recebidos da UXA-034.

## 13. Base insuficiente

Quando a Pessoa compartilhar pouco, a experiência deverá distinguir:

- relato curto, mas suficiente para uma hipótese limitada;
- relato que ainda possui lacuna material;
- relato que não permite relação segura entre situação e direção;
- ausência total de conteúdo autorizado.

A Guivos poderá:

- fazer uma pergunta opcional;
- apresentar a síntese com desconhecidos;
- permitir contar mais;
- permitir manter em aberto;
- permitir continuar sem personalização.

A Guivos não poderá:

- completar lacunas por suposição;
- exigir mais exposição para liberar o ecossistema;
- chamar atividade de avanço humano;
- apresentar Próximo Passo pessoal antes da confirmação suficiente.

## 14. Privacidade, autonomia e dignidade

A família preserva:

- compartilhamento mínimo;
- revisão anterior ao processamento;
- controles separados para áudio e transcrição;
- ausência de microfone automático;
- ausência de autorização pelo ato de digitar ou gravar;
- remoção de trechos;
- proteção de informações de terceiros;
- perguntas opcionais;
- possibilidade de `não sei`;
- possibilidade de `prefiro não informar`;
- continuidade sem personalização;
- ausência de culpa por pausar ou compartilhar pouco;
- ausência de pontuação de qualidade do relato.

## 15. Segurança e encaminhamento

O conjunto não define protocolo clínico, emergencial ou jurídico.

Uma futura implementação deverá possuir regras próprias para situações em que o conteúdo indique risco imediato, necessidade de ajuda profissional ou proteção adicional.

A orientação não deverá diagnosticar, prometer confidencialidade absoluta ou substituir atendimento apropriado.

## 16. Acessibilidade funcional

A futura implementação deverá:

- oferecer alternativa textual equivalente à voz;
- anunciar início, pausa e fim da gravação;
- não depender de animação de onda sonora;
- permitir controle por teclado e tecnologia assistiva;
- manter títulos, estados e consequências em texto;
- preservar foco ao alternar modalidade;
- permitir correção de transcrição sem depender de reprodução do áudio;
- não utilizar tempo de fala como medida de qualidade;
- permitir gravação em partes;
- preservar conteúdo em falha de conexão quando tecnicamente possível;
- informar claramente perdas antes de descarte.

Este incremento não conclui conformidade técnica de acessibilidade.

## 17. Critérios de saída do pacote

A UXA-068 estará materializada quando:

- os oito SVGs existirem;
- texto e voz tiverem orientação equivalente;
- o microfone não iniciar automaticamente;
- áudio e transcrição estiverem separados;
- perguntas forem adaptativas e opcionais;
- a razão de cada pergunta estiver visível;
- assuntos diferentes não forem descartados silenciosamente;
- a síntese separar as cinco dimensões e desconhecidos;
- continuar conduzir à revisão da UXA-034, sem processamento;
- a validação mecânica do Repositório for aprovada.

## 18. Cobertura visual proposta

| Família da jornada pessoal | Materializados | Validados | Pendentes |
|---|---:|---:|---:|
| Início protegido geral — UXA-034 | 4 | 4 | 0 |
| Compreensão inicial — UXA-036 | 5 | 5 | 0 |
| Expressão Guiada do Momento Atual — UXA-068 | 8 | 0 | 8 |
| **Subtotal relacionado** | **17** | **9** | **8** |

Essa contagem não substitui o inventário global de wireframes e permanece separada das famílias de Coletivos e Opportunity Boost.

## 19. Limites

A UXA-068 não:

- valida funcionalmente os oito novos SVGs;
- cria modelo de IA ou algoritmo adaptativo;
- define protocolo clínico ou emergencial;
- implementa gravação ou transcrição;
- define retenção jurídica final;
- materializa envio de arquivos;
- altera a compreensão inicial da UXA-036;
- cria protótipo navegável;
- executa teste com pessoas;
- inicia Engenharia de Produto;
- cria o ambiente de simulação das jornadas;
- inicia `Meus Coletivos`.

## 20. Próxima transição recomendada

**UXA-069 — Validação Funcional e Reformulação da Expressão Guiada do Momento Atual por Texto e Voz.**

A UXA-069 deverá avaliar os oito estados como uma continuidade única antes de protótipo, teste ou implementação.

A validação dependerá de autorização separada.
