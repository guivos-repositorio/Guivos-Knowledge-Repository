---
id: UXA-034
title: Wireframe de Baixa Fidelidade do Início Protegido da Jornada
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-07-27
parent: UXA-023
depends_on:
  - UXA-001
  - UXA-003-A1
  - UXA-005
  - UXA-009
  - UXA-011
  - UXA-011-A1
  - UXA-020
  - UXA-021
  - UXA-022
  - UXA-023
related:
  - UXA-002
  - UXA-006
  - UXA-010
  - PAS-001-CV-VIEW-001
  - PAS-001-OBJ-VIEW-001
  - PAS-001-PP-VIEW-001
normative: false
---

# Wireframe de Baixa Fidelidade do Início Protegido da Jornada

## 1. Finalidade

Este documento materializa a primeira referência gráfica móvel do início protegido da jornada pessoal da Guivos, conforme o contrato funcional validado e reformulado pela UXA-023.

O incremento demonstra a separação entre:

1. explicação anterior à autenticação;
2. entrada ou criação de conta;
3. escolha consciente da modalidade e compartilhamento mínimo;
4. revisão do conteúdo recebido;
5. autorização específica para processamento;
6. transição para uma compreensão inicial revisável.

O conjunto não representa design visual, textos definitivos, autenticação implementada, gravação real, upload real, processamento de IA, política jurídica completa, protótipo navegável ou desenvolvimento.

## 2. Posição na experiência

```text
Página Inicial pública
→ decisão voluntária de iniciar
→ início protegido da jornada
→ compreensão inicial revisável
→ Tela Hoje, jornada sem personalização ou exploração geral
→ Hoje | Jornada | Explorar | Mapa | Eu
```

A pessoa chega ao primeiro estado somente após selecionar conscientemente `Iniciar minha jornada` na Home pública.

Nenhuma coleta, gravação, upload, transcrição, extração ou personalização começa automaticamente.

## 3. Artefatos visuais

### 3.1 Estado 1 — Explicação antes da autenticação

