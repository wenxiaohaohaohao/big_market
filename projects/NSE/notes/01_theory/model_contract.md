# Model Contract v4.1

日期：2026-07-28
状态：活动理论合约（`FROZEN`）
主轴：`platform access--local capture`
论文身份：EL 原问题的独立 NSE 理论扩展

## 1. 唯一研究问题

> 平台化市场整合为什么能够普遍改善消费者接入，却只有在符合当地 latent
> comparative advantage 的产业实际进入全国市场、并把互补组织服务嵌入当地时，
> 才转化为本地生产、收入和价值捕获？

本文不是一般性的 LCA--ACA 论文，也不是把 EL 中的本地能力改名为比较优势。理论
分工冻结如下：

1. CES 需求解释消费者平台采用和价格接入；
2. NSE 解释禀赋决定的 LCA、交易约束如何影响其实际实现、共享基础设施和
   facilitating state；
3. 固定成本--单位成本组织选择解释外部平台依赖与本地组织嵌入；
4. 支付流生成 consumer-side local content \(\omega_C\) 和 producer-side
   retention \(\rho_r\)；
5. EL 兼容的收入递归只传播模型已经生成的第一轮本地收入。

## 2. 理论母体与模块来源

| 模块 | 本文使用的内容 | 理论来源 | 不使用的内容 |
|---|---|---|---|
| 消费需求 | CES 渠道份额与价格指数 | Dixit--Stiglitz | 平台战略定价、双边网络效应 |
| 禀赋与相对生产成本 | 禀赋结构约束产业结构和相对生产成本 | Lin (2011, 2012)、Ju--Lin--Wang、Romalis | 动态资本积累、完整多产业 GE |
| LCA 到 ACA 的实现 | LCA 是相对生产成本所预示的潜在专业化；交易成本与基础设施决定实际生产/出口结构（ACA） | Lin--Wang (2023)、Lin--Monga (2010) | 独立 ACA 指数、把 realization 再设为第三个状态 |
| viability 的解释边界 | 无持续补贴或保护时，正常经营企业能够获得正常利润 | Lin (2003) | 独立 viability 指数或独立门槛 |
| 组织选择 | 低固定成本--高单位成本与高固定成本--低单位成本的条件性排序 | Ahn--Khandelwal--Wei | 异质企业分布、多目的地 |
| 本地嵌入 | 专业化生产者服务和产业联系具有本地固定成本 | Rodríguez-Clare (1996) | 原文完整均衡 |
| 市场接入 | iceberg cost 以 \(1-\sigma\) 弹性进入 CES 市场接入 | 标准贸易/市场接入模型 | NEG 区位、迁移和集聚反馈 |
| 地方收入传播 | household-endogenous local multiplier | Type II IO/SAM、Moretti、EL companion | 将乘数本身作为新贡献 |
| facilitating state | 政府参与降低共享基础设施融资楔子 | Lin--Wang (2023) 的窄化适配；Lin--Monga 的一般逻辑 | 全国最优政府参与、任意产业补贴 |

## 3. 范围、主体与时序

一个 focal region \(i\) 嵌入外生全国市场。主体包括家庭、竞争性背景产业、
代表性候选产业、消费者侧本地/平台渠道、生产者侧外部平台/本地嵌入组织、
基础设施提供者和参与融资的政府。

时序：

1. 禀赋、技术和政府参与度 \(\vartheta\) 给定；
2. 基础设施提供者选择共享基础设施 \(G\)；
3. 平台化 \(z\) 同时影响 consumer access 与 producer access；
4. 候选生产者在 \(0,P,L\) 中选择；
5. 支付流决定第一轮本地收入；
6. 家庭支出递归决定名义地方收入 \(Y\) 和消费等价收入 \(R\)。

本文是小地区局部均衡，不报告 national welfare。

## 4. 消费者接入与支付流

\[
U=Q_M^{\alpha_M}N^\beta Z^{1-\alpha_M-\beta},
\qquad \alpha_M+\beta<1.
\]

\[
Q_M=
\left[
(1-a_P)^{1/\eta}Q_A^{(\eta-1)/\eta}
+a_P^{1/\eta}Q_P^{(\eta-1)/\eta}
\right]^{\eta/(\eta-1)},\qquad \eta>1.
\]

\[
p_A=1,\qquad p_P(z)=\bar p_Pe^{-z}.
\]

\[
s'(z)=(\eta-1)s(z)[1-s(z)]>0,\qquad
\frac{d\ln P_M}{dz}=-s(z)<0.
\]

