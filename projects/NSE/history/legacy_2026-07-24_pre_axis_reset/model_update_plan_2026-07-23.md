# `main.tex` 模型严谨化更新计划

日期：2026-07-23  
状态：PLAN ONLY  
目标文件：`projects/NSE/paper/main.tex`  
本计划不修改主稿；作者确认后才进入模型重写。

## 一、结论

当前 `main.tex` 已经正确表达了论文的研究问题、与 EL 的边界、三类目标结果和
NEG 的排除范围，但仍然只是一个 research scaffold，不是可以推导命题的经济模型。
问题不是简单增加公式就能解决，而是以下对象尚未闭合：

1. 地区禀赋如何决定要素价格和行业单位成本；
2. 全国需求如何转化为企业的渠道收入；
3. 企业进入、行业选择和渠道选择的先后顺序；
4. `q_i` 究竟是地区公共能力、企业能力还是政府投入；
5. 本地生产收入与平台、代理、税收之间的支付流；
6. consumer access、producer access、local income 和 national welfare 的关系；
7. facilitating policy 所矫正的唯一市场失灵；
8. 三个目标命题的存在性、唯一性和符号条件。

因此，更新不采用“在现有段落中补公式”的办法，而是保留研究问题和理论边界，
整体重写 Sections 2--6，并同步建立 appendix 中的证明。

## 二、从 notes 继承的硬约束

以下判断来自 `notes/README.md`、`NSE_project_memo_zh.md`、
`新建 文本文档.txt`、`model_contract.md` 和 `proposition_ledger.md`，
在本轮模型中必须保持一致：

- NSE 稿是独立生产侧模型，不是 `EL + endogenous rho_i`。
- 比较优势必须从禀赋、要素价格、行业要素密集度和相对单位成本推出，
  不能用外生 congruence scalar 代替。
- consumer-side access 与 producer-side access 必须分开。
- `rho_i` 是均衡会计结果，不是原始参数。
- local value capture 不是 national welfare 的充分统计量。
- EL 地方乘数只能作为 reduced-form corollary，不能进入主模型资源约束。
- facilitating state 必须对应明确市场失灵，并包含财政成本。
- 第一版不加入迁移、内生市场规模、集聚外部性、完整 NEG 或动态组织资本。
- numerical illustrations 只能称为 illustrative/normalized，不能称为 calibration。

## 三、基准模型范围选择

### 3.1 空间结构

| 选项 | 优点 | 缺点 | 决定 |
|---|---|---|---|
| 完整多地区、多行业空间 GE | 空间结构最完整 | 与企业异质性、渠道和政策同时出现时难以解析求解 | 第一版不用 |
| 单个 focal region 嵌入全国市场 | 保留地区禀赋、全国需求和跨地收入归属；可以解析求解 | 不解释全国地区体系的一般均衡反馈 | **推荐基准** |
| 纯企业 partial equilibrium | 最简单 | 禀赋和 NSE 主轴过弱 | 不推荐 |

基准模型采用“单个 focal region `i` 嵌入全国市场”。全国市场价格指数和行业需求
规模作为地区所面对的外部市场条件；地区内部的要素禀赋、行业成本、企业进入、
渠道和收入归属内生决定。其他地区只作为市场与支付归属的外部环境，不求解完整
空间 GE。

### 3.2 组织能力 `q_i`

第一版将 `q_i` 定义为地区层面的、企业共同面对的 platform-compatible
organizational environment，例如数字运营、履约、质量控制、售后和供应链服务
的可获得性。它降低直接平台渠道的固定组织成本或履约损耗。

- 基准模型：`q_i` 外生给定，用于比较静态和阈值命题；
- 政策扩展：政府公共投入 `G_i` 改善有效能力 `q_i^e=q_i+g(G_i)`；
- 第一版不让企业动态积累 `q_i`；
- 动态稿再引入 `q_{i,t}` 和旧代理资本 `a_{i,t}`。

这样可以避免当前 notes 中 `q_i` 同时代表企业投资、地区禀赋和公共投入的冲突。

### 3.3 政策模块的市场失灵

政策扩展只选择一种市场失灵：共享数字/物流/质量认证基础设施具有不可分性或
非排他性，单个企业不能获得全部投资收益，因此私人提供不足。

不在第一版同时加入 first-mover information externality、融资约束、learning
spillover 和平台议价外部性。其他市场失灵进入 Discussion。

## 四、正式模型的七个组成模块

### Module 1：禀赋、技术与比较优势

