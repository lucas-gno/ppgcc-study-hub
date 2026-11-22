"""Export data/mestrado.db and official Edital 43/2026 metadata to assets/data.js."""

import json
import pathlib
import sqlite3

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "mestrado.db"
OUT_PATH = ROOT / "assets" / "data.js"

LESSON_FILES = {
    1: "lessons/0001-teoria-dos-conjuntos.html",
    2: "lessons/0002-relacoes-binarias.html",
    3: "lessons/0003-propriedades-das-relacoes.html",
    4: "lessons/0004-relacoes-de-equivalencia.html",
    5: "lessons/0005-classes-e-particoes.html",
    6: "lessons/0006-relacoes-de-ordem.html",
    7: "lessons/0007-maximais-minimais-supremo-infimo.html",
    8: "lessons/0008-diagramas-de-hasse.html",
}

FASE_EXAM_WEIGHTS = {
    1: 20,  # Logica e Conjuntos: 4/20 na Prova 53/2025
    2: 25,  # Programacao C/Python: 5/20 na Prova 53/2025
    3: 55,  # Algoritmos e Estrutura de Dados: 11/20 na Prova 53/2025
    4: 0,
    5: 0,
}

OFFICIAL_META = {
    "titulo": "PPGCC IFCE Study Hub",
    "subtitulo": "Mestrado Acadêmico em Ciência da Computação — Turma 2027.1",
    "edital": "Edital nº 43/2026 (Retificações nº 01 e nº 02)",
    "linha": "Computação Aplicada (CA)",
    "tema_codigo": "CA05",
    "tema_titulo": "Otimização de recursos computacionais em infraestruturas institucionais baseadas em contêineres",
    "orientador": "Prof. Dr. Carlos Maurício Jaborandy de Mattos Dourado Júnior",
    "prova_escrita_data": "2026-12-04",
    "prova_escrita_horario": "09:00 - 11:00 (referência 53/2025)",
    "prova_escrita_duracao_min": 120,
    "prova_escrita_questoes": 20,
    "prova_escrita_corte": 3.0,
    "arguicao_inicio": "2026-12-14",
    "arguicao_fim": "2026-12-18",
    "arguicao_duracao_min": 20,
    "arguicao_corte": 7.0,
    "meta_npe": 8.5,
    "meta_na": 9.2,
    "meta_nf": 8.5,
    "benchmark_2025": {
        "ca01_npe_min": 3.0,
        "ca01_npe_mediana": 5.5,
        "ca01_npe_max": 8.5,
        "geral_npe_max": 9.5,
        "ca01_nf_max": 6.17,
        "geral_nf_max": 8.83,
    },
    "banca_2026": [
        {"nome": "Saulo Anderson Freitas de Oliveira", "papel": "Presidente", "areas": "Linguagens de Programação, Computabilidade"},
        {"nome": "Thiago Alves Rocha", "papel": "Vice-Presidente", "areas": "Representação do Conhecimento, Raciocínio Automatizado"},
        {"nome": "Corneli Gomes Furtado Júnior", "papel": "Membro", "areas": "Segurança de Redes, Teleinformática"},
        {"nome": "Róger Moura Sarmento", "papel": "Membro Colaborador", "areas": "Processamento Digital de Imagens, Aprendizado de Máquina"},
    ],
}

