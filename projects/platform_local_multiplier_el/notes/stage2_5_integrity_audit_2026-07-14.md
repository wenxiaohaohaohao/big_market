# Stage 2.5 学术完整性与框架锁定审计

- 项目：`platform_local_multiplier_el`
- 稿件：*Platform Intermediation and Local Multipliers*
- 审计日期：2026-07-14
- 审计范围：`paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、`code/verify_model.py`、编译后的 `output/paper.pdf`
- 审计性质：投稿前完整性检查，不是期刊接受概率保证

## 1. 结论

**Stage 2.5 结论：FAIL — 返回 Stage 2 做框架锁定后复审。**

这个结论不表示模型存在数学错误。相反，当前稿件的解析推导、存在性与唯一性、主要命题、边界分析、引用元数据、交叉引用、数值核验和 PDF 排版均通过检查。阻断项集中在 **Mode 7：research framing / contribution frame lock**：

1. “留值率在每一轮地方支出中重复进入乘数”本身与传统 open-region multiplier 中的进口或跨区漏出逻辑有明显亲缘关系，不能作为未加限定的核心创新。
2. Fan et al.（2018）已经同时处理 online/offline channel choice、贸易摩擦、地方劳动需求、名义收入与价格指数。本文必须把增量严格限定为：**渠道特定的地方收入归属如何随内生渠道替代而变化，并通过地方支出递归反馈，产生名义收入与 consumption-equivalent real income 的闭式阈值，以及中间平台渗透率处的边际拖累峰值。**
3. 当前标题 *Platform Intermediation and Local Multipliers* 对平台理论的承诺超过模型内容。模型没有平台定价、佣金、匹配、网络效应、平台竞争或平台战略行为；平台只是一个低成本、低本地收入份额的零售渠道。
4. Introduction 中 “The closest spatial e-commerce benchmark” 是无法穷尽核实的全局排序式判断，应删除或改成不带排名的表述。

在这些问题修正之前，继续做语言润色或模拟审稿不会解决主要的 desk-reject 风险。

## 2. 完成标准与结果总览

| 检查项 | 完成标准 | 结果 |
|---|---|---|
| 文献真实性 | 每条文献可由 DOI 或期刊官网确认 | 5/5 通过 |
| BibTeX 准确性 | 作者、题名、期刊、年份、卷期、页码、DOI 一致 | 5/5 通过 |
| 引用完整性 | 无 dangling citation、无 orphan BibTeX key | 通过 |
| 引用语境 | 原文支持正文对文献的描述 | 4 条通过，Faber 表述需保留“motivation”限定 |
| 外部与内部 claims | 逐项登记并核实 | 15 项：13 通过，1 项带措辞限制，1 项不可核实 |
| 数学闭合 | 假设、最优化、均衡、解析解、证明、边界一致 | 通过 |
| 计算核验 | 固定种子随机检查与差分核验全部通过 | 通过 |
| 原创性网页抽样 | 至少抽查 30% 实质性段落 | 12/30 = 40%，未发现精确或近似文本匹配 |
| 自我重复发表检查 | 搜索作者公开作品中的相同文本/模型 | 有限范围内未发现；作者身份歧义限制见第 6 节 |
| LaTeX 编译 | 无未解析引用、无 overfull box、无致命错误 | 通过 |
| PDF 视觉检查 | 无裁切、重叠、乱码、异常分页 | 8/8 页通过 |
| EL 篇幅 | 主文与附录文本词数不超过 1,950；摘要不超过 100 | 1,602；摘要 90，均通过 |
| 贡献框架锁定 | 与最近文献的增量可被一句话准确复述 | **未通过** |

## 3. 阻断项

### FM7-SUSPECTED-01：递归漏出的创新性表述过宽

当前稿件的 Proposition 1 数学上成立，但其经济直觉与标准地方乘数中的反复进口/跨区漏出并非完全分离。Chodorow-Reich（2019）系统讨论 geographic cross-sectional multipliers；更早的 regional multiplier 文献也把 local propensity to spend 与 leakage 视为乘数的核心组成。

因此，论文不能把以下宽泛命题作为唯一贡献：

> retention enters every round of local expenditure.

可辩护的窄贡献应改为：

> Integration endogenously reallocates expenditure across retail channels with different local-income incidence. The induced change in retention recursively affects local demand, generating closed-form nominal- and real-income thresholds and a non-monotone marginal incidence effect over platform penetration.

这一区分必须同时进入标题、Introduction 的研究问题、贡献段和 Conclusion。

### FM7-SUSPECTED-02：相对 Fan et al.（2018）的增量没有完全锁定

Fan et al. 已经包含 online/offline choice、e-commerce entry costs、distance frictions、trade、local labor demand、nominal wage 与 price-index effects。因此，下列内容不能单独作为本文创新：

- online/offline channel choice；
- 电子商务降低价格；
- 名义收入与实际收入可能分离；
- 地区异质性。

本文可以保留的增量是 **channel-specific local-income incidence + endogenous channel substitution + recursive local expenditure feedback** 的组合，以及由此导出的解析阈值和中间渗透率峰值。正文需要直接用一至两句与 Fan et al. 做这种“已有内容—新增内容”对照。

### IL-SERIOUS-01：无法核实的相对排序 claim

`main.tex` 第 76--78 行称：

> The closest spatial e-commerce benchmark is Fan et al. (2018).

“closest” 要求穷尽相关文献，现有检索无法证明。建议改为：

> Fan et al. (2018) provide a central spatial e-commerce benchmark ...

或者直接陈述该文做了什么，不做排序。

### FM7-SUSPECTED-03：标题与模型对象不完全一致

当前标题中的 “Platform Intermediation” 容易让编辑期待平台收费、双边市场、匹配、排名、平台竞争或租金归属的内生决定。当前模型没有这些对象，只有两个 CES 零售渠道和外生的渠道本地收入份额。

推荐标题：

1. **Retail Channel Substitution and Local Multipliers**（首选）
2. **Platform Channels and Local Multipliers**（若希望保留 platform）

首选标题最准确地描述模型，也避免把文章误送入 platform IO 的审稿标准。

## 4. 非阻断但必须修正的措辞

### IL-MEDIUM-01：Faber 的作用必须保持为 motivation

Faber（2014）研究贸易成本下降与核心—外围产业重配，并不直接推出本文维护的

\[
B(z)=\bar B e^{\varepsilon z},\qquad \varepsilon\geq0.
\]

当前 “motivates a reduced-form outward market-access response” 基本可接受，但修订时应进一步明确：`B(z)` 是本文为了隔离 outward opportunity 而采用的 maintained component，不是 Faber 的经验结论，也没有继承其完整生产区位机制。

### IL-MEDIUM-02：Moretti 的定位应更精确

Moretti（2010）直接研究 tradable-sector employment 对 local nontradable employment 的乘数，而不是本文意义上的完整收入固定点。当前正文已经说明“不把 formal multiplier model 归于该文”，这是正确的。建议把 “base-sector income” 改为更贴近原文的 “tradable-sector employment and income” 或仅称 “local-demand propagation intuition”。

### IL-MEDIUM-03：平台渠道的空间归属应写成条件而非事实

Introduction 第 55--57 行称平台渠道的 “intermediation income and supplier payments accrue elsewhere”。模型实际只要求 benchmark condition `rho_A > rho_P`；它并未证明全部平台中介收入或供应商支付都流向外部。

建议改成条件句：

> ... toward a platform channel that may use fewer locally owned intermediation and supply services.

### IL-MINOR-01：计算核验脚本的覆盖范围可以更精确

`verify_model.py` 已通过主要公式的随机抽样和中心差分核验。非阻断的覆盖遗漏包括：

- 未单独检查收入映射迭代的收敛残差；
- 未从原始外层一阶条件独立重构 Cobb--Douglas demand；
- 部分简单边界结论没有逐项 assertion；
- 输出文字 “all boundary cases” 略宽于脚本实际枚举范围。

这些不会影响现有解析证明的有效性，但正式归档前宜收紧脚本描述并补充两个独立检查。

## 5. 引用与参考文献审计

### 5.1 BibTeX 元数据

| Key | 核验结果 | 权威来源 |
|---|---|---|
| `atkin2018retail` | 作者、题名、JPE 126(1):1--73、2018、DOI 全部一致 | https://doi.org/10.1086/695476 |
| `couture2021connecting` | 作者、题名、AER: Insights 3(1):35--50、2021、DOI 全部一致 | https://pubs.aeaweb.org/doi/10.1257/aeri.20190382 |
| `faber2014trade` | 作者、题名、ReStud 81(3):1046--1070、2014、DOI 全部一致 | https://academic.oup.com/restud/article/81/3/1046/1605154 |
| `fan2018alibaba` | 作者、题名、JIE 114:203--220、2018、DOI 全部一致 | https://www.sciencedirect.com/science/article/abs/pii/S0022199618301594 |
| `moretti2010local` | 作者、题名、AER 100(2):373--377、2010、DOI 全部一致 | https://pubs.aeaweb.org/doi/10.1257/aer.100.2.373 |

结果：5 个 BibTeX entries、5 个唯一 citation keys；无重复、无缺失、无正文未定义引用，也无文献库中未使用条目。

### 5.2 引用语境

- **Couture et al.**：随机扩展电商接入、生产者和劳动者收入增益有限、部分家庭通过生活成本下降获益，正文表述得到支持。
- **Atkin et al.**：多层 CES、cost-of-living 与 nominal-income decomposition、零售劳动收入和国内商店利润，正文表述得到支持。
- **Faber**：可支持贸易成本下降、市场接入及核心—外围空间重配的背景；不能作为 `B'(z) >= 0` 的直接经验依据。
- **Moretti**：可支持 tradable-sector shock 经由 local nontradable demand 传播的直觉；不能归因一个与本文相同的解析固定点。
- **Fan et al.**：可支持 online/offline choice、entry costs、distance frictions、trade 和 spatial consumption inequality；“closest” 排名不可核实。

