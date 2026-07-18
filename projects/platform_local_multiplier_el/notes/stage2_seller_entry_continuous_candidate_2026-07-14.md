# Stage 2：连续 local-seller free-entry 候选模型

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
用途：theorem-feasibility gate；不是正式论文稿  
文件边界：本轮没有修改 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、`code/verify_model.py` 或 `output/paper.pdf`

## 1. 先给结论

这个候选模型在数学上可行，并且比现有标量 retention model 多出一个真正内生的 active-set：本地卖家是否进入平台以及进入多少，由平台佣金、固定进入成本、平台订单池和地方收入反馈共同决定。模型具有唯一均衡、显式解析解和一个真实的无进入 corner $n=0$，但在基准 routing technology 下不存在多重均衡或 hysteresis。

最有希望的结果不是再次计算一个 multiplier，而是以下联合命题：

> 平台整合在本地卖家尚未进入时把居民支出从本地代理转向外地卖家，因而降低地方收入；当订单池越过一个由 commission、fixed cost 和 local-demand feedback 共同决定的门槛后，本地卖家连续进入。佣金越高，进入门槛越晚；在外部市场接入足够强或本地卖家净留值足够高时，地方收入对整合的边际反应在门槛处由负转正。

这不是单一固定系数 SAM/Miyazawa inverse 能够推出的全局结果，因为 inverse 并不决定进入 active set、门槛位置或门槛两侧的 kink。不过，每一个给定 active set 内的收入解仍然是标准 household-closure inverse。因而本模型的准确状态是：

    mathematical_feasibility = PASS
    existence_and_uniqueness = PASS
    true_no_entry_corner = PASS
    multiplicity_or_hysteresis = NO_IN_BASELINE
    non_reducibility_to_one_fixed_inverse = CONDITIONAL_PASS
    direct_platform_prior_art_gate = PENDING_FOCUSED_AUDIT
    immediate_main_tex_rewrite = NOT_YET

## 2. Research architecture 与完成标准

### 2.1 研究问题

一个 small open region 同时面对两种平台效应：居民更多通过平台购买外地商品，以及本地卖家通过同一平台获得本地和外部订单。平台佣金和固定数字经营成本在什么条件下阻止本地卖家进入？进入门槛如何受到地方收入反馈影响？同一整合冲击能否在进入前后产生方向相反的地方收入反应？

### 2.2 方法设计

- **研究范式**：positivist analytical theory。
- **方法**：构造性均衡证明、complementarity/free-entry 条件、分段解析解和比较静态。
- **数据策略**：本阶段不使用数据；但每个 primitive 必须有 observable mapping。
- **有效性标准**：逐笔收入守恒；均衡存在且唯一；所有分母严格为正；进入与不进入条件互斥且完备；关闭 entry feedback 后严格嵌套固定系数 benchmark；解析导数接受数值差分核验。
- **设计限制**：价格、工资、平台佣金和 routing rule 均外生；不计算包含进入资源成本和劳动机会成本的完整 welfare；不内生化平台最优收费。

## 3. 环境与消费者渠道选择

地区 $L$ 是 small open region，地区 $H$ 包含外部卖家、平台总部和外部消费者。居民消费 retail composite $M$、本地 nontradable $N$ 和 numeraire $Z$：

\[
U=M^\alpha N^\beta Z^{1-\alpha-\beta},
\qquad
\alpha,\beta>0,
\quad \alpha+\beta<1.
\]

零售品由本地代理渠道 $A$ 与平台渠道 $P$ 组成：

\[
M=\left[(1-a)^{1/\eta}M_A^{(\eta-1)/\eta}
+a^{1/\eta}M_P^{(\eta-1)/\eta}\right]^{\eta/(\eta-1)},
\]

其中 $a\in(0,1)$、$\eta>1$。令

\[
p_P(z)=\bar p_Pe^{-z},
\]

则平台支出份额为

\[
s(z)=
\frac{ap_P(z)^{1-\eta}}
{(1-a)p_A^{1-\eta}+ap_P(z)^{1-\eta}}
\in(0,1),
\]

并且

\[
s_z=(\eta-1)s(1-s)>0.
\]

居民把 \(\alpha Y\) 用于零售品，其中

\[
X_A=(1-s)\alpha Y,
\qquad
X_P=s\alpha Y.
\]

