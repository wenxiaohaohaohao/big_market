# Stage 3 Phase 2 Editorial Decision Package

日期：2026-07-14  
项目：Platform Intermediation and Local Multipliers  
阶段：Stage 3, Phase 2 — Editorial synthesis  
审查合同：reviewer/reviewer_full/v1  
Panel size：5  
状态：本文件只综合 Phase 1 审稿意见；本阶段未修改论文、附录、参考文献、核验代码或 PDF。

## 1. 结论先行

正式合同决定为：

**Reject or Major Revision**

项目层面的操作建议为：

> 当前版本暂不投稿。返回 Stage 2 的 contribution–theorem architecture checkpoint，完成 major theoretical repositioning 后，再以新的五人 panel 重新进入 Stage 3。

这不是“模型算错”，也不是“项目必须放弃”。阻断项是现有贡献表述没有充分区分两部分：

1. 已有 Type-II / SAM / Miyazawa household-feedback、regional leakage 与 repeated-spending multiplier；
2. 本文新增的 price-induced channel composition、channel-specific local-income coefficients、finite thresholds，以及 CES 条件下的 marginal-drag peak。

现有审查记录没有证明本文的精确公式已经存在。因此，正确处理不是直接放弃，而是先做 equation-level prior-art audit，并把 theorem hierarchy 改写成“general share path benchmark + CES-specific result”。如果这两个任务不能产生区别于标准 multiplier recomputation 的独立理论结果，再终止或重新定位 Economics Letters 路线。

## 2. Mechanical contract evaluation

Reviewer 顺序固定为 EIC、R1 Methodology、R2 Domain、R3 Perspective、Devil's Advocate。

| Dimension | Priority | EIC | R1 | R2 | R3 | DA | Contract vector |
|---|---|---|---|---|---|---|---|
| D1 methodology rigor | mandatory | pass | pass | warn | pass | block | [pass, pass, warn, pass, block] |
| D2 domain accuracy | mandatory | pass | pass | warn | pass | warn | [pass, pass, warn, pass, warn] |
| D3 argumentative coherence | mandatory | pass | pass | pass | pass | warn | [pass, pass, pass, pass, warn] |
| D4 cross-disciplinary relevance | high | pass | pass | warn | warn | warn | [pass, pass, warn, warn, warn] |
| D5 writing and structure | normal | pass | pass | pass | pass | pass | [pass, pass, pass, pass, pass] |

### 2.1 Failure conditions

| Condition | Reviewer predicates | Quantifier and count | Fired | Contract action |
|---|---|---|---|---|
| F1：任一 mandatory dimension 为 block | [false, false, false, false, true] | any；1/5 | **true** | reject_or_major_revision |
| F2：单一 reviewer 至少两个 mandatory dimensions 为 warn 或更差，且达到 panel majority | [false, false, true, false, true] | 2/5 | **false** | major_revision |
| F3：任一 high-priority dimension 为 block | [false, false, false, false, false] | any；0/5 | **false** | major_revision |
| F0：所有 reviewer 的所有 mandatory dimensions 均为 pass | [true, true, false, true, false] | all；3/5 | **false** | accept |

审计说明：sprint contract protocol 的明文公式把 N=5 的 majority 阈值写为 4，execution manifest 使用通常意义上的 3。F2 只有 2/5，采用任一阈值都不触发，因此不影响终局判定。

### 2.2 Precedence

F1 是唯一触发项，severity 最高。合同不允许用平均分、三份 accept 建议，或事后主观判断降低该 action。DA 同时提出 CRITICAL issue，因此 Accept 也被 iron rule 排除。

**精确合同终局 action：editorial_decision=reject_or_major_revision。**

## 3. Editorial decision letter

### 3.1 为什么不能接受当前版本

数学正确性不是阻断原因。R1 独立复核了 CES demand、income fixed point、recursive-retention multiplier、finite thresholds、marginal effects、内部峰值和 boundary cases，没有发现 result-level error。其他 reviewer 也认可模型可读、内部逻辑清楚。五位 reviewer 对 D5 全部给出 pass，主文 1,884 个文本词也符合 Economics Letters 短篇 theory note 的形式。

