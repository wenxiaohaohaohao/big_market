# Stage 2：离散 local seller entry 候选模型

日期：2026-07-14  
性质：正式稿重写前的 theorem-feasibility memo  
文件边界：本文件不修改 `paper/main.tex`、`paper/appendix.tex`、`paper/references.bib`、`code/verify_model.py` 或 `output/paper.pdf`

## 1. 结论

这个候选在数学上通过可行性检验。与当前固定留值率模型不同，它确实能够在有限参数下产生：

- 真正的 local-seller no-entry corner，\(n=0\)；
- 全部潜在本地品类进入的 full-entry corner，\(n=1\)；
- 两个稳定 corner 与一个不稳定内部阈值同时存在；
- 市场规模或平台费变化引起的 regime switch 和 hysteresis；
- 一个由 primitive 决定的 multiplicity condition，而不是给定 multiplier coefficient 后的求导结果。

关键条件是

\[
\frac{\chi u}{d_0}>
\frac{\bar f-\underline f}{\bar f},
\qquad
u=\theta(1-\kappa-\ell),
\qquad
d_0=1-\beta-\chi\ell.
\]

左侧是“本地平台支出倾向 × 本地卖家每元交易收入”相对于基准收入漏出的反馈强度；右侧是潜在卖家固定成本的相对离散度。该不等式成立时，存在一个非空市场规模区间，使 no-entry 和 full-entry 都是均衡。

因此，本候选通过 **non-reducible proposition gate**：给定 \(n\) 后的收入求解仍是标准 fixed-coefficient inverse，但 entry correspondence 使同一组 primitives 对应多个收入与卖家进入均衡；固定系数 inverse 本身不能推出 corners、multiplicity 或 hysteresis。

这还不是可发表性结论。最接近的直接先例是 Li 的多地区 online-retailer entry 模型；平台 seller-entry、two-sided participation 和 entry multiplicity 本身也已有大量文献。当前可以主张的只是：**“平台费—收入空间归属—本地收入再支出—本地卖家进入”这一联合闭环产生了一个可检验的阈值候选。** 投稿前仍需对这个联合闭环做一次专项 priority audit。

**Business-stealing robustness update.** 下文第 17 节进一步表明：若采用与对称 CES/routing 一致的 per-seller order density

\[
h(n)=\frac1{n+\nu},
\qquad \nu>0,
\]

则每个 seller 的 entry payoff 对 \(n\) 严格下降，entry map 至多有一个 fixed point；no-entry 与 full-entry corners 不可能共存。换言之，上述 hysteresis 需要近似独立的品类/订单片段，不能在标准 CES business stealing 下保持。解析可行性仍成立，但本候选作为 EL 主模型的现实稳健性判定更新为 **NO-GO，除非能够提供独立订单片段或足够弱 business stealing 的可信制度依据**。

## 2. Research architecture

### 2.1 研究问题

在平台已经被消费者采用的情况下，本地卖家是否进入平台，能否通过改变交易收入的空间归属和后续本地支出，形成自我强化的 local-market-size effect？平台费和市场接入在什么 primitive 条件下会使一个地区出现低进入与高进入两个稳定均衡？

### 2.2 方法

- 范式：解析、静态、small-open-region theory；
- 均衡概念：连续统、原子化潜在卖家的 rational-expectations entry equilibrium；
- 异质性：卖家固定进入成本服从有界 uniform distribution；
- 闭合：本地收入、平台支出、本地收入归属和卖家进入联合决定；外部地区只承担收入守恒账户，不内生闭合其收入；
- 动态稳定性：使用最小的 adaptive best-response iteration \(n_{t+1}=\Phi(n_t)\)，仅用于区分局部稳定与不稳定均衡，不把它解释成完整动态模型。

### 2.3 Validity criteria

本候选只有同时满足以下要求才值得进入下一步：

1. 每一元平台支出在本地履约、平台总部、本地卖家和外地卖家之间加总为一；
2. 卖家 private entry payoff 与 aggregate local-income accounting 不重复计算；
3. 给定进入率时收入均衡唯一且正；
4. 所有 entry equilibria 都可由一个闭式集合完整列出；
5. 多重均衡必须由 entry feedback 产生，关闭该反馈后消失；
6. 关键 primitive 能映射到可观测 fee、seller origin、GMV、fulfillment compensation 和 entry cost；
7. 直接平台文献没有已经证明同一个 local-income-entry threshold。

## 3. Environment 与收入守恒

### 3.1 地区与支出

有一个本地区 \(L\) 和一个合并的外部/平台总部地区 \(H\)。本地自主收入为 \(B>0\)。本地居民把收入 \(Y\) 的比例

\[
\beta\in[0,1)
\]

用于完全本地化的非贸易服务，把比例

\[
\chi\in[0,1-\beta)
\]

