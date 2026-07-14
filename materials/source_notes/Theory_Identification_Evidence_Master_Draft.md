# 《统一市场、平台化与地方乘数：价值捕获的空间重组》
## Theory + Identification + Evidence Narrative Master Draft

## 0. 本稿的用途与定位

这不是一份给代码助手执行的 technical memo，也不是一份已经可以直接投稿的 polished draft。它是一份**论文内部讨论稿**：用于把目前项目最核心的智识骨架完整地搭起来，并为后续的 introduction、theory section、empirical strategy、results narrative 乃至 appendix 中的 formal derivation 提供统一底稿。

这份稿子的任务，不是把所有细节都定死，而是把以下三个层次打通：

1. **理论层**：这篇文章到底在重写什么对象；
2. **识别层**：经验部分究竟要识别什么，而不识别什么；
3. **叙事层**：图表与证据链如何为理论与识别服务，而不是零散堆叠结果。

全文必须始终守住四个中心句：

- 统一市场降低空间摩擦；
- 平台化改变价值归属；
- 地方发展取决于 retained value，而不只是 local spending；
- 因而 effective local multiplier 不是传统意义上的 local multiplier，而是一个由本地留值率重写过的对象。

如果用一句更浓缩的话来概括本文的理论主张，那就是：

> **在统一市场与平台化并行推进的条件下，市场接入（access）与地方价值捕获（capture）不再是同一个对象；地方乘数因而必须被重写为 retained value 的函数。**

这也是本文能够从普通“中国县域政策论文”提升为 EJ 目标论文的关键。

---

## 1. 这篇文章真正的问题是什么

### 1.1 不是“统一市场是否促进发展”

如果把文章问题写成“统一市场是否促进县域发展”，文章会迅速滑向普通政策评估：你只需要给出一个平均处理效应，最多再补一点异质性。这种写法并不要求你提出新的理论对象，也不要求你与地方乘数文献、空间经济学文献和平台文献同时对话。

但本文真正的问题更强，也更一般：

> **在统一市场与平台化同步加深时，为什么价值创造地与价值捕获地会发生空间脱钩；这种脱钩为什么会改写地方乘数；为什么不同地区会系统性地表现出 access gains 主导或 leakage 主导的不同结果？**

这一定义立刻改变了文章的层级。因为它要求你回答的不是“有没有影响”，而是：

- 影响究竟通过什么对象传导；
- 为什么传统的 local multiplier 语言不够了；
- 为什么相同的市场整合冲击会在不同地区产生截然不同的地方发展后果。

### 1.2 不是“平台抽成导致地方受损”

如果把问题写成“平台抽成伤害地方经济”，则又会把文章写窄。平台当然可能抽取佣金、广告费、技术服务费，但平台更根本的作用不是“拿走一部分钱”，而是**重新组织交易**。在一个平台化、跨区域组织高度发达的经济里，一笔原本在地方内部完成的交易，会被拆分成多个空间节点：

- 消费发生在本地；
- 卖家可能在外地；
- 平台可能在外地；
- 结算和利润确认也可能在外地；
- 本地只留下履约、配送和少量末端服务收入。

因此，平台化在本文中不是一个“坏行为”，而是一种 **organizational technology**：

- 它降低匹配和交易成本；
- 它扩大市场接入；
- 它也改变 surplus 的空间分配。

### 1.3 真正被重写的理论对象：地方乘数

本文最需要 formalize 的命题，不是“平台会改变分配”，而是：

\[
\widetilde m_i = m_i \omega_i
\]

其中：

- \(m_i\) 是地方非贸易部门的“纯”本地收入传播能力；
- \(\omega_i\) 是本地支出中最终被保留为本地工资、利润和税基的份额；
- \(\widetilde m_i\) 是我们真正观察到的、对地方发展有意义的**有效地方乘数**。

只要这个式子立住，整篇文章的理论层级就出来了。因为它意味着：