## 6. Claim registry

| ID | 稿件 claim | 类型 | 结论 | 依据/处理 |
|---|---|---|---|---|
| C01 | Couture et al. 使用 randomized e-commerce expansion | 外部事实 | VERIFIED | AEA 期刊页与摘要 |
| C02 | Couture et al. 对 local producers/workers 的收入增益证据有限 | 外部事实 | VERIFIED | AEA 期刊页与摘要 |
| C03 | 部分家庭收益来自 lower living costs | 外部事实 | VERIFIED | AEA 期刊页与摘要 |
| C04 | Atkin et al. 使用 multilayer CES retail framework | 文献方法 | VERIFIED | JPE/NBER 正文 |
| C05 | Atkin et al. 分解 cost of living 与 nominal income，并含 retail labor/profits | 文献结果 | VERIFIED | JPE/NBER 正文 |
| C06 | Faber motivates outward market access response | 文献定位 | VERIFIED WITH LIMIT | 只能称 motivation；`B'(z)>=0` 是本文维护假设 |
| C07 | Moretti 提供 tradable shock 经 local nontradable demand 传播的直觉 | 文献定位 | VERIFIED | AER 正文 |
| C08 | Fan et al. 是 “closest” spatial e-commerce benchmark | 相对排名 | UNVERIFIABLE | 删除 “closest” |
| C09 | Fan et al. 包含 entry costs、distance frictions、trade、spatial consumption inequality | 文献方法 | VERIFIED | JIE 摘要/正文预览 |
| C10 | 有限 `z` 下 `0<s(z)<1` | 模型内部 | VERIFIED | Lemma 1 解析证明 |
| C11 | 收入固定点存在、唯一、正且全局稳定 | 模型内部 | VERIFIED | contraction proof |
| C12 | recursive-retention multiplier 公式及与 `m0*omega` 的比较 | 模型内部 | VERIFIED | Proposition 1 证明与脚本 |
| C13 | 三个有限冲击区域互斥且完备，不存在 nominal gain/real loss 第四区 | 模型内部 | VERIFIED | Proposition 2 证明 |
| C14 | 边际渠道替代拖累在唯一 `s^dagger<1/2` 处达到峰值 | 模型内部 | VERIFIED | Corollary 1 证明与脚本 |
| C15 | No data were used | 研究声明 | VERIFIED | 纯解析模型；代码只核验恒等式，不生成实证结果 |