当前版本不能接受，原因是：

- DA 在 mandatory D1 给出 block，F1 机械触发；
- DA-CRITICAL 尚未解决；
- closest analytical benchmarks 尚未进行 equation-level 对照；
- repeated household-spending rounds、leakage、first-round versus induced-round distinction 不能作为新的理论贡献；
- below-one-half peak 依赖 CES share path，目前的文字没有充分标出其一般性边界；
- 参数 \(\rho_c\) 的空间收入归属、制度含义和可观测映射还不够明确，因而不能支撑过宽的平台或空间经济解释。

### 3.2 为什么不应立即放弃

- 没有发现数学错误、均衡不存在、阈值排序错误或不可修复的 research-design flaw；
- R2 与 DA 都没有证明 exact CES-plus-retention formula 已由既有论文推出；
- 修订可以集中于 contribution framing、general share-path benchmark、CES corollary、parameter interpretation 和 scope；
- 不需要扩建 full spatial GE、endogenous platform pricing、firm relocation 或完整税收系统；
- 大部分修订可以通过替换宽泛表述完成，不必突破 2,000-word limit。

### 3.3 Strengths retained after review

- equilibrium existence、uniqueness 与解析解通过方法审查；
- nominal local income、consumer-price effect 与 consumption-equivalent real income 的区分基本正确；
- Proposition 1、finite thresholds 和 CES peak 的代数可复核；
- appendix 与 deterministic verification code 构成可审查的证明链；
- 现有材料仍可能支持一篇窄而清楚的 analytical letter。

## 4. Weakness sub-claim inventory

标记规则：

- raised：该 reviewer 明确提出；
- corroborated：另一 reviewer 独立支持相同主张；
- not mentioned：没有提及，不视为同意；
- disputed：明确否认问题存在，或对严重性、修复方向存在实质冲突。

| ID | Atomic weakness sub-claim | Panel evidence | Classification |
|---|---|---|---|
| SC-1 | Closest analytical benchmarks 未被直接命名并逐项比较 | EIC raised；R2 corroborated | corroborated 2/4 |
| SC-2 | 必须区分 established multiplier/accounting setup 与 price-induced channel composition 的增量 | EIC、R2、R3 | **CONSENSUS-3** |
| SC-3 | 当前 novelty gap 是文字澄清还是 major repositioning | EIC/R3 倾向非阻断；R2 要求 major revision；DA 判 CRITICAL | **SPLIT** |
| SC-4 | \(\rho_c\) 应定义为每单位 gross spending 的 marginal local factor-and-ownership income，并列出包含和排除项 | R2、R3 | corroborated 2/4 |
| SC-5 | Fixed incidence 与 price pass-through 是 short-run reduced-form primitives；不应为修复而扩建完整模型 | EIC、R2、R3 | **CONSENSUS-3** |
| SC-6 | \(R\) 不是 full welfare，这一限制应在 abstract 或 application language 附近更显眼 | EIC、R3 | corroborated 2/4 |
| SC-7 | 应再次明确 \(B\) 的 local-income injection、\(G\) 的 outside-funded private demand 及二者差别 | EIC、R3 | corroborated 2/4 |
| SC-8 | \(s\) 是 gross expenditure share，不是 adoption、users、transactions、sellers 或一般 IO market share | R3 | single-reviewer |
| SC-9 | \(\varepsilon\geq0\) 排除了 adverse production-side base-income response，应放宽或解释 benchmark | R2 | single-reviewer |
| SC-10 | 缺少对 platform price、expenditure share、channel-income differential 的经验映射 | R2 | single-reviewer |
| SC-11 | 主结果的 central peak 使用 \(G=0\)；positive-\(G\) extension 应标示或收窄应用 | R2；DA related | single-reviewer with DA support |
| SC-12 | Li working paper 的 stable repository/publication status 尚未核实 | EIC | single-reviewer |
| SC-13 | 与 Li 的 equation-level overlap 未解决，categorical priority claim 应限定 | R2；DA related | single-reviewer with DA support |
| SC-14 | \(\alpha+\beta=1\) 的讨论只延续 income fixed point，不延续完整 household problem | R1 | single-reviewer |
| SC-15 | 应加入 verify_model.py 与 deterministic seed 的 code-availability statement | R1 | single-reviewer |
| SC-16 | 若 multiplier convexity 是正式结果，应进入 Proposition 1；否则不应暗示为主贡献 | R1 | single-reviewer |
| SC-17 | Lower finite-threshold equality 的 feasibility condition 需明确 | R1 | single-reviewer |