用于平台商品，其余 \(1-\beta-\chi\) 流向模型外或 \(H\)。外地消费者对相关平台品类的自主支出为 \(A\geq0\)。所以平台总交易额为

\[
X=A+\chi Y.
\tag{1}
\]

当前候选不再重复推导家庭 CES 渠道选择。若需要与原稿连接，可以令 \(\chi=\alpha s(z)\)，但 entry theorem 只需要 \(\chi\) 是有限且满足 \(\beta+\chi<1\) 的平台支出倾向。

### 3.2 一元平台交易的空间归属

每一元平台交易严格拆分为：

| 收入项目 | 接收地 | 份额 |
|---|---:|---:|
| 本地履约、配送或售后劳动收入 | \(L\) | \(\ell\) |
| 平台佣金、广告和技术服务收入 | \(H\) | \(\kappa\) |
| 卖家端收入 | 由卖家所在地决定 | \(\varphi=1-\kappa-\ell\) |

假设

\[
\ell,\kappa\geq0,
\qquad
\ell+\kappa<1.
\]

潜在本地卖家分布在单位测度的独立品类或订单片段上。进入率为 \(n\in[0,1]\)。当一个品类的本地卖家进入后，该品类有比例 \(\theta\in(0,1]\) 的订单由本地卖家承接；否则由外地卖家承接。因此本地卖家的总订单份额为 \(\theta n\)。定义

\[
u\equiv\theta\varphi
=\theta(1-\kappa-\ell)>0.
\tag{2}
\]

平台交易中在 \(L\) 形成并由 \(L\) 接收的收入份额为

\[
\rho(n)=\ell+un,
\tag{3}
\]

在 \(H\) 形成或由 \(H\) 接收的份额为

\[
1-\rho(n)
=\kappa+(1-\theta n)\varphi.
\tag{4}
\]

式（3）和（4）严格加总为一。因为 \(\theta\leq1\)，也有 \(0\leq\rho(n)\leq1\)。

### 3.3 generation、receipt 与 spending ledger

本地当期诱发收入为

\[
I_L=\beta Y+\rho(n)X.
\]

外部当期诱发收入为

\[
I_H=(1-\beta-\chi)Y+[1-\rho(n)]X.
\]

由式（1），

\[
I_L+I_H=Y+A.
\tag{5}
\]

因此，本地居民的全部收入支出 \(Y\) 和外部平台支出 \(A\) 都有且仅有一个接收地。

收入产生地、收取地与支出地在这里被明确区分：本地履约和本地卖家收入在 \(L\) 产生并由 \(L\) 接收；平台费和外地卖家收入在 \(H\) 产生或由 \(H\) 接收；支出可以来自 \(L\) 或 \(H\)。

## 4. Local seller entry

潜在本地卖家的固定组织成本为

\[
f\sim U[\underline f,\bar f],
\qquad
0<\underline f<\bar f,
\qquad
\Delta f\equiv\bar f-\underline f.
\]

每个原子化卖家占据一个微小且预先界定的品类或订单片段，因此不改变其他卖家的订单片段。它把总平台市场 \(X\) 视为给定。进入后的 gross seller receipt density 为 \(uX\)。固定成本由本地组织、数字运营或设置劳动提供并支付给本地收入接受者。于是，卖家利润为

\[
\pi(f;Y)=uX(Y)-f,
\tag{6}
\]

但本地 aggregate seller income 仍为 \(unX\)：固定成本只是把该收入在本地劳动与本地卖家利润之间重新分配，不是第二笔收入。

进入率为

\[
n=H[uX(Y)],
\tag{7}
\]

其中 uniform CDF 为

\[
H(q)=
\begin{cases}
0, & q\leq\underline f,\\[2mm]
\dfrac{q-\underline f}{\Delta f},
& \underline f<q<\bar f,\\[3mm]
1, & q\geq\bar f.
\end{cases}
\tag{8}
\]

这里的 \(n=0\) 表示没有本地卖家进入平台，但平台仍然存在，且本地消费者仍可向外地卖家下单。\(n=1\) 表示所有潜在本地品类都进入，不表示平台支出份额等于一，也不表示外地卖家消失。

## 5. Equilibrium 与解析约化

### Definition 1：local seller-entry equilibrium

均衡是一对 \((Y,n)\in\mathbb R_{++}\times[0,1]\)，使得：

\[
Y=B+\beta Y+[\ell+un](A+\chi Y),
\tag{9}
\]

且 entry condition（7）成立。

给定 \(n\)，定义

\[
d_0=1-\beta-\chi\ell>0,
\qquad
c=\chi u,
\qquad
d_1=d_0-c
=1-\beta-\chi(\ell+u)>0.
\tag{10}
\]