1. 地方乘数不再是纯需求传导对象；
2. 地方乘数取决于价值是否留在本地；
3. 统一市场的地方后果不能仅凭 access gains 判断；
4. 平台化的核心不是价格本身，而是 **value attribution**。

---

## 2. 为什么现有文献还没有把这个问题说透

### 2.1 传统地方乘数文献的隐含前提

传统 local multiplier 文献的直觉是：一轮新增收入会转化为本地非贸易部门的进一步扩张，从而形成后续轮次的收入传播。但这套逻辑隐含了一个强前提：

> **初始支出与第一轮收入形成大体发生在同一地方。**

在本地零售、本地服务、本地经营者主导的环境中，这个近似是合理的。但在平台化环境中，同一笔地方消费可能对应外地卖家、外地平台、外地结算、本地薄履约。因此，本地支出不再自动构成本地收入的起点。

换言之，传统文献默认的是：

> local spending \(\approx\) first-round local income.

而本文要指出，这个近似在统一市场与平台化并行推进的条件下被系统性打破了。

### 2.2 空间经济学文献的不足

空间经济学擅长讲：

- market access；
- trade costs；
- core-periphery；
- real wages；
- 人口和企业在空间上的再分布。

但它通常不细分同一笔交易内部的价值归属环节。它关心商品如何在空间上流动，却较少把问题明确写成：

> **同一笔发生在 P 地的支出，究竟有多少形成 P 地的工资、利润和税基？**

这不是经典贸易流问题，而是 **spatial incidence of value capture**。本文正是在这里接上平台组织与地方发展。

### 2.3 平台文献的不足

平台文献擅长分析：

- 双边市场；
- 抽成与收费结构；
- 搜索、排序与匹配；
- 网络效应与规则设计。

但它通常不把问题写成地方发展命题，更少系统性地问：

> **平台化如何改变地方乘数的底层结构？**

本文的推进正在于此：把平台中介与 local development incidence 接起来，把“交易如何被组织”翻译成“地方发展如何被重写”。

---

## 3. 理论部分应当从什么现实观察出发

理论部分开头最重要的不是立即上方程，而是先明确：在平台化统一市场里，一笔交易至少涉及五个地点。

- 消费地 \(l^c\)
- 经营地 \(l^b\)
- 结算地 \(l^s\)
- 纳税地 \(l^t\)
- 就业地 \(l^e\)

在传统线下本地零售环境中，这五个地点高度重合，所以地方支出近似等于地方收入形成的起点。

但在平台化统一市场中，完全可能出现如下拆分：

- 消费发生在县 A；
- 商家主体注册在市 B；
- 平台总部在市 C；
- 支付与结算在市 D；
- 税基与利润确认主要记在 C/D；
- 县 A 只留下末端配送和少量服务就业。

于是，“本地花钱”与“本地形成收入”之间不再是恒等关系。

这一步极其关键。因为它告诉读者：本文不是在做一个抽象的模型游戏，而是在 formalize 一种已经广泛发生、但尚未被系统概念化的组织变迁。

---

## 4. 最小模型：两地区、三类主体、一个关键状态变量

### 4.1 模型类型

本文最准确的理论标签，不是宏观模型，也不是标准贸易模型，而是：

> **一个带有平台中介的空间地方乘数 / 空间 incidence 模型。**

它位于三类文献的交叉处：

- local multiplier；
- spatial economics；
- platform intermediation。

它不是三者任何一个的简单应用，而是把三者拼接成一个新的命题：

> market integration 改变 access；platformization 改变 attribution；local development 取决于 retention。

### 4.2 两地区设定

设经济中有两个地区：核心区 \(C\) 与外围区 \(P\)。

这个两地区设定已经足够容纳你需要的全部机制：

- 交易摩擦下降；
- 平台组织跨地区交易；
- 利润、结算和税基向核心集中；
- 地方乘数依赖留值率。

第一版完全不需要多地区网络，更不需要 full spatial GE。