本地 nontradable 支出为 $\beta Y$。地方固定工资和弹性供给闭合沿用现稿，因此本文的 $Y$ 是 nominal local income；相应价格指数只能用于 consumption-equivalent real income，不能称完整社会福利。

## 4. 平台订单、佣金与本地卖家进入

### 4.1 订单池与 routing

除本地居民的平台支出外，外部消费者还带来平台订单

\[
E(z)=\bar E e^{\varepsilon z},
\qquad \bar E>0,\quad \varepsilon\geq0.
\]

可供本地卖家争取的总订单池为

\[
Q(Y,z)=s(z)\alpha Y+E(z).
\tag{1}
\]

令 $n\geq0$ 为本地活跃平台卖家的连续质量，$\chi>0$ 为平台上外地卖家的有效 routing weight。平台以对消费者不可见的方式在本地与外地供给之间分配同质订单。本地卖家的订单份额和每个本地卖家的订单额分别为

\[
\theta(n)=\frac{n}{n+\chi},
\qquad
q(n,Y,z)=\frac{Q(Y,z)}{n+\chi}.
\tag{2}
\]

这一 routing rule 的作用是隔离空间 incidence：本地卖家进入改变订单收入属于哪个地区，但不改变消费者面对的 $p_P(z)$。它不是消费者对“本地标签”的偏好。

### 4.2 佣金、利润与固定成本

平台对本地卖家的 gross sales 收取比例佣金 $\tau\in[0,1)$。平台总部 $H$ 收取 $\tau q$，本地卖家收到 $(1-\tau)q$。令 $\mu\in(0,1)$ 是卖家净收入中的 operating-surplus share，$F>0$ 是进入所需的固定本地投入。每个卖家在支付固定成本前后的 operating profit 为

\[
\pi(n,Y,z)=
\mu(1-\tau)\frac{Q(Y,z)}{n+\chi}-F.
\tag{3}
\]

自由进入写成 complementarity condition：

\[
n\geq0,\qquad
F-\mu(1-\tau)\frac{Q}{n+\chi}\geq0,\qquad
n\left[F-\mu(1-\tau)\frac{Q}{n+\chi}\right]=0.
\tag{4}
\]

若 $n>0$，卖家净利润为零，固定成本前的 operating surplus 恰好支付 $F$。基准假设 variable inputs 和 fixed-entry inputs 均位于 $L$，所以一元本地卖家 gross sale 中，$1-\tau$ 成为本地工资、固定投入收入或本地经营收入，$\tau$ 成为总部收入。净利润为零不意味着本地没有收入；它意味着本地净 seller-owner rent 在自由进入边际上为零。

定义 break-even order pool

\[
Q_E(\tau)=\frac{F\chi}{\mu(1-\tau)}.
\tag{5}
\]

由（2）—（4），本地卖家实际取得的 gross orders 满足

\[
\theta(n)Q=
\begin{cases}
0,&Q\leq Q_E,\\[2mm]
Q-Q_E,&Q>Q_E.
\end{cases}
=\left[Q-Q_E\right]_+.
\tag{6}
\]

当 $Q\leq Q_E$ 时，存在真正的无进入 corner $n=0$；当 $Q>Q_E$ 时，卖家质量连续调整，而不是外生指定一个 local-seller share。

## 5. Income generation、receipt 与 spending 的空间守恒

| 交易或收入 | 收入产生地 | 收取地 | 后续支出处理 |
|---|---|---|---|
| Autonomous base income $B>0$ | $L$ | $L$ 居民 | 按 $\alpha,\beta$ 继续支出 |
| 本地代理销售 $X_A$ 的 $\rho_A$ 部分 | $L$ 的代理、劳动和所有者 | $L$ | 进入下一轮地方支出 |
| 本地代理销售的 $1-\rho_A$ 部分 | $H$ | $H$ | small-region benchmark 中不回流 |
| 平台订单由外地卖家承接 | $H$ | $H$ | 不进入 $L$ 的下一轮支出 |
| 本地卖家承接订单的 $1-\tau$ 部分 | $L$ 的 variable/fixed inputs | $L$ | 进入下一轮地方支出 |
| 同一订单的佣金 $\tau$ | 平台总部中介服务 | $H$ | 不进入 $L$ 的下一轮支出 |
| 本地 nontradable 支出 $\beta Y$ | $L$ | $L$ | 进入下一轮地方支出 |
| 外部订单 $E$ | 支出发起于 $H$ | 若由本地卖家承接，则 $1-\tau$ 归 $L$ | 形成第一轮 $L$ 收入后继续传播 |

