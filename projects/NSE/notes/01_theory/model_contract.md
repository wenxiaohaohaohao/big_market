# Model Contract v2.1

日期：2026-07-24

状态：活动理论合约

主轴：`platform access--local capture`；NSE 构成地方发展侧的结构骨架

## 1. 合约目的

本文件约束当前过渡性论文的模型范围。任何新增主体、变量或机制必须回答：

1. 它改变 consumer-side access、comparative-advantage realization、
   organizational embeddedness、local capture、nominal local income 或
   consumption-equivalent income 中的哪一个对象？
2. 它是否产生当前模型没有的新命题？
3. 它是否可以通过已有变量表达？

不能回答上述问题的模块不进入基准模型。

## 2. 冻结的研究问题

> 为什么平台化市场整合能够普遍改善消费者接入，却只有在潜在比较优势能够通过
> 适宜的本地组织和基础设施条件得到实现时，才会转化为本地生产和地方收入？

主结果必须同时包含：

- 平台化降低消费价格或提高品类接入；
- 平台化改变本地与外部渠道的交易份额；
- 本地生产者利用全国市场的能力取决于 LCA 及交易条件；
- 名义地方收入和消费等价实际收入可以出现不同符号；
- 结构阈值随 LCA 强度和 facilitating infrastructure 系统变化。

## 3. 理论层级

### 3.1 研究对象

平台化统一市场对地方消费者、生产者和交易服务收入的联合影响。

### 3.2 NSE 地方结构骨架

```text
endowment structure
  -> relative production cost
  -> latent comparative advantage
  -> total cost under actual infrastructure
  -> actual comparative advantage
  -> viability and realized entry
  -> organizational embeddedness
  -> local complementary services and linkages
  -> endogenous local production and capture.
```

### 3.3 EL 连接

EL 提供 access--capture 分解和第一轮收入传播逻辑。新稿必须内生化第一轮本地
收入及留值，但不得把 EL 固定点重复计入生产侧资源约束。

### 3.4 理论边界

- consumer preferences 和渠道需求使用标准消费/贸易理论；
- \(p_P(z)\) 与 \(M(z)\) 是平台化带来的 consumer-side 和 producer-side 冲击；
- NSE 决定地方如何通过产业选择、基础设施、viability 和组织嵌入回应冲击；
- payment-flow accounting 将上述选择转化为 local capture；
- EL 将第一轮地方收入映射为名义和消费等价实际收入。

NSE 可以贯穿地方发展转化链的多个环节，但不替代平台冲击、消费者需求或 EL
收入传播的理论来源。

## 4. 最小环境

### 4.1 空间范围

一个 focal region \(i\) 嵌入全国市场。全国支出和外部价格指数可以作为小地区
面对的外生市场条件。

基准模型不求解全国地区体系的一般均衡，因此不报告严格意义上的 national welfare。

### 4.2 经济主体

- 本地代表性家庭；
- 一个竞争性背景部门 \(0\)；
- 一个候选本地产业 \(j\)；
- 本地代理或本地交易服务提供者 \(A\)；
- 地区外平台渠道 \(P\)；
- 本地嵌入式生产者服务组织 \(L\)，作为候选组织方式，不必设为独立产业；
- 地方政府，仅在政策部分提供共享性基础设施。

不在基准模型引入企业生产率分布。若一个代表性候选企业已经能够产生进入和组织
阈值，则异质企业属于扩展。

### 4.3 平台化冲击

平台化程度为 \(z\)。它可以同时影响：

\[
p_P'(z)<0
\]

和：

\[
M'(z)>0.
\]

前者是本地消费者通过平台购买外部商品的成本；后者是本地生产者面对的全国市场
接入。两者由同一改革过程推动，但在模型中保持为两个不同的作用渠道。

## 5. Block A：消费者接入

本地家庭将一部分支出用于渠道复合品。传统渠道 \(A\) 和外部平台渠道 \(P\)
之间采用 CES 聚合：

\[
C_M
=
\left[
C_A^{(\eta-1)/\eta}
+
C_P^{(\eta-1)/\eta}
\right]^{\eta/(\eta-1)},
\qquad \eta>1.
\]

对应的平台支出份额记为：

\[
s(z)
=
\frac{p_P(z)^{1-\eta}}
{p_A^{1-\eta}+p_P(z)^{1-\eta}}.
\]

因此：

\[
s'(z)>0,
\qquad
P_M'(z)<0.
\]

这一部分只负责建立 consumer access 和消费价格效应，不负责决定本地产业进入。