ARGUICAO_PERGUNTAS = [
    {
        "id": 1,
        "tipo": "TIPO_1",
        "peso_pts": 5 / 3,
        "titulo": "Google Borg vs. Kubernetes: Cell Sharing e Preempção",
        "pergunta": "No modelo do Google Borg (Verma et al., EuroSys '15), como o escalonamento misto (Prod vs. Non-Prod) eleva a utilização de servidores sem degradar aplicações sensíveis à latência, e como esse conceito se traduz para Classes de QoS no Kubernetes?",
        "pontos_chave": [
            "Cell sharing: co-locação de tarefas de longa duração prioritárias (Prod) com lotes tolerantes a falha (Batch/Non-Prod).",
            "Overcommitment controlado usando slack (folga entre limite reservado e consumo real).",
            "Tradução para Kubernetes QoS: Guaranteed (requests == limits, oom_score_adj -997), Burstable e BestEffort (oom_score_adj 1000).",
        ],
    },
    {
        "id": 2,
        "tipo": "TIPO_1",
        "peso_pts": 5 / 3,
        "titulo": "Autopilot (Rzadca et al., EuroSys '20) e Mitigação de Superdimensionamento",
        "pergunta": "Por que estimativas estáticas humanas levam a baixa utilização em clusters (15%-25%) e quais mecanismos estatísticos o Google Autopilot utiliza para fazer ajuste vertical/horizontal evitando oscilações (flapping) e OOM?",
        "pontos_chave": [
            "Medo de alertas/OOM leva desenvolvedores a superdimensionar requests/limits estáticos.",
            "Autopilot aplica janelas móveis exponenciais (ML/estatístico) para estimar consumo máximo com margem de segurança alpha.",
            "Histerese assimétrica: scale-up rápido sob risco de contenção/OOM e scale-down conservador para evitar flapping.",
        ],
    },
    {
        "id": 3,
        "tipo": "TIPO_1",
        "peso_pts": 5 / 3,
        "titulo": "Recursos Compressíveis (CFS Throttling) vs. Incompressíveis (OOM-Killer)",
        "pergunta": "Na camada de kernel Linux (cgroups), qual a diferença operacional entre esgotar a cota de CPU e esgotar o limite de memória RAM, e qual o impacto na latência de cauda (P99) de serviços web?",
        "pontos_chave": [
            "CPU é recurso compressível: o escalonador CFS congela threads após consumir cpu.cfs_quota_us dentro de 100ms (CPU Throttling), mantendo o processo vivo porém elevando P99.",
            "Memória RAM é recurso incompressível: ultrapassar memory.max dispara o OOM-Killer com SIGKILL imediato (ExitCode 137).",
            "Validação experimental: comparar baseline estático, referência dinâmica e abordagem proposta em carga estável, variável e de pico.",
        ],
    },
    {
        "id": 4,
        "tipo": "TIPO_2",
        "peso_pts": 5 / 3,
        "titulo": "Alinhamento Profissional DGTI/IFCE e Ambiente de Pesquisa",
        "pergunta": "De que maneira sua atuação diária como Analista de TI na DGTI do IFCE fornece requisitos reais, restrições institucionais e um laboratório experimental viável para o tema CA05?",
        "pontos_chave": [
            "Conhecimento direto de cargas heterogêneas reais (SUAP administrativo diurno, picos de matrícula/Moodle, laboratórios acadêmicos).",
            "Restrições reais do setor público (ciclos licitatórios pela Lei 14.133/2021, orçamento finito) tornam otimização por software crítica.",
            "Experiência em infraestrutura/redes permite instrumentar métricas (Prometheus/cgroups) em ambiente de testbed representativo sem expor dados sensíveis.",
        ],
    },
    {
        "id": 5,
        "tipo": "TIPO_2",
        "peso_pts": 5 / 3,
        "titulo": "Transição de Base Não-Exata e Dedicação ao Programa",
        "pergunta": "Considerando que o Mestrado exige 360 horas diurnas e dedicação mínima de 20h semanais com rigor formal em Ciência da Computação, como você organiza sua rotina na DGTI e preenche eventuais lacunas teóricas?",
        "pontos_chave": [
            "Apoio formal da chefia (Anexo IV) e cumprimento estruturado das 20h+ semanais compatibilizando aulas diurnas e pesquisa aplicada.",
            "Nivelamento intensivo já executado antes da seleção cobrindo Matemática Discreta, C/Python, Análise de Algoritmos e leitura integral de Borg/Autopilot/K8s.",
            "Compromisso com publicações em eventos Qualis A (ex.: SBRC) alinhadas aos projetos do orientador.",
        ],
    },
    {
        "id": 6,
        "tipo": "TIPO_2",
        "peso_pts": 5 / 3,
        "titulo": "Metodologia de Validação do Protótipo CA05",
        "pergunta": "Como você estruturaria o experimento para provar cientificamente que o seu método adaptativo de alocação supera tanto as configurações estáticas quanto uma estratégia dinâmica de referência?",
        "pontos_chave": [
            "Desenho experimental pareado com perfis de carga reproduzíveis (estável, variável e pico/burst).",
            "Métricas coletadas em alta resolução: utilização efetiva de CPU/RAM, tempo de resposta (incluindo P95/P99), vazão, taxa de violações de SLA e overhead do controlador.",
            "Validação estatística com múltiplas rodadas, intervalos de confiança e testes de hipótese (p < 0.05) garantindo reprodutibilidade.",
        ],
    },
]


def export_database(db_path: pathlib.Path = DB_PATH, out_path: pathlib.Path = OUT_PATH) -> dict:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        fases = [dict(r) for r in conn.execute("SELECT * FROM fases_edital ORDER BY numero").fetchall()]
        for f in fases:
            f["peso_prova"] = FASE_EXAM_WEIGHTS.get(f["id"], 0)

        topicos = [dict(r) for r in conn.execute("SELECT * FROM topicos_edital ORDER BY id").fetchall()]
        for t in topicos:
            t["lesson_file"] = LESSON_FILES.get(t["id"])

        topic_to_fase = {t["id"]: t["fase_id"] for t in topicos}

        questoes = [dict(r) for r in conn.execute("SELECT * FROM questoes ORDER BY id").fetchall()]
        for q in questoes:
            q["fase_id"] = topic_to_fase.get(q["topico_id"])

        obras = [dict(r) for r in conn.execute("SELECT * FROM obras_artigos ORDER BY id").fetchall()]
        perfil_row = conn.execute("SELECT * FROM perfil_curriculo LIMIT 1").fetchone()
        perfil = dict(perfil_row) if perfil_row else {}

        payload = {
            "meta": OFFICIAL_META,
            "fases": fases,
            "topicos": topicos,
            "questoes": questoes,
            "obras": obras,
            "arguicao_perguntas": ARGUICAO_PERGUNTAS,
            "perfil_curriculo": perfil,
        }

        js_content = (
            "/* Arquivo gerado automaticamente por scripts/export_db.py a partir de data/mestrado.db */\n"
            "window.PPGCC_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
        )
        out_path.write_text(js_content, encoding="utf-8")
        return payload
    finally:
        conn.close()


if __name__ == "__main__":
    data = export_database()
    print(
        f"Exported {len(data['fases'])} fases, {len(data['topicos'])} topicos, "
        f"{len(data['questoes'])} questoes, {len(data['obras'])} obras -> {OUT_PATH}"
    )
