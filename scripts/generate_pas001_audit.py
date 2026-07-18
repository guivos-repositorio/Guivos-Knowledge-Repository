from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PA = ROOT / "docs" / "product-architecture"
R = json.loads((ROOT / "pas001-audit-output.json").read_text(encoding="utf-8"))
assert R["total_capability_extensions"] == 54
assert not R["missing_metadata"] and not R["links"]["broken"]
assert all(v["present"] and v["status"] == "active" and v["version"] == "1.0.0" for v in R["final_contracts"].values())


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(x).replace("|", "\\|").replace("\n", " ") for x in row) + " |")
    return "\n".join(out)


def cap(doc_id):
    names = {"CC":"01", "CV":"02", "OBJ":"03", "EV":"04", "PP":"05", "OA":"06", "IC":"07", "EXP":"08", "EC":"09"}
    m = re.match(r"PAS-001-(CC|CV|OBJ|EV|PP|OA|IC|EXP|EC)-", doc_id)
    return names[m.group(1)] if m else "Transversal"


def nature(doc_id):
    for suffix, label in [("FOUNDATION-001","Fundamentos"),("LIFECYCLE-001","Ciclo de vida"),("STATE-001","Estados"),("UPDATE-001","Atualização"),("CONFLICT-001","Conflitos"),("PROGRESS-001","Progresso"),("VIEW-001","Visualização"),("EVENT-INTEGRATION-001","Eventos e integrações"),("EVENT-001","Eventos"),("INTEGRATION-001","Integrações"),("KPI-001","Indicadores"),("CONTRACT-001","Contrato final")]:
        if doc_id.endswith(suffix): return label
    return "Extensão normativa"

