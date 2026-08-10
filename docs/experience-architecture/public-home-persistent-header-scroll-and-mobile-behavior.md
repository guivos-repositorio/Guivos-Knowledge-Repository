---
id: GKR-UX-HOME-NAV-004
title: Comportamento Persistente do Header — Scroll, Densidade e Mobile na Home Pública
status: draft
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-08-10
parent: GKR-UX-HOME-NAV-002
depends_on:
  - UXA-020
  - UXA-021
  - GKR-UX-HOME-NAV-001
  - GKR-UX-HOME-NAV-002
  - GKR-UX-HOME-NAV-003
  - GKR-UX-HOME-NARR-005
  - GKR-UX-HOME-SYS-001
normative: false
---

# Comportamento Persistente do Header — Scroll, Densidade e Mobile na Home Pública

## 1. Finalidade

Este documento refina o comportamento conceitual do Header Persistente da Home pública de `guivos.com` ao longo da narrativa e em diferentes larguras de tela.

Seu objetivo é definir:

- o que significa `persistente` na experiência da Home;
- como o Header pode reduzir presença sem desaparecer;
- como preservar a dominância perceptiva da Hero;
- como os acessos devem se comportar durante a rolagem;
- como desktop e mobile preservam a mesma arquitetura de intenção;
- quais controles podem ser condensados sem perder encontrabilidade;
- limites de interação, movimento, contraste e acessibilidade.

Este documento não define pixels, breakpoint final, altura, paleta, tipografia, animação específica, componente final, tecnologia de implementação ou layout fechado.

---

## 2. Decisão central

Na Home pública, `Header Persistente` significa:

> **uma camada de orientação e acesso que permanece previsvisivelmente disponível durante a exploração da Home, sem competir com a narrativa.**

A hipótese principal rejeita um Header que desaparece completamente durante a rolagem para reaparecer somente quando o visitante muda de direção.

O Header pode:

- reduzir altura;
- reduzir espaçamento;
- simplificar tratamento visual;
- alterar superfície/fundo para preservar contraste;
- condensar elementos conforme largura disponível;
- adaptar a densidade entre o primeiro viewport e o restante da Home.

Mas não deve perder sua função de orientação.

Regra:

> **persistir não significa ocupar mais espaço; significa continuar encontrável e previsível.**

---

## 3. Dois estados perceptivos principais

A arquitetura admite dois estados de apresentação do mesmo Header.

### Estado A — entrada / Hero

Objetivo:

> **estar presente sem disputar o primeiro plano com a pergunta-mãe.**

Princípios:

- inventário semântico do Header permanece disponível;
- a Hero continua sendo o foco perceptivo dominante;
- o Header pode usar uma presença visual mais leve;
- eventual transparência ou sobreposição só é aceitável quando contraste e leitura forem robustos;
- vídeo, fotografia ou mídia da Hero não podem tornar navegação ilegível;
- `Iniciar Jornada` continua claro, mas não deve superar a mensagem da Hero em atenção.

### Estado B — narrativa em progresso

Depois que o visitante começa a percorrer a Home, o Header pode assumir uma forma mais compacta e estável.

Objetivo:

> **diminuir ocupação e manter orientação.**

Princípios:

- continuidade visual previsível;
- menor altura/densidade quando adequado;
- contraste consistente sobre diferentes macroexperiências;
- nenhum aumento progressivo de pressão comercial;
- nenhum desaparecimento completo como comportamento padrão.

A transição entre os estados deve parecer adaptação funcional, não evento publicitário.

---

## 4. Regra de estabilidade do CTA `Iniciar Jornada`

`Iniciar Jornada` permanece a porta própria da Journey no Header.

Durante a rolagem, não deve:

- pulsar;
- crescer para capturar atenção;
- mudar de significado;
- surgir somente depois de determinada seção como gatilho de conversão;
- transformar-se em banner sticky;
- bloquear conteúdo;
- repetir-se em múltiplas posições sem necessidade.

Pode adaptar dimensões ou tratamento visual junto com a compactação do Header, desde que preserve reconhecimento e clareza.

Regra:

> **a disponibilidade de `Iniciar Jornada` é persistente; sua pressão perceptiva não deve aumentar com a rolagem.**

---

