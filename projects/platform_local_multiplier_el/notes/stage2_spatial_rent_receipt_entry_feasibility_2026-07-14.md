# Stage 2：平台租金收取地 × 本地卖家进入的解析可行性测试

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
性质：正式稿重写前的 theorem-feasibility memo  
文件边界：本文件不修改 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、`code/verify_model.py` 或 `output/paper.pdf`

## 1. 结论

这一候选通过了解析可行性关，并且比“只加入 seller entry”更接近原项目真正关心的空间机制。

核心比较保持以下对象完全不变：

- 平台费率；
- 消费者面对的平台价格；
- online/offline 支出份额；
- 外部订单与 seller technology；
- seller 的 net-of-fee margin。

唯一变化是：在总 take rate 固定时，本地居民平台交易产生的佣金中，有多少按交易支付给既有的本地 transaction-service node。令该比例为 \(\lambda\in[0,1]\)，并在比较中固定节点的服务容量和质量。模型证明：即使 fee 和消费者条件相同，提高 \(\lambda\) 也能通过本地收入再支出扩大订单池，越过 local seller 的 free-entry threshold。若总部独占佣金时没有本地卖家、与本地服务节点分享时有本地卖家，则存在唯一阈值 \(\lambda^*\)，收入与 seller mass 在阈值处连续，但其边际反应出现严格向上的 kink。

更重要的是，关闭本地再支出后，\(\lambda\) 仍改变第一轮地方收入，却不再改变 seller entry：

\[
\left.\frac{\partial n}{\partial\lambda}\right|_{\text{no respending}}=0.
\]

因此，新的 entry effect 不是把平台利润做一次事后地区分账，而是 **rent receipt location 通过 local spending feedback 改变平台的供给组织**。

阶段判定为：

```text
mathematical_feasibility = PASS
income_conservation = PASS
existence_and_uniqueness = PASS
true_no_entry_corner = PASS
local_respending_necessity = PASS
fixed_inverse_non_reducibility = PASS_FOR_ACTIVE_SET_RESULT
direct_platform_prior_art = CONDITIONAL_PASS_NOT_CERTIFIED
EL_scope = PASS_WITH_STRICT_CUTS
formal_main_tex_rewrite = PAUSED_PENDING_ADVERSARIAL_REVIEW
```

## 2. 为什么需要改测这一候选

### 2.1 老文献不是否定依据

SAM、Miyazawa、MRIO 和 local multiplier 文献已经包含固定收入系数下的重复支出与跨地区流量。这只说明给定 seller mass 和 rent allocation 后，收入方程使用的是标准 inverse。它们通常不包含数字平台的 commission、seller free entry、online/offline substitution 或佣金收取地对 seller participation 的反馈，不能单独否定本候选。

### 2.2 真正的直接先例

Fan et al. (2018) 和 Li 的当前 e-commerce working paper 已经把地区收入、市场接入与 online retailer entry 放进空间均衡。Anderson--Bedre-Defolie、Etro、Teh 等平台文献已经研究 commission 与 seller entry。因此以下命题均不足以成为贡献：

- demand 或 income 增加促进 seller entry；
- commission 提高阻碍 entry；
- fixed cost 产生 no-entry threshold；
- entry 后地方收入增加；
- generic positive feedback 产生 tipping。

尚可检验的窄问题是：

> 在 fee、price 与 technology 不变时，平台租金的收取地是否会通过地方收入再支出改变 seller-entry active set？

### 2.3 原连续模型的必要性测试未通过

原连续候选可以产生“进入前地方收入下降、进入后地方收入上升”。但若把居民后续支出固定在冲击前水平，第一轮 accounting 仍可产生相同的符号反转：传统代理收入减少，而本地 seller 外销与净收入增加。因此，phase reversal 本身不能证明 local multiplier 是必要机制。

本候选修正这一点：在没有本地再支出时，rent receipt location 不进入 seller payoff；只有允许本地佣金收入重新形成平台需求，\(\lambda\) 才能移动 entry threshold。

## 3. 环境

### 3.1 家庭与渠道份额

沿用内部 CES 渠道选择。地区 \(L\) 的居民把收入比例 \(\alpha\) 用于零售，把比例 \(\beta\) 用于完全本地化的 nontradables，其中

\[
\alpha,\beta>0,
\qquad
\alpha+\beta<1.
\]