### 4.3 三类主体/部门

至少保留三类对象：

1. **可贸易品供给者**：可以位于 C 或 P；
2. **本地非贸易部门**：其扩张决定地方乘数；
3. **平台/中介部门**：负责匹配、流量、支付和交易组织，且可能集中于 C。

### 4.4 关键状态变量：本地留值份额

设外围地区 P 的总消费支出为 \(X_P\)。定义本地 retained value share 为：

\[
\omega_P = \omega(S_P,R_P,D_P,T_P,\tau)
\]

其中：

- \(S_P\)：供给能力；
- \(R_P\)：留值能力；
- \(D_P\)：平台依赖；
- \(T_P\)：数字适应能力；
- \(\tau\)：统一市场下的空间摩擦 / 交易成本。

这里最关键的建模思想是：

> **\(\omega_P\) 不是会计恒等式，而是一个内生状态变量。**

这一步把“value capture”从叙事词语变成模型对象。

---

## 5. 从支出到 retained value：第一组推导

定义外围地区 P 的 retained value 为：

\[
RV_P = \omega_P X_P
\]

相应地，地方价值外流为：

\[
Leak_P = (1-\omega_P)X_P
\]

这个定义虽然简单，但有三层重要含义。

第一，所谓“地方需求”被拆成了两部分：

- 创造本地收入的部分；
- 被组织性地转移到外部的部分。

第二，leakage 不是误差项，而是结构项。它不是没观测到的残差，而是整篇文章要研究的对象。

第三，平台化影响的不只是 \(X_P\) 的水平，更是 \(\omega_P\) 的大小。同样一笔本地消费，在不同的交易组织模式下，留在本地的价值份额可以完全不同。

---

## 6. 为什么地方乘数必须被重写：第二组推导

设本地非贸易部门的“纯”乘数为 \(m_P\)。它表示：一单位本地初始收入形成，会在本地引起多少后续轮次的收入扩张。

于是地方总收入可写为：

\[
Y_P = A_P + m_P \cdot RV_P
\]

即：

\[
Y_P = A_P + m_P\omega_P X_P
\]

其中 \(A_P\) 为外生初始收入或与该机制无关的收入基底。

于是，可定义真正与地方发展相关的**有效地方乘数**：

\[
\widetilde m_P = m_P\omega_P
\]

这一步就是全文最关键的理论重写。

### 6.1 为什么这不是定义游戏

表面上看，这似乎只是把一个乘数和一个份额乘起来。但这种看法只有在 \(\omega_P\) 被当作一个外生 accounting share 时才成立。

在本文里，\(\omega_P\) 不是固定常数。它是统一市场、平台化组织方式、地方供给结构和地方捕获能力共同决定的内生对象。因此：

- 它会随着 integration 和 platformization 的推进而变化；
- 它在地区间系统性不同；
- 它正是 access 不能自动转化为 development 的机制所在。

因此，\(\widetilde m_P = m_P\omega_P\) 不是简单重命名，而是对 local multiplier 的结构性修正。

### 6.2 与传统文献的区别

传统文献的隐含逻辑是：

> local spending → local income → local service expansion.

本文的重写则是：

> local spending → retained local value → local income propagation.

这不是同一个对象。

---

## 7. 一体化净效应的分解：第三组推导

统一市场推进可以被写成交易摩擦下降，即 \(\tau \downarrow\)。它同时影响两件事：

1. 本地获得的市场接入和交易规模 \(X_P\)；
2. 本地留值份额 \(\omega_P\)。

于是：

\[
Y_P = A_P + m_P\omega_P X_P
\]

对 \(\tau\) 求导，有：

\[
\frac{dY_P}{d\tau}
= m_P\left(\omega_P\frac{\partial X_P}{\partial \tau} + X_P\frac{\partial \omega_P}{\partial \tau}\right)
\]

若把一体化理解为 \(\tau\) 的下降，则其地方净效应应分解为：

