# Stage 2.5 修改后学术完整性复审

- 项目：platform_local_multiplier_el
- 当前题目：*Retail Channel Substitution and Local Multipliers*
- 复审日期：2026-07-14
- 复审范围：paper/main.tex、paper/appendix.tex、paper/references.bib、
  code/verify_model.py、output/paper.pdf
- 性质：Stage 2 框架重写后的强制完整性检查，不是期刊接受概率保证

## 1. 最终结论

**Stage 2.5：PASS。Mode 7（research framing）已从阻断状态改为 CLEAR。**

上一轮阻断项已全部修正：

1. 标题不再承诺模型没有处理的平台定价、双边市场或战略中介，而是准确
   对应两种零售渠道之间的替代。
2. 论文明确承认 channel choice、price--income divergence、geographic
   multiplier 和 recurring leakage 均已有文献基础。
3. 可辩护的增量已限定为：整合引致的渠道替代内生改变地方收入留值率，
   该留值率进入后续本地需求反馈，从而产生名义收入与
   consumption-equivalent real income 的闭式有限冲击阈值，以及在
   \(G=0\) 的 CES benchmark 中边际留值拖累的唯一内部峰值。
4. 相对 Fan et al.（2018）和 Li（2025）的边界已直接写入
   Introduction；论文不再把 online/offline choice 或价格收益与地区
   收入损失的并存本身称为创新。