因为 \(\ell+u\leq1\) 且 \(\beta+\chi<1\)，\(d_1>0\)。式（9）有唯一正解

\[
Y(n)=
\frac{B+(\ell+un)A}{d_0-cn}.
\tag{11}
\]

再定义

\[
Q=(1-\beta)A+\chi B>0,
\qquad
M=uQ.
\tag{12}
\]

代入式（1）得到一个有用的消去结果：

\[
X(n)=A+\chi Y(n)
=\frac{Q}{d_0-cn},
\tag{13}
\]

所以 marginal seller receipt 为

\[
q(n)=uX(n)
=\frac{M}{d_0-cn}.
\tag{14}
\]

全部均衡因此等价于一个一维 fixed point：

\[
n=\Phi(n)
\equiv H\!\left(\frac{M}{d_0-cn}\right).
\tag{15}
\]

\(\Phi\) 连续并将紧集 \([0,1]\) 映射到自身，因此至少存在一个均衡。给定任何 fixed point \(n\)，式（11）唯一确定正收入 \(Y\)。

## 6. 所有均衡的完整闭式表述

定义

\[
M_0=\underline f d_0,
\qquad
M_1=\bar f d_1.
\tag{16}
\]

### Lemma 1：equilibrium set

所有均衡且仅有以下三类：

1. **No-entry corner**

   \[
   n=0
   \quad\Longleftrightarrow\quad
   M\leq M_0.
   \tag{17}
   \]

2. **Full-entry corner**

   \[
   n=1
   \quad\Longleftrightarrow\quad
   M\geq M_1.
   \tag{18}
   \]

3. **Interior entry**

   对 \(c>0\)，任何内部均衡必须满足

   \[
   M=\mathcal M(n)
   \equiv
   (\underline f+\Delta f\,n)(d_0-cn),
   \qquad 0<n<1.
   \tag{19}
   \]

   等价地，它是下列二次方程在 \((0,1)\) 中的根：

   \[
   c\Delta f\,n^2
   -(\Delta f\,d_0-c\underline f)n
   +(M-M_0)=0.
   \tag{20}
   \]

   令

   \[
   \mathscr D=
   (\Delta f\,d_0-c\underline f)^2
   -4c\Delta f(M-M_0).
   \]

   若 \(\mathscr D\geq0\)，候选根为

   \[
   n_{\pm}=
   \frac{
   \Delta f\,d_0-c\underline f
   \pm\sqrt{\mathscr D}}
   {2c\Delta f};
   \tag{21}
   \]

   只有落在 \((0,1)\) 的根是均衡。由于式（20）是二次式，内部均衡最多两个。式（17）、（18）和（21）因此构成完整的均衡集合算法，不需要数值求根。

### 稳定性

用最小 adaptive entry dynamics

\[
n_{t+1}=\Phi(n_t)
\tag{22}
\]

定义局部稳定性。若式（17）或（18）中的不等式严格成立，相应 corner 附近的 \(\Phi\) 为常数，故局部稳定。

在内部均衡，

\[
\Phi'(n)=
\frac{c(\underline f+\Delta f\,n)}
{\Delta f(d_0-cn)}.
\tag{23}
\]

同时

