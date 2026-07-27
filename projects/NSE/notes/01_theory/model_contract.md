# Model Contract v3.1

日期：2026-07-27

状态：活动理论合约（`FROZEN`）

主轴：`platform access--local capture`
论文身份：EL 原问题的独立 NSE 理论扩展

## 1. 研究问题与理论分工

本文研究：

> 平台化市场整合为什么能够普遍改善消费者接入，却只有在潜在比较优势得到实现、
> 生产组织嵌入当地时，才转化为本地生产、收入和价值捕获？

理论分工固定如下：

1. 标准 CES 需求解释消费者渠道替代和价格接入；
2. NSE 解释禀赋决定的 latent comparative advantage（LCA）如何与软硬基础设施
   共同决定 actual comparative advantage（ACA）、viability、实际进入和本地组织
   嵌入，并严格区分这些概念；
3. 支付流决定 consumer-side retention \(\omega_C\) 和 producer-side retention
   \(\rho_r\)，二者都不是外生“本地能力”函数；
4. EL 兼容的收入递归将第一轮本地收入映射为名义地方收入和消费等价实际收入；
5. facilitating-state 模块只解释基础设施供给及融资约束，不求解全国最优政策。

NSE 可以贯穿生产成本、实际交易条件、企业自生能力、组织形式和基础设施供给，但
不得取代平台冲击、消费者需求或收入传播的理论来源。全文最终解释的对象仍是
platform access 与 local capture 的分离。

## 2. 空间范围、主体与时序

### 2.1 空间范围

一个 focal region \(i\) 嵌入全国市场。外部参照地区为 \(h\)。全国候选产业需求
规模和参照地区成本对 focal region 而言外生。背景产业给出候选产业面对的要素
机会成本；在本文考察的局部区间，边际要素服务可按该机会成本弹性供给，例如来自
闲置产能或额外工时。因此 \(B_0+B_j\) 是短期 transaction-related nominal
income，不是充分就业条件下的长期净福利。本文不求解完整多地区一般均衡，
因此不报告 national welfare。

### 2.2 主体

- 本地代表性家庭；
- 竞争性背景产业 \(0\)；
- 代表性候选产业 \(j\)；
- 消费者侧本地渠道 \(A\) 和外部平台渠道 \(P\)；
- 生产者侧外部平台组织 \(P\) 和本地嵌入式组织 \(L\)；
- 基础设施提供者；
- 通过融资参与度 \(\vartheta\) 影响基础设施融资成本的政府。

消费者侧的 \(A/P\) 是购买渠道；生产者侧的 \(P/L\) 是本地候选产业进入全国市场
后的组织方式。两个 \(P\) 都依赖外部平台，但支付流不同，正文必须按语境区分。

### 2.3 时序

1. 地区禀赋、产业技术和政府参与度 \(\vartheta\) 给定；
2. 基础设施提供者选择 \(G\)；
3. 平台化程度 \(z\) 决定消费者平台价格和生产者市场接入；
4. 候选产业比较不进入、外部平台组织和本地嵌入组织的利润；
5. 家庭分配支出，支付流形成第一轮本地收入；
6. EL 兼容的本地收入递归闭合 \(Y\) 和 \(R\)。

## 3. 消费者接入与渠道支付流

### 3.1 偏好

\[
U=Q_M^{\alpha_M}N^\beta Z^{1-\alpha_M-\beta},
\qquad
\alpha_M+\beta<1.
\]

市场品复合品为：

\[
Q_M=
\left[
(1-a_P)^{1/\eta}Q_A^{(\eta-1)/\eta}
+a_P^{1/\eta}Q_P^{(\eta-1)/\eta}
\right]^{\eta/(\eta-1)},
\qquad \eta>1.
\]

平台化降低平台有效价格：

\[
p_P(z)=\bar p_Pe^{-z},
\qquad p_A=1.
\]

平台支出份额和市场品价格指数为：

