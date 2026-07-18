# Economics Letters 理论短文项目备忘录

## 平台中介、地方留值与地方乘数

**性质：** 供合作者讨论的项目方案（不是论文定稿）  
**拟投稿期刊：** *Economics Letters*  
**计划周期：** 45 天  
**目标投稿日：** 2026 年 8 月 28 日  
**数据需求：** 纯理论版本不使用原创数据；只做解析证明和透明的示意性数值图

**文献核验状态（2026-07-14）：** 暂定通过，可以开始模型与写作；相邻文献筛查仍需继续，不使用“直接竞争者为零”或“已完成创新性证明”等绝对表述

**投稿稿更新（2026-07-17）：** 当前英文稿已经采用一般 homothetic
两渠道需求，CES 降为 Supplement 中的闭式特例。正式主结果现为：
（M1）有限整合冲击下唯一且有序的能力阈值；（M2）严格凹 share-speed
下唯一的 capture-drag 峰值；（M3）integration 与 organizational
capacity 的 log-income increasing differences。标准地方 multiplier
只作为 benchmark。本备忘录后文保留项目形成过程和旧版 CES 推导，若
与当前稿冲突，以 `README.md`、`paper/main.tex` 和
`paper/supplement.tex` 为准。

---

## 建议转发给合作者时附上的短消息

> 雅淇，我把大项目中最干净、也最适合独立成文的理论机制拆成了一个 *Economics Letters* 方案。它不是大项目的压缩版，而是一篇不需要原创数据、集中证明一个反直觉结果的短理论文章。下面是完整设想，想请你重点判断三件事：理论结果是否足够独立、是否与大项目边界清楚，以及我们是否愿意用六周把它完成。

---

## 一、项目摘要

本项目拟从原有“统一大市场、平台化与地方发展”研究中，抽取一个可以独立成立的最小理论问题，写成一篇约 2,000 英文词的 *Economics Letters* 短文。

论文研究的问题是：

> **当市场一体化降低平台交易成本、扩大外围地区的市场准入时，为什么地方名义收入仍可能下降，甚至居民的消费等价实际收入也可能下降？**

基本机制是，市场一体化同时产生三种作用：

1. **消费价格效应：** 平台交易成本下降，居民面对的零售价格指数下降；
2. **外部市场准入效应：** 本地生产者更容易进入外部市场，基础部门收入提高；
3. **空间价值捕获效应：** 居民支出从本地代理渠道转向平台直连渠道，交易收入更多流向外部供货商、平台和总部地区，本地留值率下降。

第三种作用并不只发生在第一轮交易。新增地方收入在后续消费中仍会在本地渠道和平台渠道之间分配，因此平台造成的空间漏出会在每一轮支出循环中重复发生。由此，本地留值率进入地方乘数的分母，而不是简单地在一个传统乘数之后乘上一次。

论文拟证明两个核心结果：

- **递归留值命题：** 对地方外部支出的有效收入乘数为
  \[
  \mathcal M(\omega)=\frac{\omega}{1-\beta-\alpha\omega},
  \]
  并且它小于“先计算完全本地化乘数、再乘一次留值率”的结果；
- **实际收入阈值命题：** 市场一体化的地方影响由外部市场准入、消费价格收益和递归收入漏出三者的相对大小决定。模型给出“名义收入与消费等价实际收入均提高”“名义收入下降但实际收入提高”“二者均下降”三个解析区域。

本文不建立完整的全国空间一般均衡，不研究税收、企业迁移或平台最优定价。它是一篇有明确边界的、小型开放地区静态均衡论文。完整的多地区生产、税收与实证识别留给后续大项目。

---

## 二、为什么值得单独写成一篇 Letter

### 2.1 现有大项目中已经存在一个可独立抽取的理论核

原项目包含统一市场、平台中介、地方留值、税基、企业区位、地方乘数和新结构经济学等多条机制。对于模型加实证的大论文，这种丰富性是优势；对于 *Economics Letters*，它会造成模型过重、贡献不够集中。

最适合独立发表的理论核并不是“平台是否有利于地方发展”，而是：

> **平台化使本地支出与本地收入形成脱钩，并且这种脱钩会通过后续支出循环递归地改变地方乘数。**

这可以形成一个一般性的理论命题，不依赖中国特定制度，也不依赖一套难以在短期内获得的交易数据。

### 2.2 文章必须是“一个新结果”，而不是概念性笔记

单纯定义 retained value，或写出

\[
Y=A+m\omega X,
\]

还不足以构成一篇理论 Letter，因为这很容易被理解为会计分解。本文必须完成两个推进：

1. 从消费者在本地代理与平台渠道之间的选择中，内生推导平均留值率 \(\omega\)；
2. 让 \(\omega\) 进入收入固定点，从而产生新的乘数公式、实际收入阈值和平台扩张阶段性结果。

因此，本文真正出售的不是 retained value 这个术语，而是：

> **内生渠道替代—递归空间漏出—实际收入符号反转。**

### 2.3 与后续大论文可以形成清楚的分工

| 维度 | 本 EL 理论短文 | 后续模型加实证大论文 |
|---|---|---|
| 地理 | 一个小型地区 + 外部经济 | 多地区、核心—外围网络 |
| 渠道 | 本地代理、平台直连 | 多平台、多渠道、生产与履约网络 |
| 平台 | 交易效率与收入归属为参数 | 可扩展至平台定价、佣金、排序与治理 |
| 生产 | 外部市场准入收入的简化表达 | 企业进入退出、生产区位与供给能力 |
| 劳动市场 | 短期弹性本地服务供给 | 工资、就业、迁移、通勤与住房 |
| 财政 | 不建模 | 税源归属、税基留存与政府支出 |
| 经验部分 | 无原创数据 | 因果识别、结构参数与定量反事实 |
| 核心贡献 | 一个闭式机制与阈值 | 测度、识别、空间 GE 与政策量化 |

