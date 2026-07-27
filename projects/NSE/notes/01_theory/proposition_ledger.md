# Proposition Ledger v3.1

日期：2026-07-27
对应合约：`notes/01_theory/model_contract.md`

## 1. 正式结果状态

| ID | 正式结果 | 关键条件 | 解析结论 | 边界或反例 | 状态 |
|---|---|---|---|---|---|
| L0 | 平台化提高平台支出份额并降低消费价格指数 | CES；\(\eta>1\)；\(p_P=\bar p_Pe^{-z}\) | \(s'=(\eta-1)s(1-s)>0\)；\(d\ln P_M/dz=-s<0\) | \(s\to0,1\) 时边际份额响应趋近零 | PROVED |
| P1 | 更强 LCA 分别降低 ACA 与 viable-entry 所需基础设施 | 双重相对成本；\(\gamma+\chi z>0\)；\(\Omega(z)>0\) | \(\partial G_A/\partial \mathcal C^P_{ij}>0\)、\(\partial G_E/\partial \mathcal C^P_{ij}>0\)（内部解） | \(G_A\neq G_E\) 一般成立；阈值截断于零时只有弱单调 | PROVED |
| P2 | 本地嵌入组织存在阈值并改变支付归属 | \(d_L<d_P\)；\(F>0\)；\(\Omega(z)>0\) | \(G_L=\max\{0,G_X\}\) if \(F>\bar F\)，否则 \(G_L=\max\{0,G_L^0\}\)；\(\partial G_L/\partial c>0\) | \(F\leq\bar F\) 时平台依赖区间消失，不能继续用 \(G_X\) 定义均衡阈值 | PROVED |
| P3a | 名义地方收入存在唯一最小阈值 | \(D>0\)；端点跨越；固定区间严格单调；状态切换向上跳 | \(G_Y=\inf\{G:d\ln Y/dz\geq0\}\) 唯一 | 若零点位于状态切换，阈值是离散边界 | PROVED |
| P3b | 实际收入阈值弱低于名义收入阈值 | \(\alpha_Ms(z)>0\) | \(G_R\leq G_Y\)；同一连续区间内 \(G_R<G_Y\) | 同一离散切换可使 \(G_R=G_Y\) | PROVED |
| C1 | 更强 LCA 降低收入阈值 | 更低 \(c\) 提高每个给定 \(G\) 的 \(B_j\) 和 \(\theta_r\) | \(G_R,G_Y\) 对 LCA strength 弱下降；同一内部区间严格下降 | 离散状态切换或零截断处可为弱关系 | PROVED |
| P4 | 政府参与提高基础设施，并与保护不等价 | \(\mathcal U_I''<0\)；\(C''\geq0\)；\(\kappa_I'<0\) | \(G'(\vartheta)>0\)；结构门槛映射为 \(\vartheta_H\) | 不声称 \(\vartheta\) 为全国福利最优；无门槛跨越时 \(\vartheta_H\) 不存在 | PROVED |
| C2 | EL 递归传播放大第一轮收入但不重复支付 | \(D=1-\beta-\alpha_M\omega_C>0\) | \(Y=(B_0+B_j)/D\)；\(R=Y/P_M^{\alpha_M}\) | \(D\leq0\) 时固定点不稳定，排除 | VERIFIED |

## 2. 证明索引

| 结果 | 证明位置 | 代码核验 |
|---|---|---|
| L0 | `paper/appendix.tex`, Consumer block | CES 解析恒等式与有限差分 |
| P1 | `paper/appendix.tex`, Proof of Proposition 1 | 成本网格；raw/clipped threshold 检查 |
| P2 | `paper/appendix.tex`, Proof of Proposition 2 | \(F>\bar F\) 与 \(F\leq\bar F\) 两个区域 |
| P3 | `paper/appendix.tex`, Proof of Proposition 3 | 全局 \(G\) 网格、状态跳跃和二分根 |
| P4 | `paper/appendix.tex`, Proof of Proposition 4 | FOC 有限差分和闭式示例 |
| 全部 | `code/theory/validate_model.py` | 解析、有限差分、边界与反例 |

## 3. 参数区域核验

基准 illustrative 参数在 \(z=0.5,c=0.9\) 时产生：

\[
G_P^0=0.330038,\qquad
G_L^0=0.652932,\qquad
G_X=0.881716,
\]

\[
G_A=0.611694,\qquad
G_R=0.330500,\qquad
G_Y=0.835116.
\]

因此：

- 候选产业在 \(G<G_E\) 时不进入，在 \(G_E\leq G<G_L\) 时依赖外部平台；
- \(G_E<G_A\) 说明 viability 与 ACA 是不同条件，盈利进入不自动证明相对总成本优势；
- \(G<G_L\) 时维持外部平台依赖；
- \(G\geq G_L\) 时形成本地嵌入；
- 实际收入先于名义地方收入对平台化转正；
- 严格排序不是由同一连续区间假定得到，而是数值例中的均衡结果；正式命题仍只在
  充分条件下声称严格排序。

政府参与的闭式示例产生：

\[
G(0.05)=0.3172,\qquad
G(0.50)=0.4724,\qquad
G(0.95)=1.0258.
\]

五个政府参与门槛全部为内部值：

\[
\vartheta_E=0.1044,\quad
\vartheta_R=0.1063,\quad
\vartheta_A=0.6991,\quad
\vartheta_Y=0.8694,\quad
\vartheta_L=0.8928.
\]

三种参与度分别对应低、中、高基础设施路径，支持改革路径图。

## 4. 机制关闭

| 情景 | 被关闭或减弱的机制 | 理论预期 |
|---|---|---|
| \(\ell_A=\ell_P\) | consumer-side capture loss | \(\Lambda(z)=0\) |
| \(\ell_P>\ell_A\) | consumer-side capture loss 反向 | \(\Lambda(z)<0\)，渠道替代提高本地留存 |
| \(\rho_P=\rho_L\) | producer-side 空间支付差 | 组织选择只影响成本和销售，不影响留值率 |
| \(\chi=0\) | 基础设施与平台 producer access 互补 | 收入效应失去 \((\sigma-1)\chi G\) 项 |
| \(\lambda>0\) | 外部平台服务完全外地化 | \(\rho_P\) 上升，组织切换的 capture gain 缩小 |
| \(F\leq\bar F\) | 独立的平台依赖区间 | 企业可由不进入直接转入 \(L\) |
| protection | 外部渠道效率 | 本地化可能增加，但消费者接入和边际进入恶化 |

## 5. 完成定义

本台账中的 `PROVED` 表示同时完成：

1. 正式命题陈述；
2. 明确参数条件；
3. 解析证明；
4. 边界和反例；
5. 代码有限差分或参数网格核验。

正文写作不得把附录中的条件性结论改写为无条件一般命题。
