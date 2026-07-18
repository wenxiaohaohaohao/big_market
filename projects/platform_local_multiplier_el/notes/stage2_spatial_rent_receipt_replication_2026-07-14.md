# Stage 2：spatial rent-receipt candidate 独立解析复核

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
性质：独立 algebra、income-incidence 与 counterfactual replication  
文件边界：未修改 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、`code/verify_model.py` 或 `output/paper.pdf`

## 1. 复核结论

从 primitive income flows、seller zero-profit condition 和 household spending closure 重新推导后，候选模型的核心解析结果成立：

1. income map、$D_0(\lambda)$、$D_1(\lambda)$ 及其正性正确；
2. no-entry 与 positive-entry 分支均有唯一闭式解；
3. 恒等式
   \[
   Q_1-Q_E=\frac{D_0}{D_1}(Q_0-Q_E)
   \]
   正确，因此两个 active sets 互斥且完备；
4. 在 $Q_0(0)<Q_E<Q_0(1)$ 下，存在唯一 $\lambda^*\in(0,1)$；
5. $Y$ 和 $n$ 在阈值处连续，$Y$ 的右导数严格大于左导数，$n$ 的左导数为零、右导数严格为正；
6. 固定 seller mass 时只剩平滑的 fixed-coefficient multiplier；
7. 固定居民平台订单后，seller entry 完全不随 $\lambda$ 变化。因此 local platform respending 是“receipt location 改变 seller active set”的必要机制。

没有发现实质代数错误。发现一处排版错误和三项必须在正式写作中收紧的经济解释：

- 原候选式（22）分子中的 `phi` 缺少 LaTeX 反斜杠，应为 $\phi$；
- “no respending” 必须明确究竟只冻结平台订单，还是冻结所有 household induced spending；两种定义都给出 $dn/d\lambda=0$，但收入导数不同；
- $\lambda$ 只有在 local commission receiver 的支出倾向与居民相同的假设下，才是纯 receipt share。若接收者储蓄或外流，应另设 marginal spending propensity；
- fixed cost $F$ 必须由本地要素提供。若其支付给总部或外部软件/广告服务商，本地收入方程需要扣除相应外流。

## 2. 只从 primitives 建立收入账本

固定渠道整合状态，令

\[
\phi=\alpha s>0,
\qquad
c_0=\beta+\alpha\rho_A(1-s),
\qquad
\bar d=1-c_0.
\tag{R1}
\]

本地居民平台支出为 $\phi Y$，外部消费者订单为 $E$，所以 seller-facing order pool 为

\[
Q=E+\phi Y.
\tag{R2}
\]

本地 seller mass 为 $n\geq0$，外地 seller routing weight 为 $\chi>0$：

\[
\theta(n)=\frac{n}{n+\chi},
\qquad
q(n)=\frac{Q}{n+\chi}.
\tag{R3}
\]

平台 take rate 为 $\tau\in(0,1)$。本地居民交易产生的 commission 中，$\lambda\tau\phi Y$ 由本地服务节点或本地收入接受者收取，其余由远程总部收取。外部订单 $E$ 产生的 commission 全部归总部。本地 seller 获得其 gross sales 的 $1-\tau$。

### 2.1 居民支出的完整守恒

本地居民一元收入的本地 receipts 为

\[
R_L^Y=
\left[c_0+\lambda\tau\phi
+(1-\tau)\theta\phi\right]Y.
\tag{R4}
\]

外部 receipts 为

\[
R_H^Y=
\left[1-c_0-\lambda\tau\phi
-(1-\tau)\theta\phi\right]Y.
\tag{R5}
\]

由于 $R_L^Y+R_H^Y=Y$，居民支出没有遗漏或重复。式（R4）中的四个本地项目分别是 nontradable income、传统代理留值、local commission receipt 和本地 seller payout。

### 2.2 外部订单的完整守恒

外部订单形成的本地与外部 receipts 分别为

\[
R_L^E=(1-\tau)\theta E,
\tag{R6}
\]

\[
R_H^E=
\left[\tau+(1-\tau)(1-\theta)\right]E.
\tag{R7}
\]

同样有 $R_L^E+R_H^E=E$。这里把 $E$ 的全部 commission 留在总部是一个明确的基准 assumption，而不是由代数要求的结论。

### 2.3 Fixed cost 不重复计算的条件

若每个 seller 的 variable local-factor payment 是 $(1-\mu)(1-\tau)q$，fixed local-input payment 是 $F$，free entry 时

\[
F=\mu(1-\tau)q.
\]

二者之和恰为

\[
(1-\mu)(1-\tau)q+F=(1-\tau)q.
\]