如果未来大论文在没有本理论命题的情况下仍能依靠新数据、识别策略和定量空间模型独立成立，那么先发表这篇 Letter 是合理的。反之，如果未来大论文唯一的理论创新就是本文的两个命题，则不宜拆分。

---

## 三、文献定位：不是把三个模型机械拼接

### 3.1 母框架：Atkin、Faber 与 Gonzalez-Navarro（2018）

Atkin et al. 研究外资零售进入对家庭福利的影响，将福利变化分为生活成本效应与名义收入效应。其六项分解不仅包括新店和竞争带来的价格指数变化，也包括零售劳动收入、国内商店利润以及非零售部门的其他收入效应。该文为本文提供两个关键起点：

- 居民可以在不同零售渠道之间选择；
- 价格收益与本地劳动、利润损失可以同时存在。

Atkin et al. 的需求结构是多层 CES 商店—产品选择，不能简单称为一个只有两个渠道的消费侧部分均衡模型。该文已经测量和分解地方名义收入渠道，但没有用一个重复支出的固定点内生闭合地方收入，也没有让渠道特定的本地留值率进入每一轮支出。

因此，本文不能把“低价平台替代传统商店”或“价格提高福利但本地零售受损”本身声称为新发现。本文的新增部分是：把渠道收入的空间归属嵌入地方支出固定点，使留值损失在后续支出中递归传播。

### 3.2 市场一体化冲击：Faber（2014）

Faber 研究交通基础设施和贸易成本下降如何改变核心与外围地区的生产活动。他说明市场一体化并不保证生产向外围扩散，外部竞争可能使活动进一步向核心集中。

本文只保留其中最小的一层：同一个市场一体化指数 \(z\) 一方面降低平台渠道的有效交易成本，另一方面扩大外围地区生产者的外部市场准入。本文不使用 Faber 的资本流动、工业区位和工资均等化结构。

### 3.3 地方传播机制：Moretti（2010）

Moretti 的地方乘数思想是：可贸易部门收入或就业增加后，居民对本地非贸易服务的需求上升，从而诱发后续就业和收入。本文用 \(\beta Y\) 表示这一最小机制。

Moretti（2010）主要研究地方劳动力市场中的就业乘数，而不是从凯恩斯式支出递推推导 \(1/(1-c)\) 的模型。因此本文不是“加入 Moretti 的完整模型”，也不能声称把 Moretti 的乘数从 \(1/(1-c)\) 修正为 \(s/(1-sc)\)。本文只借用其经济直觉，把可贸易收入—本地非贸易需求反馈写入地方收入闭合条件。

若把所有本地消费合并为一个支出倾向 \(c\)，并用 \(s\) 表示留值率，\(s/(1-sc)\) 可以作为本文乘数的退化特例；但在本文符号中 \(s\) 已表示平台份额，留值率必须记为 \(\omega\)。完整结果仍是

\[
\mathcal M(\omega)=\frac{\omega}{1-\beta-\alpha\omega}.
\]

### 3.4 关键经验动机：Couture et al.（2021）

Couture et al. 将随机对照试验与调查和行政数据结合，研究中国农村电商扩展。他们发现，对农村生产者和工人的收入增长证据有限，收益主要来自部分年轻、较富裕和更偏远家庭的生活成本下降。这是“消费价格改善但地方收入没有同步上升”的直接经验动机。

本文不能声称“解决”了 Couture et al. 的零收入结果，因为生产约束、卖家采用和观察期限也可能解释该结果。安全的定位是：本文提供一种与其联合事实一致的理论机制，即平台扩展在降低消费价格的同时，可能通过降低每一轮支出的地方留值率压缩地方收入传播。

### 3.5 最接近的空间电商 GE：Fan et al.（2018）

Fan et al. 建立多地区一般均衡模型，研究电商如何通过消除固定市场进入成本、减弱距离对贸易成本的影响而增加城际贸易并缓解空间消费不平等。该文表明小城市可能因消费可及性改善获得更大的福利收益，因此是本文必须正面区分的最近邻。

本文与 Fan et al. 的差异不是“部分均衡对一般均衡”，而是研究对象不同：Fan et al. 量化线上贸易、空间商品流动与实际工资福利；本文研究渠道收入的空间归属，并让渠道特定的本地要素收入份额进入重复支出的地方收入固定点。本文的结论是，小地区是否受益不仅取决于消费可及性，也取决于 \(\rho_A-\rho_P\)、外部市场准入能力和递归地方需求反馈。

### 3.6 电子商务与市场结构：Goldmanis et al.（2010）

Goldmanis et al. 把电子商务理解为搜索成本下降，并说明市场份额会从低效率企业流向高效率企业。该文意味着“电商冲击小型传统商户”本身也不是本文的创新。

本文的区别必须保持在空间收入归属：相同的消费者支出和相同的价格变化，因中介收益由本地代理还是外部平台捕获，会产生不同的地方收入与后续乘数。

### 3.7 暂定贡献表述与创新性边界

现阶段最稳妥的贡献表述是：

> We embed endogenous retail-channel choice in a small-region local-multiplier model. Platform-mediated integration changes not only the consumer price index but also the local factor-income share of each spending round. This recursive leakage yields a closed-form effective multiplier and real-income thresholds that separate local income gains, consumer gains with local income losses, and joint losses.

对创新性的暂定判断是：目前尚未识别出同时包含“内生渠道替代、渠道特定地方留值、递归地方需求传播和同一实际收入阈值”的论文。这是继续开发模型的依据，但不是“直接竞争者为零”的证明。关键词搜索不能替代前向—后向引文核查和逐篇排除矩阵。

论文中可使用：