因此，平台“发生在本地的一笔消费”与“本地卖家从外部获得的一笔订单”不能由同一个固定 retention coefficient 代替。前者在无本地卖家时完全流向 $H$，后者只有在进入 active set 开启后才成为 $L$ 的收入。

## 6. 均衡定义与唯一解析解

### 6.1 均衡定义

给定 $z$，一个 local-income equilibrium 是

\[
(M_A,M_P,N,Z,Y,n,\theta)
\]

使得：

1. 家庭最优化并产生平台份额 $s(z)$；
2. 平台 routing 满足（2）；
3. seller entry 满足（4）；
4. 所有本地收入按上表守恒；
5. 地方收入满足

\[
Y=B+\beta Y+\rho_A(1-s)\alpha Y
+(1-\tau)\theta(n)[s\alpha Y+E].
\tag{7}
\]

使用（6），收入映射可以写成

\[
T(Y)=B+c_0Y
+(1-\tau)[E+s\alpha Y-Q_E]_+,
\qquad
c_0=\beta+\alpha\rho_A(1-s).
\tag{8}
\]

### 6.2 存在性、唯一性与稳定性

定义

\[
D_0=1-\beta-\alpha\rho_A(1-s)>0,
\tag{9}
\]

\[
D_1=1-\beta-
\alpha\bigl[\rho_A(1-s)+(1-\tau)s\bigr]>0.
\tag{10}
\]

因为 \(\rho_A\leq1\)、\(1-\tau\leq1\)，有

\[
D_0,D_1\geq1-\alpha-\beta>0.
\]

映射（8）连续、将 \(\mathbb R_+\) 映射到自身，并且其两个线性区间的斜率分别为

\[
c_0<1,
\qquad
c_1=c_0+\alpha s(1-\tau)<1.
\]

所以 $T$ 是 contraction，均衡存在、唯一，并且从任意 $Y_0\geq0$ 进行收入轮次迭代都收敛到该均衡。

### 6.3 两个候选分支

强制关闭 entry 时的收入和平台订单池为

\[
Y_0=\frac{B}{D_0},
\qquad
Q_0=E+\frac{\alpha sB}{D_0}.
\tag{11}
\]

定义

\[
\mathcal A(z)
\equiv E(z)+\frac{\alpha s(z)B}{D_0(z)},
\qquad
\mathcal C(\tau)
\equiv\frac{F\chi}{\mu(1-\tau)}.
\tag{12}
\]

于是 $Q_0=\mathcal A$、$Q_E=\mathcal C$。若 $\mathcal A\leq\mathcal C$，唯一均衡为

\[
n=0,
\qquad
Y=Y_0=\frac{B}{D_0}.
\tag{13}
\]

若 $\mathcal A>\mathcal C$，自由进入分支为

\[
Y_1=
\frac{B+(1-\tau)E-F\chi/\mu}{D_1},
\tag{14}
\]

\[
n=
\frac{\mu(1-\tau)D_0}{FD_1}
[\mathcal A-\mathcal C]>0.
\tag{15}
\]

证明分支合法性的关键恒等式是

\[
Q_1-Q_E=
\frac{D_0}{D_1}(Q_0-Q_E).
\tag{16}
\]

因此 inactive candidate 合法当且仅当 active candidate 不合法，反之亦然。不存在两者同时成立的参数区间。在 $\mathcal A=\mathcal C$ 时，$n=0$，并且（13）与（14）给出同一个 $Y$。

## 7. 候选主命题：commission-delayed seller activation

**Proposition 1（进入门槛、连续进入与地方收入增量）**  
在上述 assumptions 下，均衡唯一。本地卖家进入当且仅当

\[
\boxed{
E(z)+\frac{\alpha s(z)B}
{1-\beta-\alpha\rho_A[1-s(z)]}
>
\frac{F\chi}{\mu(1-\tau)}.}
\tag{17}
\]