1. 地区禀赋为 `E_i=(K_i,L_i)`；自然资源只在需要特定行业时作为扩展。
2. 行业 `j` 的资本密集度为 `alpha_j`。
3. 企业生产率为 `z`，生产函数采用 CRS Cobb--Douglas 或 CES：

   `y_ij(z)=z k^{alpha_j} l^{1-alpha_j}`。

4. 成本最小化给出：

   `c_ij(z)=B_j r_i^{alpha_j} w_i^{1-alpha_j}/z`。

5. 潜在比较优势由行业价格相对于单位成本的盈利空间定义，而不是研究者外生指定
   `C_i`。如需汇总指标，只在 numerical section 定义。

**验收门槛**：给定禀赋与行业密集度后，必须能够明确比较两个行业的相对成本和
viability；所有要素价格处理必须说明是内生均衡价格还是条件于地区禀赋的基准价格。

### Module 2：全国需求与两类 market access

1. 全国行业需求使用 CES，替代弹性为 `sigma>1`。
2. producer-side access 由外销市场规模 `M_j` 和 outbound trade/access cost
   `tau_i^out` 决定。
3. consumer-side access 由本地居民面对的价格指数和 inbound cost
   `tau_i^in` 决定。
4. 统一市场冲击可以共同降低两者，但模型中必须保留两个符号，避免把消费福利改善
   与本地生产扩张视为同一结果。

**验收门槛**：能够出现 `consumer welfare 上升、local production income 下降`
的参数区域；否则论文的 access--capture puzzle 没有被模型化。

### Module 3：企业进入与渠道选择

企业进入行业后，在两种全国市场渠道中选择：

- `A`：通过本地代理间接销售。固定成本较低、边际中介楔子较高，本地代理服务的
  value added 留在地区；
- `D`：平台直连全国市场。边际接入成本较低，但需要较高固定组织成本、支付平台
  commission，且平台收入归属于地区外。

利润不能继续使用未定义的 `R-VC-F`，而应由 CES demand、单位成本、渠道楔子、
commission 和固定成本推导：

`pi_ij^r(z)=revenue_ij^r(z)-variable_cost_ij^r(z)-fixed_cost_ij^r`。

需要依次推导：

1. 不进入、代理渠道、平台直连的利润；
2. 各渠道零利润 cutoff；
3. 渠道间 indifference cutoff；
4. productivity sorting；
5. 比较优势、平台接入成本和 `q_i` 对 cutoff 的影响。

**验收门槛**：所有 cutoffs 有存在性、唯一性和排序条件；不存在只凭图示宣布的
渠道排序。

### Module 4：均衡定义

正式列出：

1. 家庭优化；
2. 企业成本最小化和渠道选择；
3. 行业进入或企业质量分布；
4. 地区要素市场 clearing；
5. 产品销售与全国需求一致；
6. 平台、代理和政府预算；
7. equilibrium definition；
8. 参数限制和边界情况。

若完整自由进入使预期利润为零，必须说明 local owner profit 是否仍是收入构成；
不能一边使用自由进入零利润，一边把正利润作为主要留值来源。

### Module 5：本地收入和 value capture 会计

不再直接相加

`W_i + Pi_i^local + S_i^local + T_i^local`

而不说明这些项目是否重叠。改为从支付流建立 mutually exclusive accounting：

1. 本地生产 value added；
2. 本地代理/履约服务 value added；
3. 本地所有者获得的净经营盈余；
4. 地区外平台 commission 和外地中间投入形成的 leakage；
5. 地方财政净收入，扣除政策真实资源成本。

定义：

`rho_i = local value added associated with covered transactions /
gross value of the same covered transactions`。

正文同时报告：

- local production income；
- local disposable income；
- consumer welfare；
- national welfare。

平台位于地区外、但位于国内时，platform profit 是 local leakage，却不是 national
resource loss。这一所有权假设必须明确。

**验收门槛**：逐项支付流加总回 gross transaction value；税收和服务收入不得
重复计入。

### Module 6：核心命题

命题按逻辑顺序调整为：

#### Proposition 1：Comparative advantage and platform entry

平台接入成本下降降低平台渠道 cutoff；在满足生产率分布和需求条件时，
低单位成本、符合比较优势的行业具有更强的企业进入或销售响应。

不能预先假定符号。需要证明“更强响应”是 cutoff 的绝对变化、进入企业质量变化，
还是销售额弹性更高，并选择一个严格定义。

#### Proposition 2：Organizational-capability threshold

定义平台化相对于代理渠道的本地收入差：

`Delta V_i(q_i; A_ij,tau,phi,...)`。

若：

- `Delta V_i` 对 `q_i` 严格递增；
- 低能力边界为负、高能力边界为正；

