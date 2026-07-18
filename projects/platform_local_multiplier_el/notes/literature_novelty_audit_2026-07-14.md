# Literature Novelty Audit — 可审计版本

**项目：** `platform_local_multiplier_el`
**核验日期：** 2026-07-14
**结论状态：** **有条件通过，尚不能写“cleared”**
**用途：** 内部决策与 Introduction 文献定位；不是对“不存在竞争者”的证明

---

## 一、结论先行

本轮核验得到的准确结论是：

> 在本轮实际核验的高相关候选文献中，尚未识别出一篇同时包含“平台或线上—线下渠道替代”“渠道特定的地方收入留存”“居民支出—地方收入的递归反馈”三个核心部件的论文。

这支持继续开发项目，但不支持“直接竞争者为零”或“已经证明不存在竞争者”的说法。检索数据库和引文索引都可能漏收工作论文、未发表稿件及非英文研究；题名筛查也不能替代全文阅读。

更重要的是，本轮发现了原查重结论忽略的一支实质性先例：**区域投入产出与空间社会核算文献早已把工资—消费流、区域外购漏出和多轮支出乘数放在同一体系内。** BEA 的 RIMS II 指南明确说明，多轮支出会因储蓄、税收和进口漏出而递减；Jun（2004）把生产地、居住地和消费地的系数置于同一都市投入产出矩阵；Hermannsson（2016）则直接强调工资和消费流对于 Type II 地方乘数的重要性。

因此：

- **不能**把“漏出进入乘数分母”或 \(\omega/(1-\alpha\omega)\) 一类几何级数本身声称为创新；
- **不能**把“本地所有权影响地方发展”声称为创新；
- **不能**把“线上渠道降低价格但冲击本地零售”声称为创新；
- 目前唯一可能成立的窄贡献，是把这三支既有思想连接为：

> 市场整合内生改变线上渠道份额，线上渠道份额再改变每轮支出的地方要素收入留存率；价格指数下降与收入传播收缩共同决定名义收入和消费等价实际收入的符号及阈值。

这是一个**联合建模增量**，不是任何单一部件的首次提出。

---

## 二、什么才算“直接竞争者”

为了避免凭印象判断，本轮预先固定四个判据：

| 代码 | 判据 | 操作性定义 |
|---|---|---|
| P | 平台/渠道替代 | 交易成本、线上效率或平台条件改变消费者或企业在线上与线下渠道间的选择 |
| L | 地方留值 | 明确区分本地与外地要素收入、利润所有权、总部收益或消费支出的空间归属 |
| M | 递归地方乘数 | 当期地方收入影响后续本地消费或需求，形成收入/支出的固定点或 Type II 乘数 |
| T | 联合阈值 | 同时比较价格收益与地方名义收入变化，得到实际收入、福利或符号反转条件 |

本次把同时满足 **P + L + M** 的论文定义为直接竞争者；T 不是最低必要条件，但若也满足 T，则与本项目高度重合。只满足其中一个或两个判据的论文属于前驱或最近邻，必须引用和区分，但不直接否定项目。

---

## 三、检索与筛查范围

### 3.1 不再把关键词结果数当作“证明”

本轮采用三层筛查：

1. **种子文献引文网络：** 检查 Atkin–Faber–Gonzalez-Navarro（AFG）、Moretti、Fan et al. 和 Couture et al. 的前向引用及高相关后向引用；RePEc 页面当日分别显示 105、205、70 和 89 条前向引用记录。合计 469 条是**带重复的索引记录数**，不是 469 篇已经全文阅读的论文。
2. **机制分支追踪：** 分别沿线上—线下空间竞争、平台费与加入决策、地方所有权、区域投入产出/Type II 乘数、地方劳动市场五条分支追踪。
3. **高相关候选核验：** 对题名和摘要显示可能覆盖至少两个判据的论文，读取官方摘要、开放版本或正文，并填写下列逐篇矩阵。

因此，本文件可以审计“为什么排除这些最近邻”，但仍不能审计所有数据库中每一条低相关记录的全文。