进入后的本地 seller mass 由（15）给出。相对于禁止本地卖家进入的 benchmark，进入引致的地方收入增量为

\[
\boxed{
Y_1-Y_0=
\frac{(1-\tau)[\mathcal A(z)-\mathcal C(\tau)]}{D_1}>0.}
\tag{18}
\]

式（17）的左侧包含两个 access source：外部订单 $E$，以及由地方收入循环融资的居民平台订单 $\alpha sB/D_0$。右侧是由固定进入成本、外地 seller competition 和平台 take rate 共同决定的 break-even order pool。

令

\[
d_A=1-\beta-\alpha\rho_A>0.
\]

因为 $D_0=d_A+\alpha\rho_As$，有

\[
\mathcal A_z
=E_z+
\frac{\alpha B d_A}{D_0^2}s_z>0
\tag{19}
\]

只要 $E_z\geq0$。因此进入门槛至多一个。若 $E(z)=\bar E e^{\varepsilon z}$ 且 $\varepsilon>0$，则

\[
\lim_{z\to-\infty}\mathcal A(z)=0,
\qquad
\lim_{z\to\infty}\mathcal A(z)=\infty,
\]

所以存在唯一 $z^*$ 满足

\[
\mathcal A(z^*)=\mathcal C(\tau).
\]

由 implicit-function theorem，

\[
\boxed{
\frac{dz^*}{d\tau}
=
\frac{F\chi}
{\mu(1-\tau)^2\mathcal A_z(z^*)}>0.}
\tag{20}
\]

同理，$F$ 或 $\chi$ 增加使门槛推迟，$\mu$、$B$、$\beta$ 或 $\rho_A$ 增加使门槛提前。后两个比较静态来自更强的 pre-entry local-demand feedback，而不是平台 seller-profit equation 本身。

## 8. 候选推论：进入前后的符号反转

在无进入区间，$E$ 尚未成为 $L$ 收入，因为所有平台订单均由外地卖家承接。于是

\[
\frac{dY_0}{dz}
=-
\frac{\alpha\rho_A s_zY_0}{D_0}<0
\qquad(\rho_A>0).
\tag{21}
\]

其含义是：平台价格下降把居民零售支出从具有本地收入份额的代理渠道转向完全外流的平台订单。

在进入区间，令

\[
N_1=B+(1-\tau)E-F\chi/\mu=D_1Y_1>0.
\]

则

\[
\frac{dY_1}{dz}
=
\frac{
(1-\tau)E_zD_1
+\alpha[(1-\tau)-\rho_A]s_zN_1
}{D_1^2}.
\tag{22}
\]

所以进入后地方收入上升的充要条件为

\[
(1-\tau)E_zD_1
>
\alpha[\rho_A-(1-\tau)]s_zN_1.
\tag{23}
\]

若 $1-\tau\geq\rho_A$ 且 $E_z>0$，该条件自动成立。更一般地，即使本地卖家净留值低于本地代理，足够强的 outward market-access growth 仍可使（23）成立。

**Corollary 1（entry-induced phase reversal）**  
若存在唯一 $z^*$，$\rho_A>0$，且进入后的参数满足（23），则 $Y(z)$ 在 $z^*$ 连续但不可微：进入前严格下降，进入后严格上升。该结果是一个 V-shaped local-income response 与 active-seller kink，而不是收入水平的离散跳跃。

佣金还具有第二个清楚的 active-region 效果：

\[
\frac{\partial Y_1}{\partial\tau}
=-
\frac{ED_1+\alpha sN_1}{D_1^2}<0,
\tag{24}
\]

并且

\[
\frac{\partial n}{\partial\tau}<0.
\tag{25}
\]

因此 take rate 同时推迟本地卖家进入，并在进入后降低本地 seller mass 和地方收入。

## 9. Multiplicity 与 tipping 审计

### 9.1 基准结论

基准模型不存在 multiplicity 或 hysteresis。原因不是假定了唯一性，而是 per-seller order $Q/(n+\chi)$ 随 $n$ 严格下降，加上地方支出映射的最大斜率小于一。式（16）进一步证明 no-entry 和 positive-entry candidates 的合法区间不重叠。

模型具有：

- 一个真实的 $n=0$ corner；
- 一个唯一的进入阈值 $z^*$；
- 在阈值处连续的 $n$ 和 $Y$；
- 一个 derivative kink。

