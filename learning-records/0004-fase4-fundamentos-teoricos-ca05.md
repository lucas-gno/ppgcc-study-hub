# Registro de Aprendizagem 0004: Fase 4 — Fundamentos Teóricos CA05

**Data de Conclusão:** 20/11/2026  
**Linha de Pesquisa:** Tema CA05 — *"Otimização de recursos computacionais em infraestruturas institucionais baseadas em contêineres"*  
**Orientador Alvo:** Prof. Dr. Carlos Maurício Jaborandy de Mattos Dourado Junior  
**Instituição:** PPGCC IFCE (Edital 43/2026 - Turma 2027.1)  
**Status da Fase 4:** 100% Concluída (Aulas 0028 a 0033)

---

## 1. Visão Geral das Aulas Concluídas

| Aula | Título do Módulo | Widgets & Simuladores Interativos | Questões Mapeadas |
|---|---|---|---|
| **0028** | Arquitetura e Fundamentos de Sistemas de Contêineres | Simulador de Isolamento de Kernel (Namespaces + Cgroups) | 5 Questões Calibradas (Namespaces, Cgroups, OverlayFS, Chroot) |
| **0029** | O Sistema Google Borg: Arquitetura e Escalonamento | Simulador de Escalonamento e Preempção Borg (Prod vs Non-Prod) | 5 Questões Calibradas (Borgmaster/Paxos, Borglet, Cell Sharing, Overcommit) |
| **0030** | Autopilot: Auto-Tuning e Auto-Scaling Dinâmico | Simulador de Direitos e Dimensionamento Autopilot (Rzadca et al., 2020) | 5 Questões Calibradas (VPA vs HPA, Margem $\alpha$, Histerese, OOM loop) |
| **0031** | Classes de Serviço e QoS no Kubernetes | Simulador de QoS e Calculadora do `oom_score_adj` | **Questão Oficial 06 do mestrado.db** + 4 Questões Calibradas |
| **0032** | Métricas de Desempenho e Alocação (Throttling e OOM) | Simulador de CFS Quota vs OOM-Killer e Linha do Tempo de Throttling | 5 Questões Calibradas (CFS, Throttling multithread, ExitCode 137, Eviction) |
| **0033** | Otimização em Infraestruturas Institucionais (DGTI/IFCE) | Calculadora de Sizing e Overcommitment Institucional (SUAP/Moodle/Labs) | 5 Questões Calibradas (Alinhamento de Pesquisa, SLAs, Lei 14.133, $P_{99}$) |

---

## 2. Conceitos Centrais Dominados

### 2.1. O Mecanismo Linux de Contêineres (Aulas 28 e 32)
- **Namespaces:** Provêm isolamento de visão espacial (`pid`, `net`, `mnt`, `ipc`, `uts`, `user`, `cgroup`).
- **Control Groups (Cgroups):** Provêm limitação e contabilidade volumétrica de recursos físicos (CPU, Memória, I/O, PIDs).
- **Recursos Compressíveis vs Incompressíveis:**
  - *CPU (Compressível):* Quando o contêiner esgota a cota de microssegundos no CFS (`cpu.cfs_quota_us` / `cpu.cfs_period_us`), o kernel apenas suspende temporariamente a execução de suas threads (*CPU Throttling*). O processo continua vivo (`ExitCode 0`), mas sofre picos drásticos de latência $P_{99}$.
  - *Memória RAM (Não-Compressível):* Quando o contêiner excede `memory.max`, o kernel não tem como atrasar requisições de alocação física. O *OOM-Killer* envia um sinal incondicional `SIGKILL` (sinal 9), resultando no código de término $128 + 9 = 137$ (*ExitCode 137*).

### 2.2. A Transposição do Google Borg para o Kubernetes (Aulas 29, 30 e 31)
- **Cell Sharing:** O segredo da alta utilização do Borg e do Kubernetes é misturar cargas prioritárias de longa duração (*Prod / Guaranteed*) com tarefas em lote tolerantes a interrupção (*Batch / BestEffort*).
- **Hierarquia de Extermínio sob Escassez de Nó (Node Memory Pressure):**
  - **1º BestEffort:** `oom_score_adj = 1000`. Mortos imediatamente pelo OOM-killer do kernel Linux. *(Cobrança da Questão 06 de mestrado.db)*.
  - **2º Burstable:** `oom_score_adj \in [2, 999]`, inversamente proporcional à fração de memória requisitada:
    $$\text{Score} = \min\left(\max\left(\left\lfloor 1000 - \frac{1000 \times \text{MemoryRequest}}{\text{NodeMemory}} \right\rfloor, 2\right), 999\right)$$
  - **3º Guaranteed:** `oom_score_adj = -997`. Altamente protegidos contra o OOM-killer.

### 2.3. Auto-Tuning e Sizing Dinâmico (Aula 30 - Rzadca et al., EuroSys 2020)
- Humanos superdimensionam recursos por medo de alertas de plantão, mantendo clusters operando com 15% a 25% de uso real.
- O Autopilot substitui esse palpite por estimadores estatísticos em janela móvel:
  $$L_{rec}(t) = (1 + \alpha) \cdot \hat{U}_{max}(t)$$
- Amortecimento assimétrico (*Damping / Histerese*): Scale-up rápido para salvar o contêiner de colapso; Scale-down lento e conservador para evitar oscilações desnecessárias (*flapping*).

### 2.4. Aplicação Direta ao Caso do IFCE / DGTI (Aula 33)
- **Restrições Institucionais:** Ciclos licitatórios longos (Lei 14.133/2021) de 6 a 18 meses para compra de novos servidores e limites orçamentários rígidos.
- **Heterogeneidade de Cargas:** SUAP (diurno/administrativo, alta prioridade), SIGAA/Moodle (picos em finais de período) e Laboratórios de Alunos (efêmeros, candidatos perfeitos para *BestEffort*).
- **Impacto Comprovado:** Políticas de consolidação e overcommitment seguro permitem reduzir a quantidade necessária de servidores físicos em até 50% a 60%, economizando energia e liberando capacidade para novos serviços acadêmicos.

---

## 3. Próximos Passos: Fase 5 (Tópicos 34 a 37)
Com os 33 tópicos teóricos e práticos 100% cobertos e testados, avançaremos para a **Fase 5: Arguição Oral & Alinhamento Prático com a Banca**:
1. **Aula 34:** Roteiro de Entrevista com a Banca Examinadora (Perguntas Tipo 1 - Técnicas e Institucionais).
2. **Aula 35:** Defesa de Pré-Projeto e Memorial Acadêmico no Tema CA05.
3. **Aula 36:** Simulado Geral de Arguição Oral com Feedback Interativo.
4. **Aula 37:** Plano Estratégico de Estudos e Cronograma Final até o Dia da Prova.
