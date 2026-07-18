# Economics Letters 稿件修订路线图：有限能力阈值与一般 share-response

日期：2026-07-17  
项目：`platform_local_multiplier_el`  
目标期刊：*Economics Letters*  
状态：M1--M3 已实施并通过最终独立审查与交付核验。

## 1. 结论先行

本轮采用附件建议中的以下组合：

1. 将有限一体化冲击下的唯一能力阈值升级为主命题；
2. 将 CES 峰值结果升级为一般严格凹 share-response 下的单峰命题；
3. 将 integration 与 organizational capacity 的 log-income increasing differences 写成短 Corollary；
4. 将现有 multiplier Proposition 降为已知 benchmark；
5. 本轮不加入 platform-fee extension；
6. multi-channel covariance 仅保留为可选 Appendix Remark，不作为贡献中心。

这是一条“替换式升级”路线，不是在现稿上继续叠加命题。作者已确认把
主文需求块从 CES 改为一般 homothetic demand；固定题目与机制主线保持
不变。贡献表述以 M1--M3 的精确条件为边界，不使用 priority claim，也
不把 standard multiplier、CES channel choice 或 recursive leakage
包装成本文创新。

## 2. 已核实的起点

- 当前 `verify_model.py`：10,000 组随机均衡、5,000 组 CES 峰值参数和边界案例全部通过；
- 当前主文 `texcount -sum`：1,633；
- 当前主文加附录 `texcount -inc -sum`：2,362；
- 当前主文已经有任意 \(z_0\to z_1\) 的 finite ratios，但没有 finite shock 下关于 \(\kappa\) 的唯一双阈值；
- 当前主文已经证明 CES 下的闭式峰值，但没有一般 share-response 定理；
- 当前 \(\partial\Lambda/\partial\kappa<0\) 已隐含 integration--capacity increasing differences，因此该交叉偏导只能作为解释性 Corollary，不能包装成独立重大贡献。

## 3. 数学修改合同

### M1. 新 Proposition 1：有限冲击下的唯一能力阈值

保留 \(G=0\)，定义

\[
D_j(\kappa)=d_A+\alpha s_j\Delta(\kappa),\qquad
\mathcal D(\kappa)=\frac{D_1(\kappa)}{D_0(\kappa)}.
\]

证明

\[
\frac{\partial\ln\mathcal D(\kappa)}{\partial\kappa}
=-
\frac{\alpha\delta_\rho d_A(s_1-s_0)}
{D_1(\kappa)D_0(\kappa)}<0.
\]

在

\[
\mathcal D(0)>
\frac{\mathcal B}{\mathcal P^\alpha}>
\mathcal B>
\mathcal D(1)
\]

下，给出唯一且有序的

\[
0<\kappa_R^F<\kappa_Y^F<1,
\]

三个 finite-change sign regions，以及

\[
\kappa(q)=\frac{1}{\delta_\rho}
\left[
\Delta_0-
\frac{(q-1)d_A}{\alpha(s_1-qs_0)}
\right].
\]

必须写明的条件：

- \(G=0\)；
- \(s_1>s_0\) 且 \(0<\mathcal P<1\)；
- \(\kappa\) 不改变 \(s_j\)、\(B_j\) 或 \(P_{Mj}\)；
- \(D_j(\kappa)>0\)；
- \(q\) 位于 \(\mathcal D(1)\) 与 \(\mathcal D(0)\) 之间，且闭式解的分母为正；
- 两个 equality boundaries 单独陈述；
- 若允许高能力地区出现 \(\Delta(\kappa)\leq0\)，不能沿用旧 Proposition 的全程 \(\Delta>0\) 叙述，必须从比率恒等式重新证明。

该命题替换当前 fixed-\(\kappa\) finite-threshold Proposition 与局部 \(\kappa(q)\) threshold 段，不与它们并列。

### M2. 新 Proposition 2：一般 concave share-response 下的唯一峰值

主文需求块采用可微 homothetic two-channel unit expenditure function。令 \(s\) 为平台 expenditure share，\(z\) 为平台价格的负 log wedge；由 envelope/Shephard identity 得到

\[
\frac{d\ln P_M}{dz}=-s.
\]

对需求系统诱导的 share-speed 施加

\[
s'(z)=g(s),\quad
g\in C^2([0,1]),\quad
g(0)=g(1)=0,\quad
g(s)>0,\quad
g''(s)<0\quad\text{for }s\in(0,1).
\]

固定满足 \(\Delta(\kappa)>0\) 的能力水平，定义