因此不能把它写成“discontinuous tipping”或“multiple equilibria”。最准确的术语是 **continuous seller activation threshold**。

### 9.2 什么额外机制才会产生真正 tipping

真正的 multiplicity 需要额外 increasing returns，例如 seller mass 提高平台排名、信任或履约密度，使一个卖家的订单获得率在低 $n$ 区间随总 $n$ 上升；或者平台承担只有在足够多卖家加入后才值得支付的固定本地区域运营成本。形式上可将 routing weight 改为 $v(n)n$，其中 $v'(n)>0$。这可能使 entrant payoff 不再单调，从而允许 $n=0$ 与 $n>0$ 并存。

该扩展不应自动加入 EL：它需要新的 primitive、稳定性选择和 welfare 讨论，而且容易把结果变成对任意 increasing-return function 的假设复述。基准模型没有为了追求更强叙事而人为制造多重均衡。

## 10. 关闭 entry feedback 后如何退化为标准 inverse

固定本地 seller routing share 为外生常数 \(\bar\theta\in[0,1]\)，不允许它由 entry condition 调整。收入变为

\[
Y(\bar\theta)=
\frac{B+(1-\tau)\bar\theta E}
{1-\beta-\alpha\rho_A(1-s)
-\alpha s(1-\tau)\bar\theta}.
\tag{26}
\]

这就是一个固定 coefficient 的 scalar SAM/Miyazawa household-closure inverse。令 \(\bar\theta=0\) 得到（13）；指定任何正 \(\bar\theta\) 只会重新计算 first-round vector 和 propagation coefficient。

因此必须精确区分：

1. **仍是 coefficient recomputation 的部分**：给定 active set 后的 $Y_0$、$Y_1$、式（18）中的传播分母，以及式（26）。
2. **固定 inverse 不能单独产生的部分**：complementarity condition、进入门槛（17）、佣金引起的门槛移动（20）、$n=0$ 与 $n>0$ 的 active-set 切换，以及阈值两侧的符号反转和 kink。

所以这个候选模型不是“完全脱离 SAM/Miyazawa”，也不需要如此。它的数学工具是已知的，候选贡献必须来自平台 fee—seller entry—spatial receipt—local spending 的新经济映射。

## 11. 创新性三层判定

### A. 数学工具与理论祖先

条件于 $n=0$ 或 $n>0$，收入方程仍属于 Miyazawa/SAM/Type-II household closure；contraction、piecewise-linear fixed point 和 free-entry zero-profit 也都是标准工具。这些不能作为创新声明。

### B. 直接平台文献覆盖到哪里

定向检索已经发现明显相邻的直接先例：

