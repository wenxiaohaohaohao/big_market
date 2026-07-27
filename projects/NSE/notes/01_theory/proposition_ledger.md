# Proposition Ledger v4.0

日期：2026-07-27
对应合约：`notes/01_theory/model_contract.md`

## 1. 正式结果

| ID | 结果 | 必要条件 | 结论 | 边界/反例 | 状态 |
|---|---|---|---|---|---|
| L0 | Consumer access | CES；\(\eta>1\)；\(p_P=\bar p_Pe^{-z}\) | \(s'=(\eta-1)s(1-s)>0\)，\(d\ln P_M/dz=-s<0\) | \(s\to0,1\) 时份额边际响应趋近零 | PROVED |
| P1 | LCA and actual entry | LCA 双重相对生产成本；\(\gamma>0\)；固定成本含正常回报 | \(G_E\) 存在；内部解处 \(\partial G_E/\partial c>0\)，\(\partial G_E/\partial\mathcal C^P_{ij}>0\) | 原始阈值小于零时截断为零；actual entry 对应本文的 LCA-to-ACA realization，不另设 \(G_A\) | PROVED |
| P2 | Organizational embeddedness | \(d_L<d_P\)，\(F>0\)，\(\Omega=(\sigma-1)\gamma>0\) | \(G_L\) 存在；内部解处 \(\partial G_L/\partial c>0\)；切换后 \(\rho_L>\rho_P\)、\(\mathcal R_L>\mathcal R_P\)、\(B_j^L>B_j^P\) | \(F\leq\bar F\) 时平台依赖区间消失 | PROVED |
| P3a | Nominal-income threshold | \(\psi>0\)；\(\ell_A>\ell_P\)；端点跨越；状态内严格单调、状态间无向下跳 | \(G_Y=\inf\{G:d\ln Y/dz\geq0\}\) 唯一 | 若高端满足 \((\sigma-1)\psi\leq\Lambda\)，名义阈值可以不存在 | PROVED |
| P3b | Real-income threshold ordering | \(\alpha_Ms(z)>0\)；P3a 的单调结构 | \(G_R\leq G_Y\)；同一连续组织区间内 \(G_R<G_Y\) | 离散进入/组织切换可使阈值重合；基准中 \(G_R=G_E\) | PROVED |
| C1 | Stronger LCA lowers income thresholds | 更低 \(c\) 提高各状态的 \(B_j\) 并提前状态切换 | \(G_R,G_Y\) 随 LCA 增强而弱下降；相同内部状态内严格下降 | 零截断和离散状态变化处仅弱关系 | PROVED |
| P4 | Government participation and threshold crossing | \(\mathcal U_I''<0\)，\(C''\geq0\)，\(\kappa_I'(\vartheta)<0\) | \(G'(\vartheta)>0\)；\(H\in\{E,L,R,Y\}\) 的 \(\vartheta_H\) 唯一（存在时） | 不证明 \(\vartheta\) 全国最优；不包含 external-channel restriction | PROVED |

## 2. 非正式但必须报告的结果

| ID | 内容 | 作用 | 状态 |
|---|---|---|---|
| B1 | \(D(z)\geq1-\alpha_M-\beta>0\) | 说明收入递归稳定性来自份额限制，不是额外假设 | VERIFIED |
| B2 | \(F>\bar F\iff G_P^0<G_L^0<G_X\) | 给出三区域存在的充要排序 | PROVED |
| B3 | \(\ell_A=\ell_P\Rightarrow\Lambda=0\) | 关闭 consumer-side capture gap | VERIFIED |
| B4 | \(\ell_P>\ell_A\Rightarrow\Lambda<0\) | 反向渠道支付归属 | VERIFIED |
| B5 | \(\lambda=1\Rightarrow\rho_P=\rho_L=1\) | 关闭 producer-side spatial-payment gap | VERIFIED |
| B6 | \(\chi^{ext}>0\) | 正 infrastructure--platform complementarity 扩展 | VERIFIED |
| B7 | 外部渠道限制提高 \(p_P,d_P\) | 可诱导 \(L\)，但提高消费价格并抬高 \(G_P^0\) | PROVED AS POLICY EXAMPLE |

## 3. 当前 illustrative baseline

\[
\alpha_M=0.35,\quad \beta=0.30,\quad \eta=6,\quad \sigma=4,
\]

\[
\ell_A=0.70,\quad\ell_P=0.10,\quad B_0=1,
\]

\[
\mathcal M_0=5,\quad\psi=0.19,\quad\gamma=0.10,
\]

\[
c=0.9,\quad d_P=0.4,\quad d_L=0.1,\quad f=0.34,\quad F=0.53.
\]

在 \(z=0.5\)：

\[
G_P^0=G_E=G_R=0.210619,
\]

\[
G_L^0=0.718802,\qquad
G_Y=0.555415,\qquad
G_X=G_L=1.090996.
\]

其中 \(G_R=G_E\) 是由进入时的离散跳跃决定的精确 infimum，不是网格近似。

State illustration：

\[
\kappa_p=4.0,\quad\kappa_g=0.30,\quad a_I=0.80,
\]

\[
\vartheta_E=\vartheta_R=0.2331,\quad
\vartheta_Y=0.8308,\quad
\vartheta_L=0.9863.
\]

## 4. 术语约束

- LCA 是相对生产成本所预示的潜在专业化；ACA 是交易成本加入后实际出现的
  生产和出口结构。ACA 与 realization 不再作为两个独立状态；
- viability 是 Lin (2003) 的企业属性。本文利润条件与其相容，但不另设 viability
  index 或 threshold；
- \(G\) 是共享非企业专用基础设施，\(f\) 是进入固定成本，\(F\) 是本地组织专用
  固定成本；
- \(\ell_r\) 与 \(\rho_r\) 是支付归属比率，不是能力参数；
- external-channel restriction 不是 NSE 中所有 protection 的一般定义；
- \(Y\) 和 \(R\) 不是 national welfare；
- numerical exercises 不是 calibration。

## 5. 验收

- [x] 解析公式与数值实现使用 \(\psi,\gamma,\chi^{ext}\) 的同一含义；
- [x] \(G_A\)、独立 ACA index、独立 realization 状态和 viability threshold 已从
  活动模型删除；
- [x] 离散收入阈值按结构事件精确返回；
- [x] P1--P4 均有证明；
- [x] 所有关键边界与反例已进入附录；
- [x] 支付流没有重复计入固定成本或外部支付。