给定整合状态 \(z\)，平台支出份额为 \(s=s(z)\in(0,1)\)。本节把 \(z\) 固定，只比较租金收取地。定义

\[
\phi\equiv\alpha s>0,
\qquad
c_0\equiv
\beta+\alpha\rho_A(1-s),
\tag{1}
\]

其中 \(\rho_A\in[0,1]\) 是传统本地代理渠道每元支出形成的本地收入份额。居民平台支出为 \(\phi Y\)。

### 3.2 平台订单与 seller routing

外部消费者提供外生订单 \(E\geq0\)。可由本地或外地卖家承接的订单池为

\[
Q=E+\phi Y.
\tag{2}
\]

本地活跃 seller mass 为 \(n\geq0\)，外地 seller 的有效 routing weight 为 \(\chi>0\)。平台在不改变消费者价格的情况下分配订单：

\[
\theta(n)=\frac{n}{n+\chi},
\qquad
q(n)=\frac{Q}{n+\chi}.
\tag{3}
\]

\(\theta Q\) 是本地 seller 总订单，\(q\) 是每个本地 seller 的订单。一个直接 microfoundation 是 proportional routing：平台对标准化订单按 seller 的有效曝光或履约权重分配；每个本地 seller 具有一单位权重，外地 sellers 的合计权重为 \(\chi\)。因此每单位权重获得 \(Q/(n+\chi)\) 的订单。该结构包含标准 business stealing：给定 \(Q\)，更多本地 sellers 降低每个 seller 的订单。它不是消费者对“本地标签”的偏好，也不要求 seller entry 改变消费者价格。

### 3.3 Commission、进入与平台租金收取地

平台按 gross sales 收取比例费率

\[
\tau\in(0,1).
\]

令 \(\mu\in(0,1]\) 是 seller net-of-fee receipt 中可用于覆盖固定设置成本的 operating-surplus share，\(F>0\) 是固定本地投入成本。自由进入满足

\[
n\geq0,
\qquad
F-\mu(1-\tau)\frac{Q}{n+\chi}\geq0,
\qquad
n\left[
F-\mu(1-\tau)\frac{Q}{n+\chi}
\right]=0.
\tag{4}
\]

基准假定 local seller 的 net-of-fee payout 用于本地 variable inputs 和固定设置投入；free-entry residual owner profit 为零。本地 commission receiver 与其他本地收入接受者具有相同的边际支出倾向。因此这些收入进入同一个地方收入循环。若其中一部分被外地要素提供者收取或储蓄，应把相应份额从本地收入中扣除。

定义 break-even order pool

\[
Q_E=\frac{F\chi}{\mu(1-\tau)}.
\tag{5}
\]

于是

\[
\theta(n)Q=[Q-Q_E]_+.
\tag{6}
\]

令 \(\lambda\in[0,1]\) 表示本地居民平台交易所产生的 commission 中，按交易支付给既有本地 transaction-service node、形成其可支配本地要素收入并在本地继续支出的比例。总 take rate \(\tau\) 固定，总部保留其余份额。\(\lambda\) 不是股权、注册地址、税务确认地、无条件返还或 seller subsidy：

\[
\underbrace{\lambda\tau\phi Y}_{\text{local commission receipt}},
\qquad
\underbrace{(1-\lambda)\tau\phi Y}_{\text{remote HQ receipt}}.
\tag{7}
\]

\(\lambda\) 不改变 \(\tau\)、平台价格、\(s\)、seller payout、节点服务质量或 routing technology。它是既有服务合同下的 transaction-attributed payout share，而不是 fee subsidy。若 payout 会改变节点努力、平台采用、信任、履约或消费者价格，则本 partial-equilibrium counterfactual 不适用。

基准只把本地居民交易的 buyer-side commission sharing 写入式（7）。外部订单 \(E\) 的平台费仍归总部；这样可以把本地交易服务节点的收入与 seller 的外部市场接入分开。

## 4. 收入守恒

每元本地居民平台支出分为三种互斥收入：

1. 若订单由本地 seller 承接，\((1-\tau)\) 归本地 seller 的劳动、投入与经营收入；否则该 seller payout 归外地；
2. \(\lambda\tau\) 归本地交易服务节点或地方收入接受者；
3. \((1-\lambda)\tau\) 归远程平台总部。