- **access effect**：更低摩擦扩大交易和可达性，提高 \(X_P\)；
- **leakage effect**：更低摩擦也可能使外部主体更容易穿透本地需求，从而降低 \(\omega_P\)。

因此，统一市场的地方净效应并不由 access gains 单独决定，而取决于：

> **市场接入增加得有多快，以及价值捕获流失得有多快。**

这正是本文异质性命题的理论核心。

---

## 8. 地区异质性：为什么有些地方是 access 主导，有些地方是 leakage 主导

比较两个外围地区 \(P_1\) 与 \(P_2\)。若：

- \(S_{P_1} > S_{P_2}\)；
- \(R_{P_1} > R_{P_2}\)；
- \(D_{P_1} < D_{P_2}\)；
- \(T_{P_1} > T_{P_2}\)；

则合理推断：

\[
\omega_{P_1} > \omega_{P_2}
\]

且当 \(\tau \downarrow\) 时，\(P_1\) 更可能把 access gains 转化为本地收入，而 \(P_2\) 更可能主要经历 leakage。

这就把文章从“平均效应”推进到“地方 incidence”问题：

> **相同的一体化冲击，为什么在不同地区穿过不同结构后，形成不同的有效地方乘数？**

这正是经验部分应当识别的对象。

---

## 9. 新结构经济学应嵌在什么位置

### 9.1 不应写成表层标签

不能把文章写成“建立一个新结构经济学模型来研究统一市场”。那样会迅速缩窄文章的对话对象，降低 general-interest positioning。

### 9.2 应作为 \(\omega_i\) 的深层生成机制

更自然的写法是：地方供给能力 \(S_i\) 与留值能力 \(R_i\) 并不是黑箱，它们更深层地受到当地要素禀赋结构、适宜产业组织、基础设施和制度能力的共同影响。

可写为：

\[
S_i = S(E_i,O_i,G_i)
\]

\[
R_i = R(E_i,O_i,G_i,L_i)
\]

其中：

- \(E_i\)：要素禀赋结构；
- \(O_i\)：与禀赋匹配的产业与组织形式；
- \(G_i\)：交通、仓配、数字基础设施等关键公共投入；
- \(L_i\)：本地服务链接和商贸网络。

进一步可定义：

\[
C_i = \text{congruence between endowments and production-organization system}
\]

然后写成：

\[
\omega_i = \omega(C_i,D_i,T_i,\tau_i)
\]

这意味着 NSE 在本文中的作用是解释：

- 为什么有些地方更能把 access 变成 capture；
- 为什么异质性不是随机噪声；
- 为什么政策含义应是赋能式建设，而不是恢复地方保护。

### 9.3 这一步的学术分寸

这样写时，NSE 是深层解释语言，而不是表层标签。它不会拉低 EJ 档次，反而会增加异质性命题的结构深度。

---

## 10. 理论部分至少需要推出哪些 proposition

建议至少 formalize 四个命题：

### Proposition 1: Integration improves access.
在其他条件不变时，\(\tau\downarrow\) 提高 market access，扩大交易规模与选择集，并倾向于提高 \(X_P\)。

### Proposition 2: Integration may reduce retention under platform dependence.
当地区平台依赖高、留值能力低时，\(\tau\downarrow\) 可能降低 \(\omega_P\)，或至少使其上升远慢于 \(X_P\)。

### Proposition 3: The effective local multiplier depends on retention.
地方收入对本地支出的响应不是 \(m_P\)，而是 \(m_P\omega_P\)。因此，相同需求冲击在不同地区产生不同地方发展后果。

### Proposition 4: Structural congruence determines whether access translates into development.
高 congruence 地区更可能是 access 主导；低 congruence 地区更可能是 leakage 主导。

只要这四个命题立住，理论部分就已经足够支撑一篇 EJ 级别文章的核心 contribution。

---

## 11. 经验部分究竟要识别什么

