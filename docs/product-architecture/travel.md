---
id: GPA-003
title: Guivos Travel
status: consolidated
version: 1.3.0
owner: Guivos
last_updated: 2026-08-13
---

# Guivos Travel

## Papel

Guivos Travel é o produto responsável por viagens e experiências relacionadas a deslocamento, destinos e turismo dentro do Ecossistema Guivos.

## Operação vigente

O Guivos Travel já existe operacionalmente e possui as seguintes frentes de serviço:

1. **Hotéis**;
2. **Experiências**;
3. **Aluguel por temporada**;
4. **Aéreo**;
5. **Pacotes**;
6. **Ônibus**;
7. **Locação de veículos**;
8. **Cruzeiro marítimo**;
9. **Câmbio**.

Essas frentes constituem serviços reais da operação do Travel e não capacidades hipotéticas ou futuras.

A apresentação pública desses serviços pode ser organizada por necessidade de viagem sem alterar sua natureza operacional:

```text
PARA ONDE IR
→ Pacotes
→ Cruzeiro marítimo
→ destinos e possibilidades

COMO CHEGAR
→ Aéreo
→ Ônibus

ONDE FICAR
→ Hotéis
→ Aluguel por temporada

COMO SE MOVIMENTAR
→ Locação de veículos

O QUE VIVER
→ Experiências

O QUE PRECISA PARA IR
→ Câmbio
```

`Descobrir destinos` é uma camada de descoberta e inspiração do Travel e **não** um décimo serviço operacional.

## Escopo principal

- destinos;
- roteiros;
- hospedagens;
- passeios;
- experiências locais;
- parceiros de turismo;
- planejamento de viagens;
- ofertas e jornadas relacionadas a viagens;
- operação dos nove serviços vigentes descritos neste documento.

## Home Pública do Guivos Travel

A arquitetura estratégica, narrativa e funcional da Home Pública do produto é governada por `GKR-UX-HOME-TRAVEL-MASTER-001`.

A Home deve equilibrar:

```text
inspiração
+
operação real
+
acesso direto aos serviços
```

Pergunta-mãe:

> **Até onde o seu próximo momento pode levar você?**

A Home deve permitir tanto a descoberta de lugares e experiências quanto o acesso direto aos serviços para quem já sabe o que procura.

### Descoberta de destinos

A descoberta de destinos deve privilegiar:

- imagens reais;
- lugares reais;
- cenários reais;
- destinos reais;
- experiências reais.

Regra:

> **As imagens devem aproximar a pessoa de possibilidades reais, e não criar uma camada genérica de inspiração desconectada do que o Travel consegue oferecer.**

A relação de referência é:

```text
IMAGEM REAL
↓
LUGAR REAL
↓
CONTEXTO REAL
↓
POSSIBILIDADE REAL DE VIAGEM
```

A Home não governa páginas internas de resultados, hotel, voo, pacote, experiência, reserva, passageiro, pagamento, voucher, perfil, checkout ou pós-venda.

## Limites

Guivos Travel não substitui o Guivos Journey, o Guivos Mall, o Guivos Business, o Guivos Media, o Guivos Intelligence ou o Guivos Ads.

Seu domínio principal é a operação especializada de viagens e experiências turísticas.

Uma viagem pode fazer parte da trajetória mais ampla de uma pessoa, mas o Travel não deve transformar toda viagem em uma narrativa obrigatória de evolução.

## Relação com o Programa de Pontos do Guivos Business

Guivos Travel admite utilização de pontos nas ofertas em que essa modalidade estiver efetivamente elegível, em conexão com o Programa de Pontos do Guivos Business.

O fluxo comercial de referência é:

```text
EMPRESA
↓
GUIVOS BUSINESS
↓
PROGRAMA DE PONTOS
↓
PESSOA RECEBE O BENEFÍCIO
↓
pode utilizar em ofertas elegíveis do
MALL / TRAVEL
↓
A PESSOA ESCOLHE COMO UTILIZAR
```

Neste fluxo específico, `Empresa` identifica a empresa cliente do Guivos Business. Essa terminologia não substitui `Organização` como tipo estrutural amplo de participante do ecossistema.

Os pontos são um benefício transacional e não representam nível de evolução da pessoa.

Esta relação arquitetural não cria taxa de conversão, emissão, expiração, transferência, pagamento híbrido, elegibilidade detalhada ou outras regras econômicas que dependam de autoridade própria.

## Relações principais

- recebe participantes e recomendações originadas no Guivos Journey;
- pode utilizar recursos comerciais do Guivos Mall;
- pode atender programas corporativos do Guivos Business;
- pode receber utilização de pontos do Programa de Pontos do Guivos Business em ofertas elegíveis;
- utiliza conteúdo do Guivos Media;
- utiliza Guivos Intelligence para personalização e análise;
- pode receber campanhas do Guivos Ads;
- possui Home Pública especializada governada por `GKR-UX-HOME-TRAVEL-MASTER-001`.