5. Faber 只用于说明空间整合冲击；\(B'(z)\geq0\) 被明确标为本文维护的
   reduced-form component，不再归因于其生产区位模型。

三名独立复审者分别从 EL 编辑定位、引文与故事一致性、解析模型与固定点
核算三个角度完成最终只读复审，结论均为 PASS，无剩余阻断项。

## 2. 完成标准与复审结果

| 检查项 | 标准 | 结果 |
|---|---|---|
| 题目与模型对象 | 不承诺平台定价、网络效应或空间 GE | PASS |
| 贡献边界 | 相对最近文献可用一句窄而准确的话复述 | PASS |
| 引文真实性与语境 | 元数据可核实，正文表述受原文支持 | 9/9 PASS |
| 引用完整性 | 无 missing citation、无 orphan BibTeX key | PASS |
| 数学闭合 | 假设、优化、均衡、解析解、证明与边界一致 | PASS |
| 计算核验 | 随机抽样、差分、固定点与边界检查通过 | PASS |
| 原创性网页抽样 | 至少复查 30% 实质性 prose blocks | 16/30，未发现匹配 |
| EL 篇幅 | texcount -inc -sum 合计不超过 1,950 | 1,884，PASS |
| Abstract | 不超过 100 词 | 90，PASS |
| LaTeX | 无未解析引用、reference、overfull 或 fatal error | PASS |
| PDF | 逐页无裁切、重叠、乱码或异常公式分页 | 9/9 PASS |

## 3. 本轮 Stage 2 框架修改

### 3.1 标题、摘要和研究问题

标题改为 *Retail Channel Substitution and Local Multipliers*。摘要不再把
“区分两种乘数”包装为主要创新，而是直接陈述：

- 相对平台渠道价格下降引起渠道份额变化；
- 当平台渠道留值较低时，渠道选择内生提高后续支出面对的漏出率；
- 论文给出 nominal income 与 consumption-equivalent real income 的
  闭式阈值；
- 内部峰值结论严格限定在没有 autonomous external retail spending
  的 \(G=0\) benchmark。

### 3.2 文献定位

Introduction 现在区分四组已有结果：

1. Couture et al.（2021）、Goldmanis et al.（2010）和 Brown et al.
   （2019）分别说明电商接入、零售份额重配和本地所有权/收入捕获的重要性；
2. Atkin et al.（2018）提供 price-index 与 nominal-income 分解的动机；
3. Fan et al.（2018）与 Li（2025）已经处理线上/线下渠道、空间贸易、
   价格、地区收入或就业重配；
4. Moretti（2010）和 Chodorow-Reich（2019）说明地方需求传播和反复
   leakage 不是本文首创。

因此，正文只声称“单独解析刻画 retention-feedback mechanism”，不再
声称发现 channel choice、price--income divergence 或 recurring
leakage。Li（2025）来自作者网站，文献库中准确标为
“Unpublished manuscript”，不误写为正式 IMF Working Paper。

### 3.3 机制与乘数对象

模型现在严格区分：

\[
m_B(\omega)=\frac{\partial Y}{\partial B}
=\frac{1}{1-\beta-\alpha\omega}
\]

与

\[
\mathcal M_G(\omega)=\frac{\partial Y}{\partial G}
=\frac{\omega}{1-\beta-\alpha\omega}
=\omega m_B(\omega).
\]

前者传播一美元已经形成的本地收入；后者先对一美元外部零售支出应用
第一轮地方收入归属 \(\omega\)，再传播所得本地收入。正文与附录均说明
\(\partial Y/\partial B\) 是在固定 \(z,\omega,G\) 时对 realized
autonomous-income injection 的偏导，等价于改变 level shifter
\(\bar B\)，而不是沿 \(z\) 的总导数。

收入闭合也已明确：

- \(B\) 是模型化零售与非贸易部门之外形成的自主本地增加值，且不包含
  \(G\) 产生的收入；
- \(G\) 是由地区外部融资的名义零售支出；
- 非贸易品 \(N\) 与已计入 \(\rho_c\) 的渠道服务相互区分；
- 每轮支出购买新生产的产出，其中本地部分按 \(\rho_c\) 形成新的要素
  与所有者收入；未留存部分流向外部经济。

### 3.4 结果范围

Proposition 2 和 Corollary 1 的主要阈值均明确限定 \(G=0\)。摘要、
Introduction 与 Conclusion 同步使用这一范围，不再把
\(s^\dagger<1/2\) 无条件推广到 \(G>0\)。

对内部峰值的解释也已补足：若没有传播分母，CES substitution term
\(s(1-s)\) 在 \(1/2\) 达峰；随着平台份额上升、留值率下降，
\(D(s)\) 上升并削弱地方需求反馈，因而比率在 \(1/2\) 之前达到峰值。
正文同时强调累计漏出 \(\Delta\rho s\) 仍单调上升，避免把边际峰值误写
为累计漏出的峰值。

## 4. 引文与最近文献边界

九个 citation keys 与九个 BibTeX entries 一一对应，无缺失或未使用条目。
逐项语境复查结果：

- Couture et al.（2021）：随机电商扩张、当地生产者/工人收入增益有限、
  部分家庭通过生活成本下降获益，PASS；
- Goldmanis et al.（2010）：搜索成本下降与零售市场份额重配，PASS；
- Brown et al.（2019）：本地与外部所有权影响地区收入捕获及传播，PASS；
- Atkin et al.（2018）：价格指数与名义收入分解，PASS；
- Fan et al.（2018）：线上/线下贸易与地区实际收入，PASS；
- Li（2025）：Amazon logistics、价格收益、部分地区收入损失与就业重配，
  PASS；
- Moretti（2010）与 Chodorow-Reich（2019）：地方需求传播、开放地区
  leakage 与 multiplier，PASS；
- Faber（2014）：只作为贸易摩擦下降这一空间冲击的动机，PASS。

定向最近文献检索没有发现与“内生渠道份额 + 渠道特定本地收入份额 +
递归本地需求 + 本文闭式阈值”完全相同的模型。这个结论只表示本轮定向
检索未发现 exact match，不构成穷尽性全球首创声明。Li（2025）是必须
持续跟踪的最新相邻工作；投稿前应再次核查其版本变化。

## 5. 数学与计算复审

独立解析复审确认：

1. 有限 \(z\)、正价格、\(a\in(0,1)\)、\(\eta>1\) 下
   \(0<s(z)<1\)；
2. 收入映射的 contraction、存在性、唯一性、正性与全局递推稳定性成立；
3. \(m_B\) 与 \(\mathcal M_G\) 的公式、解释和证明一致；
4. 沿 \(z\) 的总导数正确包含 \(B'(z)=\varepsilon B(z)\)；
5. Proposition 2 的三个区域互斥且完备，两个等号边界正确；
6. 不存在 nominal income 上升而 real-income index 下降的第四种情形；
7. \(s^\dagger<1/2\) 的唯一性和全局最大值证明正确；
8. \(G>0\)、反向 retention、\(\omega=0,1\)、\(\eta\to1,\infty\)
   等边界与主模型一致。

计算核验结果：

    PASS: 2000 deterministic random draws and all listed boundary checks
    (seed=20260714).

核验脚本同时检查固定点残差和迭代收敛、中心差分导数、有限冲击区域、
multiplier elasticity/convexity、内部峰值与预设边界案例。函数命名已与
论文统一为 local_income_multiplier 和 gross_spending_multiplier。

## 6. 原创性启发式复查

按上一轮相同的 30 个实质性 prose blocks 口径，重新抽查 16 段，覆盖
Abstract、Introduction、Model、Results、Conclusion 和 Appendix，
占 53.3%。代表性精确短语包括：

- “A fall in the relative price of a platform retail channel”
- “closed-form characterization of a retention-feedback mechanism”
- “Each induced spending round purchases newly produced output”
- “The multiplier m_B propagates one dollar already formed as local income”
- “Absent the propagation denominator, the CES substitution term”
- “the price-index gain can offset a nominal-income loss”

公开网页检索未发现精确或具有实质意义的近似文本匹配；返回结果均为无关
主题或仅共享一般术语。这是启发式公开网页检查，不替代 iThenticate、
Turnitin 或出版社 Crossref Similarity Check。

## 7. LaTeX、篇幅与 PDF

- python code/verify_model.py：PASS；
- code/build_paper.ps1 -KeepAux：成功生成 9 页 output/paper.pdf；
- final LaTeX log：无 undefined citation、undefined reference、
  overfull/underfull box、LaTeX fatal error；
- texcount -inc -sum：
  - main.tex：1,353；
  - appendix.tex：531；
  - 合计：1,884；
  - Abstract：90 词；
- PDF 逐页渲染检查：9/9 页无裁切、重叠、乱码、公式越界或不可接受的
  断页。

MiKTeX 的 C 盘日志写入权限和未检查更新提示是非致命环境警告；最终
LaTeX log 与 PDF 均完整。

## 8. AI research failure modes

| Mode | 结论 | 依据 |
|---|---|---|
| 1. 代码结果缺少解析支持 | CLEAR | 所有主要结果均有正式证明 |
| 2. 虚构或错配文献 | CLEAR | 9/9 元数据及正文语境复核通过 |
| 3. 虚构统计或经验结果 | CLEAR | 纯理论稿，无数据或经验估计 |
| 4. 无效实验捷径 | N/A | 无实验或 ML pipeline |
| 5. 无解释的异常输出 | CLEAR | 比较静态来自解析证明并经脚本交叉核验 |
| 6. 错述方法或数据 | CLEAR | 模型边界及 data statement 与实际一致 |
| 7. 研究框架未锁定 | **CLEAR** | 标题、问题、贡献、文献让步与模型一致 |

## 9. 保留的非阻断限制

1. \(\rho_A,\rho_P\) 是短期外生收入归属参数，论文不解释其如何由平台
   合同、佣金、供应链、所有权或税制内生决定。
2. \(B(z)\) 是维护的 reduced-form、非负 base-income response，不是从
   Faber 的空间生产模型推导出来的。
3. 这是 small-open-region short-run income model，不是 platform IO、
   multi-region spatial GE 或完整社会福利分析。
4. 公开网页原创性检查不是专业相似度报告。
5. Li（2025）是未发表稿，投稿前需要核查是否更新或正式发表。

这些限制已经在正文中明确，不阻断 Stage 2.5，但必须在后续审稿模拟和
投稿版本中继续保持。

## 10. 文件处置与下一步

本轮修改并复审：

- paper/main.tex
- paper/appendix.tex
- paper/references.bib
- code/verify_model.py
- 根目录与子项目 README.md

新建本复审报告，保留上一轮 FAIL 报告作为审计历史。已重新生成
output/paper.pdf。没有自动 commit，也没有 push。

依据 Academic Research Suite 的阶段规则，Stage 2.5 通过后必须暂停。
只有作者明确确认，才进入 Stage 3 正式多角色审稿。
