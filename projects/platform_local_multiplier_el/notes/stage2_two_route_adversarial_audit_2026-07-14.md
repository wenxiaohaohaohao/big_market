# Stage 2 Two-Route Adversarial Novelty Audit

**日期：** 2026-07-14  
**审查对象：** 当前 scalar model，以及一地区收入流出、两地区双向收入流动的候选扩展  
**审查性质：** 独立、对抗式 novelty audit；只使用原始论文、出版商页面与作者/机构原始 working paper  
**文件边界：** 本次只新增此审查 note；未修改 `paper/main.tex`、`paper/appendix.tex` 或 `paper/references.bib`

## 0. 结论先行

| 候选路线 | 对抗式判定 | 原因 | 是否值得据此重写 EL |
|---|---|---|---|
| Scalar：\(Y=B+\beta Y+\alpha\omega(s)Y\) | **标准结果的 1×1 特例** | 它是固定价格 SAM/Miyazawa income multiplier 的单账户 resolvent；多轮反馈、分母放大、边际效应随 \(\omega\) 变化都由逆矩阵直接给出 | **否** |
| 单向两地区：外围消费收入按 \(q\) 从 \(L\) 转到 HQ \(H\) | **标准 interregional leakage/spillover/feedback 的重标记** | 令 \(r=0\) 后，局部损失、HQ 收益和重复反馈均由两地区 Leontief/Miyazawa inverse 直接给出 | **否** |
| 双向两地区：\(\Pi(q,r)=\begin{bmatrix}1-q&r\\q&1-r\end{bmatrix}\) | **仍是标准 multiregional Miyazawa/SAM coefficient recomputation** | 阈值 \(q'Y_L\) vs. \(r'Y_H\) 是 \(Y_z=L\alpha\Pi_zY\) 的代数展开；\(rY_H\) 由 \(H\) 收入内生融资正是 closed income–expenditure loop，而非新状态变量 | **否**，只可作为 benchmark |
| Platform-specific endogenous ownership/localization | **有条件可能成为不可约的经济命题** | 必须由平台费率、seller entry、fulfillment location/capacity、routing、owner residence 等 primitives 内生决定 \(q,r\)，并产生固定系数 inverse 本身不能证明的 sign、ranking、uniqueness/multiplicity 或政策命题 | **有条件是** |