\[
s(z)=
\frac{a_Pp_P(z)^{1-\eta}}
{(1-a_P)p_A^{1-\eta}+a_Pp_P(z)^{1-\eta}},
\]

\[
P_M(z)=
\left[
(1-a_P)p_A^{1-\eta}+a_Pp_P(z)^{1-\eta}
\right]^{1/(1-\eta)}.
\]

因此：

\[
s'(z)=(\eta-1)s(z)[1-s(z)]>0,
\qquad
\frac{d\ln P_M}{dz}=-s(z)<0.
\]

### 3.2 消费渠道留值

\(\ell_A\) 和 \(\ell_P\) 是每单位本地消费者渠道支出形成的本地收入含量。它们来自
同一支付流口径：

| 支付项目 | 本地渠道 \(A\) | 外部平台渠道 \(P\) |
|---|---:|---:|
| 本地零售、批发、仓储、售后增加值 | 本地 | 基准中较少或为零 |
| 外部商品生产支付 | 外部 | 外部 |
| 平台费、外地结算和外地服务 | 少或为零 | 外部 |
| 本地所有者净收入 | 本地 | 按实际所有权归属 |

基准设定为 \(\ell_A>\ell_P\)，但附录报告 \(\ell_P\geq\ell_A\)。

\[
\omega_C(z)=[1-s(z)]\ell_A+s(z)\ell_P,
\]

\[
D(z)=1-\beta-\alpha_M\omega_C(z)>0.
\]

消费者侧 capture drag 为：