## 5. Relação com as sete macroexperiências

O Header atravessa as sete macroexperiências sem se tornar parte de nenhuma delas:

1. Abrir o Horizonte;
2. Ver o Real e Perceber a Amplitude;
3. Perceber a Desconexão e Entender o Papel da Guivos;
4. Ver o Possível Virar Experiência e Perceber Quem Faz Acontecer;
5. Compreender a Coerência do Ecossistema;
6. Encontrar Substância sem Perder Autonomia;
7. Reabrir o Horizonte para a Descoberta.

Ele não precisa mudar de arquitetura a cada macroexperiência.

Evitar:

- Header temático diferente por seção;
- cor ou composição drasticamente diferente a cada movimento;
- navegação que pareça pertencer a um produto específico quando o visitante chega ao Movimento 08;
- transformar o Header em indicador obrigatório de progresso narrativo.

A narrativa muda; a orientação permanece.

---

## 6. Inventário conceitual preservado

A arquitetura vigente continua considerando:

### Institucional

- Guivos / Home;
- `Sobre`;
- `Organizações e Coletivos`.

### Utilidades e ecossistema

- Compartilhar;
- Idioma / Região;
- launcher do ecossistema;
- `Login`;
- `Iniciar Jornada`.

Launcher vigente:

- Travel;
- Ads;
- Media;
- Business;
- Intelligence;
- Mall.

Journey permanece fora do launcher e possui `Iniciar Jornada` como porta própria.

Este documento altera comportamento e prioridade de exposição, não o inventário aprovado.

---

## 7. Persistência sem simultaneidade obrigatória

Existe diferença entre:

```text
acesso persistente
≠
controle obrigatoriamente visível o tempo inteiro
```

No desktop, existe espaço suficiente para que a hipótese principal preserve a maior parte do inventário diretamente no Header.

No mobile, a arquitetura não exige que todos os elementos caibam simultaneamente em uma única linha.

O requisito é:

> **nenhum caminho essencial pode desaparecer da arquitetura ou ficar enterrado em navegação profunda e imprevisível.**

Elementos condensados devem permanecer, em regra, a no máximo uma superfície de navegação de distância a partir do Header.

---

## 8. Prioridade de exposição

A prioridade conceitual de exposição é:

### Prioridade A — identidade e continuidade

- Guivos / Home;
- `Iniciar Jornada`.

Esses elementos possuem maior exigência de presença direta, especialmente durante a rolagem.

### Prioridade B — acesso recorrente

- launcher do ecossistema;
- `Login`;
- idioma/região.

Devem possuir alta encontrabilidade e acesso rápido.

### Prioridade C — institucional e utilitário

- `Sobre`;
- `Organizações e Coletivos`;
- Compartilhar.

Continuam importantes, mas podem ser condensados primeiro quando a largura exigir.

Essa prioridade orienta responsividade; não define posição ou tamanho final.

---

## 9. Desktop

Na hipótese desktop, o Header pode preservar diretamente o inventário amplo:

```text
Guivos
Sobre
Organizações e Coletivos
Compartilhar
Idioma/Região
Launcher
Login
Iniciar Jornada
```

Princípios:

- nenhuma fileira deve parecer barra de ferramentas complexa;
- os ícones utilitários precisam permanecer secundários;
- `Sobre` e `Organizações e Coletivos` não competem com a Hero;
- Login não recebe peso equivalente ao CTA de continuidade;
- launcher permanece atalho, não vitrine;
- compactação durante o scroll pode reduzir espaço sem reordenar mentalmente toda a navegação.

---

## 10. Mobile — mesma arquitetura, outra densidade

Mobile não cria uma segunda arquitetura de navegação.

A mesma intenção precisa sobreviver com menos largura.

A hipótese de comportamento admite que somente parte dos controles permaneça diretamente visível, desde que os demais sejam recuperáveis imediatamente em uma superfície de navegação clara.

### Presença direta prioritária

Preservar preferencialmente:

- Guivos / Home;
- `Iniciar Jornada` com significado textual compreensível;
- ao menos um acesso claro à navegação restante.

### Acessos de alta prioridade

Launcher, Login e idioma/região devem permanecer muito fáceis de encontrar.