最强的 adversarial verdict 是：**把外生 access \(B(z)\) 改写为由 \(Y_H\) 融资的 inbound flow \(r(z)Y_H\)，并不足以形成 novelty。** 这一步使模型从一地区 multiplier 变成两地区 closed-loop multiplier，但它进入的正是 multiregional Miyazawa、SAM multiplier decomposition 与 transboundary income/expenditure-flow 文献的核心范围。Sonis–Hewings 已将 output–income propagation 和 multiregional feedback loops 放入 Miyazawa 框架；Rose–Stevens 更早要求按收入的**产生地、收取地与支出地**分别处理跨界流量。[Sonis and Hewings (1993)](https://hdl.handle.net/10086/7798)；[Hewings and Sonis (2000)](https://econpapers.repec.org/article/spranresc/v_3a34_3ay_3a2000_3ai_3a4_3ap_3a569-589.htm)；[Rose and Stevens (1991)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9787.1991.tb00147.x)

因此，当前最小可发表增量不是再增加一个矩阵或另一个反馈项，而是：

> **建立一个平台特有的、微观可解释的 endogenous ownership/localization margin；证明该 margin 如何改变地区收入比较静态或均衡结构；并给出可观察变量能够区分该机制与普通 MRIO coefficient shock 的预测。**

如果做不到这一点，建议停止 EL 重写，把 scalar 或双向矩阵结果保留为研究备忘录或 benchmark，而不是作为论文贡献。

---

## 1. 审查问题与完成标准

本审查回答四个问题：

1. 当前 scalar model 的哪些结论可由标准 SAM/Miyazawa multiplier 直接推出？
2. 单向与双向两地区结构是否超过标准 MRIO/Leontief inverse 的 coefficient recomputation？
3. 引入 platform-specific ownership/localization primitives 后，什么命题有机会不再只是标准 accounting decomposition？
4. 一个候选结果满足什么最小条件，才值得重写当前 EL？

完成标准如下：

- 对三条路线分别给出 `go/no-go` 判定；
- 对 \(\Pi(q,r)\) 求出 closed form、导数阈值与 aggregate implication；
- 与 Miyazawa/SAM、Sonis–Hewings multiregional extension、Rose–Stevens transboundary flows 作直接对照；
- 区分“模型记账正确性要求”和“可发表 novelty”；
- 给出可以执行的最小 novelty contract 与明确停止条件；
- 全程不修改正式稿。

---

## 2. 检索与证据边界

### 2.1 检索方法

本次是定向 primary-source audit，不是穷尽式 systematic review。检索日期为 2026-07-14，检索组合包括：

- `Miyazawa income multiplier consumption function input-output`；
- `multiregional Miyazawa Sonis Hewings feedback loops`；
- `interregional multipliers spillovers feedbacks Leontief inverse`；
- `transboundary income expenditure flows generation receipt spending`；
- `ownership data regional input-output local multiplier`；
- `e-commerce platform fulfillment location seller entry regional income`。

纳入规则：原始理论或实证论文、出版商原文/摘要、机构库作者版本、作者原始 working paper。排除规则：二手综述、博客、无作者归属的摘要站点，以及无法确认原始来源的转述。Working paper 和 industry-authored operational paper 只用于说明可采用的 platform primitives 与现有竞争性工作，不用于宣称已确定完整 priority。

### 2.2 核心先例

- Miyazawa 将 consumption function 与 interindustry system 联立，并以 inverse 表示收入—消费的内生反馈。[Miyazawa (1960)](https://academic.oup.com/qje/article-pdf/74/1/53/5206190/74-1-53.pdf)
- Pyatt–Round 在 SAM 中明确区分 transfer、open-loop 与 closed-loop effects，并写出固定价格 multiplier \((I-C)^{-1}\)。[Pyatt and Round (1979), World Bank reprint](https://documents1.worldbank.org/curated/en/317011468179066100/pdf/REP125000Accou0ing0matrix0framework.pdf)
- Defourny–Thorbecke 以 structural paths 分解 SAM 网络中的直接、间接与循环影响；“从某账户经网络回到收入和消费”本身是其标准对象。[Defourny and Thorbecke (1984), institutional full text](https://orbi.uliege.be/bitstream/2268/90536/1/Structural%20Path%20Analysis%20and%20Multiplier%20Decomposition%20within%20a%20Social%20Accounting%20Matrix%20Framework.pdf)
- Interregional multiplier 文献已明确分解 own-region effects、interregional spillovers 与 feedbacks。[Dietzenbacher (2002)](https://research.rug.nl/en/publications/interregional-multipliers-looking-backward-looking-forward/)
- Sonis–Hewings 把 Miyazawa income multipliers 扩展到 multiregional systems 并用 block/Schur structure 分解 feedback。[Sonis and Hewings (1993)](https://hdl.handle.net/10086/7798)；[Hewings and Sonis (2000)](https://econpapers.repec.org/article/spranresc/v_3a34_3ay_3a2000_3ai_3a4_3ap_3a569-589.htm)
- Rose–Stevens 的边界条件尤其重要：跨地区 personal income 和 consumption 必须区分收入的 generation、receipt 和 spending location；三者全部内生的流量才应放入 closed regional IO system。[Rose and Stevens (1991)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9787.1991.tb00147.x)

---

## 3. 模型映射与精确推导

### 3.1 Scalar model 是 1×1 fixed-price multiplier

当前候选核心为

\[
Y=B+\beta Y+\alpha\omega(s)Y,
\qquad
Y=\frac{B}{1-\beta-\alpha\omega(s)}
\]

（若保留外生政府项，则把分子改成当前稿的相应外生注入；这里不影响 novelty 判断。）

令 \(a(s)=\beta+\alpha\omega(s)\)，则

\[
Y=[1-a(s)]^{-1}B.
\]

这是 \(Y=(I-A)^{-1}B\) 在一个内生账户上的特例。以下性质都由该表达式直接产生：

- 一次冲击经过无穷轮反馈形成 geometric series；
- retention/coefficient 越高，multiplier denominator 越小；
- marginal effect 含有 resolvent 的平方或左右 inverse；
- 把一阶 direct effect 与 induced feedback effect 分开；
- 给定 CES share \(s(z)\) 后出现 hump shape 或有限阈值。

其中 CES 价格指数与 share equation 可以提供 demand-system 内容，但只要 \(s(z)\) 仍是外生给定或单方程 reduced form，把它代入 \(\omega(s)\) 仍只是“需求份额变化 + multiplier coefficient 更新”。**它并没有改变 multiplier 理论的 novelty 判定。**

### 3.2 双向两地区结构

设

\[
\mathbf Y=\mathbf B+\beta\mathbf Y+\alpha\Pi(q,r)\mathbf Y,
\qquad
\Pi(q,r)=
\begin{bmatrix}
1-q&r\\
q&1-r
\end{bmatrix},
\]

其中每一列表示“消费地的一元支出最终流向哪个收入地”。第一列对应 \(L\) 消费，第二列对应 \(H\) 消费。定义

\[
k\equiv 1-\alpha-\beta>0,
\qquad
h\equiv k+\alpha(q+r)>0.
\]

则

\[
[(1-\beta)I-\alpha\Pi]^{-1}
=\frac{1}{kh}
\begin{bmatrix}
k+\alpha r&\alpha r\\
\alpha q&k+\alpha q
\end{bmatrix}.
\]

所以

\[
Y_L=\frac{kB_L+\alpha r(B_L+B_H)}{kh},
\qquad
Y_H=\frac{kB_H+\alpha q(B_L+B_H)}{kh}.
\]

因为 \(\Pi\) 每列加总为一，封闭的两地区系统只重新分配收入：

\[
Y_L+Y_H=\frac{B_L+B_H}{k},
\]

与 \(q,r\) 无关。这个不变量具有直接的对抗式含义：

> 如果模型保持 column-stochastic \(\Pi\)、固定 \(\alpha,\beta\) 和固定 \(B_L+B_H\)，它只能产生地区间收入转移，不能产生两地区合计收入损失或收益。

要得到 aggregate effect，必须加入系统外 leakage、真实资源成本、价格/福利变化、税收扭曲、劳动供给、投资或生产率反应等。单纯增加 “rest of world leakage” 仍是标准 MRIO/SAM；它改善模型完整性，但不自动构成 novelty。

### 3.3 双向阈值

令 \(q=q(z)\)、\(r=r(z)\)，并暂时固定 \(\mathbf B\)。标准 resolvent derivative 给出

\[
\mathbf Y_z
=L\alpha\Pi_z\mathbf Y,
\qquad
L=[(1-\beta)I-\alpha\Pi]^{-1}.
\]

定义

\[
g(z)\equiv q'(z)Y_L-r'(z)Y_H.
\]

由于

\[
\Pi_z\mathbf Y=g(z)
\begin{bmatrix}-1\\1\end{bmatrix},
\qquad
L\begin{bmatrix}-1\\1\end{bmatrix}
=\frac{1}{h}\begin{bmatrix}-1\\1\end{bmatrix},
\]

有

\[
\boxed{
Y_{L,z}=-\frac{\alpha}{h}[q'Y_L-r'Y_H],
\qquad
Y_{H,z}=+\frac{\alpha}{h}[q'Y_L-r'Y_H].
}
\]

因此：

- \(q'Y_L>r'Y_H\)：\(L\) 失去收入，\(H\) 获得同额收入；
- \(q'Y_L<r'Y_H\)：\(L\) 获得收入，\(H\) 失去同额收入；
- \(q'Y_L=r'Y_H\)：边际中性；
- 单向路线只是令 \(r=r'=0\)，于是 \(q'>0\) 时 \(L\) 必然下降、\(H\) 必然上升。

这是清楚且可用的 benchmark，但它不是独立的新经济命题。其完整证明只有两步：系数矩阵求导，以及 inverse 对差分方向 \((-1,1)'\) 的作用。任何熟悉 MRIO/SAM 的读者都可以把它识别为 **coefficient shock 经 interregional feedback inverse 的传播**。

---

## 4. 哪些结论可由标准 MRIO/SAM/Leontief inverse 直接推出

| 候选结论 | 标准框架能否直接推出 | 判定依据 |
|---|---:|---|
| 留存率下降会降低本地 multiplier | 是 | 1×1 或多账户 \((I-A)^{-1}\) 的单调性；Pyatt–Round、Miyazawa 已覆盖 income–consumption closure |
| 平台把本地支出中的一部分转为 HQ 收入，本地收入经过多轮反馈下降 | 是 | 单向 interregional coefficient shock；属于 spillover + feedback decomposition |
| HQ 收入又通过 outbound spending 回到 \(L\) | 是 | multiregional Miyazawa closed loop 的标准结构；“由 \(Y_H\) 融资”正是 endogenous household/institution account closure |
| \(q'Y_L\) 与 \(r'Y_H\) 决定两地收入边际方向 | 是 | 恒等式 \(Y_z=L\alpha\Pi_zY\)；阈值是净流量导数的记账展开 |
| 反馈使 direct loss 被放大或被回流抵消 | 是 | Leontief/Miyazawa inverse 与 structural path decomposition 的直接内容 |
| 两地区内部重新分配但 aggregate income 不变 | 是 | column-stochastic \(\Pi\) 的 adding-up identity |
| 固定的 HQ ownership share 造成更高地区外泄漏 | 是 | ownership 可作为 SAM/IO 系数；external ownership 与 IO 的结合已有先例。[Jackson (1989)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2257.1989.tb00487.x) |
| 固定 fulfillment-local-labor share 提高本地 retained income | 是 | 增加账户或改变路径系数即可；属于更细的 SAM accounting |
| 收入产生地、收取地、支出地不同 | 是，且必须正确处理 | Rose–Stevens 已将其作为 transboundary-flow closure 的核心分类，不是平台文献的新问题 |
| 给定任意 \(q(z),r(z)\) 后的非线性或交叉点 | 通常是 | 若函数外生给定，结果是 coefficient path 的重新计算；复杂函数形状不等于机制 novelty |

### 4.1 与 Sonis–Hewings 的直接比较

双向 \(\Pi(q,r)\) 的卖点可能被表述为：“过去 scalar model 的 access 是外生的；现在 \(H\) 的收入会融资 \(H\to L\) 的 outbound access，因此出现双向反馈。”但这正是 Sonis–Hewings multiregional Miyazawa structure 的典型内容：地区子系统之间通过收入与支出路径连接，inverse 的 block structure 汇总内部、外部与 feedback effects。[Sonis and Hewings (1993)](https://hdl.handle.net/10086/7798)；[Hewings and Sonis (2000)](https://econpapers.repec.org/article/spranresc/v_3a34_3ay_3a2000_3ai_3a4_3ap_3a569-589.htm)

因此，\(rY_H\) 的内生融资确实比外生 \(B(z)\) 更完整，但它只完成了从 one-region reduced form 到 multiregional closure 的升级。**模型完整性提高，不等于 contribution boundary 被越过。**

### 4.2 与 Rose–Stevens 的直接比较

当前 \(\Pi\) 的文字解释把“消费地的一元支出流向哪个收入地”压缩为一个映射。对于一般 IO/SAM benchmark 可以如此抽象；但一旦声称识别 platform ownership 或 localization，这个压缩会产生概念问题：

- 商品或服务在哪里生产/履约，是 **income generation location**；
- 平台、seller、物流企业和资本所有者在哪里收取利润/要素收入，是 **income receipt/ownership location**；
- 收入获得者在哪里消费，是 **spending location**。

Rose–Stevens 的核心警告正是不能把这三者混为一谈，否则 regional closure 会错误地纳入或排除跨界流量，并造成 multiplier bias。[Rose and Stevens (1991)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9787.1991.tb00147.x)

所以，如果继续平台路线，至少需要把 \(\Pi\) 分解为 generation、ownership/receipt 和 spending 三个 incidence mappings，或以等价账户明确区分 seller margin、platform fee、fulfillment labor 与 owner payout。**但这首先是 validity requirement；完成它本身仍不是 novelty，因为 Rose–Stevens 与 ownership-augmented IO 已经提供先例。**

---

## 5. 双向 \(q/r\) 候选的最强反驳与判定

### 5.1 最强支持性解释

对该候选最有利的表述是：平台化不只提高外围收入外流 \(q\)，还可能通过 HQ 消费、seller access 或 fulfillment network 提高回流 \(r\)；因此净效应取决于两条内生收入基数加权的边际路径，而不是单一 retention coefficient。这个表述比 scalar narrative 更平衡，也能排除“所有平台化必然伤害外围”的机械结论。

### 5.2 为什么仍不足以越过 coefficient recomputation

即使采用最有利的解释，仍有四个致命问题：

1. **阈值是净流量恒等式，不是 primitive theorem。** \(q'Y_L-r'Y_H\) 只说明“边际流出大于边际流入时，本地收入下降”。它没有解释什么决定 \(q'\) 或 \(r'\)。
2. **\(Y_H\) 进入回流项不是新反馈。** 它是把 \(H\) household/institution account 闭合后的标准 income–expenditure feedback。
3. **固定 \(q,r\) 或外生 \(q(z),r(z)\) 都可以直接写入 \(A(z)\)。** 所有结果仍由 \(Y_z=L A_zY\) 推出。
4. **column-stochastic 结构排除了 aggregate effect。** 若论文想讨论 market-size、aggregate output 或 welfare，而模型只显示地区间 income relocation，结果的经济含义会被高估。

因此，双向候选适合作为“已知 benchmark 的最简表达”，不适合作为 EL 的主贡献。

### 5.3 路线判定

```text
route_scalar = DO_NOT_REWRITE
route_one_way_matrix = DO_NOT_REWRITE
route_bidirectional_exogenous_qr = DO_NOT_REWRITE
route_platform_endogenous_localization = CONDITIONAL_GO
```

---

## 6. Platform-specific ownership/localization：什么仍是已知，什么可能成为增量

### 6.1 只增加固定平台账户，不足以形成 novelty

以下改动会改善解释和测量，但仍能由扩展 SAM 直接编码：

- 把每一元线上销售拆成 seller revenue、platform fee、fulfillment/logistics labor、tax 和 capital income；
- 规定 platform fee 全部归 HQ owners；
- 规定 fulfillment labor 的固定比例支付给本地居民；
- 规定本地 seller 的固定占比；
- 让不同收入账户采用不同 marginal propensity to consume。

固定 ownership data 与 interindustry accounts 的结合至少可追溯到 Jackson 的原始应用；local versus absentee ownership 确实会改变本地可捕获收入，但这一事实本身已有 IO 与资源所有权实证先例。[Jackson (1989)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2257.1989.tb00487.x)；[Brown, Fitzgerald, and Weber (2019)](https://www.journals.uchicago.edu/doi/full/10.1086/705505)

### 6.2 有条件可能成为不可约命题的 primitives

| Primitive | 必须如何内生化 | 可争取的结果 | 主要失败风险 |
|---|---|---|---|
| Platform fee / commission | 平台依据两地需求、seller participation 或竞争选择费率，且费率影响 seller margin 与 demand | 费率变化同时改变 extraction 和 market access；得到 primitive elasticity threshold | 若费率只作为外生 \(q\)，仍是 coefficient shock |
| Local seller entry | seller entry 由预期本地/外地 demand、平台费和 fixed cost 决定 | 线上 access 可提高 \(r\)，但本地收入反馈可能放大或抑制 entry；形成 entry threshold | 若 entry share 外生校准，只是重新命名 \(r(z)\) |
| Fulfillment location/capacity | 平台选择 facility location/capacity；routing 受成本、时效与容量约束 | facility localization 改变劳动收入与履约成本，可能产生离散区位或 tipping result | 仅给固定 local-labor share 仍是 SAM 细分 |
| Order routing | 每笔订单在 seller、platform 和 fulfillment nodes 之间内生分配 | 同一 consumer share 可对应不同地区 income incidence，形成可检验异质性 | 任意 routing matrix 会被视为参数化 accounting |
| Owner residence and payout | 利润分配、owner residence 与消费地分离，并影响后续支出 | 证明“production local”不等于“income retained local”的条件 | Rose–Stevens/Jackson 已覆盖固定 ownership；必须有平台特有选择或制度冲击 |
| Tax nexus / local tax incidence | facility/nexus 规则影响平台区位、价格、税与履约网络 | policy 通过区位选择而非单一需求份额影响地区收入 | 若税只作为额外 leakage，仍是标准财政 SAM |

平台区位与 seller participation 并非空白领域：Amazon fulfillment-network 研究已把 facility location、运输/履约成本和需求放在同一选择问题中；近期 spatial e-commerce 工作也研究设施扩张、seller entry 与地区收入差异。[Houde, Newberry, and Seim, NBER Working Paper 23361](https://www.nber.org/system/files/working_papers/w23361/w23361.pdf)；[Li, working paper](https://elmerli.github.io/ecommerce.pdf)。电子商务的地区价格、进入和福利效应也已有多地区结构模型及随机实验背景。[Fan et al. (2018)](https://www.sciencedirect.com/science/article/abs/pii/S0022199618301594)；[Couture et al. (2021)](https://www.aeaweb.org/articles?id=10.1257%2Faeri.20190382)

这意味着一个新模型不能只说“平台有 fulfillment network”；它必须把该网络与 **local income incidence** 的特殊问题连接起来，并提出上述文献不能从既有状态变量直接得到的结果。

### 6.3 最小的 endogenous-localization 表达

为了看清什么才是额外机制，令两地区总收入在 closed benchmark 下为常数 \(T\)，并写 \(y=Y_L\)。定义净外流

\[
n(y,z)=q(y,z)y-r(y,z)(T-y).
\]

则本地均衡可以写成

\[
ky=B_L-\alpha n(y,z),
\]

其比较静态为

\[
[k+\alpha n_y]y_z=-\alpha n_z,
\]

其中

\[
n_y=q+r+q_y y-r_y(T-y),
\qquad
n_z=q_z y-r_z(T-y).
\]

这一表达给出严格的 novelty 分界：

- 若 \(q_y=r_y=0\)，就回到标准 denominator \(k+\alpha(q+r)\) 和阈值 \(q_zY_L-r_zY_H\)；
- 若 \(q_y\) 或 \(r_y\) 来自平台/卖家优化，才出现额外 endogenous-localization Jacobian；
- 在局部唯一且稳定的均衡下，正 denominator 主要改变 amplification，**并不会自动创造新的 sign reversal**；
- 只有当平台 FOC/entry condition 对 \(q_z,r_z\) 给出 primitive restrictions，或 \(r_y\) 足够强导致 tipping/multiplicity，才可能形成实质命题。

这也是对“加一个 endogenous share 就算 novelty”的进一步否决：**状态依赖本身不够；需要可解释的优化条件、稳定性条件和非平凡结论。**

---

## 7. 最小 novelty contract

只有同时满足以下七条，才建议重写 EL。

### NC-1：Known-benchmark nesting

论文必须显式把 scalar、单向和双向固定系数模型作为已知 benchmark。关闭新增平台 primitive 后，模型应退化为标准 multiregional Miyazawa/SAM inverse。不能把 recurring feedback、Leontief denominator 或 \(q'Y_L-r'Y_H\) 本身列为贡献。

**验收测试：** 文稿能用一段话准确说明 Pyatt–Round、Sonis–Hewings、Rose–Stevens 已经覆盖什么。

### NC-2：Incidence accounting 正确

至少区分：

1. 销售/履约与要素收入的产生地；
2. seller、platform、worker、capital owner 的收取/所有权所在地；
3. 各收入获得者的支出地。

**验收测试：** 每一元线上支出可以在账户图中守恒追踪，且不会把 local fulfillment、local ownership 与 local spending 当作同一件事。

### NC-3：至少一个平台特有的 endogenous primitive

候选包括 fee/pass-through、seller entry、facility localization/capacity、order routing 或 tax-nexus-induced network choice。它必须由清楚的 choice problem、participation condition 或技术约束决定，而非任意指定 \(q(z),r(z)\)。

**验收测试：** \(q_z,r_z,q_y,r_y\) 中至少一个能从 primitives 和 FOC/entry condition 推出符号或界限。

### NC-4：一个固定系数 inverse 不能独立证明的 proposition

合格结果至少应属于以下一种：

- primitive elasticity threshold，而非 \(q'Y_L-r'Y_H\) 的流量恒等式；
- platform fee、entry 或 localization 的 ranking result；
- 稳定唯一均衡与 multiplicity/tipping 的条件；
- 同样的 consumer adoption shock 在不同 ownership/fulfillment structures 下产生可排序的地区收入反应；
- 一个政策改变平台的内生区位/路由，因此产生固定 \(A\) benchmark 不包含的额外项。

**验收测试：** 关闭平台优化或 entry/localization feedback 后，命题中的关键项消失，而不是只换一个 coefficient 名称。

### NC-5：Observable mapping 与 falsifiable prediction

每个关键 primitive 必须对应可测对象，例如 platform fee、seller origin、fulfillment node、local warehouse labor compensation、owner residence 或 order routing。至少提出一个能区分平台机制与普通 trade-cost/coefficient shock 的预测。

**验收测试：** 研究者能够说明需要哪一种数据来拒绝模型，而不只是用不可观察的 \(q,r\) 反推结果。

### NC-6：Prior-art dominance test

新的 theorem 必须逐项对照：

- standard SAM/Miyazawa closed-loop multiplier；
- Sonis–Hewings multiregional feedback；
- Rose–Stevens generation/receipt/spending locations；
- fixed ownership-augmented IO；
- platform fulfillment/location/seller-entry 文献。

**验收测试：** 能用一句精确的话指出“新项在哪里、旧模型为什么没有、关闭它时如何退化”。

### NC-7：EL scope feasibility

在约 2,000 字级别的 EL 中，最多保留一个主要 proposition、一个直接 corollary 和一项定量/经验 discipline。若机制必须依赖完整多地区、多行业、动态 facility network 才成立，则不适合当前短文，应另立完整论文。

**验收测试：** 主结果可在正文一页内陈述；证明和账户细节可放 appendix；模型不靠大量未识别参数维持结论。

---

## 8. 值得重写的最小候选结果

目前最有希望、又可能控制在 EL 篇幅内的候选不是完整 spatial platform model，而是下述窄命题：

> **Platform-localization threshold：** 平台化同时提高 HQ extraction 和 local market access。若 local seller/fulfillment participation 由本地收入或需求内生支持，则外围收入效应取决于“HQ extraction elasticity”与“endogenous local participation elasticity”的 primitive threshold；后者进入均衡 Jacobian，并可能产生强放大或 tipping。固定 participation 时，命题严格退化为标准 \(q'Y_L-r'Y_H\) benchmark。

这个候选只有在以下内容都能完成时才合格：

1. 用平台费、seller fixed cost 或 facility capacity 明确推导 local participation；
2. 给出稳定性/唯一性条件；
3. 得到 primitive threshold 或 regime result；
4. 说明 observed fulfillment/seller-location data 如何检验；
5. 证明结果并非任意选择 \(r(z)\) 的产物。

如果推导后最强结果仍只是

\[
\operatorname{sign}(Y_{L,z})
=-\operatorname{sign}[q'(z)Y_L-r'(z)Y_H],
\]

则 novelty contract 失败，不应重写 EL。

---

## 9. 建议的下一步与停止规则

### 推荐选项：先做一页 theorem feasibility memo，再决定是否重写

**优点：** 成本最低；能在动正式稿前检验 primitive threshold 是否真的存在；可以及时发现结果只是 coefficient recomputation。  
**缺点：** 可能确认该路线不成立，但这正是本阶段需要的信息。

具体只需完成：

1. 选择一个 endogenous margin：优先 local seller entry 或 fulfillment localization，二选一；
2. 写出 choice/entry condition 和 income-incidence accounts；
3. 推导一个 proposition；
4. 执行 NC-1 至 NC-7；
5. 只有七项全部通过才修改正式稿。

### 不推荐选项 A：直接把 scalar 改成双向 \(\Pi(q,r)\)

**优点：** 代数短、叙述直观、能表现双向收入流。  
**缺点：** 最强阈值属于标准 MRIO/Miyazawa；无法解释 \(q'\)、\(r'\)；column-stochastic setting 只有 redistribution；正式稿重写成本无法换来可信 novelty。

### 不推荐选项 B：一次加入完整 platform spatial GE

**优点：** 理论上可内生化 fee、entry、facility 和 routing。  
**缺点：** 超过当前 EL 的篇幅和识别能力；直接面对既有 e-commerce spatial models；容易把清楚的地方收入问题变成大而未决的模型。

### Hard stop rule

满足下列任一条件即停止 EL 重写：

- \(q,r\) 最终仍是外生函数或校准份额；
- 结果只能写成净流出大于净流入的恒等式；
- ownership/localization 只通过固定系数进入；
- 不区分 income generation、receipt 与 spending；
- 新机制没有可观察映射；
- 需要完整 spatial GE 才能得到任何非平凡结论。

---

## 10. 核心来源核验矩阵

| 来源 | 来源性质 | 本审查使用的原始内容 | 对判定的作用 | 限制 |
|---|---|---|---|---|
| [Miyazawa (1960)](https://academic.oup.com/qje/article-pdf/74/1/53/5206190/74-1-53.pdf) | QJE 原文 | consumption function 与 IO system 联立、income feedback inverse | scalar model 的直接先例 | 不是 multiregional platform model |
| [Pyatt and Round (1979)](https://documents1.worldbank.org/curated/en/317011468179066100/pdf/REP125000Accou0ing0matrix0framework.pdf) | Economic Journal 原文的机构 reprint | fixed-price SAM multiplier；transfer/open-loop/closed-loop decomposition | recurring income–expenditure rounds 属于标准 SAM | 固定价格框架 |
| [Defourny and Thorbecke (1984)](https://orbi.uliege.be/bitstream/2268/90536/1/Structural%20Path%20Analysis%20and%20Multiplier%20Decomposition%20within%20a%20Social%20Accounting%20Matrix%20Framework.pdf) | Economic Journal 作者/机构全文 | structural paths 与 multiplier decomposition | 路径叙事本身不是 novelty | 不讨论数字平台 |
| [Dietzenbacher (2002)](https://research.rug.nl/en/publications/interregional-multipliers-looking-backward-looking-forward/) | Regional Studies 出版记录与摘要 | intracountry、intercountry spillover、feedback decomposition | 单向/双向地区反馈已有标准分类 | 本审查使用摘要核验范围 |
| [Sonis and Hewings (1993)](https://hdl.handle.net/10086/7798) | Hitotsubashi Journal 机构库 | Miyazawa 框架的 multiregional extension 与 regional substructures | 直接反驳“\(Y_H\) 融资回流是新反馈” | 需要在正式写作时取得稳定全文页码 |
| [Hewings and Sonis (2000)](https://econpapers.repec.org/article/spranresc/v_3a34_3ay_3a2000_3ai_3a4_3ap_3a569-589.htm) | Annals of Regional Science 出版记录与摘要 | multiregional Miyazawa income multiplier 的 block/LDU factorization | 双向 inverse/block feedback 的直接先例 | 本审查使用摘要核验范围 |
| [Rose and Stevens (1991)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9787.1991.tb00147.x) | Journal of Regional Science 出版商摘要 | generation、receipt、spending location；闭合边界 | ownership/localization accounting 的最低 validity 标准 | 正式引用时应取得全文核对精确措辞 |
| [Jackson (1989)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2257.1989.tb00487.x) | Growth and Change 出版商摘要 | interindustry linkages 与 corporate ownership data 联结 | 固定 ownership coefficients 不是平台特有创新 | 实证应用较早，不能单独覆盖现代平台机制 |
| [Brown, Fitzgerald, and Weber (2019)](https://www.journals.uchicago.edu/doi/full/10.1086/705505) | JAERE 原文 | local/absentee ownership 改变地区可捕获收入 | 支持 ownership incidence 的经济重要性 | 资源部门，不是平台 |
| [Houde, Newberry, and Seim](https://www.nber.org/system/files/working_papers/w23361/w23361.pdf) | NBER working paper | fulfillment facility location、成本、需求与平台网络选择 | 说明平台区位可被微观化，也说明已有竞争性先例 | Working paper；版本可能更新 |
| [Li](https://elmerli.github.io/ecommerce.pdf) | 作者 working paper | facility expansion、seller entry、regional income effects | 说明 endogenous entry/localization 路线已有相邻工作 | 未经同行评审、版本可能更新 |
| [Fan et al. (2018)](https://www.sciencedirect.com/science/article/abs/pii/S0022199618301594) | Journal of International Economics 出版商页面 | multi-region online/offline trade、firm entry、price/variety | 防止把 spatial e-commerce access 误当空白 | 与本地 income ownership 问题不完全相同 |
| [Couture et al. (2021)](https://www.aeaweb.org/articles?id=10.1257%2Faeri.20190382) | AER: Insights 原文页面 | e-commerce expansion 的 randomized evidence；consumer gain 与 producer-income response 可分离 | 支持区分 access/welfare 与 local income | 不识别本模型的 ownership channel |

---

## 11. 限制与 AI 使用说明

1. 本审查是面向“是否值得重写”的定向 novelty stress test，不是完整文献计量或系统综述，因此不宣称绝对 priority。
2. 对 Sonis–Hewings、Rose–Stevens、Jackson 等部分来源，本次以出版商/机构库的原始摘要与可取得全文核验研究范围；正式投稿前仍应取得稳定全文并核对页码和精确措辞。
3. Platform fulfillment 与 seller-entry 部分含 working papers；它们用于界定当前竞争性研究和可行 primitives，不作为定论证据。
4. 本次没有依赖其他 agent 的结论；模型映射、closed form 与 comparative statics 均在本 note 中独立推导。
5. 本 note 由 AI 辅助检索、推导与撰写。所有关键先例均链接至原始出版商、机构库或作者版本；数学结论应在进入正式稿前由作者再次逐式复核。

---

## 12. 最终决策

**当前三条现成路线均不足以支持重写：**

- scalar 是 1×1 SAM/Miyazawa multiplier；
- 单向矩阵是标准 interregional leakage/spillover；
- 外生双向 \(q/r\) 及 \(q'Y_L\) vs. \(r'Y_H\) 是标准 multiregional coefficient shock 与 closed-loop feedback。

**唯一保留的 conditional route：** 平台特有的 endogenous ownership/localization margin，并通过 primitive choice/entry condition 产生一个固定系数 inverse 无法独立证明、可观察且可证伪的结果。

**推荐动作：** 不修改正式稿；先做一个一页 theorem feasibility memo。只有 NC-1 至 NC-7 全部通过，才进入 EL 重写。