经验部分最大的陷阱，是构造某种“县级统一市场推进度指数”，再用它去解释地方发展结果。这个做法的问题在于：

1. 概念上混杂，把规则统一、交易摩擦、平台渗透和结果表现混在一起；
2. 识别上循环，容易把 outcome 塞回 treatment；
3. 解释上失效，无法区分 access 改善、platform adoption、城市吸附和一般趋势。

因此，经验部分必须放弃“地方统一市场推进度”的念头。

真正需要识别的是：

> **当 integration 与 platformization shock 到来时，哪些地方能够把 access gain 变成本地 retained value，哪些地方则主要发生 value leakage？**

这意味着经验对象不是“shock 有没有平均效果”，而是：

> **shock 如何穿过既有地方结构，作用于 \(\omega_i\) 与 \(\widetilde m_i\)。**

这就决定了主规格必须是 **shock × pre-determined structure**。

---

## 12. 理论对象与经验对象的一一映射

理论部分的核心式子是：

\[
Y_i = A_i + m_i\omega_i X_i
\]

经验部分当然无法直接观测每一个结构参数，但必须建立清晰的 proxy 体系。

### 12.1 Shock 对应什么

shock 不是结果，而是外部或制度性变化，能够独立改变：

- 交易摩擦；
- 平台渗透；
- 跨地成交可能性；
- 物流、支付和流通可达性。

理论上至少可以区分两类：

- **integration shock**：交通、物流、规则统一、跨区流通便利化；
- **platformization shock**：电商平台扩张、即时零售进入、支付结算体系扩展。

第一版经验设计最好先把最强、最干净的一类 shock 做透，而不是同时铺太大。

### 12.2 Structure 对应什么

structure 是预定异质性，决定 shock 到来时地方是 access 主导还是 leakage 主导。至少应拆成三类：

1. **Supply capacity**：本地可贸易供给基础、产业带基础、组织化供给能力、履约与仓配能力；
2. **Retention capacity**：本地主体密度、本地服务业嵌入度、本地工资份额、税基本地化能力、本地结算和金融服务能力；
3. **Platform dependence / digital intermediation exposure**：本地对外部平台、外部卖家、外部结算与跨地经营的依赖程度。

数字适应能力 \(T_i\) 很重要，但更适合作为补充机制，而不应替代 supply / retention / dependence 三主轴。

### 12.3 Outcomes 应如何分层

经验结果不能一上来就是 GDP、居民收入、夜间灯光。必须形成分层证据链。

**第一层：最靠近 retained value 的主结果**

- 本地商户进入/退出；
- 本地零售和本地服务就业；
- 本地经营性收入；
- 税基 proxy；
- 本地工资收入 proxy；
- retained value proxy。

**第二层：机制变量**

- 外部卖家 penetration；
- 外部结算比重；
- 平台依赖度变化；
- 本地履约份额；
- 价格与品种变化。

**第三层：消费者福利与 access gains**

这一层的作用是证明：

- access 的确改善了；
- 因此“本地收入没有同步改善”不能解释为“没有整合”。

**第四层：宏观辅助结果**

- 夜间灯光；
- GDP；
- 居民收入。

它们有用，但不应成为文章第一证据。

---

## 13. 为什么主方程必须是 shock × structure

平均效应回归当然可以作为 baseline，但绝不应成为文章中心。设你估：

\[
Y_{it} = \beta Shock_{it} + \mu_i + \tau_t + \varepsilon_{it}
\]

即便 \(\beta\) 显著，你也只能说 shock 平均上与结果相关，完全无法区分：

- 是 access gain 主导；
- 还是 leakage 主导；
- 是否某些地区受益、某些地区受损，平均后接近零；
- 也无法解释为什么不同地方不同。

但本文真正的价值恰恰是解释“为什么不同地方不一样”。因此更自然的主规格应为：