因此在地区收入中计入完整 net-of-fee seller payout、同时在私人利润中扣除 $F$，没有 double counting，前提是 $F$ 确实支付给本地要素。

## 3. Free entry 与 aggregate local-seller orders

Seller complementarity condition 为

\[
n\geq0,
\qquad
F-\mu(1-\tau)\frac{Q}{n+\chi}\geq0,
\qquad
n\left[F-\mu(1-\tau)\frac{Q}{n+\chi}\right]=0.
\tag{R8}
\]

定义

\[
Q_E=\frac{F\chi}{\mu(1-\tau)}.
\tag{R9}
\]

若 $Q\leq Q_E$，唯一 aggregate entry outcome 是 $n=0$。若 $Q>Q_E$，zero profit 给出

\[
n=\frac{\mu(1-\tau)}F(Q-Q_E)>0,
\tag{R10}
\]

并且

\[
\theta(n)Q=Q-Q_E.
\tag{R11}
\]

合并两个区域：

\[
\theta(n)Q=[Q-Q_E]_+.
\tag{R12}
\]

## 4. Income map 与存在唯一性

由 $Y=B+R_L^Y+R_L^E$ 以及式（R12），收入映射为

\[
T(Y;\lambda)=
B+c_0Y+\lambda\tau\phi Y
+(1-\tau)[E+\phi Y-Q_E]_+.
\tag{R13}
\]

定义

\[
D_0(\lambda)=1-c_0-\lambda\tau\phi
=\bar d-\lambda\tau\phi,
\tag{R14}
\]

\[
D_1(\lambda)
=D_0(\lambda)-(1-\tau)\phi
=\bar d-\phi[1-\tau+\lambda\tau].
\tag{R15}
\]

由于 $\rho_A\leq1$、$\lambda\leq1$，

\[
D_1\geq1-\alpha-\beta>0,
\qquad
D_0>D_1>0.
\tag{R16}
\]

映射的两个斜率分别为 $1-D_0$ 与 $1-D_1$，都位于 $[0,1)$。所以 $T$ 是全局 contraction，在 $\mathbb R_+$ 上存在唯一正 fixed point。给定 $Y$ 后，式（R8）又唯一决定 aggregate $n$，故完整均衡唯一。

## 5. 两个分支、订单池恒等式与 active-set 完备性

### 5.1 No-entry candidate

若 $n=0$，

\[
Y_0(\lambda)=\frac{B}{D_0(\lambda)},
\tag{R17}
\]

\[
Q_0(\lambda)=E+\frac{\phi B}{D_0(\lambda)}.
\tag{R18}
\]

该分支合法当且仅当 $Q_0\leq Q_E$。

### 5.2 Positive-entry candidate

若 $n>0$，

\[
Y_1(\lambda)=
\frac{B+(1-\tau)(E-Q_E)}{D_1(\lambda)}
=
\frac{B+(1-\tau)E-F\chi/\mu}{D_1(\lambda)}.
\tag{R19}
\]

令 $Q_1=E+\phi Y_1$。从式（R19）直接消去得到

\[
\begin{aligned}
Q_1-Q_E
&=E-Q_E+
\frac{\phi[B+(1-\tau)(E-Q_E)]}{D_1}\\
&=\frac{D_0(E-Q_E)+\phi B}{D_1}\\
&=\frac{D_0}{D_1}(Q_0-Q_E).
\end{aligned}
\tag{R20}
\]

因为 $D_0/D_1>0$，$Q_1-Q_E$ 与 $Q_0-Q_E$ 同号。因此：

\[
Q_0\leq Q_E
\Longleftrightarrow n=0,
\qquad
Q_0>Q_E
\Longleftrightarrow n>0.
\tag{R21}
\]

不存在两个分支同时合法的参数区间，也没有遗漏第三个 aggregate equilibrium。

## 6. Receipt-localization threshold

由式（R18），

\[
\frac{dQ_0}{d\lambda}
=\frac{\tau\phi^2B}{D_0(\lambda)^2}>0.
\tag{R22}
\]

若

\[
Q_0(0)<Q_E<Q_0(1),
\tag{R23}
\]

则连续性和严格单调性保证存在唯一 $\lambda^*\in(0,1)$，满足 $Q_0(\lambda^*)=Q_E$。条件（R23）还自动推出 $Q_E>E$。解

\[
E+\frac{\phi B}{\bar d-\lambda^*\tau\phi}=Q_E.
\]

得到

\[
\boxed{
\lambda^*=
\frac{
\bar d-\phi B/(Q_E-E)
}{\tau\phi}.}
\tag{R24}
\]

因此，原候选式（22）的经济和代数内容正确；源文件中的 `phi` 应排版为 `\phi`。

## 7. 阈值连续性与一侧导数

在 $\lambda=\lambda^*$，