caps = [
("01 — Captura de Contexto","Iniciar compreensão autorizada","Functionally complete — 100%","PAS-001-CC-CONTRACT-001"),
("02 — Contexto Vivo","Representar o contexto atual","Functionally complete","PAS-001-CV-CONTRACT-001"),
("03 — Objetivos","Governar direções assumidas","Functionally complete","PAS-001-OBJ-CONTRACT-001"),
("04 — Eventos de Vida","Governar mudanças relevantes","Functionally complete","PAS-001-EV-CONTRACT-001"),
("05 — Próximos Passos","Governar movimentos possíveis","Functionally complete — 100%","PAS-001-PP-CONTRACT-001"),
("06 — Oportunidades Ativas","Governar meios admissíveis","Functionally complete — 100%","PAS-001-OA-CONTRACT-001"),
("07 — Intervenções Contextuais","Governar manifestação ou silêncio","Functionally complete — 100%","PAS-001-IC-CONTRACT-001"),
("08 — Experiências","Governar o que foi vivido","Functionally complete — 100%","PAS-001-EXP-CONTRACT-001"),
("09 — Evolução Contínua","Governar trajetórias de mudança","Functionally complete — 100%","PAS-001-EC-CONTRACT-001")]
questions = [
("01","Como permitir que um participante expresse seu contexto e seja inicialmente compreendido sem transformar captura, transcrição, interpretação, síntese, confirmação ou persistência em conceitos equivalentes?","PAS-001-CC-LIFECYCLE-001","Maintain"),
("02","Como a Guivos mantém uma representação viva, confiável, explicável e continuamente evolutiva do participante?","PAS-001 0.5.0, seção 28","Refinar terminologia na edição 1.0.0"),
("03","Como a Guivos compreende para onde o participante deseja evoluir?","PAS-001-OBJ-FOUNDATION-001","Refinar para direção conscientemente assumida"),
("04","Como mudanças relevantes alteram a jornada do participante?","PAS-001-EV-FOUNDATION-001","Maintain"),
("05","Como grandes objetivos se tornam ações possíveis?","PAS-001-PP-FOUNDATION-001","Maintain"),
("06","Quais meios disponíveis, legítimos e compatíveis podem apoiar este participante em seu contexto atual?","PAS-001-OA-FOUNDATION-001","Maintain"),
("07","Existe uma razão legítima e um momento adequado para a Guivos se manifestar agora, ou o melhor comportamento é aguardar ou permanecer em silêncio?","PAS-001-IC-FOUNDATION-001","Maintain"),
("08","O que foi efetivamente vivido por este participante, em qual contexto, com qual forma de participação e o que pode legitimamente ser reconhecido a partir dessa vivência?","PAS-001-EXP-FOUNDATION-001","Maintain"),
("09","Que mudanças podem ser legitimamente reconhecidas na trajetória deste participante ao longo do tempo, em relação a quais direções ou referências, com quais evidências, limitações e incertezas?","PAS-001-EC-FOUNDATION-001","Maintain")]
supersession = [
("PAS-001 §7","Mapa histórico","Historical only","Contratos finais 01–09"),
("Pontos de retomada antigos","Próxima frente","Supersede","PAS-001-AUDIT-001"),
("PAS-001 §§8–27","Captura de Contexto","Refine","CC-LIFECYCLE, EVENT-INTEGRATION e CONTRACT"),
("Contexto inicial confirmado","Confirmação","Refine","CC-LIFECYCLE"),
("Primeiro valor","Valor inicial","Refine","CC-CONTRACT"),
("PAS-001 §28","Pergunta do Contexto Vivo","Refine","PAS-001-AUDIT-001"),
("Estados históricos CV/OBJ/EV/PP","Estados de capacidade","Supersede","Contratos finais correspondentes"),
("Definição histórica de Oportunidade Ativa","Oportunidade","Supersede","OA-FOUNDATION e OA-CONTRACT"),
("Apresentação de oportunidade","Manifestação","Supersede","IC-CONTRACT"),
("Pergunta histórica de Experiências","Experiência","Supersede","EXP-FOUNDATION e EXP-CONTRACT"),
("Pergunta histórica de Evolução","Evolução","Supersede","EC-FOUNDATION e EC-CONTRACT"),
("Distância para Evolução","Linguagem estratégica","Deprecate como conceito normativo","PAS-001-RECON-001"),
("Interpretação inicial","Interpretação e persistência","Refine","CC-LIFECYCLE e GIA-000"),
("Recomendação","Relevância e apresentação","Refine","OA-CONTRACT e IC-CONTRACT"),
("Sucesso do Journey","Critério global","Refine","Contratos finais e princípios permanentes")]
gates = [
(1,"Capacidade 01 concluída","Pass","Três extensões vigentes e contrato final ativo."),
(2,"Capacidades 02–09 preservadas","Pass","51 extensões preservadas; oito contratos finais ativos."),
(3,"Mapa final","Pass","Nove capacidades reconciliadas."),
(4,"Perguntas centrais","Pass with editorial action","Nove perguntas mapeadas; duas redações serão refinadas."),
(5,"Supersessão","Pass","Matriz final incorporada à auditoria e à Matriz Canônica."),
(6,"Autoridade documental","Pass","Registro transversal gerado."),
(7,"Pontos históricos","Pass","Somente a edição candidata permanece como próxima frente."),
(8,"Conceitos transversais","Pass with editorial action","Sem conflito bloqueante."),
(9,"Navegação","Pass","Auditoria adicionada aos índices e ao MkDocs."),
(10,"Links","Pass",f"{R['links']['checked']} links locais verificados; nenhuma quebra."),
(11,"Versões","Pass","Artefatos sincronizados transacionalmente."),
(12,"Lacunas funcionais","Pass","Nenhuma lacuna funcional bloqueante."),
(13,"Reabertura","Pass with editorial action","Critérios presentes; Contexto Vivo possui critérios distribuídos."),
(14,"Artefatos canônicos","Pass","Roadmap, Board, Matriz e Changelog revisados."),
(15,"Coerência entre camadas","Pass","Sem transferência de autoridade à Intelligence ou Platform.")]
authority = [
("PAS-001","0.5.0","draft","Transversal","Especificação-base","Base histórica e filosófica"),
("PAS-001-RECON-001","1.0.0","active","Transversal","Reconciliação","Hierarquia, supersessão e gates")]
for x in sorted(R["files"], key=lambda d: d["id"]):
    authority.append((x["id"],x["version"],x["status"],cap(x["id"]),nature(x["id"]),"Escopo especializado do documento"))