说明：C01--C09 是外部可核实 claims；C10--C14 是由论文自身假设与证明支持的内部 claims。后者不能用数值脚本代替证明，当前稿件已提供正式证明。

## 7. 原创性与自我重复检查

### 7.1 网页文本抽样

以 20 个或以上英文词的连续 LaTeX prose block 为计数单位，主文识别 20 段、附录识别 10 段，共 30 段。抽查 12 段，占 40%。检索的代表性短语覆盖 Abstract、Introduction、Model、Results、Conclusion 和 Appendix，包括：

1. “Digital platforms can make a small region better connected”
2. “Evidence from rural China makes this distinction relevant”
3. “channel-specific income incidence and its recurrence”
4. “effective local multiplier is more sensitive to retention”
5. “retention enters every round of local expenditure”
6. “The series shows why” 与其后完整句片段
7. “This is the peak of the marginal drag”
8. “Platform-mediated integration changes both consumer access”
9. “The contraction theorem gives a unique fixed point and global convergence”
10. “Every denominator is positive, proving the inequality and both equality cases”
11. “The numerator is strictly decreasing” 与完整符号判断句
12. “At equal prices the perfect-substitutes problem has multiple cost-minimizing allocations”

结果：未发现与现有网页或论文的精确或具有实质意义的近似文本匹配。搜索结果中的相似词组均来自无关主题。