### 3.2 证据等级

- **F：** 阅读了可获得的正文或开放工作论文；
- **A：** 核验了期刊、作者或研究机构页面上的摘要与书目信息；
- **B：** 仅用于扩展候选集的题名/引文记录，不据此做强结论。

下表只列已经达到 F 或 A 的高相关候选。判据中的“△”表示相关但没有完成本项目所需的空间归属或递归闭合。

---

## 四、逐篇纳入—排除矩阵

### 4.1 理论、结构与区域核算文献

| 文献 | 证据 | P | L | M | T | 判定与排除理由 |
|---|---:|:---:|:---:|:---:|:---:|---|
| Atkin, Faber & Gonzalez-Navarro (2018), JPE | F/A | ✓ | △ | — | △ | 有渠道选择、价格福利以及本地工资和利润分解；没有居民支出反复形成地方收入的固定点。是**消费—收入分解最近邻**，不是直接竞争者。 |
| Fan, Tang, Zhu & Zou (2018), JIE | A | ✓ | △ | — | ✓ | 多地区电商 GE、空间贸易与实际工资福利；收入由空间 GE 决定，但没有渠道特定的本地所有权/留值参数，也没有 Moretti/Type II 式本地支出循环。 |
| Faber (2014), ReStud | F/A | — | △ | — | △ | 市场整合、核心—外围不对称和生产区位重配；是供给侧空间重组基准，但没有平台渠道、总部利润归属或地方支出递归。 |
| Goldmanis et al. (2010), EJ | A | ✓ | — | — | — | 电商降低搜索成本并把市场份额从低效率企业转向高效率企业；没有收入归属和地方需求乘数。 |
| Guo & Lai (2017), JIE | A | ✓ | — | — | △ | 线上商家与异质线下商家的价格、区位和福利；不追踪利润归属地或地方收入乘数。 |
| Colombo & Hou (2021), RIO | A | ✓ | — | — | — | 线下零售商和无区位线上零售商的区位—价格均衡；没有地方收入形成。 |
| Guo & Lai (2022), *Economics Letters* | A | ✓ | — | — | △ | 线上—线下竞争与价格歧视福利，是目标期刊中的直接题材先例；研究价格与总产出，不研究地方留值和乘数。 |
| Guo & Lai (2024), ARS | A | ✓ | — | — | △ | 明确区分城市/农村市场并研究线上竞争、区位和空间价格；没有收入归属和地方乘数。 |
| Aiba (2024), ARS | A | ✓ | △ | — | △ | 在新经济地理模型中研究 IT、远程购买、企业区位和空间消费不平等；没有总部利润漏出或地方消费—收入固定点。 |
| Gokan, Thisse & Zhu (2025), IDE DP | F | ✓ | — | — | △ | 当前最接近的线上—线下空间理论：企业选择零售形式，消费者选择渠道，并比较消费者剩余和总福利。正文检索未发现 local income、ownership、retention 或 multiplier 模块。 |
| Moretti (2010), AER P&P | F/A | — | — | ✓ | — | 可贸易就业通过本地非贸易需求产生地方就业乘数；不含平台渠道、利润空间归属或消费价格指数。 |
| Jun (2004), ARS | A | — | ✓ | ✓ | — | **重要先例。** 都市投入产出模型同时区分生产地、居住地与消费地，并用矩阵逆得到多轮影响。没有平台渠道内生替代和消费价格福利。 |
| Hermannsson (2016), *Spatial Economic Analysis* | A | — | ✓ | ✓ | — | **重要先例。** 明确把工资与消费流纳入地方投入产出表，并指出其对 Type II 地方乘数至关重要。没有平台或线上—线下选择。 |
| BEA RIMS II User's Guide | F | — | △ | ✓ | — | **机械结构的先例。** 明确说明多轮支出因储蓄、税收和进口漏出而衰减，也按地方供给条件处理区域外购。不是平台论文，但否定“递归漏出公式本身新颖”。 |
| Fleming & Goetz (2011), EDQ | A | — | ✓ | — | — | 以企业所有者居住地衡量本地所有权，并发现小型本地企业密度与县域收入增长正相关；没有渠道与递归乘数。 |
| Kolko & Neumark (2010), JUE | A | — | ✓ | — | — | 研究本地所有权是否缓冲城市就业冲击；没有平台渠道、消费价格或地方支出固定点。 |
| Eden, Ma & Parkes (2023), “Platform Equilibrium” | A | ✓ | △ | — | △ | 平台费、卖家加入和总福利的理论模型；没有地区、总部所在地和地方乘数。它说明“平台费影响加入和福利”也不能单独作为创新。 |