O design poderá testar se aparecem diretamente ou em primeira camada de navegação, conforme largura e clareza.

### Acessos institucionais/utilitários

`Sobre`, `Organizações e Coletivos` e Compartilhar podem ser condensados na primeira superfície de navegação mobile.

Regra:

> **condensar é permitido; enterrar, remover ou transformar em caça ao ícone não é.**

---

## 11. Launcher e menu geral não são a mesma coisa

O launcher do ecossistema possui semântica própria:

> **acessar ambientes conhecidos da Guivos.**

Uma eventual navegação geral mobile possui outra semântica:

> **encontrar acessos institucionais e utilitários que não cabem diretamente no Header.**

Portanto, se o design utilizar ambos, não devem parecer dois menus indistinguíveis.

A grade de pontos deve continuar significando ecossistema/produtos, enquanto uma eventual navegação geral deve ser reconhecível como navegação da Home.

Se a largura obrigar o launcher a ser incorporado temporariamente a uma superfície geral, ele deve manter agrupamento e rotulagem próprios como `Ecossistema` ou equivalente, sem dissolver os produtos entre links institucionais.

---

## 12. Idioma / Região no mobile

O globo continua sendo a referência conceitual para idioma/região.

No mobile:

- pode permanecer visível diretamente quando houver espaço;
- pode integrar a primeira superfície de navegação quando a densidade exigir;
- nunca deve depender de rodapé para ser encontrado;
- deve continuar identificado de forma acessível como `Idioma e região` ou equivalente;
- não deve ser confundido com localização automática do visitante.

A decisão de exposição direta versus primeira camada permanece para design responsivo.

---

## 13. Login no mobile

`Login` deve continuar encontrável sem esforço.

Pode:

- permanecer textual diretamente no Header quando houver espaço;
- integrar a primeira superfície de navegação mobile;
- receber representação compacta somente se continuar inequívoca e acessível.

Não deve:

- competir visualmente com `Iniciar Jornada`;
- ser escondido em submenu profundo;
- ser substituído por avatar no estado público não autenticado sem significado claro.

---

## 14. Comportamento de superfícies abertas

Launcher, idioma/região e eventual navegação condensada devem abrir somente por ação explícita do visitante.

Princípios:

- apenas uma superfície principal de Header aberta por vez;
- fechamento claro;
- `Esc` ou mecanismo equivalente quando aplicável;
- retorno de foco ao controle de origem;
- navegação por teclado;
- leitura adequada por tecnologia assistiva;
- ausência de abertura automática por scroll;
- ausência de áudio ou movimento obrigatório;
- superfícies não podem bloquear permanentemente a narrativa.

O formato final — popover, sheet, drawer, menu, modal ou equivalente — permanece para design.

---

## 15. Contraste e adaptação ao conteúdo

Como a Home pode alternar fotografia, vídeo, fundos claros/escuros e diferentes densidades, o Header deve possuir estratégia de contraste adaptável.

A adaptação pode ocorrer por:

- superfície própria;
- mudança de contraste;
- borda/sombra sutil;
- alteração controlada de tratamento visual;
- solução equivalente.

Não deve ocorrer por:

- ilegibilidade temporária;
- mudança de identidade da marca;
- inversões excessivas a cada pequeno bloco;
- depender da mídia estar carregada para ser legível.

Acessibilidade prevalece sobre transparência estética.

---

## 16. Scroll e movimento

O comportamento do Header deve respeitar as regras gerais da Home:

- movimento serve compreensão e continuidade;
- nenhuma animação deve atrasar acesso;
- compactação não deve saltar ou mover alvos de forma imprevisível;
- o visitante não deve perseguir controles que mudam de posição continuamente;
- `prefers-reduced-motion` ou equivalente deve possuir comportamento estável;
- a mudança entre estado Hero e estado compacto deve continuar compreensível sem animação.

Regra:

> **o Header pode se adaptar ao scroll; não deve reagir nervosamente a ele.**

---

## 17. Relação com o CTA da Hero

O CTA de descoberta da Hero continua sendo contextual à abertura.

Ele não precisa permanecer sticky.

Ao sair da Hero:

