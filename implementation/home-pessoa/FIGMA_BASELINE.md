# Home Principal / Pessoa — Baseline de implementação Figma v3

Status: inspeção inicial concluída; implementação visual ainda não validada; publicação bloqueada.

## Fontes
- Design de referência: Figma `guivos.com 2.0`, frame `16152:941`, **Journey Pessoa / Home Principal / Desktop — v3**.
- Arquivo: `sGzdhwQKqsyZOhkqXYsFfv`.
- Documento estratégico: https://guivos-repositorio.github.io/Guivos-Knowledge-Repository/experience-architecture/public-home-master-document/
- Tamanho do frame desktop: 1440 × 10129 px.
- Regras: design original intocável, não substituir nenhum asset, preservar textos/estados/comportamentos, não publicar sem aprovação explícita.

## Inventário estrutural (coordenadas verticais do Figma)
| Área | Início y | Altura |
| --- | ---: | ---: |
| Header | 0 | 97 |
| M01 Hero | 97 | 816 |
| M02+M03 | 913 | 1501 |
| M04+M05 | 2414 | 884 |
| M06+M07 | 3298 | 1766 |
| M08 | 5064 | 1090 |
| M09+M10 | 6154 | 1755 |
| Assinatura global | 7909 | 252 |
| M11 | 8161 | 1137 |
| Pré-rodapé | 9298 | 74 |
| Rodapé | 9372 | 757 |

## Constatações
- A árvore contém instâncias Figma, vetores, imagens, vídeos, carrosséis, navegação e gráfico.
- M01 possui três imagens marcadas `Imagem (provisória)` que devem ser mantidas no baseline visual.
- Alguns estilos de texto são renderizados como Outfit mesmo quando os nomes das camadas citam Goldplay; resolver pela propriedade efetiva do design e não pelo nome da camada.
- M08 descreve comportamento de hover que altera a imagem de destaque conforme produto selecionado.
- M11 tem valores demonstrativos 3.482, +412, −287; não representar como dados operacionais reais.
- O frame inspecionado é desktop; variante mobile e seus estados precisam de extração específica antes de afirmar fidelidade responsiva.
- O documento GKR registra engenharia pausada antes de W0-01; esta trilha é isolada para avaliação e não altera status canônico automaticamente.

## Critérios de validação
1. Extrair especificações em alta fidelidade de cada seção e instância compartilhada.
2. Salvar originais estáticos (imagens/SVGs) localmente e conferir cada referência de asset.
3. Conferir fontes, texto, dimensões, alinhamentos, bordas, gradientes e espaçamento.
4. Conferir estados de interação, scroll, hover, controles, carrosséis e mídia.
5. Comparar screenshots nas mesmas dimensões e registrar cada divergência.
6. Bloquear merge e publicação enquanto houver divergência não resolvida.

Nenhuma divergência está previamente autorizada; mudanças ao próprio Figma estão fora de escopo.
