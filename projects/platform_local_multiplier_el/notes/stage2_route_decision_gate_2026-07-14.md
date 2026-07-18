# Stage 2：Equation-level prior-art audit 与路线决策闸门

日期：2026-07-14  
项目：*Platform Intermediation and Local Multipliers*  
性质：正式稿重写前的内部决策文件  
文件边界：本轮未修改 paper/main.tex、paper/appendix.tex、paper/references.bib、code/verify_model.py 或 output/paper.pdf

## 1. 决策结论

本轮严格执行了以下顺序：

1. 冻结现有正式稿；
2. 对标量模型进行 equation-level prior-art audit；
3. 独立推导并数值核验最小两地区 spatial-incidence 模型；
4. 由独立审查者压力测试候选命题是否只是 SAM/Miyazawa/MRIO coefficient recomputation；
5. 在通过理论贡献闸门之前不重写正式稿。

最终判定如下。

| 路线 | 数学可解性 | 创新性判定 | 是否据此重写 EL |
|---|---|---|---|
| 当前 scalar model | 通过 | 标准 household-closure / Miyazawa multiplier 的 \(1\times1\) 特例 | **否** |
| 单向两地区收入流出 | 通过 | 标准 interregional leakage、spillover 与 feedback | **否** |
| 外生双向 \(q/r\) access--capture model | 通过 | 阈值是 multiregional inverse 对系数变化的直接展开 | **否** |
| 平台特有的 endogenous ownership/localization margin | 尚未建立 | 只有在产生 primitive-level theorem 时才可能越过现有文献 | **有条件继续检验** |

因此，**当前不能开始重写 main.tex**。下一步不是把 \(\omega\) 机械改成 \(2\times2\) 矩阵，而是先用一个极小的 choice problem 检验 platform fee、local seller entry 或 fulfillment localization 中的一项能否产生固定系数 inverse 无法独立证明的命题。

## 2. 原项目机制与当前 EL 简化之间的关系

原项目包含四层经济机制：

1. 市场接入与消费价格；
2. 本地中介、平台租金和利润所有权造成的价值捕获差异；
3. 本地生产、外销与外地竞争；
4. 本地收入向非贸易部门的传播。

当前 EL 保留了第 1 层和第 4 层，并把第 2 层压缩为固定渠道留值参数 \(\rho_A,\rho_P\)，把第 3 层压缩为外生的 \(B(z)\)。这种简化确实删除了原项目最有空间含义的对象：生产地、收入产生地、收入收取/所有权地和支出地之间的分离。

但本轮审计也表明：**创新性不足不能只归因于“模型删得太多”。** 更根本的问题是，当前稿把已经成熟的 recursive household-spending multiplier 当作贡献中心。简单把被删除的空间流量重新放回一个外生矩阵，同样落在既有 multiregional SAM/Miyazawa/MRIO 框架内。

正确修复方向是：恢复一个平台特有且内生的空间组织选择，而不是恢复所有原项目机制。

## 3. 标量模型的逐方程映射

当前核心收入方程为

\[
Y=B+\omega G+(\beta+\alpha\omega)Y,
\]

故

\[
Y=\frac{B+\omega G}{1-\beta-\alpha\omega}.
\]

令

\[
c\equiv\beta+\alpha\omega,
\qquad
E\equiv B+\omega G,
\]

则

\[
Y=E+cY=(1-c)^{-1}E.
\]

这正是固定价格 SAM/Miyazawa household closure 的单账户形式。由此直接得到

\[
m_B=\frac{1}{1-\beta-\alpha\omega},
\qquad
\mathcal M_G=\frac{\omega}{1-\beta-\alpha\omega},
\]

以及几何级数

\[
\mathcal M_G
=\omega\sum_{k=0}^{\infty}(\beta+\alpha\omega)^k.
\]

### 3.1 与已有框架的精确关系

