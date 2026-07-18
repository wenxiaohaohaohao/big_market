# Stage 2 最终路线闸门：平台交易服务收益、本地再支出与 seller entry

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
文件性质：正式重写前的 theorem-feasibility、prior-art 与机制必要性综合判定  
文件边界：本轮继续冻结 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、`code/verify_model.py` 与 `output/paper.pdf`

## 1. 最终结论

本轮没有因为早期 local-multiplier、SAM、Miyazawa 或 MRIO 文献包含相似分母，就否定“平台经济—本地留存—中介重组—地方乘数”这一研究问题。旧文献只用于划定代数祖先：它们说明固定收入留存系数下的递归支出反馈不是新的；它们没有研究数字平台如何改变交易服务收益的空间归属，也没有直接给出本文保留的 seller-organization 命题。

真正构成约束的是两类更接近的当代文献：

1. 多地区 e-commerce 模型已经研究线上渠道、地区收入、seller entry 与市场接入，因此“地方需求扩大促进进入”不能作为新结果；
2. platform fee、revenue sharing、local intermediary 与 free entry 文献分别覆盖若干单独模块，因此普通的 fee-entry threshold 或“收益提高导致进入”也不能作为新结果。

在这一更严格、也更合适的参照系下，本轮有界检索**没有发现**以下联合命题的直接先例：

> 在平台总 take rate、消费者价格、平台支出份额、seller net-of-fee margin 与交易技术不变时，提高本地交易产生的平台收益中支付给本地 transaction-service node 的比例，会通过本地收入再支出扩大订单池，改变 local seller 的 free-entry active set；固定居民平台订单后，这一 seller-organization 反应严格消失。

因此，本轮 gate 为：

```text
mathematical_feasibility              = PASS
income_conservation                   = PASS
existence_and_uniqueness              = PASS
platform_respending_necessity         = PASS_WITHIN_RECEIPT_ONLY_COUNTERFACTUAL
proportional_routing_business_stealing = PASS
narrow_direct_prior_gate              = PASS_CONDITIONALLY
priority_or_first_claim               = NOT_AUTHORIZED
institutional_exclusion_restriction   = EXPLICIT_ASSUMPTION_REQUIRED
stage2_theorem_feasibility            = CONDITIONAL_PASS
formal_main_tex_status                = FROZEN_PENDING_USER_CONFIRMATION
```

推荐路线是：以“local transaction-service payout × local platform-order respending × seller free entry”为唯一新增机制，重写一篇新的解析 Letter。原标量 multiplier 只能作为 benchmark；原 continuous phase-reversal 候选和离散 hysteresis 候选不进入正式稿。

## 2. 创新性判定采用的分层标准

### 2.1 代数祖先，不是直接否定

Miyazawa、SAM、Type-II multiplier 与 multiregional income-feedback 文献已经说明：当家庭收入重新进入消费需求时，均衡含有几何级数或 inverse；地方漏出会改变该 inverse 的系数。它们因此排除以下主张：

- “每轮支出都再次发生 leakage”本身是新机制；
- \(1/[1-\beta-\alpha\omega]\) 这一分母本身是新结果；
- 把标量 \(\omega\) 换成固定空间矩阵本身构成平台理论贡献。

这些文献没有排除以下研究对象：平台组织如何决定谁收取交易收益、该收益在何地重新支出，以及这种空间 incidence 如何改变平台生态中的 seller active set。旧文献与当前项目不处于同一 primitive 层级，不能用“代数相似”替代直接 prior-art 判断。

### 2.2 直接相邻的现代平台文献