对于本地居民向本地 seller 下单的一元交易：

\[
(1-\tau)+\lambda\tau+(1-\lambda)\tau=1.
\]

对于本地居民向外地 seller 下单的一元交易，seller payout 与远程 commission 合计为外部收入，local transaction-service payout 仍为 \(\lambda\tau\)，总额同样为一。外部订单 \(E\) 的平台费全部归总部。

令本地与外部收入账户分别为

\[
I_L
=c_0Y+\lambda\tau\phi Y
+(1-\tau)\theta(E+\phi Y),
\tag{L1}
\]

\[
\begin{aligned}
I_H={}&(1-\alpha-\beta)Y
+\alpha(1-s)(1-\rho_A)Y\\
&+(1-\lambda)\tau\phi Y
+(1-\tau)(1-\theta)\phi Y\\
&+\tau E+(1-\tau)(1-\theta)E.
\end{aligned}
\tag{L2}
\]

逐项相加得到

\[
I_L+I_H=Y+E.
\tag{L3}
\]

固定投入 \(F\) 由本地要素提供。正进入时，free entry 给出

\[
F=\mu(1-\tau)q.
\]

每个 seller 的 variable local-factor income 为 \((1-\mu)(1-\tau)q\)，fixed local-input income 为 \(F\)，二者相加恰为 \((1-\tau)q\)。因此在地区收入中计入完整 net-of-fee seller payout、同时在私人利润中扣除 \(F\)，没有 double counting；seller owner 的 equilibrium residual profit 为零。

## 5. Local-income equilibrium

### Definition 1

给定 \((s,E,\tau,\lambda)\)，均衡是 \((Y,n,\theta,Q)\)，使家庭支出、routing、free entry 与下列收入固定点同时成立：

\[
Y
=B+c_0Y+\lambda\tau\phi Y
+(1-\tau)[E+\phi Y-Q_E]_+,
\qquad B>0.
\tag{8}
\]

定义

\[
\bar d=1-c_0,
\tag{9}
\]

\[
D_0(\lambda)=\bar d-\lambda\tau\phi,
\tag{10}
\]

\[
D_1(\lambda)
=D_0(\lambda)-(1-\tau)\phi
=\bar d-\phi[1-\tau+\lambda\tau].
\tag{11}
\]

由于 \(\rho_A\leq1\)、\(\lambda\leq1\) 且 \(1-\tau+\lambda\tau\leq1\)，

\[
D_0(\lambda),D_1(\lambda)
\geq1-\alpha-\beta>0.
\tag{12}
\]

### Lemma 1：存在性、唯一性与全局稳定性

式（8）的右侧是连续、分段线性的 contraction。无进入区间的斜率为

\[
c_0+\lambda\tau\phi<1,
\]

进入区间的斜率为

\[
c_0+\phi[1-\tau+\lambda\tau]<1.
\]

因此存在唯一正收入均衡，收入迭代 \(Y_{t+1}=T(Y_t)\) 从任意非负初值收敛。这里的“全局稳定”只指收入轮次；模型没有另行设定 seller-entry dynamics。给定 \(Y\)，式（4）唯一决定 \(n\)：若 \(Q\leq Q_E\)，则 \(n=0\)；若 \(Q>Q_E\)，则

\[
n=\frac{\mu(1-\tau)}F(Q-Q_E)>0.
\tag{13}
\]

故完整均衡存在且唯一。

## 6. 分段解析解

### 6.1 强制无进入候选

若 \(n=0\)，

\[
Y_0(\lambda)=\frac{B}{D_0(\lambda)},
\tag{14}
\]

\[
Q_0(\lambda)
=E+\frac{\phi B}{D_0(\lambda)}.
\tag{15}
\]

该候选合法当且仅当

\[
Q_0(\lambda)\leq Q_E.
\tag{16}
\]

### 6.2 正进入候选

若 \(n>0\)，

\[
Y_1(\lambda)
=\frac{
B+(1-\tau)(E-Q_E)
}{D_1(\lambda)}
=\frac{
B+(1-\tau)E-F\chi/\mu
}{D_1(\lambda)}.
\tag{17}
\]

定义 \(Q_1=E+\phi Y_1\)。直接代数给出

\[
Q_1-Q_E
=\frac{D_0(\lambda)}{D_1(\lambda)}
[Q_0(\lambda)-Q_E].
\tag{18}
\]