限制：这是公开网页的启发式检查，不等同于 iThenticate、Turnitin 或出版社 Crossref Similarity Check。投稿前仍建议对最终英文版本运行专业相似度检测。

### 7.2 自我重复发表

对可识别作者姓名和项目标题进行了公开网页检索，未发现已发表或公开流通的同文稿版本。Wenxiao Dong 的公开学术主页可识别；“Yaqi Hu” 存在同名与身份歧义，无法仅凭公开搜索穷尽核实其全部工作论文。因此结论是“有限范围内未发现”，而不是“确认不存在”。

## 8. 数学与机制审计

### 8.1 通过项

1. **家庭外层问题**：`alpha,beta>0` 且 `alpha+beta<1` 保证 Cobb--Douglas 各项正支出；间接效用常数 `K` 推导正确。
2. **渠道内层问题**：`a in (0,1)`、正价格、有限 `z`、`eta>1` 下 CES 支出最小化有唯一内部解；`s -> 0/1` 被正确处理为极限而非有限参数 corner。
3. **导数**：`d ln P_M/dz=-s`、`ds/dz=(eta-1)s(1-s)`、`omega'=-Delta rho(eta-1)s(1-s)` 一致。
4. **收入闭合**：`beta+alpha*omega <= alpha+beta < 1`，收入映射是 contraction；存在性、唯一性、正性和全局递推稳定性成立。
5. **Proposition 1**：乘数、几何级数解释、与 first-round adjustment 的严格比较、等号条件和 retention elasticity 正确。
6. **Proposition 2**：有限冲击比率的三个区域互斥且完备；两个等号边界处理正确；nominal income 上升而 real income 下降被正确排除。
7. **Corollary 1**：`Lambda(s)` 的唯一内部峰值推导正确，且 `s^dagger<1/2`；正文正确区分 marginal drag 与 cumulative leakage。
8. **边界分析**：`rho_A=rho_P`、`rho_A<rho_P`、`omega=0/1`、`alpha/beta` 极限、`eta->1/infinity`、`G>0` 的一般导数均与主模型一致。