### 支付归属

每单位传统渠道交易和平台交易必须分别列出：

- 商品生产支付；
- 本地代理、批发、仓储、物流和售后服务；
- 外部平台费、结算和外地组织服务；
- 本地所有者利润。

传统渠道与平台渠道的留值率不能作为任意能力函数。它们由所有权和服务所在地的
支付流计算。

## 6. Block B：NSE 结构实现与本地组织嵌入

### 6.1 禀赋与生产成本

地区 \(i\) 的禀赋为：

\[
E_i=(K_i,L_i).
\]

行业 \(j\) 的要素密集度为 \(\theta_j\)。背景部门形成机会成本
\((w_i,r_i)\)，候选产业的单位生产成本为：

\[
c^P_{ij}=c_j(w_i,r_i;\theta_j).
\]

### 6.2 LCA

令 \(0\) 为地区内部基准产业，\(h\) 为外部参照地区。生产成本比较指标为：

\[
\mathcal C^P_{ij}
=
\frac{c^P_{ij}/c^P_{i0}}
     {c^P_{hj}/c^P_{h0}}.
\]

若：

\[
\mathcal C^P_{ij}<1,
\]

则地区 \(i\) 在产业 \(j\) 上具有 latent comparative advantage。

\(1/c_{ij}\) 只能作为成本竞争力的单调变换，不能单独称为严格比较优势。

### 6.3 交易成本、ACA 与 viability

渠道 \(r\) 下的总成本为：

\[
c^T_{ijr}
=
c^P_{ij}+t_{ijr}(G_i).
\]

令 \(c^T_{i0}\) 和 \(c^T_{h0}\) 为两地基准产业的对应总成本。定义：

\[
\mathcal C^T_{ij}
=
\frac{\min_r c^T_{ijr}/c^T_{i0}}
     {\min_r c^T_{hjr}/c^T_{h0}}.
\]

当：

\[
\mathcal C^P_{ij}<1
\quad\text{且}\quad
\mathcal C^T_{ij}<1,
\]

候选产业既具有 latent comparative advantage，又在现有软硬基础设施与交易环境下
形成 actual comparative advantage（ACA）。LCA 比较要素生产成本；ACA 比较包含
交易成本在内的总成本。二者都不是用观察到的产值或出口份额反推得到的指标。

viability 进一步要求企业在开放竞争市场中，不依赖持续保护或补贴即可覆盖全部
实际成本并获得社会可接受的正常利润。企业进入、生产和外销是比较优势得到实现的
均衡表现，不能反过来用作 LCA 或 ACA 的定义。

企业利润写为：

\[
\pi_{ijr}
=
M(z)b_j(c^T_{ijr})
-
f_{ijr}(G_i).
\]

producer-side 组织方式只包括外部平台组织 \(P\) 与本地嵌入式组织 \(L\)。
本地代理 \(A\) 属于 Block A 的消费者渠道，不能与 producer-side 的 \(L\) 混用。

企业进入和组织选择为：

\[
n_{ij}^*
=
\mathbf 1
\left\{
\max_r\pi_{ijr}\geq0
\right\},
\]

\[
r_{ij}^*
\in
\arg\max_r
\left\{
0,\pi_{ijP},\pi_{ijL}
\right\}.
\]

### 6.4 组织嵌入与本地产业联系

\(P\) 使用外部平台已有的营销、结算、履约或供应链组织服务；\(L\) 使用由本地
主体提供的对应服务。二者的利润差为：

\[
\Delta\pi_{ij}^{L-P}
=
\pi_{ijL}-\pi_{ijP}.
\]

组织选择不仅影响企业利润，也决定同一交易的服务支付位置。对组织方式 \(r\)，
将交易所需服务成本逐项分为：

\[
H_{ijr}
=
H_{ijr}^{local}
+
H_{ijr}^{external}.
\]

本地组织服务收入由 \(H_{ijr}^{local}\) 进入 \(S_i^{local}\)；外部平台及外地
服务支付由 \(H_{ijr}^{external}\) 进入 leakage。两者必须来自同一成本和支付流
表，不能另外设定任意的 local-service share。

这里的 local linkages 只表示候选产业生产和平台销售所需配套服务由本地提供，
不包含 NEG 式集聚外部性、内生供应商品种或动态累积因果。

若 \(\Delta\pi_{ij}^{L-P}\) 对 \(G_i\) 或市场规模具有 single crossing，模型可以
产生 organizational-embedding threshold。该阈值进入基准模型的唯一理由是它改变
\(S_i^{local}\) 和 external payments，进而改变名义或实际收入阈值。