因此两个候选的合法区间完全互补：

\[
Q_0\leq Q_E
\Longleftrightarrow n=0,
\qquad
Q_0>Q_E
\Longleftrightarrow n>0.
\tag{19}
\]

不存在多重均衡或 hysteresis。

正进入分支的收入也严格为正。若 \(Q_E\leq E\)，式（17）的 numerator 不小于 \(B>0\)；若 \(Q_E>E\)，分支合法性给出 \(Q_1>Q_E>E\)，而 \(Q_1=E+\phi Y_1\)，故 \(Y_1>0\)。

## 7. 主候选命题：receipt-induced seller activation

### Proposition 1

假定

\[
Q_0(0)<Q_E<Q_0(1).
\tag{20}
\]

则存在唯一 \(\lambda^*\in(0,1)\)，使得

\[
n(\lambda)=0
\quad\text{当且仅当}\quad
\lambda\leq\lambda^*,
\]

\[
n(\lambda)>0
\quad\text{当且仅当}\quad
\lambda>\lambda^*.
\]

阈值满足

\[
E+\frac{\phi B}
{\bar d-\lambda^*\tau\phi}
=Q_E.
\tag{21}
\]

若 \(Q_E>E\)，其闭式解为

\[
\boxed{
\lambda^*
=\frac{
\bar d-\phi B/(Q_E-E)
}{\tau\phi}.}
\tag{22}
\]

条件（20）恰好保证式（22）落在 \((0,1)\)。

### 经济含义

\(\lambda\) 不进入 seller 的 net-of-fee margin，也不改变消费者价格。它先改变本地 transaction-service node 的 buyer-side payout；该收入被继续用于平台消费，使 \(Q_0\) 上升。当 \(Q_0\) 越过 \(Q_E\) 时，本地 sellers 才开始进入。因此，同一 take rate 可以在 HQ-exclusive receipt 与 local-service revenue sharing 下对应不同的 seller organization。

### 证明要点

由式（15），

\[
\frac{dQ_0}{d\lambda}
=\frac{\tau\phi^2B}{D_0(\lambda)^2}>0.
\tag{23}
\]

所以 \(Q_0\) 对 \(\lambda\) 严格单调。结合式（20）和连续性，唯一阈值存在。式（18）保证阈值两侧分别只有无进入和正进入候选。解式（21）即得式（22）。

## 8. 推论：收入与 seller mass 的 kink

在无进入区间，

\[
\frac{dY_0}{d\lambda}
=\frac{\tau\phi Y_0}{D_0}>0.
\tag{24}
\]

在正进入区间，

\[
\frac{dY_1}{d\lambda}
=\frac{\tau\phi Y_1}{D_1}>0.
\tag{25}
\]

在 \(\lambda=\lambda^*\) 时，两分支收入相同，且

\[
Y^*=\frac{Q_E-E}{\phi}.
\tag{26}
\]

但右侧斜率严格大于左侧斜率：

\[
\boxed{
\left.\frac{dY}{d\lambda}\right|_{+}
-
\left.\frac{dY}{d\lambda}\right|_{-}
=\tau\phi Y^*
\left(
\frac1{D_1(\lambda^*)}
-\frac1{D_0(\lambda^*)}
\right)>0.}
\tag{27}
\]

seller mass 从零连续开始增长，其右导数为

\[
\boxed{
\left.\frac{dn}{d\lambda}\right|_{+}
=
\frac{
\mu(1-\tau)\tau\phi^2Y^*
}{FD_1(\lambda^*)}>0,}
\tag{28}
\]

而左导数为零。

这个 kink 有两层来源：local commission receipt 的直接收入效应，以及 seller entry 后 net-of-fee seller receipts 开始参与本地收入循环。收入水平不跳跃；不能称 discontinuous tipping 或 hysteresis。

## 9. Local respending 的必要性

### Proposition 2：关闭再支出后的结果

只关闭待识别的 platform-order respending：将居民平台订单固定为一个外生数 \(\bar X_P\)，不允许新增本地收入改变下一轮平台需求，但保留其他 nonplatform local-income propagation \(c_0\widehat Y\)：

\[
\widehat Q=E+\bar X_P.
\tag{29}
\]

rent receipt location 仍改变地方收入：