![Início protegido antes da autenticação](../assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-034-protected-entry-explanation-mobile.svg`

### 3.2 Estado 2 — Acesso protegido

![Acesso protegido sem coleta iniciada](../assets/wireframes/uxa-034-protected-entry-access-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-034-protected-entry-access-mobile.svg`

### 3.3 Estado 3 — Modalidade e compartilhamento mínimo

![Escolha de modalidade e compartilhamento mínimo](../assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-034-protected-entry-sharing-mobile.svg`

### 3.4 Estado 4 — Revisão e autorização específica

![Revisão do conteúdo e autorização específica](../assets/wireframes/uxa-034-protected-entry-review-mobile.svg)

Arquivo:

`docs/assets/wireframes/uxa-034-protected-entry-review-mobile.svg`

Dimensão de referência de cada arquivo:

- canal: aplicativo móvel;
- largura: 390 pixels;
- altura: 844 pixels;
- orientação: retrato;
- condição: baixa fidelidade;
- navegação: sequência protegida, não formulário linear obrigatório.

## 4. Pergunta do wireframe

> **A pessoa consegue compreender o processo, entrar com segurança, compartilhar somente o necessário, revisar o que foi recebido e autorizar usos específicos sem confundir conta, coleta, processamento e personalização?**

A validação funcional especializada do conjunto permanece como ato posterior.

## 5. Princípios transversais

Os quatro estados preservam:

- voluntariedade;
- explicação anterior à autenticação;
- ausência de coleta automática;
- autenticação separada de autorização;
- modalidades equivalentes;
- compartilhamento mínimo e progressivo;
- finalidades visíveis;
- revisão anterior ao processamento material;
- controles de correção, limitação, remoção, pausa e exclusão;
- processamento específico e interrompível;
- personalização bloqueada antes do gate;
- saída para exploração sem personalização.

## 6. Estado 1 — Explicação antes da autenticação

O primeiro estado declara:

> **Você está entrando em um ambiente protegido**

> **Nenhuma informação pessoal foi coletada até aqui**

A pessoa recebe uma explicação curta do processo:

```text
entender o que acontecerá
→ entrar ou criar conta
→ escolher como compartilhar
→ revisar o conteúdo recebido
→ autorizar somente os usos desejados
→ revisar a compreensão inicial
```

Ações principais:

- `Continuar com segurança`;
- `Entender como funciona`;
- `Voltar à Página Inicial`;
- `Explorar sem personalização`.

O estado não apresenta campo de relato, microfone, upload ou autorização genérica.

## 7. Estado 2 — Acesso protegido

O segundo estado apresenta alternativas legítimas:

- `Entrar na minha conta`;
- `Criar uma conta`;
- `Recuperar acesso`;
- `Voltar e entender o processo`;
- `Explorar sem personalização`.

A superfície declara:

> **Entrar protege o rascunho, mas não autoriza processamento**

> **Nenhuma coleta foi iniciada**

A criação de conta não deverá:

- iniciar gravação;
- abrir upload automaticamente;
- autorizar transcrição;
- autorizar análise de arquivos;
- formar compreensão persistente;
- ativar personalização.

## 8. Estado 3 — Modalidade e compartilhamento mínimo

Depois do acesso protegido, a pessoa poderá escolher:

- `Escrever`;
- `Falar`;
- `Enviar arquivo`;
- `Responder perguntas opcionais`;
- `Começar com uma frase`.

Nenhuma modalidade é superior ou obrigatória.

O estado demonstra:

> **Comece somente com o que fizer sentido agora**

> **Você não precisa contar toda a sua vida**

Também apresenta:

- finalidade atual;
- o que será salvo como rascunho;
- o que ainda não será processado;
- alerta sobre informações sensíveis e de terceiros;
- ações `Pausar`, `Salvar rascunho` e `Excluir rascunho`;
- opção `Prefiro não informar` quando aplicável.

## 9. Texto, voz e arquivos

### 9.1 Texto

Digitar não constitui autorização de processamento.

A pessoa poderá editar, remover trechos, limitar finalidade e revisar antes de autorizar.

### 9.2 Voz

Antes de gravar, a interface deverá explicar:

- finalidade;
- início e fim da gravação;
- transcrição;
- manutenção ou descarte do áudio;
- revisão e correção;
- remoção e regravação;
- risco de informações de terceiros.

Gravação e transcrição possuem controles separados quando seus efeitos forem diferentes.

### 9.3 Arquivos

Antes do envio, a pessoa deverá conhecer:

- finalidade;
- tipos de extração previstos;
- limites de leitura;
- retenção;
- tratamento de dados sensíveis ou de terceiros;
- remoção do arquivo e de informações derivadas;
- revisão anterior ao uso material.

Upload não autoriza leitura irrestrita.

## 10. Estado 4 — Revisão do conteúdo recebido

Antes de qualquer processamento material, a pessoa visualiza um inventário:

- texto fornecido;
- respostas opcionais;
- gravações;
- transcrições;
- arquivos;
- extrações propostas;
- itens removidos ou limitados;
- finalidades associadas.

Cada item poderá oferecer:

- `Revisar`;
- `Editar`;
- `Corrigir`;
- `Substituir`;
- `Remover`;
- `Limitar uso`;
- `Excluir`.

O inventário distingue conteúdo original, transcrição, extração e interpretação.

## 11. Autorização específica

A autorização aparece somente depois da revisão.

O estado demonstra escolhas separadas para:

- utilizar o texto revisado na compreensão inicial;
- utilizar a transcrição revisada;
- processar extrações aprovadas do arquivo;
- manter ou excluir o original;
- formar compreensão persistente;
- utilizar a compreensão para personalização futura.

A última opção permanece bloqueada até que a compreensão inicial seja apresentada, revisada e autorizada no gate correspondente.

O wireframe declara:

> **Criar conta não autorizou estas ações**

> **Você pode continuar sem personalização**

## 12. Processamento visível e interrompível

Após autorização específica, o estado poderá evoluir por:

```text
rascunho salvo
→ aguardando revisão
→ autorizado para processamento específico
→ em processamento
→ pausado, interrompido ou com falha
→ compreensão inicial disponível
```

A pessoa deverá poder:

- interromper quando aplicável;
- retirar autorização futura;
- corrigir origem;
- excluir itens compatíveis;
- compreender efeitos de uma remoção;
- continuar sem personalização material.

## 13. Compreensão inicial e gate

A conclusão do relato não garante recomendação, oportunidade, Próximo Passo ou resultado.

A compreensão inicial deverá distinguir:

- fatos fornecidos;
- fontes;
- transcrições e extrações;
- inferências;
- desconhecidos;
- limitações;
- correções realizadas.

Antes de qualquer personalização material, a pessoa deverá poder:

- revisar;
- corrigir;
- limitar;
- remover;
- discordar;
- pedir nova análise;
- continuar sem personalização;
- voltar à exploração geral.

## 14. Pausa, rascunho e exclusão

O wireframe diferencia:

- pausar a sessão;
- salvar rascunho;
- excluir rascunho;
- remover um item;
- retirar autorização;
- excluir conteúdo original;
- excluir informações derivadas quando aplicável;
- encerrar a jornada.

Nenhuma dessas ações deverá ser apresentada como equivalente às demais.

## 15. Informações sensíveis e de terceiros

A superfície deverá:

- alertar antes de voz e arquivos;
- permitir remoção de trechos e itens;
- não incentivar exposição excessiva;
- não exigir informação de terceiros;
- não utilizar culpa ou urgência artificial;
- oferecer proteção adicional quando houver risco material;
- orientar ajuda adequada quando necessário.

O wireframe não define protocolo clínico, jurídico ou emergencial.

## 16. Acessibilidade funcional

A sequência deverá:

- permitir leitura sem depender de cor;
- oferecer títulos e estados textuais;
- manter ações principais e saídas reconhecíveis;
- não depender de gestos ocultos;
- anunciar gravação, upload, revisão e processamento;
- permitir navegação por teclado e tecnologia assistiva em implementação futura;
- preservar foco e progresso ao pausar;
- manter alternativa textual para voz e arquivos.

A criação não conclui conformidade técnica de acessibilidade.

## 17. Critérios de validação posterior

A validação funcional especializada deverá verificar:

- se a pessoa entende que deixou a Home pública;
- se compreende que nenhuma coleta começou no primeiro estado;
- se conta e autorização permanecem separadas;
- se entrar, criar conta e recuperar acesso são claros;
- se explorar sem personalização permanece legítimo;
- se texto, voz, arquivos e perguntas são percebidos como alternativas;
- se o compartilhamento mínimo é compreendido;
- se pausa, rascunho e exclusão têm efeitos distintos;
- se original, transcrição, extração e interpretação são distinguíveis;
- se a revisão antecede o processamento;
- se as autorizações são específicas;
- se personalização permanece bloqueada antes do gate;
- se a transição para a compreensão inicial não parece automática;
- se o conjunto evita exposição excessiva e pressão.

## 18. Limites

Este incremento não:

- cria autenticação real;
- define provedor de identidade;
- implementa gravação, transcrição ou upload;
- define modelo de IA;
- define retenção jurídica definitiva;
- substitui políticas de privacidade e termos;
- conclui textos finais;
- cria referência para computador ou tablet;
- cria protótipo navegável;
- executa teste com usuários;
- conclui acessibilidade técnica;
- inicia Engenharia de Produto.

## 19. Próximos atos governados

Após integração e nova autorização, poderão ocorrer separadamente:

1. validar funcionalmente o wireframe móvel do início protegido;
2. criar a referência móvel da Página Inicial pública;
3. validar a revisão da compreensão inicial;
4. validar a transição para a primeira Tela Hoje;
5. criar estados especializados de texto, voz e arquivos;
6. criar referência do início protegido para computador;
7. retomar independentemente os testes dos Resultados Empresariais.

Nenhum ato é iniciado automaticamente.