### 6.5 为什么这不是外生能力的重新命名

NSE 模块必须生成：

- 是否存在本地生产；
- 本地销售规模；
- 采用外部平台还是本地嵌入式服务；
- 本地配套服务是否形成；
- 生产利润和组织服务支付的空间归属。

不得直接设定：

\[
\kappa_i=\kappa(CA_i,G_i)
\]

再代回 EL 模型作为唯一扩展。

## 7. Block C：第一轮本地收入和 capture

对同一组交易，第一轮本地收入定义为互不重复的支付项：

\[
V_i
=
W_i^{local}
+
\Pi_i^{local}
+
S_i^{local}
+
T_i^{local}
-
C_i^{policy}.
\]

其中：

- \(W_i^{local}\)：本地生产和服务劳动收入；
- \(\Pi_i^{local}\)：本地居民所有企业获得的净经营盈余；
- \(S_i^{local}\)：本地代理、履约、认证、营销和供应链服务增加值；
- \(T_i^{local}\)：地方财政净收入，只在政策部分使用；
- \(C_i^{policy}\)：公共投入的真实资源成本。

本地价值留存率是：

\[
\omega_i
=
\frac{V_i}
{\text{与 }V_i\text{ 对应的交易总价值}}.
\]

分子和分母必须对应同一交易集合。

### 7.1 平台化的第一轮收入分解

\[
\Delta V_i
=
\underbrace{\Delta V_i^{producer}}_{\text{本地生产和外销}}
+
\underbrace{\Delta V_i^{local\ services}}_{\text{本地平台配套服务}}
-
\underbrace{\Delta V_i^{agent\ displacement}}_{\text{本地渠道被替代}}
-
\underbrace{\Delta V_i^{external\ payments}}_{\text{平台及外地服务支付}}.
\]

\(\Delta V_i^{producer}\) 必须由 Block B 的进入和销售决定，不能使用外生增长率。
\(\Delta V_i^{local\ services}\) 和
\(\Delta V_i^{external\ payments}\) 必须由 Block B 的组织选择与同一支付流表
决定，不能使用外生留值能力函数。

## 8. 名义收入与消费等价实际收入

EL 的精确传播公式在下一阶段根据 companion paper 的最终记号逐项映射。活动
contract 只冻结两个要求：

1. 第一轮收入 \(V_i\) 先由 NSE 和支付流生成；
2. 收入传播不得重复计算生产、平台服务或本地代理支付。

可暂记为：

\[
Y_i=\mathcal M_i(\omega_i)V_i.
\]

消费等价实际收入为：

\[
R_i
=
\frac{Y_i}{P_M(z)^\alpha}.
\]

核心分解为：

\[
\frac{d\ln R_i}{dz}
=
\frac{d\ln Y_i}{dz}
-
\alpha\frac{d\ln P_M(z)}{dz}.
\]