Fan et al. 与 Li 的多地区 e-commerce 模型已经将线上/线下渠道、地区收入、market access、firm 或 retailer entry 放进同一空间均衡。因此，seller entry 不能单独承担创新。Couture et al. 记录的农村 e-commerce terminal 及其 transaction-contingent manager reward，为本地交易服务收益提供制度映射，但没有推导地方收入再支出改变 seller active set 的定理。直接相邻模块还包括 Cai et al. 的 local commission 与 operator participation、Adebola--Arora--Zhang 的 human intermediary、Bhargava et al.、Feldman et al. 与 Duan et al. 的 revenue allocation，以及 Brown et al. 的 local/absentee income incidence。完整逐项判定见 [narrow direct-prior check](stage2_rent_receipt_narrow_prior_check_2026-07-14.md)。本轮没有发现同时固定总 take rate 与消费者条件、只改变收益收取地并关闭/开启地方再支出的同一联合结果。

因此，当前状态只能写成 `conditional novelty`，不能写成 `first`, `unprecedented` 或“现有文献从未研究”。投稿前仍需刷新 Li working paper 的最新版本，并检查最接近的 human-intermediary working paper 是否新增了 regional respending 或 provider-entry extension。

## 3. 被排除的两个候选

### 3.1 Continuous seller-entry phase reversal：NO-GO

该候选能够产生无进入与正进入两个区域，也能出现政策边际效应在进入后改变符号。然而数值与解析反例表明，即使冻结本地再支出，第一轮 margin 重组本身也可以造成 phase reversal。于是：

\[
\text{phase reversal}\not\Rightarrow
\text{local multiplier is necessary}.
\]

该结果无法把项目的核心机制与普通 entry comparative statics 区分开，不适合作为 EL 主命题。

### 3.2 Discrete entry、multiplicity 与 hysteresis：NO-GO

在一般 seller order density \(h(n)\) 下，strategic complementarity 要求 business-stealing elasticity 足够低。标准 proportional CES/routing 给出

\[
h(n)=\frac{1}{n+\nu}.
\]

在合法支出份额条件下，进入者增加必然降低单个 seller 的回报，free-entry fixed point 唯一；原先构造的 corner coexistence、multiplicity 与 hysteresis 消失。除非另加一个独立品类或局部网络外部性制度，否则该候选依赖不可信的机制。为保持 Letter 简洁，本路线停止。

## 4. 选定候选的最小环境

令 \(s\in(0,1)\) 为居民平台渠道支出份额，并定义

\[
\phi=\alpha s,
\qquad
c_0=\beta+\alpha\rho_A(1-s).
\]

居民平台订单为 \(\phi Y\)，外部消费者对本地市场产生外生平台订单 \(E\geq0\)，故平台订单池为

\[
Q=E+\phi Y.
\]

若本地 active sellers 的连续质量为 \(n\)，外地 sellers 的合计 routing weight 为 \(\chi>0\)，则

\[
\theta(n)=\frac{n}{n+\chi},
\qquad
q(n)=\frac{Q}{n+\chi}.
\]

这是一种 proportional non-price routing：每个本地 seller 有一单位曝光或履约权重，外地 sellers 合计权重为 \(\chi\)。给定 \(Q\)，更多本地 sellers 降低每个 seller 的订单，因而保留标准 business stealing。

平台总 take rate 为 \(\tau\in(0,1)\)。每个 seller 的 net-of-fee order revenue 中，比例 \(1-\mu\) 支付给本地可变要素，比例 \(\mu\in(0,1]\) 是可用于覆盖本地固定投入 \(F>0\) 的 operating-surplus share。free-entry condition 为

\[
n\geq0,
\qquad
F-\mu(1-\tau)\frac{Q}{n+\chi}\geq0,
\qquad
n\left[F-\mu(1-\tau)\frac{Q}{n+\chi}\right]=0.
\]

定义 entry order threshold

\[
Q_E=\frac{F\chi}{\mu(1-\tau)}.
\]

则本地 sellers 获得的总订单为

\[
\theta Q=[Q-Q_E]_+.
\]

## 5. 唯一的 payout primitive

为避免把参数误解为任意地区转移，正式稿不应把 \(\lambda\) 称为 ownership share、税收返还、affiliate accounting location 或 seller subsidy。建议使用