\[
Y^*=\frac{Q_E-E}{\phi}.
\tag{R25}
\]

由 $Q_0=Q_E$ 和式（R20），$Q_1=Q_E$，故

\[
Y_0(\lambda^*)=Y_1(\lambda^*)=Y^*,
\qquad
n(\lambda^*)=0.
\tag{R26}
\]

所以收入和 seller mass 均连续，没有 level jump。

No-entry 分支的一侧导数为

\[
\left.\frac{dY}{d\lambda}\right|_-
=\frac{\tau\phi Y^*}{D_0(\lambda^*)}.
\tag{R27}
\]

Positive-entry 分支的一侧导数为

\[
\left.\frac{dY}{d\lambda}\right|_+
=\frac{\tau\phi Y^*}{D_1(\lambda^*)}.
\tag{R28}
\]

由于 $D_1<D_0$，

\[
\boxed{
\left.\frac{dY}{d\lambda}\right|_+
-
\left.\frac{dY}{d\lambda}\right|_-
=\tau\phi Y^*
\left(\frac1{D_1}-\frac1{D_0}\right)>0.}
\tag{R29}
\]

在 active region，式（R10）给出

\[
\frac{dn}{d\lambda}
=\frac{\mu(1-\tau)\phi}{F}
\frac{dY_1}{d\lambda}.
\]

所以

\[
\boxed{
\left.\frac{dn}{d\lambda}\right|_-
=0,
\qquad
\left.\frac{dn}{d\lambda}\right|_+
=
\frac{
\mu(1-\tau)\tau\phi^2Y^*
}{FD_1(\lambda^*)}>0.}
\tag{R30}
\]

阈值的准确性质是 continuous activation with an upward derivative kink，不是 discontinuous tipping 或 hysteresis。

## 8. 固定 seller mass counterfactual

固定 seller mass $\bar n$，等价于固定

\[
\bar\theta=\frac{\bar n}{\bar n+\chi}.
\]

收入方程为

\[
Y=B+c_0Y+\lambda\tau\phi Y
+(1-\tau)\bar\theta(E+\phi Y),
\]

所以

\[
\boxed{
Y(\bar\theta,\lambda)=
\frac{B+(1-\tau)\bar\theta E}
{1-c_0-\phi[\lambda\tau+(1-\tau)\bar\theta]}.}
\tag{R31}
\]

这是一条标准 fixed-coefficient multiplier。$\lambda$ 平滑改变收入，但不存在 $\lambda^*$ 或 active-set kink。

在一个正进入均衡点固定 $\bar\theta=\theta(n)<1$，固定-mass 导数为

\[
\left.\frac{dY}{d\lambda}\right|_{\bar n}
=\frac{\tau\phi Y}{D_{\bar\theta}},
\]

\[
D_{\bar\theta}
=1-c_0-\phi[\lambda\tau+(1-\tau)\bar\theta].
\tag{R32}
\]

允许 free entry 时，边际新增订单通过 seller-mass 调整全部成为本地 seller orders，因此分母为 $D_1$。当 $\chi>0$、$n<\infty$ 时，$\bar\theta<1$，从而

\[
D_1<D_{\bar\theta},
\]

free-entry income response 严格大于固定-mass response。该差异是 endogenous entry 的边际放大，不是收入水平的额外记账项。

## 9. No-respending counterfactual 的两种精确定义

原候选把 “other income” 留作文字占位。为避免 counterfactual 含义不清，应区分以下两个关闭方式。

### 9.1 只关闭 platform-order respending

把居民平台订单固定为 $\bar X_P$，但保留 nonplatform local-income propagation $c_0\widehat Y$：

\[
\widehat Q=E+\bar X_P.
\tag{R33}
\]

Seller entry 为

\[
\widehat n=
\frac{\mu(1-\tau)}F
[\widehat Q-Q_E]_+,
\tag{R34}
\]

与 $\lambda$ 无关。收入为

\[
\boxed{
\widehat Y(\lambda)=
\frac{
B+\lambda\tau\bar X_P
+(1-\tau)[\widehat Q-Q_E]_+
}{1-c_0}.}
\tag{R35}
\]

因此

\[
\frac{\partial\widehat n}{\partial\lambda}=0,
\qquad
\frac{\partial\widehat Y}{\partial\lambda}
=\frac{\tau\bar X_P}{1-c_0}>0.
\tag{R36}
\]

这一定义最适合证明：receipt localization 仍有收入效应，但只有 platform-demand respending 才能改变 seller organization。

### 9.2 关闭全部 household induced respending

若把所有后续 household spending 都固定在基准值，可把既有其他收入写成常数 $\widetilde B$：