\[
Y_{it} = \beta Shock_{it} + \theta_1 Shock_{it}\times Supply_i + \theta_2 Shock_{it}\times Retention_i + \theta_3 Shock_{it}\times PlatformDep_i + \mu_i + \tau_t + X'_{it}\Gamma + \varepsilon_{it}
\]

若有更丰富的控制，也可扩展为：

\[
Y_{it} = \beta Shock_{it} + \sum_k \theta_k Shock_{it}\times Structure_i^k + \mu_i + \tau_t + \lambda_{pt} + \varepsilon_{it}
\]

这里真正重要的不是公式形式，而是其经济学含义：

- \(\beta\) 捕捉 shock 的平均影响；
- \(\theta_k\) 捕捉的是 \(\widetilde m_i\) 的异质性；
- 文章真正的核心在 \(\theta_k\)，而不在 \(\beta\)。

系数解释也很清楚：

- 若 \(\theta_1>0\)，说明供给能力高的地区更能把 shock 转化为本地生产与收入；
- 若 \(\theta_2>0\)，说明留值能力高的地区更能留下交易剩余；
- 若 \(\theta_3<0\)，说明平台依赖越强，shock 越可能表现为 leakage 而非 local development。

这与理论中的 \(\omega_i\) 与 \(m_i\omega_i\) 完整对应。

---

## 14. 固定效应、比较组与识别闭合

固定效应的目标不是“技术上更稳”，而是逼近你真正关心的 counterfactual。最基本地，至少应有：

- 县固定效应 \(\mu_i\)：控制时间不变的县域异质性；
- 年固定效应 \(\tau_t\)：控制全国共同冲击。

若数据允许，可进一步考虑：

- 省份×年固定效应；
- 行业×年固定效应；
- 更细的区域趋势控制。

但必须强调：这篇文章识别真正闭合的关键，不在于某一种 FE 神奇地解决一切，而在于：

1. shock 是独立构造的；
2. structure 是预定的；
3. interaction 的经济学解释清楚；
4. outcomes 分层排列，能够拆 access 与 leakage。

这才是识别真正站得住的地方。

---

## 15. 最可能遇到的批评与应对

### 批评一：这是否只是城市化或人口流失趋势？

回应重点应是：

- 使用预定结构，而不让结果倒灌到解释变量；
- 控制人口、城镇化趋势和基线经济规模；
- 展示 access gains 与本地收入结果可以分离。

### 批评二：这是否只是平台 adoption，而非市场整合？

回应重点应是：

- 尽可能区分 integration shock 与 platform shock；
- 或清楚说明平台是统一市场在组织层面的关键实现机制；
- 通过机制变量表明，不是单纯 adoption，而是跨地 value attribution 的变化。

### 批评三：这是否只是“大城市虹吸”？

回应重点应是：

- 你的故事不是人口或企业向大城市迁移，而是交易内部价值归属的改变；
- 用外部卖家 penetration、外部结算、税基流向等变量说明，这是“captured elsewhere”，而不只是一般集聚。

### 批评四：这是否只是行政县边界问题？

回应重点应是：

- 承认县不是完美经济单元；
- 但中国县域是高分辨率观察窗口；
- 做相邻县、县域群或更大单元的稳健性。

### 批评五：这是否只是 outcome selection 的故事？

回应重点应是：

- 做分层结果，而不是只挑一个“坏指标”；
- 同时展示消费福利改善和本地收入不改善；
- 证明你不是靠悲观口径撑起结论，而是在识别 access 与 capture 的分离。

---

## 16. 图表系统应如何服务论证

图不是装饰，而是整篇文章论证顺序的一部分。最自然的证据链应是：

1. **先证明现象存在**：access 与 local development 的确可以脱钩；
2. **再证明这种脱钩具有结构性**：不是随机噪声，而是与地方初始结构相关；
3. **再证明其组织机制**：平台化改变价值归属与结算位置；
4. **最后上升为论文命题**：effective local multiplier depends on retained value.

如果图表顺序错了，例如一上来先放地图或总量趋势，读者会误以为你在写 descriptive county paper。