\[
r=\lambda\tau\in[0,\tau]
\]

并称其为 `local transaction-service payout rate`：居民平台购买所产生的总平台 take 中，按交易支付给既有本地 transaction-service node 或 terminal manager 的比例。总部保留 \(\tau-r\)。

该比较静态必须固定：

- 平台总 take rate \(\tau\)；
- consumer price、平台渠道份额 \(s\) 与外部订单 \(E\)；
- seller net-of-fee share \(1-\tau\)；
- routing technology \(\chi\)；
- seller variable-income share \(\mu\) 与 fixed cost \(F\)；
- 本地 transaction-service node 的服务能力、努力和服务质量。

这是一个 partial-equilibrium exclusion restriction，不是已经由数据识别的制度事实。Couture et al. 的 transaction-contingent terminal-manager reward 只能证明此类合同存在，不能证明现实中 payout rate 可以在服务质量、采用率与订单量完全不变时外生变化。正式稿必须把这一点作为模型假设和限制公开说明。

## 6. Local-income equilibrium 与解析解

本地收入满足

\[
Y
=B+c_0Y+r\phi Y
+(1-\tau)[E+\phi Y-Q_E]_+.
\]

定义

\[
\bar d=1-c_0,
\qquad
D_0=\bar d-r\phi,
\qquad
D_1=D_0-(1-\tau)\phi.
\]

由于 \(\alpha+\beta<1\)，两个分支的收入映射斜率都严格小于一，且

\[
D_1\geq1-\alpha-\beta>0.
\]

因此收入映射是从 \(\mathbb R_+\) 到自身的 piecewise-linear contraction，存在唯一正均衡，收入迭代全局收敛。

无本地 seller 进入时：

\[
Y_0=\frac{B}{D_0},
\qquad
Q_0=E+\frac{\phi B}{D_0}.
\]

正进入时：

\[
Y_1=
\frac{B+(1-\tau)(E-Q_E)}{D_1}
=
\frac{B+(1-\tau)E-F\chi/\mu}{D_1}.
\]

两个候选分支满足

\[
Q_1-Q_E=\frac{D_0}{D_1}(Q_0-Q_E),
\]

所以它们的 active-set 条件一致，不能同时合法，也不会遗漏第三个均衡。

## 7. 可保留的主命题

用 \(\lambda=r/\tau\) 表示 payout fraction。若

\[
Q_0(0)<Q_E<Q_0(1),
\]

则存在唯一内部阈值

\[
\lambda^*
=
\frac{\bar d-\phi B/(Q_E-E)}{\tau\phi}
\in(0,1),
\]

使得本地 seller 进入当且仅当 \(\lambda>\lambda^*\)。由于 \(Q_0(0)>E\)，该内部阈值条件也蕴含 \(Q_E>E\)。阈值处

\[
Y^*=\frac{Q_E-E}{\phi},
\qquad
n=0.
\]

收入和 seller mass 在阈值处连续，不存在离散 tipping、multiplicity 或 hysteresis；真正的结果是 active set 改变后出现严格向上的 derivative kink：

\[
Y'_-=
\frac{\tau\phi Y^*}{D_0(\lambda^*)},
\qquad
Y'_+=
\frac{\tau\phi Y^*}{D_1(\lambda^*)}
>Y'_-.
\]

同时

\[
n'_-=0,
\qquad
n'_+=
\frac{\mu(1-\tau)\tau\phi^2Y^*}{F D_1(\lambda^*)}>0.
\]

不能把“kink”本身称为新贡献；贡献候选是该 active-set change 由 transaction-service payout 的空间收取与 local platform-order respending 联合产生。

## 8. 机制必要性：关闭再支出

正确的 no-respending counterfactual 不是把所有地方收入传播关闭，而是仅固定居民平台订单 \(\bar X_P\)，同时保留其他 nonplatform local-income propagation：