### 4.2 经验与测量文献

| 文献 | 证据 | P | L | M | T | 判定与排除理由 |
|---|---:|:---:|:---:|:---:|:---:|---|
| Couture, Faber, Gu & Liu (2021), AER: Insights | F/A | △ | △ | — | △ | 农村电商带来部分生活成本收益，但生产者和工人收入增长证据有限；是核心经验动机，不提供留值—乘数理论。 |
| Dolfen et al. (2023), AEJ: Macro | A | ✓ | — | — | △ | 用支付数据估计电商消费者剩余和线上替代；不追踪商户利润归属及地方收入传播。 |
| Relihan (2022), CEP DP | A | ✓ | — | △ | △ | 线上购物节省时间后增加咖啡店等本地服务出行，是很接近的本地服务溢出机制；但它是时间配置与出行需求，不是收入递归或总部利润漏出。 |
| Chava, Oettl, Singh & Zeng (2024), *Management Science* | A | △ | △ | — | — | 电商履约中心扩张降低邻近县传统零售工人收入、门店销售和就业，并部分增加仓储、餐饮就业；是最强的地方劳动市场经验近邻，但没有结构化留值乘数。 |
| Kim & Lee (2024), HJE | A | △ | △ | — | — | 外卖平台使用提高韩国餐厅销售，且小餐厅收益更大；研究本地商户销售异质性，不研究佣金流向和多轮地方收入。 |
| Neumark, Zhang & Ciccarella (2008), JUE | A | — | △ | — | — | 沃尔玛进入降低县域零售就业和工资总额；说明“外来零售进入损害本地劳动收入”不是新现象。 |
| Forman, Ghose & Goldfarb (2009), *Management Science* | A | ✓ | — | — | — | 证明线上购买的相对吸引力取决于消费者所在地和本地门店；没有地方收入归属和乘数。 |

### 4.3 矩阵结论

在上述已经核验的高相关候选中：

- 没有一篇同时满足 P + L + M；
- AFG 最接近 **P + L**，但缺 M；
- Jun（2004）和 Hermannsson（2016）最接近 **L + M**，但缺 P 和价格福利；
- Gokan et al.（2025）、Guo & Lai（2017, 2024）及 Aiba（2024）最接近 **P + 空间福利/区位**，但缺 L 和 M；
- Couture et al.（2021）与 Chava et al.（2024）提供联合事实，但不是直接理论竞争者。

这意味着项目的文献空档不是任何单个机制，而是三个机制的交集。

---

## 五、对当前模型的直接影响

### 5.1 必须撤回或修改的表述

以下说法不再使用：

1. “现有地方乘数模型假定本地支出 100% 留在本地。”
   区域投入产出模型长期处理进口和区域外购漏出，Type II 模型还内生家庭收入与消费。
2. “本文首次让留值率进入乘数。”
   固定地方采购率或漏出率进入 Leontief/几何级数乘数并不新。
3. “AFG 是纯消费侧部分均衡，不能解释地方收入。”
   AFG 明确分解工资、利润和其他收入渠道；准确差异是它没有用重复支出固定点闭合地方收入。
4. “直接竞争者为零。”
   应改为“在本次核验的文献集中尚未识别出联合建模这三个部件的论文”。

### 5.2 仍可保留的贡献候选

当前可以保留但需要进一步做强的是：