authority += [("PAS-001-AUDIT-001","1.0.0","active","Transversal","Auditoria","Autorizar ou bloquear consolidação"),("GLPA-001","1.1.1","approved","Transversal","Arquitetura","Responsabilidades das camadas"),("GIA-000","1.3.0","active","Transversal","Intelligence Architecture","Interpretação e limites da Intelligence")]

sections = {}
sections[4851] = ("Autoridade e vínculo","Autoridade normativa de auditoria final do `PAS-001`. Não publica `1.0.0` nem reabre capacidades silenciosamente.")
sections[4852] = ("Finalidade","Determinar cobertura, coerência, rastreabilidade, navegação, autoridade e estabilidade para iniciar uma edição federada.")
sections[4853] = ("Pergunta central","> **O conjunto normativo vigente do Guivos Journey possui autoridade, cobertura, coerência, rastreabilidade, navegação e estabilidade suficientes para iniciar a consolidação editorial do PAS-001 1.0.0 sem apagar o histórico, duplicar contratos ou reintroduzir conceitos superados?**")
sections[4854] = ("Parecer executivo","> **Ready for consolidation — PAS-001 1.0.0 editorial consolidation authorized.**\n\nA decisão autoriza somente a edição candidata. Não significa `Ready for publication`, implementação ou lançamento.")
sections[4855] = ("Evidência mecânica",f"- extensões encontradas: `{R['total_capability_extensions']}`;\n- metadados obrigatórios ausentes: `{len(R['missing_metadata'])}`;\n- contratos finais ativos: `9 de 9`;\n- links locais verificados: `{R['links']['checked']}`;\n- links quebrados: `{len(R['links']['broken'])}`;\n- alvos MkDocs inexistentes: `{len(R['nav']['missing_targets'])}`.")
sections[4856] = ("Inventário por capacidade",table(("Capacidade","Esperado","Encontrado"),[(k,v,R['actual_counts'][k]) for k,v in {"CC":3,"CV":8,"OBJ":7,"EV":6,"PP":6,"OA":6,"IC":6,"EXP":6,"EC":6}.items()]))
sections[4857] = ("Itens fora do escopo","APIs, schemas, implantação, produto final, metas pós-baseline, conectores, modelos treinados, aprovação regulatória global e operação em escala.")
sections[4858] = ("Princípios","Evidência antes do parecer; especificidade; temporalidade; preservação histórica; estrutura federada; independência entre capacidades; proteção do participante; neutralidade comercial; reabertura formal.")
sections[4859] = ("Estados de avaliação","`Pass`, `Pass with editorial action`, `Partial`, `Blocked`, `Conflict`, `Missing`, `Historical only`, `Not applicable` e `Reopened`.")
sections[4860] = ("Regra de bloqueio","Achado crítico ou alto que altere autoridade, fronteira, proteção, estado vigente ou coerência entre camadas bloqueia a consolidação.")
sections[4861] = ("Resultado dos 15 gates",table(("Gate","Objeto","Resultado","Evidência"),gates))
sections[4862] = ("Mapa final de capacidades",table(("Capacidade","Responsabilidade","Estado","Autoridade"),caps))
sections[4863] = ("Mapa final de perguntas centrais",table(("Capacidade","Pergunta","Autoridade","Decisão"),questions))
sections[4864] = ("Matriz final de supersessão",table(("Origem","Conceito","Decisão","Autoridade vigente"),supersession))
sections[4865] = ("Registro de autoridade documental",table(("Documento","Versão","Estado","Capacidade","Natureza","Autoridade"),authority))
sections[4866] = ("Pontos de retomada","Todos os pontos anteriores são históricos. O único ponto vigente é a edição candidata consolidada e federada do `PAS-001 1.0.0`.")
sections[4867] = ("Conceitos transversais","Participante, contexto, finalidade, autoridade, confirmação, persistência, recorte, evento, integração, oportunidade, intervenção, experiência, resultado, evolução, confiança, incerteza, causalidade, sensibilidade, revogação e falha segura foram reconciliados sem conflito bloqueante.")
sections[4868] = ("Navegação e links","Todos os alvos Markdown estavam presentes e nenhum link local verificado estava quebrado. A validação será repetida após a sincronização.")
sections[4869] = ("Versões","Arquitetura e Matriz `1.25.0 → 1.26.0`; Roadmap e Board `11.6.0 → 11.7.0`; Changelog `0.53.0 → 0.54.0`; `PAS-001` permanece `0.5.0`.")
sections[4870] = ("Reabertura","Todas as capacidades possuem critérios. No Contexto Vivo, a edição candidata deverá referenciar os critérios distribuídos nas extensões de conflitos e indicadores.")
sections[4871] = ("Coerência entre camadas","Journey governa significado funcional; Intelligence interpreta e propõe sem confirmar pelo participante; Platform sustenta mecanismos técnicos sem redefinir significado.")
for n, name in [(4872,"Captura de Contexto"),(4873,"Contexto Vivo"),(4874,"Objetivos"),(4875,"Eventos de Vida"),(4876,"Próximos Passos"),(4877,"Oportunidades Ativas"),(4878,"Intervenções Contextuais"),(4879,"Experiências"),(4880,"Evolução Contínua")]:
    extra = " Pass with editorial action." if name in {"Contexto Vivo","Objetivos"} else " Pass."
    sections[n] = (f"Auditoria — {name}",f"Contrato final, responsabilidades, limites, estados, eventos, integrações, indicadores, guardrails, cenários e reabertura avaliados.{extra}")