渠道 \(r\in\{A,P\}\) 的本地收入含量严格定义为：

\[
\ell_r=
\frac{\text{本地要素收入+本地所有经营盈余+本地服务增加值}}
{\text{本地家庭通过渠道 }r\text{ 的总支出}},
\qquad 0\leq\ell_r\leq1.
\]

税收和转移不进入定义，因为模型没有政府预算。

\[
\omega_C(z)=[1-s(z)]\ell_A+s(z)\ell_P,
\]

\[
D(z)=1-\beta-\alpha_M\omega_C(z).
\]

由于 \(\omega_C\leq1\) 且 \(\alpha_M+\beta<1\)，
\(D(z)\geq1-\alpha_M-\beta>0\)，不另设稳定性假设。

\[
\Lambda(z)=
\frac{\alpha_M(\ell_A-\ell_P)s'(z)}{D(z)}.
\]

基准为 \(\ell_A>\ell_P\)；反向情形必须报告。

## 5. 禀赋、LCA 与实际实现

\[
e_i=\frac{K_i}{L_i}.
\]

背景产业：

\[
Y_{i0}=A_0K_{i0}^{\theta_0}L_{i0}^{1-\theta_0},
\]

\[
w_i=(1-\theta_0)A_0e_i^{\theta_0},\qquad
r_i=\theta_0A_0e_i^{\theta_0-1}.
\]

候选产业：

\[
Y_{ij}=A_jK_{ij}^{\theta_j}L_{ij}^{1-\theta_j},
\]

\[
c^P_{ij}
=
\frac{1}{A_j}
\left(\frac{r_i}{\theta_j}\right)^{\theta_j}
\left(\frac{w_i}{1-\theta_j}\right)^{1-\theta_j}
=\xi_je_i^{\theta_0-\theta_j}.
\]

Lin--Wang (2023) 没有建立
“LCA 指数—ACA 指数—viability—realization”四级理论。该文把传统理论基于
相对生产成本所预测的专业化潜力称为 LCA；企业依据包括生产成本和交易成本在内
的总成本决定是否进入，实际出现的生产和出口结构称为 ACA。其实证部分以国家
禀赋与产品要素需求之间的距离识别 LCA，以出口参与和 RCA 识别 ACA；理论部分
则让基础设施改变固定交易成本、可变交易效率和冰山成本，从而改变均衡中的
active-industry set。

本文的双重相对生产成本是该 production-cost criterion 在两地区、两产业环境中的
操作化：

\[
\mathcal C^P_{ij}
=
\frac{c^P_{ij}/c^P_{i0}}
{c^P_{hj}/c^P_{h0}}.
\]

\(\mathcal C^P_{ij}<1\) 表示地区 \(i\) 在产业 \(j\) 具有 LCA。正文中的
\(c\equiv c^P_{ij}\) 只是保持其他相对成本不变时的单调充分统计量：

\[
\frac{\partial c}{\partial\mathcal C^P_{ij}}>0.
\]

来源边界必须保持如下：

- Lin (2011)、Lin (2012) 和 Ju--Lin--Wang 支撑的是
  “禀赋结构约束比较优势和产业结构”，不是本文双重相对成本公式的直接来源；
- Lin--Wang (2023) 明确提出生产成本所预示的 LCA 与交易成本作用后的 ACA
  之间的差异，但 ACA 在该文中最终表现为实际生产、出口和 RCA，而不只是一个
  独立的 relative-total-cost index；
- Lin--Monga (2010) 将政策问题写成识别 latent-CA industries、解除阻碍企业进入
  的约束，并使这些产业成为 actual comparative advantage；
- Lin (2003) 的 viability 是另一条理论线：正常经营企业在 free, open, and
  competitive market 中不依赖外部补贴或保护而获得 socially acceptable normal
  profit。它不是 Lin--Wang 的 LCA—ACA 模型中的中间状态。

因此，本文只正式建模两个必要边际：

\[
\underbrace{\text{endowment-conditioned relative production cost}}_{\text{LCA}}
\quad+\quad
\underbrace{\text{transaction costs, infrastructure, and market size}}_
{\text{realization constraints}}
\quad\longrightarrow\quad
\underbrace{\max\{\pi_P,\pi_L\}\geq0}_{\text{actual entry and sales}}.
\]

实际进入和销售是本文对应于 LCA 转化为 ACA 的国内市场结果，不再另设
realization 变量或 \(G_A\)。固定成本 \(f,F\) 包含正常回报和机会成本，且模型
不存在持续的选择性保护，因此 \(\max\{\pi_P,\pi_L\}\geq0\) 与 Lin (2003) 的
viability 判据相容；但本文不声称完整建模 viability，也不另设 viability index 或
threshold。正式的 \(G_E\) 只是 actual-entry threshold。

## 6. Producer access 与组织选择

全国 CES 需求：

\[
q_r=\mathcal M(z,G)p_r^{-\sigma},\qquad \sigma>1.
\]

Outbound iceberg cost：

\[
\tau_O(z,G)=\bar\tau_Oe^{-\psi z-\gamma G},
\qquad \psi>0,\quad\gamma>0.
\]

\(z\) 表示平台降低搜索、协调和交付成本；\(G\) 是道路、宽带骨干、公共标准、
认证或合同执行等非企业专用的共享软硬基础设施。常数项吸收进 \(\mathcal M_0\)：

\[
\mathcal M(z,G)
=
\mathcal M_0
\exp\{(\sigma-1)(\psi z+\gamma G)\}.
\]

基准不含 \(zG\) 交互。附录扩展：

\[
\mathcal M^{ext}(z,G)
=
\mathcal M_0
\exp\{(\sigma-1)(\psi z+\gamma G+\chi^{ext}zG)\},
\qquad \chi^{ext}>0.
\]

两种组织：

\[
m_P=c+d_P,\qquad m_L=c+d_L,\qquad d_L<d_P,
\]

\[
F_P=f,\qquad F_L=f+F.
\]

- \(f\)：产品适配、认证和初始进入的企业经济固定成本；
- \(F\)：本地仓储、运营团队、质量控制或卖家服务网络的组织专用固定成本；
- \(G\)：非企业专用共享基础设施；
- \(d_P\)：外部平台和外地组织服务单位支付；
- \(d_L\)：本地组织服务单位成本。

\[
\mu=\frac{\sigma}{\sigma-1},\qquad p_r=\mu m_r,
\]

\[
\mathcal R_r=\mathcal M\mu^{1-\sigma}m_r^{1-\sigma},
\qquad
\pi_r=\frac{\mathcal R_r}{\sigma}-F_r.
\]

\[
r^*(z,G)\in\arg\max\{0,\pi_P,\pi_L\}.
\]

令：

\[
k=\frac{\mu^{1-\sigma}}{\sigma},\qquad
\Omega=(\sigma-1)\gamma.
\]

\[
G_r^0=
\frac{
\ln\left[
\frac{F_r}
{k\mathcal M_0e^{(\sigma-1)\psi z}m_r^{1-\sigma}}
\right]}
{\Omega}.
\]

\[
G_E=\max\{0,\min(G_P^0,G_L^0)\}.
\]

\[
G_X=
\frac{
\ln\left[
\frac{F}
{k\mathcal M_0e^{(\sigma-1)\psi z}
(m_L^{1-\sigma}-m_P^{1-\sigma})}
\right]}
{\Omega}.
\]

\[
G_L=
\inf\{G\geq0:\pi_L\geq\max(0,\pi_P)\}.
\]

令 \(b_r=km_r^{1-\sigma}\) 和
\(\bar F=f(b_L-b_P)/b_P\)。若 \(F>\bar F\)，有
\(G_P^0<G_L^0<G_X\)，从而出现不进入—平台依赖—本地嵌入三区域。若
\(F\leq\bar F\)，平台依赖区间消失。

## 7. Producer payment incidence

基准假定生产要素、生产企业剩余和本地组织服务均由本地所有者获得，不含进口中间品
和外部股权。第一轮候选产业本地收入为：

\[
B_j^r=\rho_r\mathcal R_r.
\]

\[
\rho_P=
1-\frac{d_P}{\mu(c+d_P)}<1,\qquad
\rho_L=1.
\]

\(\rho_L=1\) 是极化支付归属基准，不是一般事实。平台服务部分本地化：

\[
\rho_P(\lambda)
=
1-\frac{(1-\lambda)d_P}{\mu(c+d_P)},
\qquad \lambda\in[0,1].
\]

本地提供的 \(f,F\) 是本地要素和服务收入；不能在企业利润中作为成本扣除后，再从
地区支付流中重复扣除。

## 8. EL-compatible income propagation

\[
Y=B_0+B_j^{r^*}+\beta Y+\alpha_M\omega_C(z)Y,
\]

\[
Y(z,G)=\frac{B_0+B_j^{r^*}(z,G)}{D(z)},
\qquad
R(z,G)=\frac{Y(z,G)}{P_M(z)^{\alpha_M}}.
\]

定义：

\[
\zeta_r(z,G)=
\frac{B_j^r(z,G)}{B_0+B_j^r(z,G)}.
\]

固定组织状态内：

\[
\frac{d\ln Y}{dz}
=
\zeta_r(z,G)(\sigma-1)\psi-\Lambda(z),
\]

\[
\frac{d\ln R}{dz}
=
\frac{d\ln Y}{dz}+\alpha_Ms(z).
\]

这里 \(Y\) 是 local nominal income accounting measure，\(R\) 是
consumption-equivalent local income，均不是 national welfare。

## 9. Facilitating state

\[
\kappa_I(\vartheta)
=
\kappa_p-(\kappa_p-\kappa_g)\vartheta,
\qquad 0<\kappa_g<\kappa_p.
\]

\[
\max_{G\geq0}
\{\mathcal U_I(G)-\kappa_I(\vartheta)C(G)\},
\]

\[
\mathcal U_I'>0,\quad\mathcal U_I''<0,\quad
C'>0,\quad C''\geq0.
\]

唯一内点满足：

\[
\mathcal U_I'[G(\vartheta)]
=
\kappa_I(\vartheta)C'[G(\vartheta)],
\qquad G'(\vartheta)>0.
\]

这是 Lin--Wang (2023) 融资机制的窄化适配。它不等于任意成本补贴，不求解
\(\vartheta\) 的全国福利最优值。

外部渠道限制 \((\tau_C>1,d_P\uparrow)\) 只作为单独政策例子，不属于 Proposition
4，也不被称为 NSE 中所有 protection 的一般定义。

## 10. 四个正式命题

1. **LCA and actual entry**：\(G_E\) 存在；内部解处
   \[
   \frac{\partial G_E}{\partial c}>0,\qquad
   \frac{\partial G_E}{\partial\mathcal C^P_{ij}}>0.
   \]
2. **Organizational embeddedness**：\(G_L\) 存在；内部解处
   \[
   \frac{\partial G_L}{\partial c}>0,\qquad
   \rho_L>\rho_P,\quad\mathcal R_L>\mathcal R_P,\quad B_j^L>B_j^P.
   \]
3. **Nominal and real-income thresholds**：在端点跨越和单调条件下，
   \(G_R\leq G_Y\)；同一连续组织区间内严格为 \(G_R<G_Y\)。离散事件可使阈值
   重合。基准的充分高端条件分别为
   \[
   (\sigma-1)\psi>\Lambda(z),
   \]
   \[
   (\sigma-1)\psi+\alpha_Ms(z)>\Lambda(z).
   \]
4. **Government participation and threshold crossing**：
   \(G'(\vartheta)>0\)，且对 \(H\in\{E,L,R,Y\}\)：
   \[
   \vartheta_H=\inf\{\vartheta:G(\vartheta)\geq G_H\}.
   \]

## 11. 必须报告的边界和反例

1. \(\ell_A=\ell_P\)：consumer capture drag 消失；
2. \(\ell_P>\ell_A\)：capture drag 反号；
3. \(\rho_P=\rho_L\)：producer spatial-payment gap 消失；
4. \(\chi^{ext}>0\)：额外互补强化 producer response，但不是核心结论条件；
5. \(\lambda>0\)：平台服务部分本地化；
6. \(F\leq\bar F\)：平台依赖区间消失；
7. 离散进入或组织切换：可有 \(G_R=G_Y\) 或 \(G_R=G_E\)；
8. 原始阈值小于零：截断为零，比较静态弱化；
9. 外部渠道限制：可诱导本地化，但提高消费者价格并可能抬高平台进入门槛。

## 12. 第一版明确排除

- 完整 NEG、迁移、土地、住房和集聚反馈；
- 企业生产率分布和自由进入；
- 动态组织资本；
- 多平台战略定价和双边网络效应；
- 全国社会规划者、national welfare 和最优保护；
- 地方财政分成、税收归属和转移支付；
- 经验识别或真实数据 calibration。

## 13. 数值与验收合同

- 数值只证明参数区域非空，统一称 `illustrative numerical exercises`；
- 阈值算法必须精确评估 \(G_E,G_L\) 等离散事件，不能返回相邻网格点；
- 三张正文图同时输出 PDF、PNG 和 CSV；
- 基准设 \(\chi^{ext}=0\)，正互补只作为扩展；
- `validate_model.py` 必须通过解析恒等式、有限差分、边界和参数网格检查；
- 正文、附录、代码、CSV 和图形中的阈值必须完全一致；
- 核心问题始终是 platform access--local capture。