| 当前稿对象 | 已有框架中的对应对象 | 判定 |
|---|---|---|
| \(\beta+\alpha\omega\) | household/institution endogenous expenditure coefficient | 已知 |
| \((1-\beta-\alpha\omega)^{-1}\) | \(1\times1\) Leontief/SAM/Miyazawa inverse | 已知 |
| 第一轮留存 \(\omega G\) | exogenous final demand 经 local-income incidence coefficient 转化 | 已知 |
| 每轮再次发生 leakage | household closure 的 repeated rounds | 已知 |
| retention elasticity \(>1\) | rational multiplier 对系数的导数 | 直接推论 |
| \(\mathcal M_G<m_0\omega\) | 对每轮使用实际 leakage coefficient，而非只修正第一轮 | 直接推论 |

Miyazawa 将 consumption function 与生产系统联立并以 inverse 表示收入反馈；Pyatt--Round 的 SAM multiplier 区分 transfer、open-loop 和 closed-loop effects。Pennings 的 Proposition 1 更直接给出包含 \(1-\alpha\omega\) 分母的地方一般均衡项，并逐轮解释 \(\alpha\omega,(\alpha\omega)^2,\ldots\)。因此，“收入漏出在每一轮重复发生”不能再作为本文的理论创新。

### 3.2 CES share path 能保留什么

当前渠道份额

\[
s(z)=
\frac{ap_P(z)^{1-\eta}}
{(1-a)p_A^{1-\eta}+ap_P(z)^{1-\eta}}
\]

内生生成

\[
\omega(s)=(1-s)\rho_A+s\rho_P.
\]

这比直接指定 \(\omega(z)\) 更有微观基础，但只要 \(\rho_A,\rho_P\) 固定，CES 选择仍只是给标准 multiplier coefficient 提供一条参数路径。由它得到的 finite thresholds 和 below-one-half marginal-drag peak 可能是尚未被同式写出的代数结果，却仍可还原为“把 \(\omega[s(z)]\) 代入标准 inverse 后求导”。按照本轮预先设定的严格闸门，这不足以承担主贡献。

**Scalar route verdict：NO-GO。**

## 4. 两地区解析可行性

### 4.1 固定收入归属矩阵

设

\[
\mathbf y=\mathbf b+\Gamma(\omega,r)C\mathbf y,
\qquad
\Gamma=
\begin{pmatrix}
\omega&r\\
1-\omega&1-r
\end{pmatrix},
\qquad
C=\operatorname{diag}(c_L,c_H).
\]

在 \(0\le c_L,c_H<1\) 下，

\[
\|\Gamma C\|_1=\max\{c_L,c_H\}<1,
\]

所以存在唯一正的解析均衡

\[
\mathbf y=(I-\Gamma C)^{-1}\mathbf b.
\]

定义

\[
D=1-(1-r)c_H-r c_Hc_L-\omega c_L(1-c_H)>0.
\]

则

\[
\frac{\partial y_L}{\partial\omega}
=\frac{c_Ly_L(1-c_H)}{D}>0,
\qquad
\frac{\partial y_H}{\partial\omega}
=-\frac{c_Ly_L(1-c_L)}{D}<0,
\]

并且

\[
\frac{\partial(y_L+y_H)}{\partial\omega}
=\frac{c_Ly_L(c_L-c_H)}{D}.
\]

这些式子能表达标量模型遗漏的空间结果：平台化降低外围留值时，外围收入下降、总部地区收入上升；全国总收入的方向取决于两地后续支出倾向。但该系统就是标准两地区 income-feedback inverse。

**One-way matrix route verdict：NO-GO。**

### 4.2 双向 access--capture 矩阵

更强的候选为

\[
\mathbf Y=\mathbf B+\beta\mathbf Y+\alpha\Pi(q,r)\mathbf Y,
\qquad
\Pi(q,r)=
\begin{pmatrix}
1-q&r\\
q&1-r
\end{pmatrix}.
\]

令

\[
k=1-\alpha-\beta>0,
\qquad
h=k+\alpha(q+r)>0.
\]

闭式解为

\[
Y_L=\frac{kB_L+\alpha r(B_L+B_H)}{kh},
\qquad
Y_H=\frac{kB_H+\alpha q(B_L+B_H)}{kh}.
\]

因为 \(\Pi\) 是 column-stochastic，