\[
\Lambda_g(s,\kappa)=
\frac{\alpha\Delta(\kappa)g(s)}
{d_A+\alpha\Delta(\kappa)s}.
\]

以

\[
F(s)=g'(s)(d_A+bs)-bg(s),\qquad
F'(s)=g''(s)(d_A+bs)<0
\]

证明：

1. \(\Lambda_g\) 有唯一内部峰值；
2. 若 \(g(s)=g(1-s)\)，则 \(s^*(\kappa)<1/2\)；
3. \(\partial s^*/\partial\kappa>0\)；
4. \(\partial\Lambda_g^{\max}/\partial\kappa<0\)。

措辞限制：

- 写作 `strictly single-peaked`，不能一般性声称 \(\Lambda_g\) strictly concave；
- 只能声称适用于“诱导严格凹 share-speed 的两渠道 homothetic demand systems”，不能声称适用于任意需求系统；
- \(\kappa\) 只改变 retention，不能同时改变 \(g\)；
- \(\Delta=0\) 时拖累恒为零，没有唯一峰值；
- 非对称 \(g\) 只保证唯一内部峰值，不保证峰值低于 \(1/2\)。

CES

\[
g(s)=(\eta-1)s(1-s)
\]

降为 specialization；现有 \(s^\dagger\) 和 \(\Lambda_{\max}\) 闭式解移至 Appendix，不再承担一般命题地位。

### M3. 短 Corollary：integration--capacity increasing differences

在 \(G=0\) 下增加