\[
\widehat Q=E+\bar X_P,
\qquad
\widehat n=
\frac{\mu(1-\tau)}{F}[\widehat Q-Q_E]_+.
\]

于是

\[
\frac{\partial\widehat n}{\partial r}=0.
\]

本地 payout 仍直接增加收入：

\[
\widehat Y=
\frac{B+r\bar X_P+(1-\tau)[\widehat Q-Q_E]_+}{1-c_0},
\qquad
\frac{\partial\widehat Y}{\partial r}
=
\frac{\bar X_P}{1-c_0}>0.
\]

但它不再移动 seller active set。这个对照把普通收入 incidence 与本文需要的 organization effect 分开：只有居民平台订单随本地收入重新形成时，payout location 才能改变 seller organization。

该必要性只在上述 receipt-only counterfactual 内成立。它不是对所有平台合同或一般均衡环境的普遍定理。

## 9. 与固定 seller mass benchmark 的不可约差异

若本地 seller routing share 固定为 \(\bar\theta\)，则

\[
Y(\bar\theta,r)
=
\frac{B+(1-\tau)\bar\theta E}
{1-c_0-\phi[r+(1-\tau)\bar\theta]}.
\]

这是一个平滑的 fixed-coefficient multiplier。改变 \(r\) 只重算收入 inverse，不会产生 entry threshold、active-set switch 或 seller-mass kink。因此，新的结果不能由固定 seller mass 下的 coefficient recomputation 单独推出。

## 10. 收入守恒与 fixed-cost incidence

本地收入账户为

\[
I_L
=c_0Y+r\phi Y
+(1-\tau)\theta(E+\phi Y).
\]

外部收入账户包含 numeraire 与未留存的线下支付、总部平台 take、外地 seller 收入以及外部订单中未被本地 sellers 捕获的部分：

\[
\begin{aligned}
I_H={}&(1-\alpha-\beta)Y
+\alpha(1-s)(1-\rho_A)Y\\
&+(\tau-r)\phi Y
+(1-\tau)(1-\theta)\phi Y\\
&+\tau E
+(1-\tau)(1-\theta)E.
\end{aligned}
\]

逐项相加满足

\[
I_L+I_H=Y+E.
\]

free entry 给出

\[
F=\mu(1-\tau)q.
\]

每个本地 seller 的 variable local factor income 为 \((1-\mu)(1-\tau)q\)，固定投入收入为 \(F\)，二者相加等于完整 net seller payout \((1-\tau)q\)。因此 \(F\) 没有重复计入；但该守恒依赖 variable 和 fixed inputs 都由本地居民提供。正式稿必须明确这一 incidence 假设。

## 11. 对原项目机制的保留与删减

原大项目的四层机制是：

1. market access 与消费价格；
2. local intermediation、平台租金与收入收取地；
3. local production、外销与外地竞争；
4. local-income propagation。

新的 EL 候选不是把四层全部恢复。它只保留一个能在约 2,000 词内闭合的交叉机制：

\[
\text{transaction-service payout location}
\rightarrow
\text{local disposable income}
\rightarrow
\text{resident platform orders}
\rightarrow
\text{seller free-entry active set}.
\]

market access 由 \(s\) 与 \(E\) 作为给定环境进入；完整价格福利、生产区位、税收、平台定价、facility location 和多地区 GE 留给大论文。这样做确实比原项目窄，但不是把平台机制再次压缩为固定 \(\omega\)：seller participation 已由 free-entry condition 内生决定。

## 12. Economics Letters 的正式重写边界

若进入正式重写，正文只保留：

1. 一个简短 benchmark，承认固定留值下的 recursive multiplier 属于已有框架；
2. proportional routing 与 seller free entry；
3. local transaction-service payout 的唯一解释；
4. 一个 Proposition：唯一 payout threshold 与连续 seller activation；
5. 一个 Corollary：阈值处收入和 seller mass 的 derivative kink；
6. 一个 mechanism-necessity result：固定居民平台订单后 \(\partial n/\partial r=0\)。

