---
id: GKR-UX-PEOPLE-LIVE-MAP-001
title: Gráfico Vivo de Pessoas — Mapa Mundial, Atualização e Proteção das Pessoas
status: proposed
version: 0.1.0
owner: Arquitetura da Experiência da Guivos
last_updated: 2026-10-19
normative: false
maturity: design_validated_operation_proposed
related:
  - GKR-UX-OPPORTUNITIES-LIVE-001
---

# Gráfico Vivo de Pessoas — Mapa Mundial, Atualização e Proteção das Pessoas

## 1. Finalidade, decisão de design e fronteira

A superfície experimental **Gráfico Vivo de Pessoas** é um mapa mundial interativo, desenvolvido em **estação própria e isolada no Replit**, distinto do Gráfico Vivo de Oportunidades e das Homes. Seu layout visual foi declarado concluído na rodada de design de 2026-10-19; essa declaração **não equivale à aprovação de conexão a cadastros reais ou publicação**.

Finalidade narrativa: demonstrar presença territorial ampla de Pessoas que participam do ecossistema Guivos e áreas nas quais desejam evoluir, sem identificar Pessoas, construir perfis públicos, localizar indivíduos ou inferir características sensíveis. Referência de interação: mapa mundial explorável, zoom e pontos roxos, com tooltip compacto de duas linhas, no padrão aprovado para o laboratório.

Padrões herdados da Guivos: Goldplay Regular 400, Medium 500, SemiBold 600 como especificação institucional; Purple 1 #7D55C6 (Pessoas), Purple 4 #5D34A9, Gray 3 #E3E3E3 e superfícies globais brancas. A **área cartográfica** utiliza tema escuro, por decisão expressa de design. Licenças de fontes e cartografia devem ser verificadas independentemente.

## 2. Gatilho funcional pretendido e cadência

**Direção de produto proposta:** a entrada de uma Pessoa elegível no mapa decorre de um **evento verificado**, e não de intervalos periódicos de desenho. A inclusão só ocorre quando estão atendidas conjuntamente as condições:

1. Cadastro validamente concluído e **estado ativo**, segundo contrato de identidade/cadastro;
2. Área de evolução/interesse manifestada e válida para o uso previsto;
3. Região de referência de cadastro suficientemente ampla, proveniente de dado autorizado e adequado à finalidade, sem divulgar coordenadas precisas;
4. Base legal, transparência e escolhas de privacidade pertinentes; validação de proteção de dados e política de participação/exibição pública;
5. Regras de segurança da representação pública satisfeitas.

**Evento de ativação elegível:** acrescentar uma única Pessoa ao **estoque interno** de Pessoas elegíveis, uma vez por identificador interno, independentemente do número de interesses declarados. **Inativação, cancelamento de participação, revogação aplicável ou perda de elegibilidade:** remover da projeção pública e do estoque elegível, observando obrigações legais de retenção no backend. **Mudança de região ou área de evolução:** atualizar a projeção de maneira auditável, sem criar um novo cadastro/ponto em duplicidade. Alterações sem efeito sobre as condições de elegibilidade não criam movimentações artificiais.

**Cadência:** atualização lógica por **evento confirmado**; sem relógio que acrescente Pessoas ficticiamente. Transporte candidato: snapshot inicial versionado + canal SSE para mudanças ou snapshots agregados; reconexão, idempotência, ordenação, reconciliação e carimbo da última atualização. A periodicidade exata de publicação de atualizações **visíveis** deve ser validada sob risco de inferência; eventos individuais podem exigir **agregação em lotes e atraso deliberado** em vez de exposição imediata a terceiros. Metas de latência do Gráfico de Oportunidades **não se aplicam automaticamente** ao mapa de Pessoas. Sem SLA definido nesta versão.

## 3. Semântica do ponto e limite de exposição

**Intenção visual aprovada no laboratório:** um ponto corresponde a uma **persona 100% fictícia**, com uma localidade curta e uma área de evolução fictícia. A distribuição global sintética é irregular, tem concentrações maiores no Brasil e zonas com poucos/nenhum ponto, sem alegar que seja cadastro real.

**Restrição para produção:** a fórmula `1 ponto público = 1 pessoa real em sua localização de cadastro + interesse` **não está autorizada nesta especificação**. Ausência de nome NÃO significa anonimato. Coordenada/localidade combinada a interesses (especialmente saúde, espiritualidade, religião, finanças ou outros tópicos potencialmente sensíveis) e a observação temporal de novas entradas pode individualizar ou revelar atributos de uma Pessoa.

Implementação pública futura deve:

- Tratar geolocalização/área e interesses como dados pessoais potencialmente identificáveis no backend, protegidos por controle de acesso e minimização.
- Não enviar ao navegador coordenadas individualizadas, IDs internos, timestamps individuais, IPs ou sequência de novas inscrições pessoais.
- Usar **regiões amplas / células geográficas aproximadas**, com supressão de regiões pouco povoadas, agregação por densidade e proteção contra reidentificação por zoom, tooltip, filtros ou comparação temporal. Um limiar simples de 10 pessoas é apenas hipótese inicial de teste e **não basta isoladamente**.
- Mostrar categorias de evolução apenas em formato agregado, após avaliação de sensibilidade, granularidade e possibilidade de combinação que identifique indivíduos; considerar generalização ou supressão de categorias sensíveis.
- Permitir mapa aparentemente pontilhado (pontos decorativos não associados um-a-um às coordenadas reais) sempre que isso representar honestamente os totais agregados, sem induzir leitura de localização individual.
- Testar ataques de inferência por diferença entre snapshots, zoom máximo, regiões pequenas e eventos de baixa frequência.
- Não publicar como dados reais os pontos de laboratório; nenhuma conexão à base produtiva até decisão explícita de Produto, Privacidade/Jurídico, Segurança e Engenharia.

## 4. Contrato de dados candidato (não operacional)

Fonte de verdade: cadastro/estado ativo da Pessoa e manifestação de áreas de evolução devidamente autorizadas. Projeção interna por eventos versionados contendo um `event_id` idempotente, `person_id` interno protegido, `state_before`, `state_after`, `effective_at`, `eligibility_rule_version`, categoria e região normalizada; **não disponibilizar este evento bruto ao cliente público**.

A API pública, quando autorizada, entregará exclusivamente **snapshot agregado / distribuição segura**, versão e data de atualização, com medidas aplicadas de limitação espacial, cardinalidade, supressão e proteção contra inferência temporal. Preferir atualização em lotes se a divulgação de mudanças individuais gerar risco. Uma Pessoa conta uma única vez no total; regras para múltiplas áreas e revisão do interesse devem ser formalizadas e testadas.

Na indisponibilidade da fonte, não simular movimento. Exibir estado de indisponibilidade ou último dado identificado como desatualizado, sujeito à política de retenção do snapshot.

## 5. Contrato de UX do laboratório validado em design

- Mapa mundial escuro dentro de superfície Guivos; pontos roxos.
- Navegação por zoom, pan e recursos de acessibilidade, com altura ampliada e responsividade.
- Pontos fictícios distribuídos em diferentes regiões, de forma irregular e com zonas vazias; concentração maior no Brasil.
- Bandeirinha conectada por traço horizontal roxo ampliado, contorno roxo, fundo escuro translúcido e texto claro.
- Duas linhas no tooltip do laboratório: localidade curta (ex.: `Rio de Janeiro-BR`) em Goldplay SemiBold 600; área fictícia de evolução (ex.: `Relacionamentos`) em Regular 400. Sem nome de Pessoa ou identificador.
- **Não transportar automaticamente** o tooltip de pessoa individual para dados reais. Para produção, revalidar texto e granularidade como agregado seguro.
- Evitar cabeçalhos, selos e cartões demonstrativos que desviem o foco; ainda assim, jamais representar dados sintéticos como cadastros existentes da Guivos em contexto de publicação.

## 6. Critérios de aprovação antes da integração real

| Gate | Evidência necessária | Estado |
|---|---|---|
| PVM-01 Semântica de Pessoa ativa | Estados, exclusões, duplicidade, múltiplos interesses e elegibilidade | Aberto |
| PVM-02 Fonte e integridade | Cadastro, eventos verificáveis, idempotência e reconciliação | Aberto |
| PVM-03 Localização e base legal | Fonte autorizada, minimização, privacidade, direitos e transparência | Aberto |
| PVM-04 Risco de reidentificação | Zoom, pequenas regiões, categorias sensíveis e ataques de diferença | Aberto |
| PVM-05 Agregação pública | Granularidade, supressão, limite de grupos e tratamento de áreas | Aberto |
| PVM-06 Atualização segura | Publicação em lote, latência, estado desatualizado, segurança e desempenho | Aberto |
| PVM-07 Acessibilidade e visual | Tipografia, contrastes, teclado, mobile, tooltip e atribuição cartográfica | Aberto |
| PVM-08 Publicação | Revisão institucional GKR, privacidade, engenharia e autorização final | Aberto |

## 7. Registro da decisão e próximos passos

- **Layout do laboratório:** declarado finalizado pelo responsável do projeto.
- **Operação pretendida:** inclusão/remoção/atualização a cada mudança verificada das condições de elegibilidade da Pessoa, com fonte na plataforma Guivos.
- **Visualização de uma Pessoa real por ponto geolocalizado e interesse individual:** **não aprovada para produção**, sujeita a revisão de privacidade e alternativa de agregação adequada.
- **Projeto Replit:** estação independente Gráfico Vivo de Pessoas, sem integração produtiva neste momento.
- **Publicação do mapa real e atualizações ao público:** bloqueada até aprovação de PVM-01 a PVM-08.

O documento deve ser referenciado posteriormente no MENU do GKR em Experiência e Journey / Visualizações e Narrativa, mediante aprovação e publicação da governança.