---

## 17. 主图应各自承担什么命题

### Figure 1: Motivating decoupling fact

第一张图不应该是地图，而应直接证明：

> **access gains 与 local income gains 不是一回事。**

理想形式是：

- 消费便利性、价格、品种明显改善；
- 但本地商户收入、进入率、税基或就业并未同步上升，甚至反向变化。

这张图不是识别，而是把读者拉进问题本身。没有它，理论部分会显得像先验设想，而不是对事实的 formalization。

### Figure 2: Five-location transaction schematic

如果 Figure 1 证明了“脱钩存在”，Figure 2 就必须解释“脱钩如何发生”。

最适合的是一个概念图或制度图，把一笔交易拆成：

- consumption location；
- business registration location；
- settlement location；
- tax location；
- employment/fulfillment location。

它的作用非常重要：把文章从“县域结果变化”提升到“交易内部空间组织变化”。没有这张图，读者容易把你的文章误解成“平台冲击地方零售”的浅层故事。

### Figure 3: Effective local multiplier conceptual figure

这张图服务理论部分，而不是数据部分。它应直观表达：

\[
\widetilde m_i = m_i\omega_i
\]

最自然的画法是：

- 横轴为 retained value share；
- 纵轴为 effective local multiplier；
- 多条线表示不同的 \(m_i\)。

它的作用是让读者看到：即便传统本地传播能力相同，retention 的差异也足以重写地方乘数。

### Figure 4: Heterogeneity dynamics by initial structure

这张图开始进入识别核心。它应展示：

- 高供给能力 vs 低供给能力；
- 高留值能力 vs 低留值能力；
- 高平台依赖 vs 低平台依赖；

在 shock 发生前后的动态路径差异。

它的功能是让读者一眼看到：

- 平均效应可能很弱；
- 但异质性很强；
- 且这种异质性与理论预言的结构维度一致。

### Figure 5: Mechanism figure on value leakage

如果数据允许，应有一张图直接展示 leakage 的组织去向，例如：

- 外部卖家占比上升；
- 外部结算占比上升；
- 平台佣金或服务费外流上升；
- 本地履约份额或本地主体份额下降。

这张图相当于经验部分的“inside the black box”。没有它，读者会觉得你只是观察到某些县变化不好，却不知道为什么。

### Figure 6: Access gains and leakage coexist

这张图很重要，因为它能帮助你摆脱“反平台”或“反统一市场”的误解。最理想的形式是把两类指标并列：

- 一侧是价格下降、品种增加、物流改善；
- 另一侧是本地商户、就业、税基或留值下降/不改善。

其命题是：

> **efficiency gains and local capture gains are not the same object.**

### Figure 7: Optional summary figure

最后可以有一张 summary figure，把整篇文章的逻辑链压缩成一个图：

- Integration lowers frictions；
- Platformization reorganizes transaction structure；
- Access gains rise；
- Retention may rise or fall depending on local structure；
- Effective local multiplier changes；
- Local development diverges across places。

这张图很适合作为跨 literatures ambition 的收束。

---

## 18. 图与表如何分工

图负责让读者“看懂这个世界发生了什么”；表负责让读者“相信这些不是巧合”。

### 更适合用图呈现的内容

- decoupling 的现象；
- 五地点机制示意；
- effective local multiplier 的理论重写；
- 动态异质性路径；
- access 与 leakage 并存；
- capture / leakage 的空间 pattern。

### 更适合用表呈现的内容

- 主回归系数；
- 交互项估计；
- 稳健性检验；
- 替代变量口径；
- placebo 与边界检验。

如果图表做到“先把问题视觉化，再把机制视觉化，再把异质性视觉化”，它们就不是附属材料，而是理论与识别之间的桥梁。

---

## 19. 把三部分写成论文正文时，最自然的顺序

### 19.1 Introduction 后半段

应当依次完成四件事：