\[
Y_L+Y_H=\frac{B_L+B_H}{k}.
\]

当 \(q=q(z)\)、\(r=r(z)\) 时，

\[
\frac{dY_L}{dz}
=-\frac{\alpha}{h}\left[q'Y_L-r'Y_H\right],
\qquad
\frac{dY_H}{dz}
=+\frac{\alpha}{h}\left[q'Y_L-r'Y_H\right].
\]

所以外围受益的充要条件是

\[
r'Y_H>q'Y_L.
\]

这一阈值直观地对应原项目的 access 与 capture，但其数学来源是标准恒等式

\[
\mathbf Y_z=L\alpha\Pi_z\mathbf Y.
\]

\(rY_H\) 由总部收入内生融资，确实比外生 \(B(z)\) 更完整；然而这种跨地区 income--expenditure closed loop 正是 multiregional Miyazawa/SAM 的研究对象。阈值仍未解释什么 primitive 决定 \(q'\) 和 \(r'\)。

**Exogenous bidirectional \(q/r\) route verdict：NO-GO。**

## 5. 为什么机械恢复空间机制仍不够

已有区域乘数文献已经覆盖：

- 地区内与地区间 spillover、feedback 和 closed-loop multiplier；
- income generation、income receipt/ownership 和 spending location 的分离；
- 固定 local/absentee ownership coefficients 对本地乘数的影响；
- 两地区或多地区 income-consumption feedback 的 block inverse。

因此，以下改动虽有助于正确核算，却不能单独主张创新：

- 把 \(\omega\) 改成 \(\Omega\) 或 \(\Pi\)；
- 增加一个固定平台总部账户；
- 把线上销售固定拆成 seller revenue、platform fee、fulfillment labor 和 tax；
- 设定固定的 local seller share、local labor share 或 absentee ownership share；
- 令外生 \(q(z),r(z)\) 非线性，并报告交叉点或 hump shape。

Rose--Stevens 所强调的 generation、receipt 和 spending locations 是模型有效性的最低条件，而不是新颖性来源。

## 6. 唯一保留的有条件路线

一个可继续检验的 EL 必须加入且只加入一项平台特有的 endogenous ownership/localization margin，例如：

1. local seller entry；
2. fulfillment facility location/capacity；
3. order routing；
4. platform fee 与 seller participation 的联合决定；
5. owner residence/payout 与平台组织选择的联动。

该 margin 必须来自明确的 optimization、entry condition 或 capacity constraint，而不是任意指定 \(q(z),r(z)\)。合格的主命题至少应是以下一种：

- primitive elasticity threshold，而不是 \(q'Y_L-r'Y_H\) 的净流量恒等式；
- fee、entry 或 localization 的严格 ranking；
- 均衡唯一性、multiplicity 或 tipping 条件；
- 同一 consumer adoption shock 在不同 ownership/fulfillment structures 下产生可排序且可证伪的地区收入反应；
- 一项政策通过改变平台的内生区位或路由产生固定系数 benchmark 中不存在的项。

关闭新增 primitive 后，模型必须严格退化为标准 multiregional inverse；主命题中的关键项也必须随之消失。

## 7. 下一阶段 novelty contract

只有以下七项全部通过，才允许修改正式稿：

1. **Known benchmark nesting**：明确把 scalar 和固定系数 matrix 当作已有 benchmark。
2. **Incidence accounting**：区分收入产生地、收取/所有权地和支出地。
3. **Platform-specific choice primitive**：至少一个关键份额由 FOC、entry 或 capacity condition 决定。
4. **Non-reducible proposition**：主结果不能由固定 \(A\) 下的 \((I-A)^{-1}\) 单独推出。
5. **Observable mapping**：关键 primitive 对应 fee、seller origin、facility node、local labor compensation、owner residence 或 routing 等可测对象。
6. **Prior-art dominance test**：逐项对照 SAM/Miyazawa、multiregional feedback、transboundary ownership 和 spatial e-commerce 文献。
7. **EL scope feasibility**：正文最多一个主命题和一个推论，能够在约 2,000 词内自足表达。