则存在唯一 `q_i^*`。进一步通过 increasing differences 证明：

`partial q_i^* / partial A_ij < 0`，

其中 `A_ij` 必须是由价格和成本推出的 comparative-advantage strength。

这是全文的核心命题，应先于政策模块完成。

#### Corollary 1：Access--capture separation

在 `q_i<q_i^*` 的参数区域，统一市场仍可通过进口价格指数改善消费者福利，
但本地生产收入下降。

#### Proposition 3：Facilitation versus protection

在共享基础设施供给不足的市场失灵下，对具有潜在比较优势的行业，比较：

- `G_i`：降低直接平台进入的共同固定成本；
- `s_i`：保护或补贴本地销售。

两种政策必须具有政府预算约束和可比财政成本。结论只能是：

`W_i^facilitation > W_i^protection`

在一组明确参数条件下成立，不写成 NSE 的无条件政策判断。

#### Corollary 2：EL local recirculation

只在 appendix 中将第一轮本地收入映射为

`Y_i=I_i/(1-lambda_i)`。

需要说明这是 reduced-form amplification，不参与主模型 welfare 和资源约束。

### Module 7：Numerical illustrations

只有解析命题完成后才编写数值代码。至少生成：

1. `comparative-advantage strength × q_i` 二维相图；
2. consumer welfare 与 local income 符号区域；
3. `q_i^*` 对 `tau^out`、commission、固定成本的敏感性；
4. 等财政成本下 facilitation 与 protection 的福利边界；
5. 每张图对应 source-data CSV。

参数表分为：

- normalized parameters；
- literature-informed parameters；
- sensitivity ranges。

没有数据依据的参数不得标为 calibrated。

## 五、`main.tex` 逐节更新表

| 当前部分 | 当前问题 | 更新方式 | 主要 notes 来源 |
|---|---|---|---|
| Abstract | 使用 planned/should/remain to be completed；没有已证明结果 | 最后重写；在命题完成前只保留内部 draft abstract | project memo；proposition ledger |
| Introduction | 只有两段；没有文献缺口、贡献和与 EL 的严格边界 | 扩展为 puzzle、NSE mechanism、literature gap、contributions、roadmap | README；两个 project memo；原始重估笔记 |
| Environment | 主体、需求、生产、时序和均衡均未定义 | 重写为 Modules 1--4 | model contract；inventory Sections 1--4 |
| Endowments and Viability | 只有概念性一段 | 写出成本最小化、相对成本、viability definition 和 P1 | 原始重估笔记第1、5项；inventory Sections 1--3 |
| Firm Entry and Capability | `R-VC-F` 是黑箱；`q_i` 身份不明 | 写出 CES revenue、渠道成本、cutoffs、sorting 和 P2 | memo；原始重估笔记第2、6项；inventory Section 4 |
| Local Value Capture and Welfare | 没有支付流与资源约束 | 使用 Module 5 重写，增加 access--capture corollary | 原始重估笔记第3、4项；inventory Section 5 |
| Facilitation versus Protection | 同时列出多种市场失灵；无政府预算 | 只保留共享基础设施外部性，形成 P3 | 原始重估笔记第7项；inventory Section 6 |
| Numerical Illustrations | 只有图形愿望清单 | 命题完成后建立代码、参数表和 source data | memo；future empirical strategy |
| Empirical Implications / NEG | 边界正确，但预测尚未由命题推出 | 将每项预测链接到 P1--P3；NEG 只作为限制 | data strategy；原始重估笔记第8项 |
| Conclusion | 仍为未来时 | 最后改为已完成结果、适用边界和后续研究 | 全部已验证命题 |
| Appendix | 只有占位文字 | 放 equilibrium details、proofs、accounting、EL corollary、robustness | proposition ledger |

## 六、文献与模型部件映射

候选文献来自 `NSE_literature_variable_inventory.md`；进入正式 BibTeX 前必须逐条
核实 metadata 和实际论断。