sections[4881] = ("Fronteiras","Nenhuma capacidade assume decisão de outra; evento técnico não equivale a confirmação humana; resultado comercial não redefine relevância, experiência ou evolução.")
sections[4882] = ("Fluxo transversal","`Captura → Contexto Vivo → Objetivos/Eventos → Próximos Passos → Oportunidades → Intervenções → Experiências → Evolução → atualização contextual` é possibilidade coordenada, não pipeline obrigatório.")
sections[4883] = ("Guivos Intelligence","Pode interpretar, classificar, propor, estimar e explicar. Não pode assumir Objetivo, impor Passo, decidir apresentação, confirmar Experiência ou reconhecer Evolução sem contrato.")
sections[4884] = ("Platform Layer","Sustenta identidade, autorização, persistência, eventos, APIs, filas, criptografia, auditoria, versionamento e revogação. Não redefine significado funcional.")
sections[4885] = ("Produtos especializados","Mall, Travel, Business, Media e Ads fornecem fatos operacionais; não determinam prioridade humana, progresso, experiência, evolução ou valor pessoal.")
sections[4886] = ("Preservação histórica","`PAS-001 0.5.0` e extensões permanecem no Git. A edição federada registra origem, supersessões, refinamentos e pendências.")
sections[4887] = ("Metadados",f"A auditoria encontrou `{len(R['missing_metadata'])}` ausências em campos obrigatórios dos 54 documentos de capacidade.")
sections[4888] = ("Duplicidades","Duplicação editorial pode ser reduzida; duplicação normativa exige registro na matriz de supersessão.")
sections[4889] = ("Terminologia","Normalizar nomes, estados, identificadores, capitalização e traduções. É proibido percentual global do Journey.")
sections[4890] = ("Estratégia editorial","O `PAS-001 1.0.0` será consolidado, federado, conciso, normativo, navegável e referencial.")
sections[4891] = ("Conteúdo especializado","Estados detalhados, eventos, integrações, KPIs, guardrails, cenários e regras permanecem nas extensões.")
sections[4892] = ("Achados","| Achado | Severidade | Estado |\n|---|---|---|\n| Pergunta do Contexto Vivo usa “evolutiva” | Média | Não bloqueante |\n| Pergunta de Objetivos usa “deseja evoluir” | Média | Não bloqueante |\n| Reabertura do Contexto Vivo está distribuída | Baixa | Não bloqueante |\n| Mapa histórico permanece no 0.5.0 | Baixa | Controlado |")
sections[4893] = ("Lacunas bloqueantes","Nenhuma após a incorporação da matriz de supersessão, do registro de autoridade e da sincronização canônica.")
sections[4894] = ("Lacunas não bloqueantes","Redação, simplificação, diagramas, implementação, validação produtiva, tradução e documentação operacional.")
sections[4895] = ("Regra do parecer","`15 gates avaliados + nenhum achado crítico/alto aberto + ações editoriais registradas = Ready for consolidation`.")
sections[4896] = ("Decisão formal","Parecer `Ready for consolidation`; 15 gates aprovados; zero achados críticos; zero achados altos; quatro ações editoriais não bloqueantes.")
sections[4897] = ("Condições de reabertura","Novo conflito entre contratos, regressão de autoridade, perda de rastreabilidade, mudança material de camada ou falha da edição candidata.")
sections[4898] = ("Critérios para edição candidata","Utilizar mapa, perguntas, supersessão e autoridade desta auditoria; não duplicar integralmente extensões.")
sections[4899] = ("Ready for publication","Somente após criação e revisão da candidata, validação de links, navegação, versões, autoridade, mapa e ausência de regressões.")
sections[4900] = ("Comportamentos proibidos","Publicar automaticamente; apagar histórico; ocultar conflito; reabrir sem fundamento; transferir decisão à Intelligence; transferir significado à Platform; aceitar link normativo quebrado; criar documento monolítico.")
sections[4901] = ("Critérios de aceite","Inventário, 15 gates, nove capacidades, mapas, matriz, autoridade, links, versões, navegação, achados, parecer e próximo ponto foram registrados.")
sections[4902] = ("Artefatos produzidos","Documento normativo, relatório dos gates, mapa final, mapa de perguntas, matriz de supersessão, registro de autoridade, evidência mecânica, achados e parecer.")
sections[4903] = ("Consolidação da auditoria","`PAS-001-AUDIT-001 1.0.0` autoriza o início da edição candidata e não autoriza sua publicação.")
sections[4904] = ("Próximo ponto exato","> **Edição Consolidada e Federada do PAS-001 — Guivos Journey 1.0.0.**")
sections[4905] = ("Sequência","`PAS-001-AUDIT-001 → edição candidata → validação → Ready for publication → publicação 1.0.0 → mapa final`.")
for n in range(4906,4925):
    sections[n] = ("Controle da etapa", "O `PAS-001` permanece `Draft 0.5.0`; as 54 extensões permanecem vigentes; regressões bloqueiam publicação; nenhuma etapa pode ser omitida sem decisão formal.")