> To our knowledge, existing work has not jointly modeled endogenous retail-channel substitution, channel-specific local income retention, and recursive local-demand propagation in a tractable spatial framework.

不要声称“首次提出地方留值率”“首次证明平台降低地方福利”，也不要写 “no paper has ever considered”。

---

## 四、最小模型的完整设定

### 4.1 地理、部门与时间顺序

经济由一个小型外围地区 \(L\) 和其余经济 \(H\) 构成。平台总部和大部分外部供货商位于 \(H\)。外围地区足够小，因此其行为不改变外部价格。

外围地区包含：

1. 一个产生基础收入的可贸易或出口部门；
2. 本地代理型零售渠道 \(A\)；
3. 平台直连渠道 \(P\)；
4. 本地非贸易服务部门；
5. 居民家庭。

模型是一阶段静态均衡。市场一体化程度 \(z\) 给定后：

1. 平台有效价格和外部市场准入收入确定；
2. 家庭选择两个零售渠道；
3. 渠道份额决定本地平均留值率；
4. 本地支出、收入和非贸易服务需求共同满足收入固定点；
5. 得到地方收入、就业方向和消费等价实际收入。

### 4.2 家庭偏好与支出份额

代表性居民的偏好为

\[
U=M^\alpha N^\beta Z^{1-\alpha-\beta},
\qquad
\alpha,\beta>0,\quad \alpha+\beta<1.
\]

其中：

- \(M\) 是可以通过代理或平台购买的零售品；
- \(N\) 是完全在当地生产和消费的非贸易服务；
- \(Z\) 是从外部经济购买的数值品。

将 \(N\) 和 \(Z\) 的价格归一化为 1：外部数值品供给固定 \(p_Z=1\)，本地服务价格 \(p_N=1\) 由短期弹性供给和外部机会成本钉住。收入为 \(Y\) 时，居民分别支出

\[
X_M=\alpha Y,\qquad
X_N=\beta Y,\qquad
X_Z=(1-\alpha-\beta)Y.
\]

这里 \(Z\) 提供自然的区域外漏出，保证地方收入循环不会无界扩张。

### 4.3 两种零售渠道

零售品 \(M\) 是本地代理渠道商品 \(M_A\) 与平台渠道商品 \(M_P\) 的 CES 组合：

\[
M=
\left[
(1-a)^{1/\eta}M_A^{(\eta-1)/\eta}
+a^{1/\eta}M_P^{(\eta-1)/\eta}
\right]^{\eta/(\eta-1)},
\qquad \eta>1.
\]

相应价格指数为

\[
P_M(z)=
\left[
(1-a)p_A^{1-\eta}
+a p_P(z)^{1-\eta}
\right]^{1/(1-\eta)}.
\]

令市场一体化或平台交易效率提高时，平台有效价格下降：

\[
p_P(z)=\bar p_Pe^{-z}.
\]

平台支出份额为

\[
s(z)=
\frac{a p_P(z)^{1-\eta}}
{(1-a)p_A^{1-\eta}+a p_P(z)^{1-\eta}}.
\]

因此有

\[
\frac{d\ln P_M}{dz}=-s(z)<0,
\]

以及

\[
\frac{ds}{dz}=(\eta-1)s(1-s)>0.
\]

第一式是直接消费价格收益；第二式表示平台效率改善会把支出从代理渠道转向平台渠道。

### 4.4 渠道的本地要素收入份额

令 \(\rho_A\) 和 \(\rho_P\) 分别为一元代理渠道和平台渠道销售额中，成为外围地区本地工资、本地利润或本地所有者收入的份额。

平均本地留值率为

\[
\omega(z)=(1-s)\rho_A+s\rho_P.
\]

定义

\[
\Delta\rho=\rho_A-\rho_P.
\]

若代理渠道较多使用本地销售、履约、售后和本地所有资本，而平台渠道更多使用外部供货、总部服务和平台资本，则 \(\Delta\rho>0\)。这时

\[
\frac{d\omega}{dz}
=-\Delta\rho(\eta-1)s(1-s)<0.
\]

为了避免把结论直接塞进假设，附录应给出一个四五行的成本份额微观基础。令渠道 \(c\in\{A,P\}\) 使用本地服务投入和外部投入生产交易服务，其 CRS 单位成本中本地投入份额为 \(\rho_c\)。平台生产率提高降低 \(p_P\)，而 \(\rho_P<\rho_A\) 表示平台技术的本地投入强度更低。

这一设定允许反向情况：如果平台带来大量本地履约、直播运营、仓储或本地所有权，使 \(\rho_P\geq\rho_A\)，平台扩张不会造成本文所说的留值损失。这个反向情况应在论文中明确写出。

### 4.5 外部市场准入收入

令本地可贸易或出口部门带来的、已经归属于本地居民的增加值收入为

\[
B(z)=\bar B e^{\varepsilon z},
\qquad \varepsilon\geq0.
\]

其中 \(\varepsilon\) 表示本地把更低交易成本转化为外部销售和基础收入的能力。\(B\) 是本地工资、利润等增加值收入，而不是出口销售总额。正文将其视为市场准入弹性；附录可用外部 CES 需求给出一行推导。

高 \(\varepsilon\) 地区拥有更强的本地生产、品牌、物流或平台经营能力；低 \(\varepsilon\) 地区虽然可以买到更便宜的外部商品，却难以对外扩大销售。本文不进一步解释这些能力的来源，避免重新引入完整的新结构经济学模块。

### 4.6 地方收入固定点

令 \(G\) 表示游客、外部政府采购或其他外部主体在本地零售市场中的支出，并假设其在两个渠道之间的分配与居民相同。

居民在非贸易服务上的支出 \(\beta Y\) 完全成为本地收入；居民和外部主体在零售品上的支出只有 \(\omega\) 留在本地。因此地方收入满足