- o CTA de descoberta pode sair naturalmente do campo de visão;
- `Iniciar Jornada` continua no Header;
- a própria narrativa passa a conduzir o visitante;
- não é necessário substituir o CTA da Hero por outro CTA flutuante.

Isso preserva:

```text
Hero → descobrir
Header → iniciar quando desejar
```

---

## 18. Relação com o Movimento 11

Ao chegar à macroexperiência final de Descoberta, o Header continua estável.

A Home não precisa alterar `Iniciar Jornada` para criar uma sensação de fechamento comercial.

O Movimento 11 pode convidar à continuidade e descoberta enquanto o Header mantém a porta transversal já conhecida.

Regra:

> **o fim da narrativa não precisa transformar o Header em mecanismo de conversão.**

---

## 19. Acessibilidade de controles icônicos

Controles representados por ícones precisam possuir nome acessível e estado compreensível.

No mínimo:

- Compartilhar;
- Idioma e região;
- Ecossistema / launcher;
- eventual navegação geral mobile.

Evitar:

- ícone sem `aria-label` ou equivalente;
- tooltip como única fonte de significado;
- interação exclusiva por hover;
- foco invisível;
- grade de pontos sem nome acessível;
- globo sem explicação acessível.

---

## 20. Anti-padrões

Rejeitar ou revisar se:

1. o Header desaparece completamente durante longos trechos da rolagem como comportamento padrão;
2. reaparece de forma abrupta e cobre conteúdo;
3. `Iniciar Jornada` aumenta agressivamente de destaque ao longo da Home;
4. o Header muda de arquitetura a cada macroexperiência;
5. mobile remove acesso institucional importante sem alternativa imediata;
6. mobile esconde Login, launcher ou idioma/região em navegação profunda;
7. launcher e menu geral parecem o mesmo controle com funções diferentes;
8. o visitante precisa memorizar onde um acesso reaparece;
9. a grade de pontos vira menu genérico de todos os links da Guivos;
10. transparência prejudica contraste sobre mídia;
11. ícones ficam sem rótulo acessível;
12. animação do Header move alvos enquanto a pessoa tenta clicar;
13. o Header ocupa mais protagonismo que a Hero;
14. uma mudança de seção dispara modal, menu ou CTA sem solicitação;
15. a versão mobile substitui `Iniciar Jornada` por símbolo ambíguo.

---

## 21. Critérios de aceitação

Uma futura materialização é aderente quando:

- o Header continua previsível durante toda a Home;
- a Hero domina o primeiro viewport;
- compactação reduz espaço sem reduzir compreensão;
- `Iniciar Jornada` permanece disponível sem aumentar pressão;
- desktop oferece acesso amplo sem parecer barra de ferramentas;
- mobile preserva a mesma arquitetura de intenção;
- caminhos condensados continuam a uma camada de distância;
- launcher mantém semântica própria de ecossistema;
- Login e idioma/região continuam encontráveis;
- acessos institucionais permanecem acessíveis;
- contraste é robusto com e sem mídia;
- controles funcionam por teclado e tecnologia assistiva;
- o comportamento permanece íntegro com movimento reduzido.

---

## 22. Liberdades preservadas para design

Continuam abertos:

- altura inicial e compacta;
- breakpoint;
- ordem material final dentro dos núcleos aprovados;
- alinhamento;
- transparência ou superfície sólida;
- formato de compactação;
- tipo de menu mobile;
- exposição direta ou primeira camada de Login, globo e launcher no mobile;
- animação específica;
- duração/easing;
- sombras, bordas e tratamento visual;
- formato do launcher;
- formato da superfície de idioma/região;
- formato do menu geral mobile;
- comportamento técnico sticky/fixed equivalente.

Essas escolhas não podem alterar a hierarquia de intenção governada por este documento.

---

## 23. Síntese de controle

```text
ENTRADA / HERO
Header presente, leve e legível
↓
Hero domina percepção
↓
visitante começa a rolar
↓
Header pode compactar
↓
permanece previsível e acessível
↓
atravessa toda a narrativa sem desaparecer
↓
Iniciar Jornada continua disponível, sem pressão crescente
↓
mobile condensa sem criar outra arquitetura
```

Regra final:

> **O Header da Guivos deve permanecer disponível sem permanecer dominante. Ele orienta enquanto a narrativa conduz.**