由于 \(P_M'(z)<0\)，价格接入收益使实际收入转正所需的结构条件弱于名义收入。

## 9. 核心命题合同

### P1a：LCA realization

存在进入所需的基础设施或组织条件阈值：

\[
G_E^*(\mathcal C^P_{ij},M).
\]

目标比较静态为：

\[
\frac{\partial G_E^*}
{\partial\text{LCA strength}}<0.
\]

P1a 只说明 producer-side entry，不足以单独构成全文贡献。

### P1b：Organizational embeddedness

在本地嵌入式组织相对于外部平台组织具有更高固定成本、但能够降低相关边际服务
成本或外部支付时，目标结果是存在：

\[
G_L^*
\quad\text{或等价的}\quad
M_L^*,
\]

使进入后的企业选择 \(L\) 而不是 \(P\)。P1b 必须进一步证明组织选择改变：

\[
S_i^{local}
\quad\text{和}\quad
\Delta V_i^{external\ payments}.
\]

若 P1b 不能改变 P2 或 P3，它不进入基准模型。

### P2：Nominal local-income threshold

定义平台化对名义地方收入的边际效应：

\[
\frac{d\ln Y_i}{dz}
=
\Gamma^{producer}(\text{LCA},G_i,M)
+
\Gamma^{linkage}(\text{LCA},G_i,M)
-
\Lambda^{agent}(s)
-
\Lambda^{external}(r_{ij}^*,\text{payment incidence}).
\]

目标结果是存在唯一：

\[
G_Y^*
\]

使：

\[
\frac{dY_i}{dz}\geq0
\iff
G_i\geq G_Y^*.
\]

其中 \(\Gamma^{producer}\) 由 viability 和进入推导，
\(\Gamma^{linkage}\) 由本地组织和配套服务支付推导；
\(\Lambda^{agent}\) 来自 consumer-side 渠道替代，
\(\Lambda^{external}\) 来自 producer-side 组织选择和支付流。

### P3：Real-income threshold and ordering

存在：

\[
G_R^*
\]

使消费等价实际收入在 \(G_i\geq G_R^*\) 时不下降，并证明：

\[
G_R^*<G_Y^*.
\]

进一步目标为：

\[
\frac{\partial G_R^*}{\partial\text{LCA strength}}<0,
\qquad
\frac{\partial G_Y^*}{\partial\text{LCA strength}}<0.
\]

严格排序是全文最重要的连接结果，因为它同时使用 EL 的价格收益和 NSE 生成的
生产、组织及本地产业联系响应。

### P4：Facilitation versus protection

只有在 \(G_i\) 对应共享性基础设施、协调失败或不可完全内部化的交易环境时，才
允许形成 facilitating-state 命题。

赋能降低真实本地交易或组织成本：

\[
f_{ijr}'(G_i)<0
\quad\text{或}\quad
t_{ijr}'(G_i)<0.
\]

保护提高外部渠道成本或价格。二者对 consumer access、producer entry 和 local
capture 的作用不相同。

P4 在概念上是 NSE 的核心组成，但在解析顺序上不得先于 P2 和 P3 完成。只有先
确定哪个结构约束阻止 LCA 转化为 ACA、viability 和 local embeddedness，才能
定义政府所要解决的共享基础设施或协调失败。

## 10. 旧组织阈值模型的处理

基准模型恢复 \(P\) 与 \(L\) 的最小利润比较和 payment-incidence 结果。归档 v1
中的完整平台进入阈值 \(M_P\)、本地组织盈利阈值 \(M_{L0}\) 和组织切换阈值
\(M_X\) 不整体进入基准 contract。

完整三阈值结果只有满足以下条件时，才作为 lemma 或 extension 恢复：

1. 组织选择改变 \(\Delta V_i^{local\ services}\) 或
   \(\Delta V_i^{external\ payments}\)；
2. 该变化进一步改变 \(G_Y^*\) 或 \(G_R^*\)；
3. 不需要引入新的独立状态变量。

## 11. 文献基座

| 层级 | 文献角色 |
|---|---|
| EL companion paper | access--capture 问题、价格与收入传播基准 |
| Lin and Wang (2023) | LCA--ACA、交易成本与 facilitating state |
| Lin (2011, 2012); Lin and Monga (2011) | 禀赋与产业结构、hard/soft infrastructure、viability、facilitating state |
| Ju, Lin and Wang (2015) | 禀赋驱动的产业结构来源，不复制完整动态模型 |
| Ahn, Khandelwal and Wei (2011) | 必要时提供中介与直接渠道的成本选择 |

Ahn 型组织选择不是全文唯一数学母体。Rodríguez-Clare 产业联系只有在正式加入
专业化投入品种或供应商进入时才能作为直接模型来源。

## 12. 第一版排除

- 完整 NEG、迁移和集聚外部性；
- 内生全国市场规模；
- 多平台竞争和平台内生定价；
- 动态组织资本；
- Pareto 企业分布和自由进入，除非代表性企业无法生成 P1--P3；
- 地方税收分成和财政联邦主义；
- national welfare 结论；
- 未经证明的“平台化降低地方收入”一般性判断。

## 13. 进入论文正文前的验收门槛

- [ ] consumer-side access 和 producer-side access 均已定义；
- [ ] 支付流可以产生 local channel displacement；
- [ ] LCA、ACA、viability、realization 和 revealed measures 未混用；
- [ ] 企业进入生成 producer-side local income；
- [ ] 组织选择生成 local complementary-service income 和 external payments；
- [ ] local linkages 是支付流结果，而不是外生能力函数；
- [ ] \(\omega_i\) 是支付流结果；
- [ ] P2 的收入阈值存在且唯一；
- [ ] P3 的严格排序得到证明；
- [ ] 政策部分只有一个明确市场失灵；
- [ ] EL 传播公式已与 companion paper 的最终版本逐项核对；
- [ ] legacy 文件未被正文直接引用；
- [ ] numerical exercises 只用于说明已证明命题。