\[
\widetilde Y(\lambda)=
\widetilde B+\lambda\tau\bar X_P
+(1-\tau)[\widehat Q-Q_E]_+.
\tag{R37}
\]

此时

\[
\frac{\partial\widetilde n}{\partial\lambda}=0,
\qquad
\frac{\partial\widetilde Y}{\partial\lambda}
=\tau\bar X_P.
\tag{R38}
\]

两种定义对 entry 的结论完全一致，但对 income multiplier 的数值不同。正式论文必须选定其中一个；推荐式（R33）—（R36），因为它只关闭待识别的 platform-order feedback。

## 10. 代数与经济解释问题清单

### 10.1 排版问题

原候选式（22）写为 `\bar d-phi B/(Q_E-E)`；正确 LaTeX 是

\[
\bar d-\phi B/(Q_E-E).
\]

这是排版错误，不改变候选阈值。

### 10.2 $\lambda$ 的经济定义需要更窄

代数把所有本地 income recipients 设为具有同一平台支出倾向 $\phi$。所以 $\lambda$ 应定义为“由本地经济主体实际收取、形成其可支配收入并按共同倾向再支出的 commission share”。如果只是注册地址、税务确认地或不分红的 affiliate accounting location，式（R13）不成立。

更一般地，可将 receipt share $\lambda_R$ 与 receiver spending propensity $m_R$ 分开；entry-relevant term 将取决于两者的组合，而不是法律意义的 receipt location 单独决定。

### 10.3 Local commission 必须对应真实服务或所有权收入

若 $\lambda\tau\phi Y$ 只是本地买家与同一家庭之间的无成本内部转账，把它反复计为新增 value added 会产生错误解释。基准应明确：该收入是本地节点提供 intermediation service 的 factor income，或本地 beneficial owners 对平台 rent 的可支配收入，而不是任意 rebate。

### 10.4 外部订单 commission 的非对称处理

模型只地方化本地居民交易产生的 commission，$E$ 的 commission 始终归总部。这是识别 local-receipt channel 的有效 benchmark，但不是制度必然。若 $\lambda$ 同时作用于 $E$ 的 commission，$Y_1$ 的 numerator 和 $\lambda^*$ 都会改变，必须重新推导。

### 10.5 Fixed cost incidence 是必要 assumption

式（R13）把 local seller 的全部 $1-\tau$ payout 计作本地收入，因此要求 variable inputs、fixed setup inputs 和 owner receipts 都在本地。如果 onboarding、广告、云服务或软件固定费支付给总部，需从本地 payout 中扣除外流；否则 entry 带来的 local capture 被高估。

### 10.6 结果没有 multiplicity

收入映射是 contraction，seller payoff 随本地 seller mass 下降；所以模型只有一个 continuous activation threshold。任何关于 history dependence、multiple equilibria 或 discontinuous tipping 的表述都与本候选不一致。

## 11. 数值核验

使用固定随机种子 20260714 完成两组独立检查。

第一组在 20,000 组合法参数上检查 piecewise fixed point、$Q_0/Q_1$ identity、阈值和连续性：

| 检查 | 最大绝对误差或结果 |
|---|---:|
| 可行性、正性或 active-set 违例 | 0 |
| closed form 与 fixed-point iteration | $1.51\times10^{-12}$ |
| 式（R20）的订单池恒等式 | $7.11\times10^{-15}$ |
| $\lambda^*$ threshold residual | $1.78\times10^{-15}$ |
| 阈值处 $Y_0=Y_1=Y^*$ | $7.11\times10^{-15}$ |

第二组在 10,000 个构造的内部阈值上，用各解析分支的中心差分核对导数：

| 导数 | 最大误差 |
|---|---:|
| no-entry $dY_0/d\lambda$ | $2.76\times10^{-9}$ |
| positive-entry $dY_1/d\lambda$ | $3.85\times10^{-9}$ |
| active-side $dn/d\lambda$ | $7.79\times10^{-10}$ |

## 12. 最终复核意见

从 algebra 和 income conservation 看，spatial rent-receipt candidate 可以进入下一道 novelty/microfoundation 审查。它相对于普通 continuous seller-entry candidate 的实质改进是一个严格 necessity test：固定平台需求后，$\lambda$ 仍改变第一轮地方收入，但不再改变 seller entry。

正式写作前必须完成三项修正：

1. 修复式（22）的 `\phi` 排版；
2. 把 no-respending counterfactual 明确定义为式（R33）—（R36）；
3. 把 $\lambda$ 限定为实际 local disposable receipt，并清楚说明 fixed-cost 和外部订单 commission 的 incidence assumptions。

在这些限定下，没有发现阻断该候选继续审查的解析问题；但本复核不构成 direct-platform priority certification，也不授权修改正式稿。