1. **平台化内生改变漏出率。** 不是把一个外生的地方采购系数放进乘数，而是由线上—线下渠道选择推导 \(\omega(z)\)。
2. **同一冲击同时影响价格与收入形成。** \(z\) 既降低平台有效价格，也降低地方留值；由此区分名义收入和消费等价实际收入。
3. **解析阈值与区域排序。** 给出外部市场准入、价格收益和乘数压缩之间的必要充分条件，而不是只做数值例子。
4. **机制关闭的反事实。** 分别关闭价格渠道、市场准入渠道、渠道替代和递归反馈，展示每个机制对符号和阈值的贡献。

### 5.3 当前最大投稿风险

即使不存在 P + L + M 的直接竞争者，审稿人仍可能认为模型只是把 CES 渠道份额接到一个老的 Type II 乘数上，结论由单调性直接得到。对 *Economics Letters* 来说，“文献中没人这样拼”不等于“理论结果足够新”。

因此，在正式写作前至少需要再得到一个不只是代数重写的结果，例如：

- 证明整合程度上存在唯一的地方收入或实际收入转折点，并给出存在条件；
- 证明名义收入阈值与实际收入阈值的严格排序及其对替代弹性、留值差、地方服务支出倾向的比较静态；
- 说明何时更强的市场准入反而扩大“消费受益但地方收入受损”的区间；
- 把平台费或总部利润份额映射到 \(\rho_P\)，证明费率变化与交易成本变化在地方福利上的非等价性。

如果这些结果无法超出一个显然的几何级数和价格指数分解，本项目不应以“新理论机制”直接投稿 EL。

---

## 六、建议的 Introduction 定位

可以使用：

> Existing research separately studies the consumer gains from online access, the spatial effects of online–offline retail competition, and the role of consumption leakages in regional multipliers. We connect these margins by allowing market integration to reallocate expenditure across channels with different local factor-income shares. Because the resulting leakage recurs through local demand, the same integration shock can lower local nominal income even when it reduces the consumer price index.

需要紧接着承认三个前驱边界：

1. AFG 已经联合测量价格收益与本地工资、利润损失；本文新增的是递归地方收入闭合；
2. Jun（2004）和 Hermannsson（2016）已经在区域投入产出框架中处理收入—消费空间流；本文新增的是平台渠道选择和价格福利；
3. Gokan et al.（2025）、Guo & Lai（2017, 2024）已经研究线上—线下空间竞争、区位与福利；本文新增的是地方收入归属和乘数传播。

暂时不要使用 “first paper” 或 “no existing paper”。如果后续完成更广的数据库检索，最多使用：

> To our knowledge, existing work has not jointly modeled endogenous online–offline channel substitution, channel-specific local factor-income retention, and recursive local-demand propagation.

---

## 七、决策与下一步

### 当前决策

**Conditional go。** 项目继续一周，但创新状态从“cleared”改为“需要用更强命题过关”。

### 一周内的硬任务

- [ ] 精读 Jun（2004）与 Hermannsson（2016）的模型矩阵，确认当前标量固定点是否只是其一维特例；
- [ ] 精读 Guo & Lai（2017）以及 Gokan et al.（2025），写出本模型相对线上—线下空间竞争文献的逐项差异；
- [ ] 把 \(\omega(z)\) 与平台费、外地供货商份额和本地履约份额建立可解释映射；
- [ ] 形成一个强于“乘数随留值率上升”的命题，并检查是否有唯一转折点或阈值排序；
- [ ] 将本文件中的 24 项候选文献/方法资料纳入 `references.bib` 候选库。

### 停止条件

满足任一条件即暂停 EL 短文：

1. 发现已经同时满足 P + L + M 的理论论文；
2. 当前核心命题可由标准 Type II 区域投入产出模型直接作为一维特例得到，且平台渠道只改变一个外生系数；
3. 无法得到超出单调性和会计分解的独立命题；
4. 为获得新结果必须扩展成完整空间 GE，导致文章不再适合六周内完成的 Letter。