\[
\mathcal M'(n)
=\Delta f(d_0-cn)\,[1-\Phi'(n)].
\tag{24}
\]

所以：

- \(\mathcal M'(n)>0\) 的内部根稳定；
- \(\mathcal M'(n)<0\) 的内部根不稳定；
- \(\mathcal M'(n)=0\) 是切触的 knife-edge。

这也给出全部内部根的稳定性，不需要额外数值判断。

## 7. 主候选命题：corner multiplicity 与 tipping

### Proposition 1

若

\[
M_1<M<M_0,
\tag{25}
\]

则模型恰有三个均衡：

\[
n=0,
\qquad
n=n^{\dagger}\in(0,1),
\qquad
n=1.
\]

两个 corner 都局部稳定；唯一内部均衡不稳定，并构成两个 basin of attraction 之间的 tipping threshold。其闭式为

\[
n^{\dagger}
=
\frac{
\Delta f\,d_0-c\underline f
+\sqrt{
(\Delta f\,d_0-c\underline f)^2
+4c\Delta f(M_0-M)
}}
{2c\Delta f}.
\tag{26}
\]

**证明。** 式（25）同时使 \(n=0\) 和 \(n=1\) 满足严格 entry inequalities。式（20）在 \(n=0\) 时为 \(M-M_0<0\)，在 \(n=1\) 时为 \(M-M_1>0\)，故至少有一个内部根。其常数项为负，两个代数根异号，所以内部正根唯一，并由式（26）给出。\(\Phi(n)-n\) 在该根左侧为负、右侧为正，故 \(\Phi'(n^{\dagger})>1\)，内部根不稳定。Q.E.D.

### Corollary 1：primitive multiplicity condition

存在非空的 \(Q\) 区间使式（25）成立，当且仅当

\[
\bar f(d_0-c)<\underline f d_0,
\]

即

\[
\boxed{
\frac{\chi u}{d_0}
>
\frac{\Delta f}{\bar f}
}.
\tag{27}
\]

在该条件下，multiplicity interval 为

\[
Q_F<Q<Q_0,
\qquad
Q_F=\frac{\bar f(d_0-\chi u)}{u},
\qquad
Q_0=\frac{\underline f d_0}{u}.
\tag{28}
\]

它是 primitive-level threshold：更高的本地平台支出倾向 \(\chi\)、更高的本地订单可得性 \(\theta\)、更低的平台抽取 \(\kappa\)，或更低的成本离散度 \(\Delta f/\bar f\)，会扩大出现两个稳定 corner 的可能性。

**证明。** \(M_1<M_0\) 等价于

\[
\bar f(d_0-c)<\underline f d_0
\Longleftrightarrow
\bar f c>\Delta f\,d_0,
\]

代入 \(c=\chi u\) 即得式（27）。再用 \(M=uQ\) 分别除以 \(u>0\)，即得式（28）。Q.E.D.

### Corollary 2：clean hysteresis 的充分条件

若进一步满足

\[
c\underline f\geq\Delta f\,d_0,
\tag{29}
\]

则 \(\mathcal M'(n)<0\) 对所有 \(n\in(0,1]\) 成立。此时均衡结构完全单调：

- \(Q<Q_F\)：唯一均衡是 \(n=0\)；
- \(Q_F<Q<Q_0\)：有两个稳定 corner 和一个不稳定内部均衡；
- \(Q>Q_0\)：唯一均衡是 \(n=1\)。

当 \(Q\) 缓慢上升时，低进入路径保持到 \(Q_0\) 才跳向 full entry；当 \(Q\) 下降时，高进入路径保持到 \(Q_F\) 才跳回 no entry。因此，相同的当前市场规模可以对应不同的 seller-entry 和 local-income 状态，取决于平台扩张的历史路径。

条件（29）比 corner coexistence 所需的式（27）更强。它用于得到干净的全局 hysteresis 分类，不应误写成 multiplicity 的必要条件。

**证明。** 由式（19），

\[
\mathcal M'(n)
=\Delta f\,d_0-c\underline f-2c\Delta f\,n.
\]

条件（29）使该导数在 \(n=0\) 弱为负、在所有 \(n>0\) 严格为负。因此 \(\mathcal M(n)\) 从 \(M_0\) 单调下降到 \(M_1\)，与任意水平 \(M=uQ\) 的交点结构正是上述三种情形。\(Q=Q_F\) 或 \(Q=Q_0\) 时，一个 corner 恰好满足无差异条件，属于非稳健边界。Q.E.D.

## 8. 平台费阈值

固定 \(Q,\chi,d_0\)，将 \(u=\theta(1-\kappa-\ell)\) 视为平台费决定的 seller-retention intensity。full-entry corner 存在当且仅当

\[
u\geq
u_F\equiv
\frac{\bar f d_0}{Q+\bar f\chi},
\tag{30}
\]

no-entry corner 存在当且仅当

\[
u\leq
u_0\equiv
\frac{\underline f d_0}{Q}.
\tag{31}
\]

若 \(u_F<u_0\)，则存在一个 fee range 使两个 corner 同时成立。相应 fee cutoffs 为

\[
\kappa_F=1-\ell-\frac{u_F}{\theta},
\qquad
\kappa_0=1-\ell-\frac{u_0}{\theta},
\qquad
\kappa_0<\kappa_F,
\tag{32}
\]

前提是两个 cutoffs 落在可行 fee 区间。高于 \(\kappa_F\) 时 full-entry corner 不再可持续；低于 \(\kappa_0\) 时 no-entry corner 不再可持续。中间区间具有 fee-induced coordination problem。

在固定 \(Q\) 和 \(\chi\) 的比较中，\(u_F<u_0\) 等价于

\[
\chi>
\frac{\Delta f\,Q}{\underline f\bar f}.
\tag{33}
\]

因为 \(Q\) 本身在更完整模型中可能随 \(\chi\) 变化，式（33）只用于固定其他对象时的 fee comparison，不能当作对 integration shock 的无条件比较静态。

这里不能把式（30）解释成“平台降低费率必然提高社会福利”。候选只刻画 local seller entry 与本地名义收入；平台利润、消费者价格、外部地区福利以及 fee 对平台服务质量的作用尚未内生化。

## 9. 与方案 B 的严格区别

README 中的方案 B 是 **消费者/家庭的平台参与固定成本**：

- 固定成本决定平台渠道是否被采用；
- no-platform corner 是 \(s=0\)；
- 采用平台后，家庭进入 \(0<s<1\) 的 CES 子问题；
- 单独加入该固定成本不会产生 \(s=1\)。

本候选是 **本地卖家的平台进入固定成本**：

- 平台和平台消费在 \(n=0\) 时仍然存在；
- \(n=0\) 只表示全部平台订单由外地卖家承接；
- \(n=1\) 表示所有潜在本地卖家品类进入，不表示平台 single-homing；
- entry 改变 seller income 的空间归属，继而改变本地收入和下一轮平台需求；
- 真正的 multiple equilibria 来自 seller entry 与 local income 的闭环，不来自消费者是否支付平台采用成本。

因此，本候选不是对方案 B 换一个固定成本符号。两者的经济主体、corner 含义、收入归属和反馈机制均不同。

## 10. 为什么结果不能由固定系数 inverse 单独推出

给定 \(n\)，式（11）确实是标准的一维 multiplier：

\[
Y(n)=
\frac{B+(\ell+un)A}
{1-\beta-\chi(\ell+un)}.
\]

这部分应明确承认 Miyazawa/SAM/Leontief ancestry。

但是，固定 \(n\) 的 inverse 总是在 \(d_0-cn>0\) 下给出唯一收入。它不能单独产生：

1. \(n=0\) 与 \(n=1\) 的 private-profit corners；
2. 对同一组 \((A,B,\kappa,\theta,\ell,f)\) 同时存在多个 \(Y\)；
3. 不稳定的 \(n^{\dagger}\)；
4. 式（27）的 cost-dispersion threshold；
5. 式（28）的 hysteresis band。

这些结果来自 entry condition

\[
n=H\{u[A+\chi Y(n)]\},
\]

即 multiplier 反过来进入 seller participation payoff。把 \(n\) 固定、令 \(\chi=0\)，或令 \(u=0\)，上述新结果都会消失。

## 11. Prior art 的三层区分

### A. 数学工具与经济学祖先

- 给定 \(n\) 的 local-income fixed point 属于 Miyazawa/SAM/Leontief household closure；
- heterogeneous fixed-cost entry、strategic complementarity、tipping 和 hysteresis 都是成熟的经济学工具；
- 因此，使用 inverse、uniform CDF 或证明 multiple equilibria 本身都不能构成创新。

这些是必须承认的 benchmark，但不能仅因使用已知数学工具就判定平台经济命题没有增量。

### B. 直接平台经济先例

本轮定向核查得到以下边界：

1. **Fan et al. (2018)** 将 e-commerce 建模为降低或消除目的地市场固定进入成本，并建立 online/offline 多地区 GE；它没有当前候选的“本地 seller receipt 提高本地收入、再融资本地平台需求”的 entry loop。
2. **Li (current working paper)** 是最接近的直接先例：online retailers 支付地区固定进入成本，其进入阈值取决于各目的地总支出；地区收入又进入 market clearing。该模型已经覆盖 online-retailer location、entry、regional income 和 value added。当前核查没有在文中找到式（27）型 local-income-entry multiplicity 或 hysteresis 命题，但它可能在更一般的 GE 中隐含这一机制，因此是下一轮必须逐式排除的首要文献。
3. **Teh (2022)** 直接研究平台 fee instrument 与 seller competition/entry 的治理，但其主问题不是收入生成地、所有权地和本地再支出的空间闭环。
4. **Lee and Musolff 的 recommender-system entry model** 包含 seller fixed cost、revenue share 和 entry；其 multiplicity 主要出现在 recommendation-mediated pricing，entry stage 则通过信息假设获得可计算性，不是 local-income multiplier。
5. two-sided platform launch 文献已经表明 buyer--seller cross-side network effects 可以产生 multiple participation equilibria。当前候选若有增量，必须明确其 feedback 来源是 **regional income receipt and respending**，而不是把常见的 cross-side network effect 改名。

### C. 当前候选可能新增的经济命题

潜在增量不是“平台有固定成本”或“进入会有多重均衡”，而是以下联合映射：

\[
\text{platform fee / routing}
\rightarrow
\text{local seller receipt}
\rightarrow
\text{local income}
\rightarrow
\text{local platform expenditure}
\rightarrow
\text{seller entry}.
\]

它给出可证伪预测：价格和消费者平台使用可以保持连续且为正，但 local-origin seller share、local seller income 和地方名义收入可在同一 fee 或 market-access neighborhood 内离散跳跃，并表现出历史依赖。该预测不同于“降低在线贸易成本增加 entry”的单调 market-access 结论。

这只是 **conditional novelty claim**。定向检索不能证明没有直接先例；在正式重写前仍须围绕 “regional income feedback + platform seller entry + ownership incidence + hysteresis” 做完整 priority audit。

## 12. Observable mapping

| Primitive / equilibrium object | 可观测对应 |
|---|---|
| \(n\) | 本地注册且活跃的平台卖家占潜在/合格卖家池的比例；或本地有供给品类覆盖率 |
| \(\theta n\) | 按 seller operating location 或 beneficial owner location 识别的 local-origin GMV share |
| \(\kappa\) | 有效平台 take rate：commission、广告、技术和 seller-service 支出占 GMV 的比例 |
| \(\ell\) | 每元 GMV 留在本地的仓储、配送、客服和售后劳动报酬 |
| \(A\) | 外地区买家对本地相关品类的 GMV |
| \(\chi\) | 本地居民收入中用于相关平台商品的边际支出比例 |
| \(B\) | 不依赖当前平台支出循环的本地基础收入或 tradable-base income |
| \(\underline f,\bar f\) | seller onboarding、合规、库存、数字运营和本地设置成本的支持区间 |
| \(Q_F,Q_0\) | seller-count/GMV regime switch 的下行和上行市场规模阈值 |
| \(\kappa_F,\kappa_0\) | fee 变化下高进入状态退出与低进入状态退出的不同 cutoffs |

关键经验区分是 seller registration location、actual operating location、beneficial owner location 和 fulfillment location 不能混为一个“本地卖家”指标。

## 13. 边界与反例审计

### 13.1 无本地平台需求反馈：\(\chi=0\)

此时 \(c=0\)，\(X=A\)，进入率唯一为

\[
n=H(uA).
\]

不存在 local-income-induced multiplicity。外地市场接入仍可促进入，但只是单向 market-size effect。

### 13.2 卖家端完全不留值：\(u=0\)

若 \(\theta=0\) 或 \(\kappa+\ell=1\)，卖家进入的 gross receipt 为零。因为 \(\underline f>0\)，唯一 entry outcome 是 \(n=0\)。收入退化为

\[
Y=\frac{B+\ell A}{1-\beta-\chi\ell}.
\]

### 13.3 无成本离散：\(\Delta f\to0\)

异质成本分布收敛到同一成本 \(f\)。entry response 变为 step correspondence。若

\[
f(d_0-c)<uQ<f d_0,
\]

no-entry 与 full-entry 仍可并存；内部点由 \(q(n)=f\) 决定并表示所有卖家恰好无差异。uniform heterogeneity 不是 multiplicity 的唯一来源，但它使 entry share 与 tipping threshold 连续且可观测。

### 13.4 \(\underline f\to0\)

只要 \(Q,u>0\)，至少有最低成本卖家进入，严格的 \(n=0\) corner 消失。这说明正的最低设置成本是 no-entry corner 的必要建模条件，而不是无害的规范化。

### 13.5 \(A=0\) 或 \(B=0\)

只要 \(Q=(1-\beta)A+\chi B>0\)，模型仍可解。\(A=0\) 时 entry 完全依赖本地基础收入融资的平台需求；\(B=0\) 时 entry 可以完全由外地市场接入启动。

### 13.6 固定成本支付给外部地区

基准假设 \(f\) 是本地劳动和组织成本。若卖家把固定 onboarding、广告或软件费支付给平台总部，式（9）必须扣除对应的外流，收入守恒和 multiplicity threshold 都会改变。不能把基准结论直接外推到这种 incidence。正式论文必须把本地设置成本 \(f\) 与平台 take rate \(\kappa\) 分开测量。

### 13.7 Business stealing

基准没有生产端 increasing returns。每个卖家占据一个固定的微小品类片段；给定总市场 \(X\)，其订单密度不随其他本地品类是否进入而增加。multiplicity 的正反馈完全来自一个 pecuniary demand linkage：更多本地 seller receipt 提高本地收入，本地收入又提高 \(X=A+\chi Y\)。

但“独立品类片段”确实关闭了 business stealing。为检查这个假设，令每个 entrant 的订单密度乘以一个弱下降函数 \(h(n)\)，其中 \(h(n)>0\)、\(h'(n)\leq0\)。aggregate local-seller capture 变为 \(unh(n)\)，marginal seller receipt 为

\[
q(n)=
\frac{u h(n)Q}
{d_0-\chi u n h(n)}.
\]

定义 per-seller business-stealing elasticity

\[
\varepsilon_b(n)
=-\frac{n h'(n)}{h(n)}.
\]

直接求导得到

\[
\frac{d\ln q(n)}{d\ln n}>0
\quad\Longleftrightarrow\quad
\varepsilon_b(n)
<
\frac{\chi u n h(n)}{d_0},
\tag{34}
\]

其中还要求 aggregate local seller share 随进入弱增，即 \(\varepsilon_b(n)<1\)。因此，模型不需要 technological increasing returns，但确实需要 local-income feedback 超过 business stealing。若式（34）在所有 \(n\) 上失败，seller payoff 不再具有本候选所需的 strategic complementarity，corner multiplicity 不能沿当前证明成立。

这不是可以忽略的附带条件，而是本候选最重要的 realism gate。基准 \(h(n)=1\) 给出 \(\varepsilon_b=0\)，从而隔离并最大化 local-income mechanism；正式论文若继续，必须把式（34）至少作为一个 robustness proposition，而不能只在文字中声称 business stealing 不重要。

### 13.8 外部地区反馈

当前 \(H\) 只作为守恒账户，\(A\) 不由 \(H\) 收入内生决定。若平台总部收入再购买本地商品，需要恢复两地区系统。该扩展会改变阈值，但不是验证当前 entry mechanism 所必需。

## 14. 数学核验

使用固定随机种子 `20260714` 对 100,000 组合法参数进行了纯解析核验：

- 式（13）的消去恒等式最大绝对误差：\(3.55\times10^{-15}\)；
- 式（5）的收入守恒最大绝对误差：\(3.55\times10^{-15}\)；
- 随机样本中有 1,606 组落入严格 corner-overlap 区间；
- 每组 overlap 样本都恰有一个 \((0,1)\) 内部根；
- 内部根都满足 fixed point，且最小 \(\Phi'(n^{\dagger})=1.0398>1\)；
- 未发现分母非正、错误根数或稳定性判定冲突。

一个示例为

\[
(\beta,\chi,\ell,\kappa,\theta)
=(0.2,0.5,0.1,0.1,0.8),
\]

\[
(\underline f,\bar f,A,B)
=(0.5,0.8,0.2,0.8).
\]

此时

\[
u=0.64,
\quad
M_1=0.344<M=0.3584<M_0=0.375,
\]

三个均衡为

\[
n=0,
\qquad
n^{\dagger}=0.87476,
\qquad
n=1,
\]

相应本地收入约为

\[
Y_0=1.0933,
\qquad
Y^{\dagger}=1.9826,
\qquad
Y_1=2.2047.
\]

内部均衡的 entry-map slope 为 \(1.7300\)，因此不稳定。

## 15. EL 篇幅与路线判断

### 可写入 2,000 词的最小版本

若选择此候选，主文只能保留：

1. 一张收入归属表；
2. 式（9）的 local-income equilibrium；
3. heterogeneous seller entry condition；
4. Lemma 1 的闭式均衡集合；
5. Proposition 1 与 Corollary 1；
6. 一段 observable prediction 和一段直接 prior-art positioning。

当前 CES 家庭优化、有限 integration threshold 和原 Proposition 1 不能与本模型全部并列进入正文，否则无法在 Economics Letters 篇幅内自足。最多把 \(\chi=\alpha s(z)\) 作为一句连接，不再重做 CES 推导。

### 当前判定

| Gate | 判定 | 原因 |
|---|---|---|
| income-incidence accounting | PASS | 每元平台支出和居民支出均严格守恒 |
| analytical solvability | PASS | 完整均衡集合与稳定性均有闭式表达 |
| genuine corners | PASS | \(n=0\) 与 \(n=1\) 都在有限参数下出现 |
| non-reducible proposition | PASS | multiplicity 与 hysteresis 来自 entry fixed point，不来自固定 inverse |
| observable mapping | PASS, conditional | 核心对象可测，但 owner/location 定义要求高 |
| direct-platform prior-art | UNRESOLVED | Li 与 platform-entry 文献高度相邻，尚未完成专项穷尽核验 |
| CES business-stealing robustness | FAIL | \(h(n)=1/(n+\nu)\) 使 entry payoff 严格下降并保证唯一均衡 |
| EL scope | NO-GO AS BASELINE | 除非可为独立订单片段提供强制度依据，否则不能把 hysteresis 当作稳健主结果 |

最终建议更新为：**不把离散 hysteresis 候选作为当前 EL 的主模型。** 它可以保留为说明 local-income complementarity 的理论边界或大论文附录，但标准 CES/routing business stealing 已使其 realism gate 失败。只有发现明确的品类隔离、地域独占或平台 routing 规则，使 per-seller orders 不随 local entry 显著稀释时，才值得重新开启。

## 16. 本轮核查的直接来源

- Fan et al. (2018), *The Alibaba Effect*: https://doi.org/10.1016/j.jinteco.2018.07.002
- Li, *Domestic Trade Shocks and E-Commerce Expansion*，当前工作论文：https://elmerli.github.io/ecommerce.pdf
- Teh (2022), *Platform Governance*: https://doi.org/10.1257/mic.20190307
- Lee and Musolff, *Entry into Markets Shaped by Recommender Systems*: https://conference.nber.org/confer/2022/DTs22/judy1.pdf
- Miyazawa (1960), income--consumption feedback benchmark: https://academic.oup.com/qje/article-pdf/74/1/53/5206190/74-1-53.pdf
- Pyatt and Round (1979), SAM multiplier benchmark: https://documents1.worldbank.org/curated/en/317011468179066100/pdf/REP125000Accou0ing0matrix0framework.pdf

证据边界：这是围绕候选 theorem 的定向核查，不是 priority certification。特别是 Li 的工作论文会更新，正式写作前必须重新下载并逐式核对最新版本。

## 17. Business-stealing robustness test

本节把第 13.7 节的局部条件写成完整 equilibrium test。

### 17.1 一般 \(h(n)\)

令本地 sellers 的总留值份额为

\[
\rho(n)=\ell+unh(n),
\]

其中 \(h(n)>0\)、\(h'(n)\leq0\)，并要求 \(unh(n)\leq1-\ell\)。给定 \(n\)，地方收入和总订单为

\[
Y(n)=
\frac{B+[\ell+unh(n)]A}
{d_0-\chi u n h(n)},
\tag{35}
\]

\[
X(n)=A+\chi Y(n)
=\frac{Q}{d_0-\chi u n h(n)},
\qquad
Q=(1-\beta)A+\chi B.
\tag{36}
\]

每个 marginal seller 的 gross receipt 为

\[
q(n)=u h(n)X(n)
=\frac{u h(n)Q}
{d_0-\chi u n h(n)}.
\tag{37}
\]

entry equilibrium 仍是

\[
n=\Phi(n)\equiv H[q(n)].
\tag{38}
\]

在成本分布有密度 \(g\) 的内部区间，entry-map slope 为

\[
\Phi'(n)=g[q(n)]q'(n),
\tag{39}
\]

其中

\[
\frac{q'(n)}{q(n)}
=
\frac{
\chi u h(n)+d_0 h'(n)/h(n)
}
{d_0-\chi u n h(n)}.
\tag{40}
\]

定义

\[
\varepsilon_b(n)
=-\frac{n h'(n)}{h(n)}.
\]

则 seller entry 具有局部 strategic complementarity 当且仅当

\[
q'(n)>0
\quad\Longleftrightarrow\quad
\varepsilon_b(n)
<
\frac{\chi u n h(n)}{d_0}.
\tag{41}
\]

多重内部 fixed points 的必要局部条件更强：由 mean-value theorem，必须在某处有

\[
\Phi'(n)>1.
\tag{42}
\]

对 uniform costs，这等价于 \(q'(n)>\Delta f\)。两个 corner 共存的全局必要充分条件仍可直接写为

\[
q(0)\leq\underline f,
\qquad
q(1)\geq\bar f.
\tag{43}
\]

若 \(q'(n)\leq0\) 对所有 \(n\) 成立，则 \(\Phi\) 弱下降，而左侧 identity map 严格上升，因此 fixed point 唯一；式（42）和（43）都不可能成立。

### 17.2 对称 CES/routing：\(h(n)=1/(n+\nu)\)

考虑

\[
h(n)=\frac1{n+\nu},
\qquad \nu>0.
\tag{44}
\]

它对应常见的对称 routing：本地 seller 总订单份额为 \(n/(n+\nu)\)，每个 seller 的订单密度为 \(1/(n+\nu)\)。此时

\[
\varepsilon_b(n)=\frac{n}{n+\nu}=nh(n).
\]

式（41）要求

\[
nh(n)<\frac{\chi u n h(n)}{d_0},
\]

即

\[
d_0<\chi u.
\tag{45}
\]

但合法支出份额给出

\[
d_0-\chi u
=1-\beta-\chi(\ell+u)
\geq1-\beta-\chi>0.
\tag{46}
\]

所以式（45）不可能成立。对所有 \(n>0\)，

\[
q'(n)<0,
\qquad
\Phi'(n)\leq0.
\tag{47}
\]

因此标准 CES/routing business stealing 下：

1. entry equilibrium 唯一；
2. no-entry 与 full-entry corners 不能共存；
3. 不存在第 7 节的 unstable tipping threshold；
4. 不存在由当前机制产生的 hysteresis。

固定随机种子 `20260714` 的 100,000 组合法参数核验中，business-stealing elasticity 与 local-feedback bound 的最小差为 \(2.25\times10^{-6}>0\)，\(d\ln q/dn\) 的 numerator 最大值为 \(-7.10\times10^{-7}<0\)，没有发现反例。

### 17.3 判定

离散候选的 multiplicity 并不依赖 technological increasing returns，但依赖极弱的 seller-to-seller demand dilution。标准对称 CES/routing 恰好违反这一要求。因此，数学上存在的 hysteresis 不能作为现实稳健的基准命题；它至多是一个明确的边界案例。