\[
\frac{\partial^2\ln Y}{\partial z\partial\kappa}
=
\frac{\partial^2\ln R}{\partial z\partial\kappa}
=
\frac{\alpha\delta_\rho d_A s'(z)}{D^2}>0.
\]

只解释为 nominal local income 与 consumption-equivalent real income 的
log increasing differences。不得写“最优 \(\kappa^*(z)\) 随 \(z\) 上升”，
因为当前模型没有 capacity choice、capacity cost 或优化问题。

### M4. 本轮不进入主文的建议

| 建议 | 处理 | 原因 |
|---|---|---|
| Platform fee 与 trade cost 非等价 | 暂缓 | 需要额外 fee incidence、pass-through 与 retention 假设；结果高度由设定驱动，并会引出平台定价问题 |
| Multi-channel covariance | 可选 Appendix Remark | 是有用恒等式，但不是主定理；若 \(\rho_c\) 随 \(z\) 变化，还必须加入 \(\sum_cs_c\rho_{c,z}\) |
| 最优能力选择 | 不加入 | 当前没有能力投资成本和选择问题 |

## 4. 贡献定位检查

### N1：exact-result audit

针对以下精确对象刷新 equation-level prior-art 对照：

- finite integration shock 下唯一且有序的 capacity thresholds；
- strict-concave share-speed 下的 unique capture-drag peak；
- symmetric share-speed 下的 pre-half peak；
- capacity 对 peak location 与 height 的比较静态。

### N2：可声称内容

Introduction 可以把 M1--M3 称为本文的 analytical results，但不得使用
“first”“novel”或“to our knowledge”等优先权表述，也不得声称本文发明
recursive leakage、CES channel choice 或 standard multiplier inverse。

### N3：本轮定位结论

方案 A 与 M1--M3 已获作者确认。贡献检查用于约束措辞和核对精确结果，
不是重新设置路线否决权；本轮不转向 seller entry、platform payout、
fee extension 或新的内生 margin。

## 5. 主文替换方案

| 当前位置 | 操作 | 新内容 |
|---|---|---|
| Abstract | 最后重写 | 只陈述 finite capacity thresholds、general single peak 和 increasing differences |
| Introduction | 压缩并重写贡献段 | 明确承认 multiplier 是 benchmark；避免把 standard leakage 当贡献 |
| CES demand lemma | 一般化 | 主文使用 homothetic demand 与 share-speed；CES 细节移 Appendix |
| Proposition 1：multipliers | 降级并压缩 | Model 末尾保留 \(m_B=1/D\)、\(\mathcal M_G=\omega/D\) 和一句递归解释 |
| Proposition 2：finite thresholds | 合并替换 | 新 Proposition 1：finite integration + unique ordered capacity thresholds |
| Corollary 1：local capacity thresholds | 删除局部三分区 | 改为一行 integration--capacity increasing differences |
| Corollary 2：CES peak | 一般化并升格 | 新 Proposition 2：general concave share-response single peak；CES 为 Appendix specialization |
| Figure 1 | 两个 panel 均更新 | Panel A 展示非 CES-specific peak；Panel B 展示 finite ratios 与两个 \(\kappa^F\) crossings |
| Conclusion | 最后重写 | 只总结通过数学与 novelty gate 的结果，并保留 reduced-form scope |

## 6. 字数预算

按 `texcount -sum` 设置内部硬目标 1,775、预留 225、绝对上限 2,000：

| 部分 | 目标计数 |
|---|---:|
| Abstract、keywords、JEL | 135 |
| Introduction | 330 |
| Model 与 benchmark | 500 |
| Results 与 Figure caption | 680 |
| Conclusion | 115 |
| Data statement | 15 |
| 合计 | 1,775 |

若超限，删除顺序固定为：

1. multi-channel Remark；
2. 主文中的 CES 闭式峰值，只在 supplement 保留；
3. multiplier 上界、弹性和级数解释；
4. 非必要边界讨论；
5. Figure caption 的重复解释。

不得通过把正文段落机械移进同一 PDF 的 Appendix 来规避 2,000-word 约束。`appendix.tex` 应作为单独 supplementary manuscript 编译和提交。

## 7. Appendix/Supplement 重构

建议顺序：

1. General homothetic demand 与 envelope identity；
2. fixed-point existence、uniqueness 与 benchmark multiplier；
3. finite-capacity threshold proof；
4. increasing-differences proof；
5. general single-peak proof；
6. CES specialization 与闭式 \(s^\dagger\)、\(\Lambda_{\max}\)；
7. boundary cases：\(\Delta\to0\)、\(\Delta<0\)、asymmetric \(g\)、endpoint crossing failure；
8. 可选 multi-channel covariance Remark；
9. \(G>0\) 只作为独立 extension，不能套用 M1 的 finite-\(\kappa\) 公式。

## 8. 图形修改

### Panel A：general share-response peak

- 至少展示 CES/logistic 与 sine share-speed；
- 所有曲线满足端点为零、内部为正、严格凹；
- 标出各自唯一峰值与 \(s=1/2\)；
- 非对称函数只作为 Appendix negative control，不与对称函数混在主图中。

### Panel B：finite capacity thresholds

- 纵轴：\(\ln(Y_1/Y_0)\) 与 \(\ln(R_1/R_0)\)；
- 横轴：\(\kappa\)；
- 标出零线、\(\kappa_R^F\) 与 \(\kappa_Y^F\)；
- 三个区域与 Proposition 1 完全对应；
- caption 继续明确 `illustration, not calibration`。

图形 source-data CSV 应同步输出 general \(g\) curves/peaks 和 finite ratios/thresholds，不能只更新 PDF。

## 9. 计算核验合同

在保留现有回归测试的基础上，扩展 `code/verify_model.py`：

1. 新增 `finite_capacity_objects`；
2. 用中心差分核对 \(\partial_\kappa\ln\mathcal D\)；
3. 将闭式 \(\kappa(q)\) 与直接残差和 bisection root 对照；
4. 验证阈值排序、三个 sign regions 和两个 equality boundaries；
5. 对不满足 endpoint crossing 的参数返回明确分类，不强行生成双阈值；
6. 对 symmetric 与 asymmetric 严格凹 \(g\) 分别验证 \(F\) 单调、唯一根和全局峰值；
7. 只对 symmetric \(g\) 检验 \(s^*<1/2\)；
8. 用有限差分核对 \(\partial s^*/\partial\kappa>0\)、\(\partial\Lambda_g^{\max}/\partial\kappa<0\)；
9. 用二维有限差分核对 log-income cross-partial；
10. 保留 CES nesting test：一般 root 必须恢复现有闭式峰值；
11. 保留 fixed point、\(G>0\) 和现有 boundary regression tests。

`code/make_mechanism_figure.py` 必须从已核验函数读取阈值和峰值，不在绘图代码中复制一套独立公式。

## 10. 执行顺序与验收标准

### Phase 0：冻结基线

- 记录 `main.tex`、`appendix.tex`、`verify_model.py` 和 figure script 的哈希；
- 保留当前通过的验证输出；
- 不覆盖历史 notes、raw materials 或旧 PDF。

验收：能够精确恢复本轮修改前状态。

### Phase 1：theorem-feasibility note

- 先在新的内部 note 写完 M1--M3 的正式假设、命题和证明；
- 两名独立数学审查者分别检查 endpoint、symmetry、\(\Delta\) 和 \(G\) 条件；
- 不触碰正式稿。

验收：无缺失条件，所有 equality/boundary cases 已分类。

### Phase 2：贡献定位检查

- multiplier 明确降为 benchmark；
- M1--M3 按各自条件陈述；
- 不使用 priority claim，不重新改变方案 A。

验收：贡献措辞与数学条件一一对应。

### Phase 3：代码优先

- 先扩展验证脚本；
- 所有新解析式通过随机、有限差分、闭式残差和边界检查；
- 再更新 Figure source-data 和 PDF。

验收：旧测试无回归；新测试全部通过；固定 seed；图形数据可复现。

### Phase 4：Appendix/Supplement

- 按第 7 节重构证明；
- CES 明确标为 general theorem 的 specialization；
- supplement 独立编译。

验收：主文每个命题均有完整证明；supplement 无未解析引用。

### Phase 5：Main text

- 严格按第 5 节做替换；
- 最后才改 Abstract、Introduction、Conclusion；
- 不增加 fee extension 或经验 calibration。

验收：`texcount -sum <= 1,950`；主文只有两个主 Proposition 和一个短 Corollary；所有范围条件在首次出现处写明。

### Phase 6：编译与审稿

- 使用项目已有 MiKTeX build script，临时目录和日志尽量指向项目内 `output/tmp`；
- 检查 undefined citation/reference、overfull box 和 fatal error；
- 逐页检查主文、supplement 和 Figure；
- 完成 fresh methodology、domain、EIC 和 Devil's Advocate review。

验收：数学 reviewer 无 result-level error；domain reviewer 接受 novelty positioning；EIC 判定符合 EL 篇幅与 salience；DA 无 CRITICAL overclaim。

### Phase 7：项目文件同步

- 更新 README 中“方案 A 唯一采用 CES”的旧决定；
- 更新中文项目备忘录、数据/代码声明和构建说明；
- 只有全部验收后才生成投稿 PDF。

验收：README、main、supplement、code、figure 和 PDF 使用同一组定义与结果。

## 11. 停止条件

任一条件成立即暂停正式改稿：

1. M1 的双阈值需要未披露的额外端点假设才能成立；
2. M2 不能从明确的 homothetic demand/share definition 得到，而只能作为任意外生 \(g\)；
3. 主文在删除可选内容后仍超过 1,950；
4. Figure 只能依靠不满足命题条件的曲线产生；
5. 新测试破坏现有 fixed-point 或边界结果；
6. 一般化需求块迫使模型扩展到 platform pricing、multi-region GE 或 endogenous capacity investment，超过 Letter 范围。

## 12. 预计工作量

| 工作包 | 预计时间 |
|---|---:|
| 数学 note、独立证明审计 | 1--2 天 |
| exact-result novelty refresh | 1--2 天 |
| 验证代码与 Figure | 1--2 天 |
| Appendix/Supplement 重构 | 1 天 |
| 主文替换与压缩 | 1--2 天 |
| 编译、逐页检查与 fresh review | 1--2 天 |
| 合计 | 6--11 个工作日 |

以上时间不包括等待合作者确认或发现 exact prior art 后的路线重选。

## 13. 实施与验收记录

完成日期：2026-07-17。

- 主文已改为一般 homothetic 两渠道需求，结构为两个 Proposition 加一个
  Corollary；standard multiplier 只保留为 benchmark。
- M1 给出 finite-change 的唯一有序能力阈值、三个严格符号区域和两个
  equality boundaries；M2 给出一般严格凹 share-speed 的唯一内部峰值、
  对称情形的 pre-half 结论及两项 capacity 比较静态；M3 只陈述
  \(G=0\) 下两种 log-income 的 increasing differences。
- Supplement 已单独生成，包含全部证明、一般 share-speed 的合法
  unit-expenditure 构造、CES 闭式特例和边界分类。
- `verify_model.py` 通过 10,000 组 deterministic random equilibria 和
  5,000 组 general share-speed draws；闭式根、bisection root、有限差分、
  CES nesting、等号和 non-crossing 分类均通过。
- 图 1 为 \(183\text{ mm}\times84\text{ mm}\) 双 panel vector figure；
  PDF、SVG、600 dpi PNG 与两份各 501 行的 source-data CSV 同步生成。
- 摘要为 100 词；主文约 1,190 词，低于 1,950 的内部上限。最终主文
  5 页，Supplement 4 页。
- MiKTeX 构建通过；项目日志无 LaTeX warning、未解析 citation/reference、
  overfull/underfull box 或 fatal error。九页 PDF 已逐页检查。
- 独立数学、结构与贡献表述审查均完成；发现的边界条件、术语、图形顺序
  和 overclaim 问题均已修正。