汇总：

- CONSENSUS-4：无；
- CONSENSUS-3：SC-2、SC-5；
- corroborated：SC-1、SC-4、SC-6、SC-7；
- genuine SPLIT：SC-3；
- 其余为 single-reviewer findings，仍需按证据逐项处理，不能自动丢弃。

### 4.1 DA-CRITICAL

DA 的核心论点是：当前所谓 retention-feedback mechanism 可以被描述为既有 Type-II / SAM / Miyazawa induced-spending multiplier 加上一个 composition-dependent coefficient。CES 改变该 coefficient，但没有额外增加 feedback state。

非 DA 证据如下：

- R2 支持 recurring feedback 与 leakage 已有先例；
- EIC 与 R3 同意必须把 accounting setup 与 incremental mechanism 分开，但不接受其必然致命；
- R1 只确认数学正确，没有对 exhaustive priority 作判断。

Editorial assessment：

> 这一批评对当前 framing 成立，但现有 records 不足以证明 exact CES-plus-retention result 已存在。因此，它是现稿的 CRITICAL defect，不是 duplication finding。

Required response：

1. 完成 equation-level prior-art comparison；
2. 给出一个不能仅以“把新的 \(\omega\) 代入标准 multiplier”概括的 theorem 或 comparative-static payoff；
3. 如果做不到，停止 Economics Letters 路线。

## 5. Disagreement arbitration

### 5.1 SC-3：clarification 还是 major repositioning

- EIC：模型和潜在贡献基本成立，主要是 salience risk；
- R1：数学成立，对 novelty severity 不表态；
- R2：closest multiplier antecedents 定位不足，必须 major revision；
- R3：accounting identity 与 mechanism 应分开，但 reduced-form insight 有可转移性；
- DA：将该问题升级为 CRITICAL。

裁决：

> 当前版本需要 major theoretical repositioning，不是普通文字润色；但现有证据尚不足以判定项目没有独立贡献。

### 5.2 逐项裁决

| Disputed question | Ruling | Reason |
|---|---|---|
| Recurring spending rounds、leakage、first-round/induced-round distinction 能否作为新贡献 | **不能** | R2 与 DA 指出其既有 lineage；EIC/R3 也要求分开 setup 与 mechanism |
| Exact CES channel substitution、channel-specific income coefficients、finite regions 与 below-one-half peak 是否已被 prior art 证明 | **未被本轮证据证明** | R2 未找到相同组合但不保证 exhaustive；DA 承认其来源不证明 exact formula |
| Below-one-half peak 是否是一般 channel-substitution 结论 | **不是** | 任意 \(s(z)\) 不保证唯一峰值或峰值低于 \(1/2\)；当前是 CES-specific |
| 是否必须加入 endogenous pricing、relocation 或 full spatial GE | **不要求** | 更合适的修复是 general benchmark、CES corollary、\(\rho_c\) mapping 和严格 scope |
| 何时应放弃 | **P1-1 或 P1-2 失败时** | 若 exact result 已存在，或只靠大幅扩建模型才能产生独立贡献，就不适合当前 Letter |

## 6. Revision roadmap

### 6.1 P1 — Required

#### P1-1. Prior-art equation audit and novelty paragraph

来源：EIC、R2、R3、DA  
追踪：SC-1、SC-2、SC-3、SC-12、SC-13、DA-CRITICAL  
预计：3–5 个工作日

验收标准：

1. 内部 comparison matrix 覆盖 Type-II / SAM / Miyazawa、Pennings、Little–Doeksen、RIMS II / Round、Forman 与 Li；
2. 对每篇文献比较 state variables、first-round incidence、feedback coefficient、endogenous share、theorem 和 application；
3. 主文明确区分 established setup、本文 exact increment、尚未认证的 priority；
4. 删除未经核实的 categorical priority language；
5. 若发现 exact theorem 已存在，立即触发停止规则。