- [Etro, “Platform competition with free entry of sellers” (IJIO, 2023)](https://doi.org/10.1016/j.ijindorg.2022.102903) 已同时研究 platform commissions、seller monopolistic competition 和 free entry；
- [Einav, Farronato and Levin, “Peer-to-Peer Markets”](https://www.nber.org/papers/w21496) 明确研究平台降低进入成本、transaction fees、seller entry，并展示由 marketplace scale economy 导致的多重均衡；
- [Kirpalani and Philippon, “Data Sharing and Market Power with Two-Sided Platforms”](https://www.nber.org/papers/w28023) 包含平台/外部市场、seller free entry 和平台收费；
- [Anderson and Bedre-Defolie, “Hybrid Platform Model”](https://cepr.org/publications/dp16243) 通过平台 fee 内生化 seller participation；
- [Fan et al., “The Alibaba Effect”](https://doi.org/10.1016/j.jinteco.2018.07.002) 已将 e-commerce 表述为降低或消除 spatial market-entry fixed cost；
- 现有 Stage 2 audit 已记录 spatial e-commerce、regional income 和 ownership-incidence 文献。

所以以下单独结果都不新：佣金降低 entry、固定成本产生 entry threshold、平台扩大 seller access、免费进入使净利润为零，或者地方收入按固定系数传播。

### C. 候选的新经济命题

本模型仍可能形成增量的部分是上述对象的**共同闭环**：

1. 居民 channel substitution 在无本地 seller 时造成地方 demand leakage；
2. 同一平台产生可供本地 seller 竞争的 local-plus-external order pool；
3. commission 决定进入盈利性，同时把平台 rent 的 receipt location 固定在 $H$；
4. seller entry 把订单的 generation/receipt location 内生地从 $H$ 切换到 $L$；
5. 该收入再进入 local spending，反过来改变 seller entry threshold；
6. 由此得到进入前负、进入后可正的 local-income response，以及 commission-delayed kink。

本轮定向检索没有发现一篇直接平台论文同时包含这六项并推出式（17）—（23）的空间收入预测。但这不是穷尽式 priority claim。正式写稿前仍需围绕“platform seller entry + regional/local multiplier + commission incidence + local/remote seller origin”进行一次专门 equation-level audit。

## 12. Observable mapping 与可证伪预测

| Primitive / equilibrium object | 可观测对应 |
|---|---|
| $s(z)$ | 居民线上/平台零售支出份额；平台相对价格或覆盖冲击 |
| $E(z)$ | 本地区卖家收到的异地潜在订单或平台外销市场规模 |
| \(\tau\) | referral fee、commission、advertising/service take rate 的合计 ad-valorem wedge |
| $n$ | 本地区活跃平台卖家数、开店数或持续有交易卖家数 |
| $F$ | onboarding、数字运营、认证、库存、广告和固定履约成本 |
| \(\chi\) | 与本地卖家争夺曝光/订单的外地卖家有效质量或 routing competition |
| \(\mu\) | 扣除平台费后的 seller operating-margin share |
| \(\rho_A\) | 传统代理/本地零售一元销售形成的本地工资与经营收入份额 |
| \(B\) | 非平台 tradable/base-sector local income |
| \(\beta\) | 本地 nontradable 支出倾向 |

直接预测包括：

1. 更高 commission、fixed cost 或外地 seller competition 使本地 seller entry 出现在更高的平台 penetration/market-access 水平；
2. 更高 base income 或更强 pre-entry local spending feedback 使 entry 提前；
3. active seller count 在门槛处从零连续开始增长，收入水平连续但斜率出现 kink；
4. 在 entry 之前，平台 penetration 越高，本地代理留值损失越大；
5. 在 entry 之后，外销增长越强、seller net-of-fee retention 越高，收入反应越可能转正；
6. 同一平台 adoption shock 对地区的影响会随初始 $B,\beta,\rho_A,F,\chi$ 而跨越不同 active sets，而不只是产生连续大小差异。

这些预测可以在后续大论文中用 seller-origin、buyer-origin、commission、active-shop、local employment 和 local business-income 数据检验；EL 本身仍可保持纯理论。

## 13. Economics Letters 的 2,000-word 可行性

该模型可以压缩为一篇 EL，但条件严格：

1. 删除现稿的 recursive-multiplier proposition、finite-threshold proposition 和 $s^\dagger<1/2$ 结果；这些只能作为已知 benchmark 或不再出现。
2. 正文只保留一个主命题：式（17）、（18）、（20）；一个推论：式（21）—（23）。
3. 家庭 CES 只保留必要的 $s(z)$ 与 $s_z>0$，完整 expenditure-minimization 推导压缩到附录。
4. 不加入两地区矩阵、平台最优收费、seller heterogeneity、税收、迁移、资本区位或 true tipping extension。
5. 建议篇幅：Abstract 90；Introduction 330；Model and accounting 650；Proposition and corollary 650；Conclusion 100；proof appendix 由极紧凑代数完成。

在“主文与附录合计不超过 1,950 个 texcount 文本词”的自定纪律下，模型处于可写但偏紧的范围。若要求把家庭优化、free-entry complementarity、contraction proof 和全部比较静态都用完整 prose 展开，则很可能超过 EL 篇幅；需要依赖公式密度和高度压缩的证明，不能再加入第二个经济机制。

可能的标题是：

> **Platform Seller Entry and Local Income Capture**

比当前标题更准确，因为新的主对象已经从固定 retention multiplier 转为 endogenous local seller activation。

## 14. 数学核验

使用固定随机种子 20260714，在合法参数域随机抽取 10,000 组参数，并完成以下核验：

- piecewise income map 的迭代解与（13）/（14）闭式解一致；
- complementarity condition 与 active-set 判定一致；
- 所有 $D_0,D_1,Y$ 为正，$n\geq0$；
- 式（21）/（22）的 $z$ 导数与中心差分一致；
- 式（24）的 commission 导数与中心差分一致。

结果为：

| 检查 | 结果 |
|---|---:|
| 参数抽样 | 10,000 |
| positive-entry cases | 1,598 |
| 可行性或符号违例 | 0 |
| fixed-point / entry residual 最大值 | \(8.54\times10^{-13}\) |
| $dY/dz$ 最大中心差分误差 | $1.18\times10^{-8}$ |
| $\partial Y/\partial\tau$ 最大中心差分误差 | $9.22\times10^{-9}$ |

## 15. 与离散 entry 候选的比较

这里的“离散候选”指代表性本地卖家或本地 seller sector 只在 enter/not-enter 之间选择的模型；不预设另一份候选模型的具体函数形式。

| 比较维度 | 连续 free-entry mass（本备忘录） | 离散/binary entry |
|---|---|---|
| 进入边界 | 有真实 $n=0$ corner；越过门槛后 $n$ 从零连续增长 | 越过门槛后 seller activity 通常离散跳升 |
| 收入路径 | $Y$ 连续、斜率出现 kink | $Y$ 可能跳跃，叙事更接近 discontinuous tipping |
| 均衡唯一性 | per-seller orders 递减且收入映射 contraction，唯一性强 | 收入反馈可能使 enter 与 no-enter 同时自洽，需要 equilibrium selection |
| 数学透明度 | 两个分支均有闭式解，门槛与 comparative statics 可逐项证明 | 单个进入条件更短，但多重均衡区间和选择规则会增加证明负担 |
| Observable mapping | $n$ 直接对应 active seller count/mass，适合地区异质性与 intensive margin | 更适合观察“某类产业/平台节点是否出现”，但弱化 seller-count variation |
| 经济强度 | 给出稳健的 activation threshold 与 kink，不夸大 tipping | 可产生更强的 jump/hysteresis 结论，但更依赖 indivisibility 和协调假设 |
| 主要风险 | routing rule 较 reduced-form；free entry 使净 owner profit 为零 | 单一代表卖家可能缺乏 aggregate microfoundation；结论对离散设定敏感 |
| EL 适配性 | **更优**：唯一均衡、解析解、一个 proposition 即可 | 若出现 multiplicity，必须解释选择、稳定性和政策含义，篇幅风险更高 |

推荐连续候选作为 EL baseline。离散候选只有在它能产生一个有明确平台 microfoundation、并且数据上可区分的 jump 或 hysteresis 命题时才应优先；不能仅因为离散模型的图形更醒目而选择它。

## 16. 七项 novelty contract 判定

| 条件 | 判定 | 原因 |
|---|---|---|
| Known benchmark nesting | PASS | 式（26）明确把固定 seller share 识别为标准 inverse |
| Incidence accounting | PASS | generation、receipt、spending location 分开守恒 |
| Platform-specific choice primitive | PASS | commission、routing 和 free-entry complementarity 内生决定 $n,\theta$ |
| Non-reducible proposition | CONDITIONAL PASS | active-set threshold 与 kink 不能由一个固定 inverse 推出；各分支内部仍是标准 inverse |
| Observable mapping | PASS | fee、seller origin、active sellers、external orders、margin 和 local income 均可对应数据 |
| Prior-art dominance test | PENDING | 已发现 fee/free-entry 强先例，但尚未发现同一 spatial-income loop；需要专门查重 |
| EL scope feasibility | PASS WITH CUTS | 只能保留一个 proposition 和一个 corollary，删除现稿其他结果 |

## 17. 最终 gate 建议

这个 continuous-entry candidate 足以通过**数学可行性关**，也通过了“不是单纯把 $\omega$ 换成另一组固定系数”的最低要求。它尚未通过最终创新性关，因为 commission 与 seller free entry 本身已有强直接先例。

下一步应当只做一件事：对式（17）—（23）进行聚焦的 direct-platform prior-art audit，搜索是否已有模型把 local/remote seller origin、platform commission、seller entry 和 regional income respending 同时闭合并推出同样的 threshold/kink。若没有直接先例，则可以据此冻结新模型并重写 EL；若已有，则停止独立 EL，并把该模型并入大论文作为 access—capture mechanism。

在完成这一步之前，正式 `main.tex` 继续冻结。