任一条件失败，则停止当前 EL 重写，并把模型作为后续大论文的 benchmark 或 appendix material。

## 8. 推荐的最小下一步

在继续触碰 main.tex 前，只做一页 theorem-feasibility memo：

1. 从 local seller entry 与 fulfillment localization 中二选一；
2. 写出最小 choice/entry condition；
3. 将线上一元支出按 generation、receipt 和 spending 三层守恒分解；
4. 推导一个 primitive-level proposition；
5. 按上节七项逐条判定；
6. 通过后才重写，失败则终止 EL 路线。

优先建议测试 **local seller entry**。它比 facility location 更容易保持解析性和 EL 篇幅，也能直接连接“统一市场带来的外销 access”与“平台抽取造成的 capture”两端。它的风险是与既有 spatial e-commerce entry models 重叠，因此 theorem 必须明确由 local-income feedback 与 ownership incidence 的联合产生，而不是普通市场规模效应。

## 9. 证据来源与边界

核心可核查来源：

- [Miyazawa (1960), *QJE*](https://academic.oup.com/qje/article-pdf/74/1/53/5206190/74-1-53.pdf)：income--consumption feedback inverse；
- [Pyatt and Round (1979), institutional reprint](https://documents1.worldbank.org/curated/en/317011468179066100/pdf/REP125000Accou0ing0matrix0framework.pdf)：SAM fixed-price multiplier 与 closed-loop decomposition；
- [Pennings (2021), *AER* author manuscript](https://documents1.worldbank.org/curated/en/559331626071176592/pdf/Cross-Region-Transfer-Multipliers-in-a-Monetary-Union-Evidence-from-Social-Security-and-Stimulus-Payments.pdf)：地方支出反馈中的 \(1-\alpha\omega\) 分母与重复轮次；
- [Sonis and Hewings (1993)](https://hdl.handle.net/10086/7798) 与 [Hewings and Sonis (2000)](https://econpapers.repec.org/article/spranresc/v_3a34_3ay_3a2000_3ai_3a4_3ap_3a569-589.htm)：multiregional Miyazawa income multipliers；
- [Rose and Stevens (1991)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9787.1991.tb00147.x)：income generation、receipt 与 spending location；
- [Jackson (1989)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-2257.1989.tb00487.x)：ownership-augmented regional IO；
- [Fan et al. (2018)](https://www.sciencedirect.com/science/article/abs/pii/S0022199618301594) 与 [Li working paper](https://elmerli.github.io/ecommerce.pdf)：多地区 e-commerce、entry 与收入效应的相邻结构模型。

限制：本轮是面向路线选择的定向审计，不宣称完成穷尽式 priority review。对只能取得出版商摘要或机构元数据的旧文献，没有虚构方程编号或超出可核查范围的精确断言。若 endogenous-entry 候选通过解析可行性，投稿前仍需对该候选命题做一次新的穷尽式检索。

## 10. 数学与文件完整性

两地区备忘录已经用固定随机种子完成两组各 10,000 次参数抽样。原两地区模型的解析导数与中心差分最大误差为 \(6.93\times10^{-8}\)；双向模型最大误差为 \(1.13\times10^{-8}\)；全国恒等式最大误差为 \(2.85\times10^{-14}\)。独立 adversarial audit 的复核误差分别低于 \(5\times10^{-10}\) 和 \(8.88\times10^{-16}\)。

正式文件在本轮结束时必须继续与冻结哈希一致；哈希和工作树状态由主执行者在交付前再次核对。

## 11. 最终 route gate

    scalar_route = NO_GO
    one_way_matrix_route = NO_GO
    exogenous_bidirectional_qr_route = NO_GO
    endogenous_platform_localization_route = FEASIBILITY_TEST_ONLY
    formal_manuscript_rewrite = PAUSED

这不是放弃“平台化重塑地方价值捕获”的研究问题。相反，它把问题重新放回真正有机会形成贡献的位置：平台的组织选择如何内生决定价值在哪个地区形成、由谁收取，并如何改变后续地方需求，而不是既定留值系数如何进入一个已知 multiplier。