不进入正式稿：

- 原 scalar paper 的三个 nominal/real-income regions；
- continuous phase reversal；
- multiplicity、hysteresis 或离散 tipping；
- full spatial GE、平台最优定价、税收与 facility location；
- “China is currently above/below the threshold”等无数据定量判断。

建议暂定标题：

> **Platform Transaction-Service Payouts and Local Seller Entry**

标题仍可在写作阶段调整，但应避免让读者预期完整 multi-region GE 或 empirical China paper。

## 13. 允许与禁止的贡献表述

### 允许的谨慎表述

- “We isolate a channel through which the share of transaction-attributed service payouts accruing locally affects local seller participation through resident platform-order respending.”
- “Holding the platform take rate and consumer conditions fixed, increasing the transaction-service payout share accruing to a local service node can move the free-entry active set.”
- “When resident platform orders are held fixed, payout location no longer affects seller mass.”
- “Our result combines spatial income incidence with seller entry; the recursive multiplier and fee-entry components separately have well-established antecedents.”

### 禁止的表述

- “We are the first to study local value retention on platforms.”
- “Existing multiplier models ignore repeated leakage.”
- “Seller entry in e-commerce has not been studied.”
- “Local agents or human intermediaries are a new platform primitive.”
- “Revenue sharing changes seller entry, and this comparative static is itself novel.”
- “The kink itself is novel.”
- “The model proves that local revenue sharing is welfare improving.”
- “The institutional evidence identifies the receipt-only counterfactual.”

## 14. 七项 novelty contract 的最终核对

| 条件 | 状态 | 依据 |
|---|---|---|
| NC-1 Known benchmark nesting | PASS | scalar/fixed-mass model明确退化为标准 multiplier |
| NC-2 Incidence accounting | PASS | local/external ledger 守恒；fixed input incidence 已列明 |
| NC-3 Platform-specific endogenous margin | PASS | seller mass 由 routing 与 free entry 决定；外生 primitives 已明确列出 |
| NC-4 Non-reducible proposition | PASS_WITH_SCOPE | fixed seller mass 没有 active-set threshold；新结果需要 entry |
| NC-5 Observable mapping | PASS_CONDITIONALLY | payout、take rate、seller location、orders 可观察；服务质量固定是假设 |
| NC-6 Prior-art dominance test | PASS_CONDITIONALLY | bounded search 未发现同一联合定理；不构成 priority certification |
| NC-7 EL scope feasibility | PASS_WITH_STRICT_CUTS | 只保留一个 Proposition、一个 Corollary 与一个 necessity test |

## 15. 最终决策与下一检查点

本轮完成了正式重写前的 theorem-feasibility、机制必要性和有界 direct-prior audit，但没有完成绝对 priority certification。结论不是旧文献已经做过这个平台问题，而是：旧文献迫使我们停止把标准 recursive multiplier 当贡献；直接平台文献迫使我们停止把普通 seller entry 当贡献；二者共同把可保留的增量收窄到 transaction-service payout location、local respending 与 seller active set 的联合机制。

最终状态：

```text
STAGE_2_THEOREM_GATE = CONDITIONAL_PASS
RECOMMENDED_ACTION   = BEGIN_NEW_FORMAL_REWRITE_AFTER_CONFIRMATION
FORMAL_FILES         = UNCHANGED_IN_THIS_STAGE
```

进入重写前仍须接受两项不可删除的限制：

1. 直接 prior-art 检索是有界审计，不是绝对 priority 证明；
2. 固定服务质量、价格和采用率而只改变 payout location 是模型 exclusion restriction，不是已有数据已经识别的事实。

若接受这两项边界，下一步可以重构 `main.tex` 和 `appendix.tex`；若要求把 payout、服务质量和平台采用全部内生化，则该机制将超出当前 EL 篇幅，应并回完整大论文。