1. 说明为什么 market integration 与 platformization 会让 value creation 与 value capture 脱钩；
2. 提出本文要重写的对象是 local multiplier，而非简单的市场整合平均效应；
3. 点出异质性的深层来源在于地方供给能力、留值能力与平台依赖结构；
4. 说明中国县域只是高分辨率识别窗口，而不是文章贡献边界。

### 19.2 Theory section

理论部分的最自然顺序是：

1. 现实观察：五个地点不再重合；
2. 定义 \(X_i\)、\(\omega_i\)、\(RV_i\)；
3. 重写地方乘数：\(\widetilde m_i = m_i\omega_i\)；
4. 分解 integration 的净效应：access effect 与 leakage effect；
5. 解释异质性来源：\(S_i\)、\(R_i\)、\(D_i\)、\(T_i\) 及其更深层的 congruence。

### 19.3 Empirical strategy

经验部分的最自然顺序是：

1. 说明识别对象不是平均政策效果，而是地方 incidence；
2. 将理论对象映射到 observable proxies：shock、structure、outcomes；
3. 给出 shock × structure 主方程；
4. 说明结果如何分层：retained value / mechanism / welfare / macro outcomes；
5. 预先处理识别批评与稳健性。

### 19.4 Results narrative

结果呈现的顺序不应是“表 1、表 2、表 3”的机械堆叠，而应沿证据链推进：

1. 先给 motivating fact，证明 decoupling 不是空想；
2. 再给异质性 reduced-form，证明结构性差异存在；
3. 再给机制证据，打开 value leakage 的黑箱；
4. 再补 access gains，同时防止读者误解文章为反效率叙事；
5. 最后用 summary synthesis 收束 contribution。

---

## 20. 这套 master draft 当前最需要避免的三类错误

### 错误一：把文章写成中国制度背景说明

理论部分不是解释“全国统一大市场政策文件”，而是提出一个一般命题。中国是 empirical window，不是理论边界。

### 错误二：把数字适应能力写成唯一主轴

数字能力重要，但它只是 \(T_i\)，而不是整个模型。模型核心仍然是 access、attribution 与 retention。

### 错误三：把 \(\omega_i\) 写成经验 proxy，而非理论对象

如果 \(\omega_i\) 只是经验部分的统计指标，理论贡献会立刻塌掉。它必须先在理论中成为核心状态变量，再在经验中寻找 proxy。

---

## 21. 当前整篇文章最硬的一句话

如果必须用一句话来压缩整篇文章的理论与经验核心，那应当是：

> **市场一体化扩大了各地的市场接入机会，但在平台化条件下，本地支出不再自动转化为本地收入；地方发展的关键因此不在于 spending 本身，而在于其中有多少最终被保留为本地 retained value，而这又取决于地方的供给能力、留值能力与平台依赖结构。**

这句话同时概括了：

- 理论对象；
- 识别目标；
- 异质性来源；
- 政策含义。

---

## 22. 最后一层判断：这篇文章是否已经有了 EJ 级别的骨架

如果从一般性、理论清晰度和经验可执行性三方面判断，这篇文章的骨架已经足够清楚：

第一，它的主问题不是“中国平台经济有没有副作用”，而是一个一般性的空间 incidence 命题：**market integration 与 platformization 如何重组 value capture。**

第二，它不是停留在“access gain 与 leakage 共存”的现象陈述，而是把地方乘数正式重写为 retained value 的函数。**这一步是整篇文章的理论升档点。**

第三，它的经验部分不是普通 DID，而是围绕 **shock × pre-determined structure** 来识别地方 incidence，从而与理论中的 \(\omega_i\) 与 \(\widetilde m_i\) 对接。

第四，它的图表与证据链不是描述性附属，而是把“现象—机制—异质性—理论重写”串起来的论证系统。

如果后续写作能继续守住这四点，那么这篇文章就不是一个普通县域平台论文，而是一篇真正具有 EJ ambition 的理论—实证结合论文。