\[
Y=B(z)+\beta Y+\omega(z)\bigl(\alpha Y+G\bigr).
\]

解得

\[
Y(z,G)=
\frac{B(z)+\omega(z)G}
{1-\beta-\alpha\omega(z)}.
\]

定义

\[
D(z)=1-\beta-\alpha\omega(z).
\]

因为 \(0\leq\omega\leq1\) 且 \(\alpha+\beta<1\)，所以

\[
D(z)\geq1-\alpha-\beta>0,
\]

均衡唯一。

经济含义是：本地支出不是凭空创造实际资源。每一元本地支出购买一元本地服务并形成相应要素收入；短期内存在闲置劳动、闲置产能或弹性就业边际，本地服务在固定外部机会成本下供给，因此调整主要表现为产出、就业和收入，而非价格。支出于外部商品、外部供货和平台总部的部分离开本地区域收入循环。所有本地收入接受者在基准模型中具有相同的边际消费倾向。

这一假设适合短期地方就业与收入分析。内生工资、住房和迁移属于大论文扩展，不应进入本 Letter。

### 4.7 消费等价实际收入及其福利解释

在 \(N\) 和 \(Z\) 价格归一化后，间接效用可写为

\[
V(z)=K\frac{Y(z)}{P_M(z)^\alpha},
\]

其中 \(K\) 是与比较静态无关的常数。因此

\[
\frac{d\ln V}{dz}
=
\frac{d\ln Y}{dz}
-\alpha\frac{d\ln P_M}{dz}.
\]

这正好把名义收入效应与生活成本效应分开。严格地说，\(V\) 是在本地服务价格固定条件下的 **consumption-equivalent real income**。只有在新增就业的机会成本可以忽略或已被固定工资假设吸收时，才可直接称为完整福利。若正文坚持使用 welfare，必须进一步显式写出劳动供给或闲置劳动假设；否则建议全文使用 resident real income。

---

## 五、拟证明的主要结果

### 引理 1：市场接入与地方捕获的分离

平台交易效率提高时，

\[
\frac{d\ln P_M}{dz}<0,
\qquad
\frac{ds}{dz}>0.
\]

若 \(\rho_A>\rho_P\)，则

\[
\frac{d\omega}{dz}<0.
\]

因此，同一个冲击同时改善消费者市场接入并降低每一元零售支出的本地收入份额。这个引理是模型入口，但不是论文单独的创新。

### 命题 1：递归留值下的有效地方乘数

外部零售支出 \(G\) 的地方收入乘数为

\[
\mathcal M(\omega)
=\frac{\partial Y}{\partial G}
=\frac{\omega}{1-\beta-\alpha\omega}.
\]

作为对照，若所有零售价值均留在本地，即 \(\omega=1\)，传统完全本地化乘数为

\[
m_0=\frac{1}{1-\beta-\alpha}.
\]

若采用“传统乘数乘一次留值率”的写法，会得到

\[
m_0\omega=\frac{\omega}{1-\beta-\alpha}.
\]

但当 \(0<\omega<1\) 时，

\[
\mathcal M(\omega)<m_0\omega.
\]

原因是 \(m_0\omega\) 只在第一轮支出中扣除一次外流，而真实模型中，后续每一轮零售消费都会再次按照 \(1-\omega\) 的比例流向外部。

这个乘数还有直观的级数表达：

\[
\mathcal M(\omega)
=
\omega\sum_{k=0}^{\infty}(\beta+\alpha\omega)^k.
\]

此外，传统一次性修正对乘数的高估量为

\[
m_0\omega-\mathcal M(\omega)
=
\frac{\alpha\omega(1-\omega)}
{(1-\alpha-\beta)(1-\beta-\alpha\omega)}>0.
\]

并且

\[
\frac{\partial\ln\mathcal M}
{\partial\ln\omega}
=
\frac{1-\beta}{1-\beta-\alpha\omega}>1.
\]

同时，

\[
\frac{\partial^2\mathcal M}{\partial\omega^2}
=
\frac{2\alpha(1-\beta)}{(1-\beta-\alpha\omega)^3}>0.
\]

因此，本地留值率下降会使有效乘数出现超过同比例的下降，而且乘数对留值率的响应是凸的。这个超比例敏感性是本文相对于简单 \(m\omega\) 叙事的主要理论推进。

需要谨慎说明：\(m\omega\) 并非在所有环境中都错误。如果 \(\omega\) 只作用于第一轮，而后续支出完全本地化，那么它可以成立。本文强调的是平台渠道在每一轮消费中持续存在时的递归留值。

### 命题 2：有限市场一体化冲击的精确阈值

正文仍令 \(G=0\)。考虑市场一体化程度从 \(z_0\) 提高到 \(z_1>z_0\)，并定义

\[
\mathcal B=\frac{B(z_1)}{B(z_0)},
\qquad
\mathcal D=\frac{D(z_1)}{D(z_0)},
\qquad
\mathcal P=\frac{P_M(z_1)}{P_M(z_0)}.
\]

当 \(\Delta\rho>0\) 时，平台份额上升导致 \(\mathcal D>1\)，平台降价导致 \(0<\mathcal P<1\)。精确地，

\[
\frac{Y_1}{Y_0}=\frac{\mathcal B}{\mathcal D},
\qquad
\frac{V_1}{V_0}=\frac{\mathcal B}{\mathcal D\mathcal P^\alpha}.
\]

因此：

1. 若 \(\mathcal B>\mathcal D\)，名义收入与消费等价实际收入均提高；
2. 若 \(\mathcal D\mathcal P^\alpha<\mathcal B<\mathcal D\)，名义收入下降、消费等价实际收入提高；
3. 若 \(\mathcal B<\mathcal D\mathcal P^\alpha\)，二者均下降。