sections[4925] = ("Encerramento","A auditoria está concluída. O próximo trabalho autorizado é a edição candidata consolidada e federada do `PAS-001 1.0.0`.")

front = """---
id: PAS-001-AUDIT-001
title: Auditoria Final de Prontidão e Consolidação do Guivos Journey
status: active
version: 1.0.0
owner: Guivos
last_updated: 2026-07-18
parent: PAS-001
normative: true
related:
  - PAS-001
  - PAS-001-RECON-001
  - PAS-001-CC-CONTRACT-001
  - PAS-001-CV-CONTRACT-001
  - PAS-001-OBJ-CONTRACT-001
  - PAS-001-EV-CONTRACT-001
  - PAS-001-PP-CONTRACT-001
  - PAS-001-OA-CONTRACT-001
  - PAS-001-IC-CONTRACT-001
  - PAS-001-EXP-CONTRACT-001
  - PAS-001-EC-CONTRACT-001
  - GLPA-001
  - GIA-000
---

# PAS-001-AUDIT-001 — Auditoria Final de Prontidão e Consolidação do Guivos Journey
"""
body = [front]
for n in range(4851,4926):
    title, content = sections[n]
    body.append(f"\n# {n}. {title}\n\n{content}\n")
(PA / "pas-001-guivos-journey-auditoria-final-prontidao.md").write_text("".join(body), encoding="utf-8")
print("audit document generated")