\[
\Lambda(z)=
\frac{\alpha_M(\ell_A-\ell_P)s'(z)}
{D(z)}.
\]

## 4. 禀赋、LCA、ACA、viability 与 realization

### 4.1 禀赋和机会成本

地区 \(i\) 的资本劳动禀赋为：

\[
e_i=\frac{K_i}{L_i}.
\]

背景产业使用 Cobb--Douglas 技术：

\[
Y_{i0}=A_0K_{i0}^{\theta_0}L_{i0}^{1-\theta_0}.
\]

当候选产业相对于背景产业足够小，背景产业决定基准机会成本：

\[
w_i=(1-\theta_0)A_0e_i^{\theta_0},
\qquad
r_i=\theta_0A_0e_i^{\theta_0-1}.
\]

候选产业的生产技术为：

\[
Y_{ij}=A_jK_{ij}^{\theta_j}L_{ij}^{1-\theta_j}.
\]

其单位生产成本为：

\[
c^P_{ij}
=
\frac{1}{A_j}
\left(\frac{r_i}{\theta_j}\right)^{\theta_j}
\left(\frac{w_i}{1-\theta_j}\right)^{1-\theta_j}
=\xi_j e_i^{\theta_0-\theta_j},
\]

其中 \(\xi_j>0\) 汇总技术参数。当 \(\theta_j>\theta_0\) 时，资本相对丰富降低候选
产业相对于背景产业的生产成本。

### 4.2 四个不得混用的概念

**Latent comparative advantage（LCA）** 由地区和产业双重相对生产成本定义：

\[
\mathcal C^P_{ij}
=
\frac{c^P_{ij}/c^P_{i0}}
{c^P_{hj}/c^P_{h0}}.
\]

\[
\mathcal C^P_{ij}<1
\]

表示地区 \(i\) 在产业 \(j\) 具有 LCA。正文中用于比较静态的 \(c\) 是
\(\mathcal C^P_{ij}\) 的单调成本充分统计量；\(1/c\) 不能单独定义比较优势。

**Actual comparative advantage（ACA）** 比较现实软硬基础设施下的相对总交付
成本。令完整的 outbound iceberg cost 为：

\[
\tau_O(z,G)=\bar\tau_O\exp[-(\gamma+\chi z)G],
\qquad \bar\tau_O>1,\quad\gamma\geq0,\quad\chi>0.
\]

分析限制在 \(\tau_O(z,G)\geq1\) 的区间。常数项
\(\bar\tau_O^{1-\sigma}\) 吸收到后文的 \(\mathcal M_0\)，因此不成为新的自由
比较静态参数。渠道 \(r\) 的总交付成本为 \(\tau_O(z,G)m_r\)。ACA 指候选产业的
双重相对总成本低于参照地区，而不是指已经观察到生产或出口。

将本地背景产业单位成本标准化为 1，以 \(\bar c_h^A>0\) 表示参照地区候选产业与
背景产业的现实总交付成本比。组织方式 \(r\) 下：

\[
\mathcal C^A_{ijr}(z,G)
=
\frac{\tau_O(z,G)(c+d_r)}{\bar c_h^A}.
\]

\[
\min_{r\in\{P,L\}}\mathcal C^A_{ijr}(z,G)\leq1
\]

表示地区 \(i\) 在产业 \(j\) 具有 ACA。对应的最低基础设施阈值是：

\[
G_A(z,c)
=
\max\left\{
0,\,
\min_{r\in\{P,L\}}
\frac{\ln[\bar\tau_O(c+d_r)/\bar c_h^A]}
{\gamma+\chi z}
\right\}.
\]

\(G_A\) 是相对总交付成本门槛，不含固定成本；\(G_E\) 是利润与 viability 门槛，
包含固定成本。两者不得合并。

**Viability** 指企业在开放竞争中、不依赖持续保护，能够覆盖生产成本、组织成本和
固定进入成本：

\[
\max_{r\in\{P,L\}}\pi_r\geq0.
\]

**Realization** 指候选产业在均衡中实际进入、生产和销售。它是可观察的均衡结果，
不是 LCA 或 ACA 的定义。由于需求规模或保护也可能支持进入，realization 本身不
证明 ACA；符合 NSE 的可持续转化要求同时考察 LCA、ACA 与 viability。

## 5. 生产者市场接入、进入与组织选择

### 5.1 市场接入

全国 CES 需求为：

\[
q_r=\mathcal M(z,G)p_r^{-\sigma},
\qquad \sigma>1.
\]

全国支出机会为 \(\mathcal M_0e^{\varepsilon z}\)。将 iceberg cost 代入 CES 需求
得到：

\[
\mathcal M(z,G)
=
\mathcal M_0
\exp\left\{
\varepsilon z+(\sigma-1)(\gamma+\chi z)G
\right\}.
\]

\(\varepsilon\) 是平台化直接扩大 producer-side market access 的效应；
\(\chi>0\) 表示平台接入与地方基础设施互补。消费者平台价格和生产者市场接入由
同一 \(z\) 推动，但不是同一个价格或成本对象。

### 5.2 两种组织方式

\[
m_P=c+d_P,
\qquad
m_L=c+d_L,
\qquad
0\leq d_L<d_P.
\]

\[
F_P=f,
\qquad
F_L=f+F,
\qquad f>0,\quad F>0.
\]

外部平台组织 \(P\) 利用现成的外部营销、结算、履约和供应链服务，固定成本较低，
但每单位外部组织支付较高。本地嵌入组织 \(L\) 需要承担额外共同固定成本 \(F\)，
但其单位组织成本更低。

CES 加成、销售额和利润为：

\[
\mu=\frac{\sigma}{\sigma-1},
\qquad
p_r=\mu m_r,
\]

\[
\mathcal R_r(z,G)
=
\mathcal M(z,G)\mu^{1-\sigma}m_r^{1-\sigma},
\]

\[
\pi_r(z,G)
=
\frac{\mathcal R_r(z,G)}{\sigma}-F_r.
\]

企业选择：

\[
r^*(z,G)\in
\arg\max\{0,\pi_P(z,G),\pi_L(z,G)\}.
\]

精确平局时选择本地嵌入程度更高的状态；这一约定只决定边界点，不改变阈值。

### 5.3 完整状态阈值

令：

\[
k=\frac{\mu^{1-\sigma}}{\sigma},
\qquad
\Omega(z)=(\sigma-1)(\gamma+\chi z)>0.
\]

两种组织方式各自达到零利润的原始阈值为：

\[
G_r^0(z,c)
=
\frac{
\ln\left[
\frac{F_r}
{k\mathcal M_0e^{\varepsilon z}m_r^{1-\sigma}}
\right]
}{\Omega(z)},
\qquad r\in\{P,L\}.
\]

实际进入阈值：

\[
G_E(z,c)=\max\{0,\min[G_P^0(z,c),G_L^0(z,c)]\}.
\]

本地组织与外部平台组织利润相等的原始阈值为：

\[
G_X(z,c)
=
\frac{
\ln\left[
\frac{F}
{k\mathcal M_0e^{\varepsilon z}
\left(m_L^{1-\sigma}-m_P^{1-\sigma}\right)}
\right]
}{\Omega(z)}.
\]

本地组织嵌入阈值必须直接按均衡选择定义：

\[
G_L(z,c)
=
\inf\{G\geq0:\pi_L(z,G)\geq\max\{0,\pi_P(z,G)\}\}.
\]

令 \(b_r=km_r^{1-\sigma}\)。当：

\[
F>\bar F
\equiv
f\frac{b_L-b_P}{b_P},
\]

有：

\[
G_P^0<G_L^0<G_X.
\]

于是存在“不进入—外部平台依赖—本地嵌入”三个区间。若
\(F\leq\bar F\)，企业从不进入直接转入 \(L\)。因此：

\[
G_L(z,c)
=
\begin{cases}
\max\{0,G_X(z,c)\},&F>\bar F,\\
\max\{0,G_L^0(z,c)\},&F\leq\bar F.
\end{cases}
\]

用 \(G_X\) 无条件定义 \(G_L\) 是错误的；这一分段定义必须在代码、正文和证明中一致。

## 6. 生产者支付流与第一轮本地收入

候选产业本地收入为：

\[
B_j^r(z,G)=\rho_r\mathcal R_r(z,G).
\]

极化基准下：

\[
\rho_P
=
1-\frac{d_P}{\mu(c+d_P)}
<1,
\qquad
\rho_L=1.
\]

这里 \(d_Pq_P\) 是支付给外部平台及外地组织服务的单位支付。生产要素收入、企业
利润和本地组织服务收入归本地。固定成本 \(f\) 和 \(F\) 决定 viability 与组织
选择；若它们由本地要素和服务提供者获得，则是本地内部支付，不能再次从本地收入
中扣除。

允许平台服务的一部分在本地提供：

\[
\rho_P(\lambda)
=
1-\frac{(1-\lambda)d_P}{\mu(c+d_P)},
\qquad \lambda\in[0,1].
\]

当企业由 \(P\) 转向 \(L\) 时：

- producer revenue 从 \(\mathcal R_P\) 上升至 \(\mathcal R_L\)；
- 外部单位服务支付下降；
- 本地服务收入和本地企业收入上升；
- \(\rho_r\) 从 \(\rho_P\) 上升至 \(\rho_L\)。

这些变化来自同一成本和支付流，不另外引入 local-capacity 函数。

## 7. EL 兼容的地方收入传播

令 \(B_0>0\) 为背景产业第一轮本地收入。家庭把收入的 \(\beta\) 用于本地非贸易品，
把 \(\alpha_M\) 用于市场品；其中 \(\omega_C(z)\) 成为本地收入。避免重复计算后的
固定点为：

\[
Y
=
B_0+B_j^{r^*}
+\beta Y+\alpha_M\omega_C(z)Y,
\]

即：

\[
Y(z,G)
=
\frac{B_0+B_j^{r^*}(z,G)}
{D(z)}.
\]

消费等价实际收入为：

\[
R(z,G)=\frac{Y(z,G)}{P_M(z)^{\alpha_M}}.
\]

定义候选产业在第一轮收入中的份额：

\[
\theta_r(z,G)
=
\frac{B_j^r(z,G)}
{B_0+B_j^r(z,G)}.
\]

在固定组织状态内：

\[
\frac{d\ln Y}{dz}
=
\theta_r(z,G)
\left[\varepsilon+(\sigma-1)\chi G\right]
-\Lambda(z),
\]

\[
\frac{d\ln R}{dz}
=
\frac{d\ln Y}{dz}+\alpha_Ms(z).
\]

\(Y\) 是名义地方收入，\(R\) 是消费等价地方收入。二者均不是 national welfare；
基础设施真实资源成本和外部主体福利没有被纳入完整全国资源约束。

## 8. Facilitating state

政府参与度 \(\vartheta\in[0,1]\) 降低基础设施融资楔子：

\[
\kappa_I(\vartheta)
=
\kappa_p-(\kappa_p-\kappa_g)\vartheta,
\qquad
0<\kappa_g<\kappa_p.
\]

基础设施提供者解决：

\[
\max_{G\geq0}
\left\{
\mathcal U_I(G)-\kappa_I(\vartheta)C(G)
\right\},
\]

其中：

\[
\mathcal U_I'>0,\quad
\mathcal U_I''<0,\quad
C'>0,\quad C''\geq0.
\]

内点一阶条件为：

\[
\mathcal U_I'[G(\vartheta)]
=
\kappa_I(\vartheta)C'[G(\vartheta)].
\]

严格凹性保证唯一解。政府参与缓解共享基础设施融资约束，但本文不声称
\(\vartheta\) 是全国福利最优值。

数值练习使用：

\[
\mathcal U_I(G)=a_I\ln(1+G),
\qquad
C(G)=\frac{G^2}{2},
\]

从而：

\[
G(\vartheta)
=
\frac{-1+\sqrt{1+4a_I/\kappa_I(\vartheta)}}{2}.
\]

保护政策同时提高消费者侧平台价格和生产者侧外部平台组织成本。它可能通过恶化
外部渠道诱导本地化，却降低消费者接入并提高边际企业的进入门槛。facilitation
提高 \(G\)，降低真实交易约束且不直接提高消费者平台价格。

## 9. 四个正式命题

### Proposition 1：LCA, ACA, and viable entry

在 \(\gamma+\chi z>0\)、\(\Omega(z)>0\) 且相应阈值为内部解时，\(G_A\) 与
\(G_E\) 分别存在并且：

\[
\frac{\partial G_A}{\partial c}>0,
\qquad
\frac{\partial G_E}{\partial c}>0.
\]

由于 \(c\) 是 \(\mathcal C^P_{ij}\) 的单调成本统计量：

\[
\frac{\partial G_A}{\partial\mathcal C^P_{ij}}>0,
\qquad
\frac{\partial G_E}{\partial\mathcal C^P_{ij}}>0.
\]

更强 LCA 分别降低形成 ACA 和 viable entry 所需的基础设施。由于 \(G_A\) 不含
固定成本、\(G_E\) 不含参照地区现实交付成本，二者一般不相等。若原始阈值小于零，
截断后的阈值只弱单调；这是边界而不是反例。

### Proposition 2：Organizational embeddedness

在 \(d_L<d_P\)、\(F>0\)、\(\Omega(z)>0\) 下，\(G_L\) 存在。在内部解处：

\[
\frac{\partial G_L}{\partial c}>0.
\]

当 \(G\geq G_L\) 时，企业选择 \(L\)，并有：

\[
\rho_L>\rho_P,\qquad
B_j^L>B_j^P.
\]

若 \(F>\bar F\)，外部平台依赖是进入和本地嵌入之间的独立均衡区间；若
\(F\leq\bar F\)，该区间可以消失。

### Proposition 3：Nominal and real-income thresholds

在每个固定组织区间内，\(d\ln Y/dz\) 和 \(d\ln R/dz\) 对 \(G\) 严格增加；进入和
从 \(P\) 转向 \(L\) 产生向上的离散跳跃。若端点跨越零，则分别存在唯一最小阈值：

\[
G_Y=\inf\left\{G:\frac{d\ln Y}{dz}\geq0\right\},
\]

\[
G_R=\inf\left\{G:\frac{d\ln R}{dz}\geq0\right\}.
\]

由于 \(\alpha_Ms(z)>0\)：

\[
G_R\leq G_Y.
\]

若两个根均位于同一连续组织区间且为内部解：

\[
G_R<G_Y.
\]

若零点由同一个离散进入或组织切换跨越，可能有 \(G_R=G_Y\)。更强 LCA 弱降低
两个阈值，并在相同内部组织区间内严格降低它们。

### Proposition 4：State enabling and protection

基础设施供给唯一并满足：

\[
G'(\vartheta)>0.
\]

对任一存在的结构或收入阈值 \(G_H\)，定义：

\[
\vartheta_H=\inf\{\vartheta:G(\vartheta)\geq G_H\},
\quad
H\in\{A,E,L,R,Y\}.
\]

政府参与提高 \(G\)，从而缩小 \(G_H-G(\vartheta)\)。更强 LCA 通过降低
\(G_A,G_E,G_L,G_R,G_Y\) 弱降低相应政府参与门槛。

facilitation 和 protection 都可能促进本地化，但不等价：前者降低真实基础设施
约束并扩大 producer access；后者提高外部平台价格或组织成本，恶化 consumer
access，并可能提高使用平台进入全国市场的边际企业门槛。

## 10. 边界和反例合同

正文或附录必须报告：

1. \(\ell_A=\ell_P\)：consumer-side capture drag 消失；
2. \(\ell_P>\ell_A\)：平台渠道替代提高 consumer-side retention；
3. \(\rho_P=\rho_L\)：组织切换不再产生 producer-side 空间支付差；
4. \(\chi=0\)：基础设施与平台 producer access 的互补性消失；
5. \(\lambda>0\)：平台服务部分本地化，外部支付差缩小；
6. \(F\leq\bar F\)：平台依赖区间消失；
7. \(G_R=G_Y\)：两个效应在同一个离散状态切换点转正；
8. 保护提高 \(d_P\)：可能降低 \(G_L\)，但同时提高平台进入门槛并损害消费者接入；
9. 阈值原始值小于零：截断阈值为零，比较静态弱化；
10. \(D(z)\leq0\)：收入递归不稳定，该参数区域排除。

## 11. 第一版明确排除

- 完整 New Economic Geography；
- 人口迁移、土地、住房和内生城市规模；
- 企业生产率分布和自由进入；
- 动态组织资本；
- 多平台战略定价和双边网络效应；
- 全国社会规划者和 national welfare；
- 地方财政分成、税收归属和转移支付；
- 使用实际数据的 calibration 或经验识别。

## 12. 数值与复现合同

数值练习只证明参数区域非空并展示解析机制，不识别或估计中国参数。所有图必须：

- 由 `code/numerical/generate_figures.py` 生成；
- 同时输出 PDF、PNG 和 CSV source data；
- 使用 `code/theory/validate_model.py` 对解析导数、阈值唯一性、边界和有限差分进行
  核验；
- 在正文中称为 `illustrative numerical exercises`，不得称为 calibration。

## 13. 正文进入条件

- [x] consumer-side 和 producer-side access 已分开定义；
- [x] LCA、ACA、viability 和 realization 已严格区分；
- [x] 企业进入和组织选择由同一利润问题生成；
- [x] \(\omega_C\) 和 \(\rho_r\) 均由支付流生成；
- [x] 固定成本、外部支付和本地内部支付不存在重复扣除；
- [x] 四个命题已经完成解析推导和边界检查；
- [x] \(G_R<G_Y\) 只在充分条件下声称；
- [x] facilitating state 对应基础设施融资约束，不等于任意补贴；
- [x] numerical exercises 已通过有限差分和参数网格检查；
- [x] local income、consumption-equivalent income 和 national welfare 已区分；
- [x] 全文研究对象仍是 platform access--local capture。