#### P1-2. Rebuild theorem hierarchy

来源：DA，兼顾 EIC/R2 对 sharp result 的判断  
追踪：SC-2、SC-3、DA-CRITICAL  
预计：4–7 个工作日

验收标准：

1. 先给 general differentiable share path \(s(z)\) 下的 drag expression；
2. 说明哪些结果只要求 \(\rho_A>\rho_P\) 和 \(s'(z)>0\)，哪些依赖 CES logistic path；
3. below-one-half peak 仅作为 CES-specific theorem 或 corollary；
4. 明确本文 payoff 为什么不等于标准 multiplier 的简单参数重算；
5. appendix 与 verify_model.py 同步；
6. 如果无法形成独立 payoff，触发停止规则。

#### P1-3. Make \(\rho_c\) auditable

来源：R2、R3、DA  
追踪：SC-4、SC-5、SC-10  
预计：2–3 个工作日

验收标准：

1. 定义为每单位 gross channel spending 形成的 marginal local factor-and-ownership income；
2. 明列 local wages、locally owned profits、taxes、logistics、warehousing、delivery 和 local suppliers；
3. 明列 external sellers、platform fees、imported inputs 与 absentee ownership；
4. 说明 fixed \(\rho_c\) 是 short-run reduced form；
5. \(\rho_A>\rho_P\) 是 benchmark condition，不是平台交易的定义性事实；
6. 给出可观测变量的简短 empirical mapping。

#### P1-4. Tighten shocks, scope, and application

来源：EIC、R2、R3、DA  
追踪：SC-5、SC-6、SC-9、SC-11  
预计：1–2 个工作日

验收标准：

1. abstract 或 contribution paragraph 附近写清 exogenous pass-through 与 fixed short-run incidence；
2. \(R\) 只称 consumption-equivalent real income，不称 full welfare；
3. 放宽 \(\varepsilon\) 或解释 nonnegative benchmark；
4. 主文标出 central peak 使用 \(G=0\)，positive-\(G\) generalization 在 appendix；
5. 不将 \(G\) 称为 fiscal multiplier 或 policy sufficient statistic；
6. 不引入现有模型不能支持的全国统一大市场政策结论。

### 6.2 P2 — Should fix

#### P2-1. Object definitions and conclusion

来源：EIC、R3  
追踪：SC-6、SC-7、SC-8  
预计：0.5–1 个工作日

验收标准：

- \(s\) 始终是 gross expenditure share；
- \(G\) 始终是 outside-funded private retail demand；
- 结论再次区分 \(B\) injection 与 gross external spending；
- \(R\) 不超出 conditional consumption-equivalent index。

#### P2-2. Boundaries and finite-threshold feasibility

来源：R1  
追踪：SC-14、SC-17  
预计：0.5–1 个工作日

验收标准：

- \(\alpha+\beta=1\) 只用于 income fixed point 的边界说明；
- lower finite-threshold equality 的参数可行域写清，并与 appendix 一致。

### 6.3 P3 — Minor

#### P3-1. Code availability

来源：R1  
追踪：SC-15  
预计：1–2 小时

验收标准：指明 verify_model.py、固定 seed 和核验范围；不得声称 reviewer 已执行本轮以外的 runtime verification。

#### P3-2. Multiplier convexity placement

来源：R1  
追踪：SC-16  
预计：1–2 小时

验收标准：若保留为 reported result，就写进 Proposition 1；否则删除主文对其作为正式贡献的暗示。

### 6.4 Global constraints

- 主文继续满足 2,000-word constraint；
- 修订应替换宽泛 novelty/application prose，不应逐项追加；
- general derivation 的完整证明与 prior-art equation matrix 放 appendix 或内部 audit note；
- 不要求 full platform IO、endogenous ownership、relocation、tax-budget system 或 full spatial GE；
- 总投入预计 11–19 个工作日，约 3–4 个日历周；
- P1-1 或 P1-2 失败时提前停止，不继续投入后续文字修订。

## 7. Stage return recommendation

### 7.1 Options

| Option | 优点 | 缺点和风险 | Recommendation |
|---|---|---|---|
| 返回 Stage 2 做 major theoretical repositioning | 保留已验证数学；可在篇幅内修复 theorem hierarchy、benchmark comparison 和 parameter mapping；尚无 exact-overlap 证据 | 需要真实 equation audit；可能发现当前结果仍不够独立 | **推荐** |
| 放弃当前 Economics Letters 项目 | 若没有独立 theorem，可避免继续投入 | 会过早放弃一个尚未被证明重复、且数学主体被认可的项目 | 只在 P1-1/P1-2 失败时采用 |

### 7.2 Exact return point

返回 Stage 2 的：

**contribution–theorem architecture checkpoint**

该检查点位于：

- 已验证的基础代数之后；
- abstract、introduction、conclusion 最终锁定之前；
- 数据收集与完整新模型之前。

工作顺序固定为：

1. P1-1 prior-art equation audit；
2. P1-2 theorem hierarchy reconstruction；
3. P1-3 parameter interpretation；
4. P1-4 scope rewrite；
5. P2/P3 corrections；
6. 全文压缩和一致性复核；
7. fresh Stage 3。

### 7.3 Re-review gate

重新进入 Stage 3 前必须同时满足：

1. P1-1 至 P1-4 的 acceptance criteria 全部通过；
2. 主文不超过 2,000 个文本词；
3. appendix、code 与主文 theorem hierarchy 一致；
4. 使用新的五人 full panel，不继承本轮评分；
5. 同一 frozen contract 下，目标为 F0：五位 reviewer 的 D1–D3 全部 pass；
6. DA 不再提出 CRITICAL issue，D4 不得 block；
7. R1 复核 general-share/CES 推导；
8. R2 复核 prior-art positioning 与 \(\rho_c\) mapping；
9. R3 复核 reduced-form scope；
10. EIC 复核 Economics Letters salience、结构和长度。

停止规则：

- P1-1 显示 exact result 已存在；
- P1-2 无法给出区别于 standard multiplier recomputation 的独立 payoff；
- 独立贡献只能通过超出 2,000 字约束的大型 GE 才能形成。

任一停止规则成立时，不再重复 Stage 3，应终止该投稿路线或将内容并回长期大论文。

## 8. Reviewer summary

| Reviewer | D1–D5 | Individual recommendation | Confidence | Core assessment |
|---|---|---|---|---|
| EIC | pass, pass, pass, pass, pass | accept | 4/5 | 数学正确、篇幅适合 sharp note；风险在 benchmark 与 scope salience |
| R1 Methodology | pass, pass, pass, pass, pass | accept | high | 独立重现核心推导；仅有 boundary、code、convexity 等局部修正 |
| R2 Domain | warn, warn, pass, warn, pass | major revision | high on antecedents; moderate on exhaustive novelty | recurring leakage 已有 lineage；exact CES-plus-retention 组合可能仍有贡献 |
| R3 Perspective | pass, pass, pass, warn, pass | accept with non-blocking D4 warning | high | 认可 transferable reduced-form benchmark；要求区分 accounting identity 与 mechanism |
| Devil's Advocate | block, warn, warn, warn, pass | reject or major revision | 0.90 critique; 0.80 priority challenge | 当前 novelty framing 可解释为标准 multiplier 加 CES-varying coefficient；未证明 exact formula 已存在 |

## 9. Phase 2 completion status

- 五份 review records 已全部纳入；
- D1–D5 vectors 已机械复算；
- F1/F2/F3/F0 已逐项判定；
- DA-CRITICAL 已与一般 weakness 分开；
- genuine split 已裁决；
- 第二位独立 editorial synthesizer 复算出相同的 D1–D5 vectors、F1/F2/F3/F0 与终局 action，对返回 Stage 2 的结论无实质矛盾；
- P1/P2/P3 revision roadmap 已绑定来源和 acceptance criteria；
- 返回 Stage 2 的精确 checkpoint 和停止规则已定义；
- 本阶段没有修改 paper source、appendix、bibliography、verification code 或 compiled PDF；
- 本阶段没有 commit 或 push。

editorial_decision=reject_or_major_revision