\[
\widehat Y
=
\frac{
B+\lambda\tau\bar X_P
+(1-\tau)[\widehat Q-Q_E]_+
}{1-c_0}.
\tag{30}
\]

但 free-entry condition 变为

\[
\mu(1-\tau)
\frac{\widehat Q}{n+\chi}=F,
\tag{31}
\]

其中没有 \(\lambda\)。所以

\[
\boxed{
\left.\frac{\partial n}{\partial\lambda}
\right|_{\widehat Q}=0.}
\tag{32}
\]

同时

\[
\frac{\partial\widehat Y}{\partial\lambda}
=\frac{\tau\bar X_P}{1-c_0}>0.
\tag{33}
\]

式（22）的 receipt-location threshold 与式（27）的 entry kink 都消失。此时 \(\lambda\) 仍具有由其余本地支出传播放大的收入效应，但不再改变 seller organization；这属于已知 incidence/accounting benchmark。

这证明 local respending 不是装饰性 denominator：在保持 \((s,E,F,\mu,\chi,\tau)\)、价格、服务能力和服务质量不变的 receipt-only counterfactual 中，它是 local transaction-service payout 改变 seller organization 的必要传导机制。

## 10. 与固定 seller mass 的区别

若把 routing share 固定为 \(\bar\theta\)，收入为

\[
Y(\bar\theta,\lambda)
=
\frac{
B+(1-\tau)\bar\theta E
}{
1-c_0-\phi[
\lambda\tau+(1-\tau)\bar\theta
] }.
\tag{34}
\]

这是标准 fixed-coefficient multiplier。\(\lambda\) 平滑改变地方收入，但不会产生 no-entry corner、\(\lambda^*\) 或 active-set kink。

在一个已进入的均衡点，固定 \(\bar\theta=\theta(n)<1\) 时的边际效应为

\[
\left.\frac{dY}{d\lambda}\right|_{n}
=\frac{\tau\phi Y}{
1-c_0-\phi[\lambda\tau+(1-\tau)\theta(n)]}.
\tag{35}
\]

允许 free entry 后，式（25）的分母为 \(D_1\)，且

\[
D_1
<
1-c_0-\phi[\lambda\tau+(1-\tau)\theta(n)].
\]

因此 endogenous entry 严格放大 receipt-localization 的收入效应。该额外放大在固定 seller mass 时消失。

## 11. 机制关闭

| 关闭项 | 参数或约束 | 结果 |
|---|---|---|
| 无 commission | \(\tau=0\) | \(\lambda\) 无经济含义，receipt-location effect 消失 |
| 全部远程收取 | \(\lambda=0\) | 没有本地 commission income；可能停留在 no-entry corner |
| 全部本地收取 | \(\lambda=1\) | local demand feedback 最大；可能激活本地 sellers |
| 无居民平台支出 | \(\phi=0\) | 本地 commission 与再支出通道消失 |
| 无本地再支出 | 固定 \(\widehat Q\) | \(dn/d\lambda=0\)，threshold 与 kink 消失 |
| 固定 seller mass | 固定 \(n\) 或 \(\theta\) | 只剩平滑 multiplier incidence；active-set result 消失 |
| 无本地 seller 可进入 | \(F\to\infty\) | \(\lambda\) 只改变地方收入，不改变交易组织 |
| 无外地 seller competition | \(\chi\to0\) | \(Q_E\to0\)，只要订单为正即进入，interior threshold 消失 |

## 12. 与原项目机制的对应

这一候选恢复了原项目在 EL 简化中被删除的三项对象：

1. **中介重组**：传统本地代理并非简单消失；\(\lambda>0\) 表示其中一部分转化为具有固定服务能力的本地平台交易服务节点，并获得 transaction-attributed payout。
2. **价值捕获地**：同一平台费可以在本地或总部形成收入；fee rate 与 receipt location 被严格分开。
3. **地方乘数改变组织边界**：地方再支出不只放大一个给定收入冲击，而是反过来改变 local seller 是否进入平台。

模型仍然没有加入税收、迁移、住房、平台最优定价、资本区位或多地区生产。它是 small-open-region analytical model，不是完整中国空间 GE。

## 13. Observable mapping