| 模型/写作部件 | 第一组候选来源 | 用途 |
|---|---|---|
| NSE 总纲、比较优势、自生能力 | Lin (2003, 2011, 2012) | 概念定义和 NSE 理论主轴 |
| 正式 NSE 结构模型 | Ju, Lin and Wang (2015)；Lin, Liu and Zhang (2023) | 禀赋、行业密集度、技术和结构升级 |
| 比较优势与异质企业 | Bernard, Redding and Schott (2007)；Melitz (2003) | 行业比较优势与企业 cutoff |
| 中介和直接/间接销售 | Ahn, Khandelwal and Wei (2011)；Bernard et al. (2010) | 代理渠道与直连渠道的成本排序 |
| 平台费用和双边市场 | Rochet and Tirole (2003)；Armstrong (2006) | commission 和平台机制边界 |
| value capture 和收入归属 | Gereffi et al. (2005)；Antras and Chor (2013)；Dedrick et al. (2010) | 支付归属与 local capture 概念 |
| 地方收入传播 | Moretti (2010)；Bartik (1991) | appendix 中的地方再循环边界 |
| facilitating state 与市场失灵 | Lin and Monga (2011)；Rodrik (2004)；Rodriguez-Clare (2005)；Pack and Saggi (2006) | 政策工具与市场失灵 |
| 组织资本 | Prescott and Visscher (1980)；Atkeson and Kehoe (2005) | 只用于未来动态扩展 |

平台与中介文献只提供可改造的机制，不得声称 Ahn--Khandelwal--Wei 已直接定义
本文的“本地代理 A / 平台直连 D”。

## 七、执行阶段与验收门槛

### Phase 0：冻结模型合约

产物：

- 更新后的 notation table；
- 主体、时序、所有权和空间范围；
- 明确 `q_i`、`G_i`、`tau^in`、`tau^out` 的经济身份。

门槛：同一符号只有一个含义；所有外生、内生和政策变量分类完成。

### Phase 1：重写 baseline environment

产物：

- 家庭需求；
- 生产技术和单位成本；
- 两渠道收入与成本；
- equilibrium definition。

门槛：模型能够独立求解，不依赖 EL 方程。

### Phase 2：求解 cutoffs 和渠道排序

产物：

- 零利润和 indifference cutoffs；
- productivity sorting；
- P1 的严格陈述和证明。

门槛：解析推导与数值抽查一致；所有 corner cases 已分类。

### Phase 3：本地收入会计和核心阈值

产物：

- payment-flow table；
- `rho_i`；
- `Delta V_i(q_i)`；
- P2 与 access--capture corollary。

门槛：会计恒等式闭合；`q_i^*` 的存在性、唯一性和比较静态均有证明。

### Phase 4：政策扩展

产物：

- 共享基础设施外部性；
- 政府预算；
- facilitation 和 protection 的等成本比较；
- P3。

门槛：若不能得到非预设的条件性政策结果，将政策模块降为 Discussion，
不强行保留 P3。

### Phase 5：数值核验

产物：

- 参数配置；
- 单元测试和边界测试；
- 四组主图与 source-data CSV。

门槛：数值结果不能与解析命题冲突；失败的参数区域必须报告。

### Phase 6：论文写作与文献整合

产物：

- 完整 Introduction 和 Literature Positioning；
- 已证明结果写入正文；
- proofs 移入 appendix；
- 完整 Conclusion、limitations 和 empirical implications；
- 经核实的 `references.bib`。

门槛：正文不再出现 planned、target result、remain to be completed 等内部措辞。

### Phase 7：最终验证

必须通过：

- 主文、appendix 和代码使用同一符号与参数定义；
- 每个 Proposition 在 appendix 有对应证明；
- 每个数值图有 source-data；
- bibliography 与正文引用双向一致；
- MiKTeX 两遍编译无 error、undefined reference 和 overfull box；
- PDF 逐页检查；
- 未把 illustrative exercise 写成 calibration 或 empirical result；
- 未引入 NEG、动态资本或 EL 固定点造成范围扩张。

## 八、停止条件

出现以下任一情况时，不继续向后写作：

1. 要素价格、行业成本和比较优势之间无法闭合；
2. 渠道 cutoff 不存在、排序不唯一或依赖未说明的参数限制；
3. `Delta V_i(q_i)` 对 `q_i` 不单调，无法得到唯一阈值；
4. 本地收入支付流不能避免重复计算；
5. facilitation 优于 protection 只是由假设直接写入，而不是模型结果；
6. P1 与 P2 实际上重复表达同一 cutoff；
7. numerical illustration 与解析结果冲突。

遇到这些问题时，先简化模型或降低命题强度，不通过增加新机制掩盖问题。

## 九、建议的实施顺序

1. 确认本计划中的四项基准选择：focal-region small-open structure、
   `q_i` 的地区共同能力解释、双渠道全国销售、共享基础设施外部性。
2. 更新 `model_contract.md` 和 notation table。
3. 重写 `main.tex` 的 Environment 至 Firm Entry 部分。
4. 先完成 P1 和 P2；在 P2 通过前不写政策模块。
5. 完成 payment-flow accounting 和福利定义。
6. 决定 P3 是正式命题还是 Discussion。
7. 编写数值核验和图形。
8. 最后重写 Abstract、Introduction 和 Conclusion。