---

## 八、可复核来源登记

以下链接是本轮判断的主要依据，优先列作者、期刊、研究机构和官方方法文档；RePEc 用于引文网络和书目信息核对。

- [AFG (2018), RePEc/JPE metadata](https://ideas.repec.org/a/ucp/jpolec/doi10.1086-695476.html)
- [AFG forward citations, RePEc/CitEc](https://ideas.repec.org/r/ucp/jpolec/doi10.1086-695476.html)
- [Moretti (2010), AEA](https://www.aeaweb.org/articles?id=10.1257/aer.100.2.373)
- [Couture et al. (2021), AEA](https://www.aeaweb.org/articles?id=10.1257/aeri.20190382)
- [Fan et al. (2018), RePEc/JIE metadata](https://ideas.repec.org/a/eee/inecon/v114y2018icp203-220.html)
- [Faber (2014), Review of Economic Studies](https://doi.org/10.1093/restud/rdu010)
- [Goldmanis et al. (2010), NBER version](https://www.nber.org/papers/w14166)
- [Gokan, Thisse & Zhu (2025), IDE-JETRO](https://www.ide.go.jp/English/Publish/Reports/Dp/968.html)
- [Guo & Lai (2017), RePEc/JIE metadata](https://ideas.repec.org/a/bla/jindec/v65y2017i2p439-468.html)
- [Guo & Lai (2022), Economics Letters](https://ideas.repec.org/a/eee/ecolet/v216y2022ics0165176522001811.html)
- [Guo & Lai (2024), Annals of Regional Science](https://ideas.repec.org/a/spr/anresc/v73y2024i1d10.1007_s00168-024-01267-0.html)
- [Colombo & Hou (2021), Review of Industrial Organization](https://ideas.repec.org/a/kap/revind/v59y2021i3d10.1007_s11151-021-09814-1.html)
- [Aiba (2024), Annals of Regional Science](https://ideas.repec.org/a/spr/anresc/v73y2024i3d10.1007_s00168-024-01288-9.html)
- [Jun (2004), Annals of Regional Science](https://ideas.repec.org/a/spr/anresc/v38y2004i1p131-147.html)
- [Hermannsson (2016), Spatial Economic Analysis](https://ideas.repec.org/a/taf/specan/v11y2016i3p315-339.html)
- [BEA RIMS II User's Guide](https://www.bea.gov/resources/methodologies/RIMSII-user-guide)
- [Dolfen et al. (2023), NBER version](https://www.nber.org/papers/w25610)
- [Chava et al. (2024), NBER version](https://www.nber.org/papers/w30077)
- [Relihan (2022), LSE/CEP record](https://ideas.repec.org/p/ehl/lserod/117805.html)
- [Fleming & Goetz (2011), RePEc/EDQ metadata](https://ideas.repec.org/a/sae/ecdequ/v25y2011i3p277-281.html)
- [Kolko & Neumark (2010), RePEc/JUE metadata](https://ideas.repec.org/a/eee/juecon/v67y2010i1p103-115.html)
- [Neumark, Zhang & Ciccarella (2008), RePEc/JUE metadata](https://ideas.repec.org/a/eee/juecon/v63y2008i2p405-430.html)
- [Forman, Ghose & Goldfarb (2009), Management Science](https://ideas.repec.org/a/inm/ormnsc/v55y2009i1p47-57.html)
- [Kim & Lee (2024), Hitotsubashi Journal of Economics](https://ideas.repec.org/a/hit/hitjec/v65y2024i1p65-93.html)

---

## 九、审计限制

1. RePEc/CitEc 引用记录不完整，且同一论文的工作论文与期刊版本会重复；
2. 本轮没有访问 Scopus、Web of Science、EconLit 的订阅检索，因此不能宣称数据库穷尽；
3. 部分付费论文只核验了正式摘要与可获得版本；
4. 2025—2026 年工作论文仍可能快速出现；
5. 因此本文件的可辩护表述始终是“在已核验集合中未识别出”，而不是“不存在”。