### 8.2 经济机制边界

当前模型识别的是 **spatial income incidence of retail-channel substitution**，不是完整的平台组织模型。`rho_A` 与 `rho_P` 是外生收入归属参数，模型没有解释它们如何由平台合同、佣金、供应链、所有权或税制内生决定。

因此，可以发表的理论故事应是：

> 当整合既提高 outward base income、降低平台价格，又内生地把支出转向本地收入含量较低的渠道时，哪一组闭式条件决定 nominal income 与 consumption-equivalent real income 的方向？

不应写成：

> 平台一般会抽走地方价值，本文建立了平台经济的一般理论。

后者超出模型能够证明的范围。

## 9. AI research failure modes

| Mode | 判断 | 说明 |
|---|---|---|
| 1. Code-generated result without analytical support | CLEAR | 所有主要结果有解析证明；脚本仅做辅助核验 |
| 2. Fabricated or mismatched references | CLEAR | 5/5 文献由 DOI/期刊页确认 |
| 3. Fabricated statistics or empirical results | CLEAR | 无数据、无统计量、无经验结果 |
| 4. Shortcut/invalid experimental design | N/A | 纯理论稿，无实验或 ML pipeline |
| 5. Unexplained surprising output | CLEAR | 比较静态由证明导出，不依赖一次运行 |
| 6. Misrepresentation of methods or data | CLEAR | Data availability 与实际研究设计一致 |
| 7. Research framing not locked | **SUSPECTED — BLOCKING** | 标题、标准 leakage 文献边界及相对 Fan 的增量尚未锁定 |

本项目不是由 Academic Research Suite 从 Stage 1 创建的，因此没有 ARS experiment passport。这里没有需要 passport 对照的实验；`verify_model.py` 被视为 deterministic algebra check，而不是研究实验。

## 10. 计算、篇幅与排版验证

- `python code/verify_model.py`
  - 结果：`PASS: 2000 deterministic random draws and all boundary cases (seed=20260714).`
- `code/build_paper.ps1 -KeepAux`
  - 结果：成功生成 8 页 `output/paper.pdf`。
- final LaTeX log：
  - 无 undefined citation；
  - 无 undefined reference；
  - 无 overfull/underfull box；
  - 无 LaTeX fatal error。
- `texcount -inc -sum`：
  - 主文 1,101；
  - 附录 501；
  - 合计 1,602；
  - Abstract 90 词。
- PDF 逐页渲染检查：8/8 页无公式裁切、文字重叠、乱码、黑块或不可接受的断页。
- MiKTeX 的 log4cxx C 盘日志权限及更新提示是非致命环境警告；不影响编译产物和 LaTeX log 完整性。

## 11. 返回 Stage 2 的推荐修订顺序

在进入多角色正式审稿前，只做以下五项框架修订：

1. 将标题改为 **Retail Channel Substitution and Local Multipliers**。
2. 把研究问题改成“什么时候 outward access 与价格收益不足以抵消递归 retention loss，以及为什么边际拖累在中间渗透率达到峰值”。
3. 在 Introduction 中明确承认 standard regional multiplier 已经包含反复 leakage；把新意限定为 **endogenous channel composition changes the leakage rate**。
4. 加入并准确定位：
   - Goldmanis et al.（2010）：e-commerce、search costs 与零售市场结构重配；
   - Chodorow-Reich（2019）：geographic cross-sectional multipliers 的标准参照；
   - Brown, Fitzgerald, and Weber（2019，可选）：local ownership、income capture 与 local multiplier 的经验相关性。
5. 删除 “closest”，收紧 Faber、Moretti 和平台收入外流的措辞。

完成后重新执行 Stage 2.5。只有 Mode 7 从 SUSPECTED 变为 CLEAR，才进入 Stage 3 的多角色审稿、针对性重写和投稿包检查。

## 12. 本轮文件处置

- 未修改 `main.tex`、`appendix.tex`、`references.bib` 或核验脚本。
- 未 commit、未 push。
- 新增文件只有本审计报告。