由于 \(\mathcal P^\alpha<1\)，不存在“名义收入提高但消费等价实际收入下降”的第四种情形。这个有限变化版本应作为正文的主命题，因为它可以直接对应后续 counterfactual。

### 推论 1：边际收入—实际收入阈值

定义递归空间漏出项

\[
\Lambda(s)=
\frac{
\alpha\Delta\rho(\eta-1)s(1-s)
}{
1-\beta-\alpha\omega(s)
}.
\]

由 \(B'(z)/B(z)=\varepsilon\) 可得

\[
\frac{d\ln Y}{dz}
=\varepsilon-\Lambda(s),
\]

以及

\[
\frac{d\ln V}{dz}
=\varepsilon+\alpha s-\Lambda(s).
\]

局部比较静态的三个结果区域分别为：

#### 区域 I：地方收入和消费等价实际收入均提高

若

\[
\Lambda(s)<\varepsilon,
\]

则外部市场准入收益足以超过平台替代造成的收入漏出；由于价格指数同时下降，消费等价实际收入也提高。

#### 区域 II：地方收入下降，但消费等价实际收入提高

若

\[
\varepsilon<\Lambda(s)<\varepsilon+\alpha s,
\]

则地方名义收入下降，但消费价格收益足以补偿收入损失。这是 local development 与 consumer welfare 分离的区域。

#### 区域 III：地方收入和消费等价实际收入均下降

若

\[
\Lambda(s)>\varepsilon+\alpha s,
\]

则即使平台价格下降、外部市场准入改善，递归收入漏出仍然使居民消费等价实际收入下降。

当 \(\varepsilon=0\) 时，消费等价实际收入下降的条件可化为

\[
\Delta\rho(\eta-1)(1-s)
>
1-\beta-\alpha\omega.
\]

负效应更容易出现在：

- 代理与平台的本地收入份额差距 \(\Delta\rho\) 较大；
- 两个渠道的替代弹性 \(\eta\) 较高；
- 平台尚未接近完全占领市场；
- 本地非贸易服务支出份额 \(\beta\) 较高，原有地方收入循环较强；
- 外部市场准入弹性 \(\varepsilon\) 较低。

一个重要但反直觉的解释是：较强的传统地方乘数并不必然保护地方。当平台冲击降低留值率时，原本较强的本地循环也会放大被替代掉的本地收入。

### 推论 2：边际渠道替代拖累在平台扩张过渡阶段最强

若 \(\Delta\rho>0\)，令

\[
D_0=1-\beta-\alpha\rho_A,
\qquad
b=\alpha\Delta\rho.
\]

则

\[
\Lambda(s)
=
\alpha\Delta\rho(\eta-1)
\frac{s(1-s)}{D_0+bs}.
\]

它在 \(s=0\) 和 \(s=1\) 时均为零，并在唯一的内部平台份额

\[
s^\dagger
=
\frac{\sqrt{D_0(D_0+b)}-D_0}{b}
\]

达到最大值。等价地，

\[
s^\dagger
=
\frac{1}{1+\sqrt{1+b/D_0}}<\frac12.
\]

令 \(q=\sqrt{1+b/D_0}\)，其最大值为

\[
\Lambda_{\max}
=(\eta-1)\frac{q-1}{q+1}.
\]

因此，在某个平台渗透阶段出现地方收入边际下降的必要且充分条件是 \(\Lambda_{\max}>\varepsilon\)。

经济含义是：平台替代造成的**边际收入拖累**通常在平台仍处于快速替代传统渠道的阶段最强，而不是平台已经完全占优之后。随着平台份额继续提高，可被替代的传统渠道变少，边际渠道重组效应下降。这里不能写成“总漏出在中间阶段最大”：累计留值损失 \(\rho_A-\omega=\Delta\rho s\) 随平台份额单调增加；\(\Lambda(1)=0\) 只是因为进一步降价不再引起渠道迁移。

这个推论适合形成论文唯一的示意图，也可能成为标题或摘要中的第二个结果。

### 推论 3：平台收益的空间归属具有纯收入效应

可将平台渠道的本地留值率写成

\[
\rho_P=\delta+\lambda\kappa,
\]

其中 \(\delta\) 是本地履约收入份额，\(\kappa\) 是平台佣金或租金份额，\(\lambda\in[0,1]\) 表示其中有多少归本地所有者或被返还本地。

在保持平台价格 \(p_P\) 不变时，提高 \(\lambda\) 不改变价格指数和渠道份额，但会提高 \(\rho_P\)、降低 \(\Delta\rho\)，从而提高地方收入和消费等价实际收入。当 \(G=0\) 时，

\[
\frac{\partial\ln V}{\partial\lambda}
=
\frac{\alpha s\kappa}{1-\beta-\alpha\omega}>0.
\]

这是一个纯粹的空间收入归属结果。考虑到篇幅，它可以只作为一句推论或机制关闭实验，不必在正文展开政策讨论。

命题 2 和后续边际阈值均明确设定 \(G=0\)。当 \(G>0\) 时，\(B\) 与 \(\omega G\) 会同时随冲击变化，不能直接使用 \(\varepsilon-\Lambda(s)\) 的简化式；\(G\) 在正文中只用于定义命题 1 的外部支出乘数。

---

## 六、机制关闭与示意性反事实

本文不做经验校准，也不做 Shapley 分解。为了说明机制，最多报告以下五个开关：

1. **关闭空间留值差：** 令 \(\Delta\rho=0\)。此时市场一体化只产生外部市场准入和价格收益；
2. **关闭渠道替代：** 令 \(\eta\to1\)，平台效率变化不再大幅重配渠道份额；
3. **关闭外部市场准入：** 令 \(\varepsilon=0\)，只考察消费价格与收入漏出；
4. **关闭递归传播：** 为保持冲击前均衡不变，使用
   \[
   Y_1^{\mathrm{no\ rec}}
   =B_1+\beta Y_0+\omega_1(\alpha Y_0+G),
   \]
   与完整固定点比较；不要简单令 \(\alpha=0\) 或 \(\beta=0\)，因为那会同时改变基准均衡与消费结构；
5. **平台租金本地化：** 在保持 \(p_P\) 不变时提高 \(\rho_P\) 或 \(\lambda\)，识别纯粹的空间所有权效应。

正文只需要展示前三个或四个。其余结果可以放在一页在线附录或代码中。

---

## 七、示意图与数值例子

### 7.1 唯一主图

建议只放一张两面板图：

- **Panel A：** 横轴为平台份额 \(s\)，画出边际收入拖累 \(\Lambda(s)\)、外部市场准入线 \(\varepsilon\) 和实际收入阈值 \(\varepsilon+\alpha s\)，直观显示三个结果区域；
- **Panel B：** 画出完整模型、\(\Delta\rho=0\)、无递归反馈和 \(\varepsilon=0\) 时的名义收入或消费等价实际收入变化，用于说明机制。

图中所有参数必须标注为 illustrative，不使用 calibrated、estimated 或 quantitative magnitude 等表述。

### 7.2 一个可用于检查非空区域的示例

可以暂用以下参数做代数和代码检查：

\[
\alpha=0.35,\quad
\beta=0.30,\quad
\eta=4,\quad
\rho_A=0.45,\quad
\rho_P=0.10,\quad
s=0.30.
\]

此时

\[
\omega=0.345,
\qquad
D\approx0.579,
\qquad
\Lambda(s)\approx0.133,
\qquad
\alpha s=0.105.
\]

于是：

- 若 \(\varepsilon=0.15\)，名义收入和消费等价实际收入均提高；
- 若 \(\varepsilon=0.05\)，名义收入下降但消费等价实际收入提高；
- 若 \(\varepsilon=0\)，二者均下降。

这只用于证明三个参数区域都非空，不能被描述为中国的现实参数。

---

## 八、论文结构与英文篇幅

官方要求下，内部应把摘要至结论控制在约 1,850—1,900 词，为公式、图注和最终修改留出空间。

| 部分 | 内容 | 目标词数 |
|---|---|---:|
| Abstract | 问题、机制、两个结果 | 80—95 |
| 1. Introduction | 现实问题、文献缺口、贡献 | 330—380 |
| 2. Model | 偏好、渠道、留值、收入闭合 | 600—650 |
| 3. Results | 两个命题、一个推论、主图 | 650—700 |
| 4. Conclusion | 一般含义与边界 | 120—150 |

不设置独立的 literature review、institutional background、calibration、policy discussion 或 robustness 章节。证明能在几行内完成的紧跟命题；机械代数放在简短附录。不要假设附录自动排除在 2,000 词限制之外。

### 8.1 暂定英文标题

首选：

> **Platform Intermediation and Local Multipliers**

备选：

> **Market Integration, Platform Intermediation, and Local Value Capture**

更强调反直觉结果的备选：

> **Cheaper Platform Access and Weaker Local Income**

### 8.2 Introduction 的叙事主线

Introduction 不应从“平台佣金流向总部”这一未经单独建模的断言开始，而应从更一般、也更容易由现有证据支持的价格—收入分离事实开始：

> Recent evidence shows that retail and e-commerce integration can lower the cost of living without generating comparable gains in local income (Atkin et al., 2018; Couture et al., 2021). Existing studies quantify consumer-access gains and direct income effects, while the local-multiplier literature emphasizes how initial income shocks propagate through local demand. We connect these two perspectives. When integration shifts expenditure toward a channel with lower local factor-income content, the local retention share falls in every round of spending. The resulting effective multiplier is \(\mathcal M(\omega)=\omega/(1-\beta-\alpha\omega)\). Integration can consequently lower local nominal income even when consumer prices fall. Closed-form thresholds determine whether nominal and consumption-equivalent real income both rise, move in opposite directions, or both fall.

这一叙事必须遵守三条边界：

1. 对 Couture et al. 使用 “provides a mechanism consistent with” 或 “rationalizes”，不用 “resolves”；
2. 对 Atkin et al. 强调“已有直接收入分解、缺少递归收入闭合”，不用“纯消费侧部分均衡”；
3. 对 Moretti 强调“借用地方需求传播思想”，不把本文公式归为对 Moretti 公式的机械修正。

### 8.3 暂定英文摘要

> We study a small region where integration expands external market access and shifts household spending toward a lower-cost platform channel with lower local factor-income content. Endogenous channel choice makes the local retention share enter every round of expenditure. We show that the effective local multiplier is more sensitive to retention than a first-round adjustment implies. Closed-form thresholds separate three outcomes: nominal and consumption-equivalent real income both rise, nominal income falls while real income rises, or both fall. The marginal income drag from channel substitution is strongest during intermediate platform penetration.

### 8.4 暂定 highlights

- Platform integration may lower local income despite cheaper access.
- Local retention enters every round of the spending multiplier.
- Real income depends on retention, substitution, and outward market access.
- Marginal channel-reallocation drag peaks at intermediate penetration.

### 8.5 关键词与 JEL

**Keywords：** platform intermediation; market integration; local multipliers; value capture; spatial incidence  
**JEL：** F15; L81; R11; R12

---

## 九、45 天执行计划与两人分工

### 第 1 周：2026 年 7 月 14—20 日

**目标：创新性和模型冻结。**

交付物：

- 10—15 篇最接近文献的对照矩阵；
- 一页 research question memo；
- 完整符号表；
- 两个命题及其证明草稿；
- 100 词以内摘要。

第 3 天冻结研究问题；第 7 天冻结模型。此后不得加入税收、迁移、企业选址或平台最优定价。

### 第 2 周：7 月 21—27 日

**目标：数学内容冻结。**

交付物：

- 唯一均衡证明；
- 命题 1、命题 2 和阶段性推论；
- \(\rho_P\geq\rho_A\) 的反向情况；
- 极限情况：\(\Delta\rho=0\)、\(\eta\to1\)、\(\varepsilon=0\)；
- 另一位作者在不看原证明的情况下独立复推。

第 14 天冻结数学内容，之后只修正错误，不增加主命题。

### 第 3 周：7 月 28 日—8 月 3 日

**目标：图、代码和初稿骨架。**

交付物：

- 一张两面板图；
- 参数网格与有限差分检查；
- 机制关闭结果；
- 可重复运行代码与简短 README；
- Introduction 和 Model 的英文初稿。

### 第 4 周：8 月 4—10 日

**目标：形成完整 v1 并获得外部反馈。**

交付物：

- 1,900—2,200 词的完整英文 v1；
- 向一位空间/城市经济学研究者和一位平台/产业组织研究者各做一次 15 分钟报告；
- 记录他们对“是否显然”“是否已有文献”“闭合是否可信”的反馈。

第 28 天冻结章节结构和图形。

### 第 5 周：8 月 11—17 日

**目标：模拟审稿和科学内容冻结。**

两位作者分别写一页拒稿式 referee report：

- 模型负责人攻击闭合、证明和比较静态；
- 论文负责人攻击创新、文献定位和过度声称。

根据报告完成 v2，并将正文压到约 1,900 词。第 35 天 science freeze。

### 第 6 周：8 月 18—24 日

**目标：完成投稿包。**

交付物：

- 主文和证明附录；
- LaTeX、BibTeX、独立图文件；
- 代码、README 和参数表；
- 100 词以内摘要；
- 3—5 条 highlights；
- cover letter；
- funding、competing interests、data/code availability 与 AI-assisted writing 声明；
- 与后续大项目的边界和相关稿件披露。

第 42 天冻结投稿包。

### 8 月 25—28 日：上传与正式提交

- 两位作者分别逐页校读；
- 完成投稿系统 dry run；
- 检查系统生成 PDF 的公式、作者信息、图形和参考文献；
- 只修复上传问题，不再重写模型；
- 8 月 28 日正式提交。

### 建议分工

| 工作 | 模型负责人 | 论文负责人 |
|---|---|---|
| 方程与证明 | 首次推导和整理 | 独立复推、找反例 |
| 数值图 | 代码、参数网格 | 经济解释、避免过度声称 |
| 文献 | 核对模型来源 | 最近近邻文献矩阵 |
| 写作 | Model、Appendix | Introduction、Results、Conclusion |
| 投稿 | 代码和复现材料 | 格式、声明、cover letter |

全程只由一位作者维护主 TeX 文件。每周安排一次 45 分钟决策会和一次 20—25 分钟进度会。第 7 天以后，任何新增机制必须以删除另一个机制为条件。

---

## 十、首周文献核验与停止条件

**当前状态（2026-07-14）：** 暂定通过，可以同步推进模型证明和英文写作；尚未达到可以公开声称“无直接竞争者”的程度。最终核验必须保留可审计的检索和排除记录。

### 10.1 必须重点查找的六类近邻文献

1. **区域投入产出与重复进口漏出**  
   检索词：regional income multiplier, import leakage, recursive local spending, regional input-output multiplier。

2. **地方所有权与本地乘数**  
   检索词：local ownership multiplier, locally owned firms, profit repatriation, local income retention。

3. **电子商务的空间收入归属**  
   检索词：e-commerce local employment, online retail local income, platform headquarters profits, spatial incidence of e-commerce。

4. **平台交易与地方福利**  
   检索词：platform trade local welfare, digital intermediation regional inequality, platform rent geography, online marketplace spatial equilibrium。

5. **连锁零售、外来所有权与利润汇回**

   检索词：chain store entry local income, foreign ownership profit repatriation regional multiplier, retail ownership local employment。

6. **平台佣金与空间收入归属**

   检索词：platform commission spatial incidence, marketplace fees local economy, digital platform rents regional income。

除关键词检索外，必须完成 Atkin et al.、Couture et al.、Fan et al.、Moretti 和 Goldmanis et al. 的前向—后向引文核查，并覆盖期刊论文与最新工作论文。

文献矩阵至少记录：研究问题、渠道选择是否内生、是否区分本地与外部收入、是否有递归乘数、是否有实际收入或福利阈值、平台收费是否内生、本文与其差异及排除理由。只有保留逐篇记录，才能支持 “to our knowledge” 的创新性表述。

### 10.2 Kill criteria

以下“停止”是指停止独立投 EL，并把结果并回大论文，而不是放弃整个研究方向。

- **Day 3：** 无法用两句话说明相对最近文献的新结果，暂停建模并重做定位；
- **Day 7：** 核心模型超过两个渠道、一个地区加外部经济、两个主要命题，立即删减；
- **Day 10：** 已有论文完整包含“内生平台份额 + 递归地方留值 + 同一福利阈值”，停止独立 EL；
- **Day 14：** 结果仍然只是 \(Y=m\omega X\) 的会计表达，停止独立 EL；
- **Day 18：** 三个结果区域只能依赖极端或不允许的参数，停止 EL；
- **Day 35：** 两位外部读者都认为结果显然或贡献无法识别，不仓促投稿；
- **大项目边界：** 如果发表 Letter 会使后续模型加实证论文失去主要理论新意，则不拆分。

---

## 十一、主要审稿风险及预先回应

### 风险 1：这是教科书式乘数或区域投入产出恒等式

**回应：** 论文不能只展示乘数公式。贡献必须来自平台份额的内生变化、留值率的递归作用、实际收入阈值以及边际渠道替代拖累在中间平台份额达到最大值。首周必须系统核对区域投入产出与地方所有权文献。

### 风险 2：\(\rho_A>\rho_P\) 直接预设平台有害

**回应：** 用渠道生产成本份额微观化 \(\rho_c\)，把 \(\rho_A>\rho_P\) 写成可检验条件，并明确给出 \(\rho_P\geq\rho_A\) 时平台效率提高名义收入和消费等价实际收入的反向结果。

### 风险 3：地方收入固定点缺乏资源约束

**回应：** 明确把模型解释为短期小型开放地区均衡：本地支出购买本地生产的服务，本地服务在固定外部机会成本下弹性供给，外部商品和总部收入形成漏出。完整工资、迁移和住房调整不属于本文。

### 风险 4：Faber 式 \(B(z)\) 过于简化

**回应：** 在附录用外部 CES 需求给出 \(B'(z)/B(z)=\varepsilon\) 的最小推导。该项只表示 outward market access，不承担生产区位结论。

### 风险 5：平台产业组织内容不够丰富

**回应：** 本文研究的不是平台最优收费，而是既定交易技术下的平台收入归属。佣金和所有权外生是有意的边界，而不是遗漏。内生平台定价属于另一篇论文。

### 风险 6：缺少数据和现实量级

**回应：** 本文是纯理论 Letter。数值图只证明参数区域非空，不声称校准。任何关于中国现实量级的判断留给后续经验论文。

---

## 十二、数据、代码与投稿材料

本项目不收集原创数据，不估计参数，也不进行政策量化。投稿时的数据声明可写为：

> No data were used for the research described in this article.

若公开图形代码，可增加：

> The code used to reproduce the illustrative results is available at [repository].

代码至少应包括：

- 参数合法性检查；
- 解析导数与有限差分的比对；
- 三个结果区域的参数网格；
- 主图生成脚本；
- README 和参数表。

按当前 *Economics Letters* 投稿指南，需准备：不超过 100 词的摘要、1—7 个关键词、最多 6 个 JEL codes、单独的 highlights 文件（3—5 条，每条不超过 85 个字符）、可编辑的 Word 或 LaTeX 源文件，以及 data-availability statement。若 AI 工具被用于文献综合、内容组织或稿件撰写，应按出版社规则披露，并由作者逐项核对所有方程、文献和表述。

---

## 十三、需要两位作者共同拍板的六个问题

1. **是否同意把 Atkin 型渠道选择作为母框架，而不使用 Faber 的完整生产区位模型？**
2. **是否同意把 Letter 的唯一理论对象固定为“递归地方留值”，将税收、企业迁移和 NSE 全部留给大论文？**
3. **是否保留 \(B(z)\) 的 outward market-access 项？** 保留它可以完整呈现三种结果区域；删除它会使模型更短，但地方收入在 \(\rho_A>\rho_P\) 时基本单向下降。
4. **主结果应强调哪一个？** 备选为“名义收入下降但实际收入提高”“价格下降但实际收入仍下降”或“边际渠道替代拖累在平台过渡期最大”。同时需要决定正文使用更严格的 resident real income，还是在补充劳动机会成本假设后使用 welfare。
5. **未来大论文能否在引用本 Letter 后，仍凭借数据、识别和多地区 GE 独立成立？**
6. **两人是否能够在前两周各投入至少 8—10 个专注小时，并严格执行 Day 7 模型冻结？**

建议合作者会议先讨论这六个问题。只要第 1—3 项达成一致，模型推导和英文初稿即可立即并行推进。

---

## 参考文献（项目阶段核心清单）

[Atkin, D., Faber, B., & Gonzalez-Navarro, M. (2018). Retail globalization and household welfare: Evidence from Mexico.](https://www.nber.org/papers/w21176) *Journal of Political Economy*, 126(1), 1–73.

[Couture, V., Faber, B., Gu, Y., & Liu, L. (2021). Connecting the countryside via e-commerce: Evidence from China.](https://www.aeaweb.org/articles?id=10.1257/aeri.20190382) *American Economic Review: Insights*, 3(1), 35–50.

Faber, B. (2014). Trade integration, market size, and industrialization: Evidence from China's National Trunk Highway System. *Review of Economic Studies*, 81(3), 1046–1070. https://doi.org/10.1093/restud/rdu010

Fan, J., Tang, L., Zhu, W., & Zou, B. (2018). The Alibaba effect: Spatial consumption inequality and the welfare gains from e-commerce. *Journal of International Economics*, 114, 203–220. https://doi.org/10.1016/j.jinteco.2018.07.002

[Goldmanis, M., Hortaçsu, A., Syverson, C., & Emre, Ö. (2010). E-commerce and the market structure of retail industries.](https://www.nber.org/papers/w14166) *Economic Journal*, 120(545), 651–682.

[Moretti, E. (2010). Local multipliers.](https://www.aeaweb.org/articles?id=10.1257/aer.100.2.373) *American Economic Review*, 100(2), 373–377.

Economics Letters. Guide for Authors. https://www.sciencedirect.com/journal/economics-letters/publish/guide-for-authors

---

## 最终压缩版

这篇 Letter 只需要证明一件事：

> **平台化市场整合会同时改善消费价格、扩大外部市场准入并改变交易收入的空间归属。当平台渠道比传统渠道保留更少的本地要素收入时，留值损失会在每一轮地方支出中重复发生，从而内生削弱地方乘数，并在可解析的参数条件下造成地方名义收入下降，甚至反转居民的消费等价实际收入。**

基于截至 2026 年 7 月 14 日的暂定文献核验，这一命题可以进入模型和投稿开发；但在完成相邻概念、前向—后向引文及工作论文核查前，不应把“无直接竞争者”写入论文或对外材料。若两位作者同时同意与后续大论文严格分工，该项目适合继续按 45 天计划推进并投向 *Economics Letters*。