| 理论对象 | 可观测对应 |
|---|---|
| \(s\) | 本地居民平台零售支出份额 |
| \(\tau\) | commission、referral fee、广告和技术服务 take rate |
| \(\lambda\) | 固定 take rate 中按本地居民交易支付给既有 terminal manager 或本地 transaction-service node 的比例 |
| \(n\) | seller operating location 位于本地且产生正收入的 active seller mass |
| \(\chi\) | 与本地 sellers 竞争 routing/曝光/订单的外地 seller 有效质量 |
| \(E\) | 外地买家对可由本地 seller 承接的订单规模 |
| \(F\) | onboarding、认证、库存、数字运营和固定履约投入 |
| \(\rho_A\) | 传统本地代理渠道一元销售形成的本地收入份额 |
| \(Y\) | 本地工资、经营收入及本地收入接受者所得；不是 full welfare |

中国农村电商项目中的 local terminal manager、交易服务站和按交易 reward 为 \(\lambda\) 提供了直接制度映射。本文不把一般平台股权、税收返还或 affiliate accounting location 与该参数混用。

## 14. 直接文献边界

- Fan et al. 和 Li 已覆盖 income-weighted market opportunity 与 online seller entry，但没有独立的平台 commission receipt residence。
- Anderson--Bedre-Defolie、Etro、Teh 等已覆盖 fee 与 free entry，但没有地方收入收取和再支出。
- Brown et al. 等 local/absentee ownership 文献说明 receipt location 对地方 multiplier 重要，但不包含平台 seller entry。
- Couture et al. 提供中国 local terminal manager 与 commission 的制度事实，但不是本命题的解析模型。

本轮有界检索未发现式（20）--（31）的同一联合命题。这只能支持 `conditional novelty`，不能写成“first paper”或最终 priority certification。

## 15. EL 可写性

若该候选通过独立复审，Economics Letters 正文只能保留：

1. 一段制度动机与准确贡献；
2. CES share 作为给定的 \(s\)，不重复完整家庭推导；
3. income ledger、free entry 与式（8）；
4. 一个 Lemma：唯一分段解；
5. 一个 Proposition：\(\lambda^*\) 与 kink；
6. 一个 Corollary：关闭 respending 后 \(dn/d\lambda=0\)；
7. 极短的讨论与可观测映射。

不应同时保留原稿的 recursive-retention multiplier、finite \(z\) regions、\(s^\dagger<1/2\)、离散 hysteresis 或两地区矩阵。建议的新工作标题是：

> **Local Platform Revenue Sharing and Seller Entry**

它比 *Platform Intermediation and Local Multipliers* 更准确，但正式标题尚未冻结。

## 16. 风险与停止条件

1. \(\lambda\) 只解释为既有本地 transaction-service node 的按交易 payout share，不能改写为总部利润任意返还、股权或税收会计参数。
2. 总 take rate 与 revenue-sharing rule 在基准中可独立变化，且服务质量固定。若 \(\lambda\) 必然改变节点努力、平台成本、采用或消费者价格，当前 exclusion restriction 失效。
3. routing rule 假定平台价格不因 seller mass 改变。若品种与价格反馈是主对象，应进入大论文，不适合当前 EL。
4. 本地 commission receiver 的消费行为被设为与其他本地收入接受者相同。若利润完全储蓄或外流，\(\lambda\) 应改为“实际本地可支配并再支出的份额”。
5. 若更广的 backward/forward citation audit 找到同一 receipt-location entry theorem，则停止独立 EL。
6. 若必须内生平台最优 \((\tau,\lambda)\) 才能让结果有经济含义，则转回大论文。

## 17. 当前路线建议

在三个候选中：

| 候选 | 解析性 | 现实稳健性 | 直接 prior-art 风险 | local multiplier 必要性 | 建议 |
|---|---:|---:|---:|---:|---|
| 普通 continuous seller activation | 高 | 高 | 高：Fan/Li + fee-entry | 低 | 不作为核心 |
| 离散 seller hysteresis | 高 | 取决于弱 business stealing | 高：generic platform tipping | 中 | 暂不采用 |
| spatial rent receipt × entry | 高 | 中高，需制度映射 | 中，未发现同一联合命题 | 高 | **首选，进入独立复审** |

因此，推荐暂时停止原 continuous phase-reversal route，把本候选送入一次独立的 algebra、incidence、microfoundation 与 direct-prior-art adversarial review。通过之前继续冻结正式稿。
