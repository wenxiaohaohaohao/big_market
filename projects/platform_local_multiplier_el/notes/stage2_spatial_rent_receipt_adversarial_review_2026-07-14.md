# Stage 2：spatial rent receipt × seller entry 独立对抗式审查

日期：2026-07-14  
审查对象：

- `notes/stage2_spatial_rent_receipt_entry_feasibility_2026-07-14.md`
- `code/verify_seller_entry_candidates.py`

审查边界：只评估收入守恒、解析正确性、机制必要性、制度 microfoundation、直接 prior art 风险与 Economics Letters 篇幅；未修改正式主稿、附录、文献库、正式验证脚本或 PDF。

## 1. 总体判定

```text
algebra = PASS_WITH_MINOR_CORRECTIONS
income_conservation = PASS_CONDITIONAL_ON_LOCAL_INPUT_INCIDENCE
existence_uniqueness = PASS
branch_legality_continuity_kink = PASS
no_respending_test = PASS_WITHIN_MODEL_NOT_UNIVERSAL
lambda_microfoundation = MAJOR_REVISION_REQUIRED
direct_platform_novelty = CONDITIONAL_NOT_CERTIFIED
EL_2000_word_feasibility = PASS_ONLY_IF_MODEL_REPLACES_CURRENT_PAPER
discrete_hysteresis_under_CES_business_stealing = FAIL
overall_verdict = CONDITIONAL_GO
formal_manuscript_rewrite = REMAINS_PAUSED
```

**结论：CONDITIONAL GO。** 新候选的收入方程、free-entry active set、唯一阈值、连续性和 kink 都是正确的。它也通过了一个比原 continuous phase-reversal 更强的 necessity test：在模型明确规定的 no-respending counterfactual 中，\(\lambda\) 不进入 seller payoff，故 seller mass 对 \(\lambda\) 完全不变。

阻断正式写作的主要问题不是数学，而是 \(\lambda\) 的经济身份。目前它同时被称为 rent receipt、terminal-manager reward、affiliate payout 和 local ownership。前两者是服务合同，后两者分别是转介合同和资产所有权；它们对成本、努力、消费者使用和付款基数的含义不同。如果不固定一种制度 microfoundation，\(\lambda\) 会被审稿人理解为任意从总部向本地的转移。任何本地转移都可能通过需求触发一个 free-entry threshold，届时“平台特有机制”会退化为 generic transfer-to-entry result。

因此，只有完成第 9 节的五项必须修正，才可把路线从 feasibility memo 升级为正式 EL 模型。

## 2. 每元交易收入守恒与 \(F/\mu\) 审查

### 2.1 完整 ledger

令

\[
\phi=\alpha s,
\qquad
c_0=\beta+\alpha\rho_A(1-s),
\qquad
\theta=\frac{n}{n+\chi},
\qquad
Q=E+\phi Y.
\]

本地诱发收入为

\[
I_L
=c_0Y+\lambda\tau\phi Y
+(1-\tau)\theta Q.
\tag{R1}
\]

要验证守恒，外部/总部收入必须明确写为

\[
\begin{aligned}
I_H={}&(1-\alpha-\beta)Y
+\alpha(1-s)(1-\rho_A)Y\\
&+(1-\lambda)\tau\phi Y
+(1-\tau)(1-\theta)\phi Y\\
&+\tau E+(1-\tau)(1-\theta)E.
\end{aligned}
\tag{R2}
\]

逐项相加得到

\[
I_L+I_H=Y+E.
\tag{R3}
\]

因此，居民支出 \(Y\) 与外部订单 \(E\) 都有且仅有一个接收地。feasibility memo 的文字核算方向正确，但正式模型必须加入类似式（R1）--（R3）的外部账户；只验证 local-income fixed point 不能单独证明全系统守恒。

### 2.2 \(F\) 与 \(\mu\) 没有重复计入，但需要改写解释

正进入时，free entry 给出

\[
F=\mu(1-\tau)\frac{Q}{n+\chi}.
\]

乘以 \(n\) 后，

\[
nF
=\mu(1-\tau)\theta Q.
\tag{R4}
\]

本地 seller 的全部 net-of-fee payout 为

\[
(1-\tau)\theta Q.
\]

其中 \(nF\) 是本地固定投入的要素收入，剩余

\[
(1-\mu)(1-\tau)\theta Q
\]

是本地 variable-input income。free-entry owner profit 为零。二者相加正好等于全部 seller payout，因此 income equation 中不能再单独加 \(nF\)，当前 memo 也没有这样做。

这个核算只有在以下 incidence assumption 下成立：固定投入和 variable inputs 都由本地要素提供并由本地收入接受者收取。若库存采购、广告、软件或履约投入来自外地，必须再乘 local-input shares。当前“本地 owner income”一词也不准确：在 free-entry equilibrium 中 owner 的 residual profit 为零；本地留值来自固定和可变投入收入。

**判定：不存在代数重复计入；存在需要写清楚的投入地假设。**

## 3. Contraction、分支、\(\lambda^*\)、连续性与 kink

### 3.1 Contraction 与唯一性

收入映射为

\[
T(Y)=B+[c_0+\lambda\tau\phi]Y
+(1-\tau)[E+\phi Y-Q_E]_+.
\]

两个线性分支的斜率分别为

\[
a_0=c_0+\lambda\tau\phi,
\]

\[
a_1=c_0+\phi(1-\tau+\lambda\tau).
\]

由于 \(\rho_A\leq1\)、\(1-\tau+\lambda\tau\leq1\) 且 \(\alpha+\beta<1\)，

\[
0\leq a_0\leq a_1\leq\alpha+\beta<1.
\]

所以 \(T\) 是全局 contraction，存在唯一正收入 fixed point。给定收入后，free entry 唯一决定 \(n\)。这一部分正确。

“全局稳定性”应限定为收入轮次 \(Y_{t+1}=T(Y_t)\) 的稳定性；seller mass 在当前模型中是静态 complementarity condition 的代数解，并没有单独设定 entry dynamics。

### 3.2 分支合法性

无进入候选

\[
Y_0=\frac{B}{D_0},
\qquad
Q_0=E+\frac{\phi B}{D_0}
\]

在 \(Q_0\leq Q_E\) 时合法。正进入候选

\[
Y_1=
\frac{B+(1-\tau)(E-Q_E)}{D_1}
\]

满足

\[
Q_1-Q_E
=\frac{D_0}{D_1}(Q_0-Q_E).
\tag{R5}
\]

因为 \(D_0/D_1>0\)，两个分支合法区间严格互补，不存在 branch overlap 或 gap。正进入候选的 numerator 也确实为正，但 memo 应补一个显式证明：若 \(Q_E\leq E\)，numerator 显然大于 \(B\)；若 \(Q_E>E\)，合法性 \(Q_1>Q_E>E\) 与 \(Q_1=E+\phi Y_1\) 直接推出 \(Y_1>0\)。

在 \(Q_0=Q_E\) 时，两个公式给出相同的 \(Y\) 和 \(n=0\)。这不是多重均衡，只是同一 boundary equilibrium 的两种分支表示。

### 3.3 \(\lambda^*\)

在

\[
Q_0(0)<Q_E<Q_0(1)
\]

下，\(Q_E>E\) 自动成立，因为 \(Q_0(0)>E\)。\(Q_0\) 对 \(\lambda\) 严格递增，因此唯一内部阈值存在。正确闭式为

\[
\lambda^*
=\frac{
\bar d-\phi B/(Q_E-E)
}{\tau\phi}.
\tag{R6}
\]

原 memo 第 345 行写成了 `\bar d-phi B/(Q_E-E)`，缺少 \(\phi\) 的反斜线。这是确定的排版错误，必须修正。

### 3.4 连续性、kink 与 \(dn/d\lambda\)

在阈值处，

\[
Y_0(\lambda^*)=Y_1(\lambda^*)
=\frac{Q_E-E}{\phi}.
\]

因为

\[
D_1=D_0-(1-\tau)\phi<D_0,
\]

右侧收入导数严格大于左侧收入导数。正进入分支上

\[
n=\frac{\mu(1-\tau)}F(Q-Q_E),
\]

所以

\[
\left.\frac{dn}{d\lambda}\right|_+
=
\frac{\mu(1-\tau)\tau\phi^2Y^*}
{FD_1(\lambda^*)}>0,
\]

而左导数为零。收入与 seller mass 都连续，但一阶导数出现 kink；不能称为 discontinuity、tipping 或 hysteresis。memo 在这一点上的措辞正确。

**数学判定：PASS，需修正一个公式排版并补两个证明句。**

## 4. “关闭 respending 后 \(dn/d\lambda=0\)”的证明强度

固定居民平台订单为 \(\bar X_P\) 后，

\[
\widehat Q=E+\bar X_P
\]

不再随本地收入或 \(\lambda\) 变化。free entry 直接给出

\[
\widehat n
=\left[
\frac{\mu(1-\tau)\widehat Q}{F}-\chi
\right]_+,
\tag{R7}
\]

其中没有 \(\lambda\)。因此 \(\widehat n\) 对所有 \(\lambda\) 都相同，不只是局部导数为零。式（31）在当前模型中成立。

它证明的是一个有条件的机制必要性：**当 \(\lambda\) 只改变 commission receipt location，并且不改变价格、\(s\)、\(E\)、\(F\)、\(\mu\)、\(\chi\)、融资约束或服务质量时，local respending 是 \(\lambda\) 影响 seller entry 的唯一通道。**

它不能证明 local multiplier 在所有制度环境中都是必要的。如果 local payout 同时：

- 补贴 seller onboarding cost；
- 缓解本地 seller 的融资约束；
- 支付 terminal manager 的获客努力并改变 \(s\)；
- 改善 routing、信任或履约并改变 \(\chi\)；
- 直接由本地 sellers 或其所有者收取；

则即使固定居民再支出，\(n\) 也可能直接随 \(\lambda\) 变化。

**判定：necessity test 在模型内严格成立，但正文必须把它称为 exclusion-restriction result，而不是普遍定理。**

## 5. \(\lambda\) 的制度 microfoundation

### 5.1 目前的问题

当前 memo 对 \(\lambda\) 使用了四种不同解释：

1. 平台 rent 的本地所有权；
2. local terminal manager 的 transaction reward；
3. affiliate commission；
4. 地方合作商或本地收入接受者的 payout。

这四者不能在同一模型中无差别互换。terminal manager reward 是对交易协助、现金收付、信任和最后一公里服务的补偿；affiliate payout 通常依赖 referral attribution；equity ownership 是对剩余利润的资产索取权；任意 local recipient 则接近地区间转移。

更根本的问题是：在当前方程中，只要向本地家庭转移 \(\lambda\tau\phi Y\)，无论这笔钱是否来自平台 fee，都会通过 \(\phi\) 提高需求并触发同一个 active-set kink。因此，平台特异性来自制度映射，而不是代数本身。

### 5.2 可核实的制度事实

Couture et al. 的 AEA Online Appendix 明确记载：农村电商项目在村内设置 terminal，terminal manager 协助家庭买卖，并对通过 terminal 完成的每笔交易获得约 3--5% reward。这为 transaction-contingent local payout 提供了直接事实基础：

https://www.aeaweb.org/articles/materials/14082

但这个事实并没有自动证明 reward 是从固定的总 platform take rate \(\tau\) 中切分，也没有证明改变 reward 不会改变 manager effort、平台采用或服务质量。

### 5.3 三种可选 microfoundation

| 方案 | 内容 | 优点 | 缺点 |
|---|---|---|---|
| A. Local transaction-service payout | 总 take rate \(\tau\) 固定，其中 \(r=\lambda\tau\) 按本地 terminal-mediated transactions 支付给既有 local service node | 与 Couture 制度事实最接近；付款基数与模型一致 | 必须假定服务数量和质量已固定，否则 \(r\) 会改变 \(s\)、\(F\) 或 \(\chi\) |
| B. Local franchise/beneficial ownership | 本地 affiliate 对当地交易费拥有合同性现金流索取权 | 可把 receipt location 与 effort 分开 | 需要证明该类按交易地分配的所有权安排实际存在；一般平台股权分红不按当地交易计算 |
| C. Policy rebate/tax sharing | 平台总部将当地交易费的一部分按规则返还当地 | 外生政策 counterfactual 清楚 | 最容易退化成 generic transfer；平台经济创新最弱 |

**推荐方案 A。** 把参数直接改称 local transaction-service payout rate，并令 \(r\in[0,\tau]\)，总部保留 \(\tau-r\)。正文只讨论既有 terminal/service-node contract 下的 payout incidence；不要同时使用 rent ownership、affiliate 和 tax rebate 四套叙述。

如果无法可信地维持“\(r\) 变化而服务质量、价格、\(s\)、\(F\)、\(\mu\)、\(\chi\) 不变”，则该 partial-equilibrium counterfactual 缺少制度基础，应判 NO-GO 或转入大论文内生化 local service provision。

## 6. 与直接 prior art 的关系

### 6.1 不构成阻断的数学祖先

给定 active set 后的收入 inverse 属于 SAM/Miyazawa/local-multiplier algebra。positive-part kink 和 free-entry complementarity 也都是标准工具。这些必须作为 benchmark 承认，但不能仅因工具已知就否定新的平台制度映射。

### 6.2 直接相邻文献

- Fan et al. 已把 online/offline channel、空间贸易和市场进入放入多地区 GE；
- Li 的当前 working paper 已使 online-retailer entry threshold 依赖各地区总支出，并将地区收入放入 market clearing，是最接近的直接结构先例；
- Teh 等 platform-governance/fee-entry 文献研究 fee instrument 与 seller competition/entry；
- Couture et al. 直接记录 local terminal manager 及 transaction-contingent reward；
- local/absentee ownership 文献已经说明收入收取地会改变地方 multiplier。

本候选没有发明其中任何一个单独模块。

### 6.3 尚可能保留的联合命题

当前定向检索没有发现下列完整联合预测的直接同式先例：

> 在总 fee、消费者价格、平台份额、外部订单、seller margin 和 routing technology 不变时，只改变当地交易费的合同收取地，可以通过 local respending 改变 local seller free-entry active set；关闭 respending 后，该 entry effect 精确为零。

这比“收入增加促进 entry”更窄，也更可证伪。它构成 `conditional novelty`，但尚不足以认证 priority。特别需要对 Li 最新版本、platform affiliate/revenue-sharing、local franchise payout 与 seller entry 文献做 backward/forward citation audit。

### 6.4 创新风险

即使没有完全同式先例，审稿人仍可能认为结果只是：

\[
\text{local transfer}
\rightarrow
\text{demand increase}
\rightarrow
\text{free-entry threshold}.
\]

因此，投稿价值取决于两点：

1. local payout 必须是平台交易组织中的真实合同对象，而不是任意 transfer；
2. 论文必须突出 receipt location 与 fee rate 的分离，以及 no-respending falsification，而不是把 kink 本身包装成复杂理论。

**Prior-art 判定：CONDITIONAL PASS，尚不能写 “first” 或 “novel mechanism” 的无条件表述。**

## 7. `verify_seller_entry_candidates.py` 审查

### 7.1 已通过的检查

脚本使用标准库、固定种子 `20260714`，本轮重新运行成功。rent-receipt 模块报告：

```text
draws = 50,000
active draws = 13,134
interior lambda thresholds = 705
max income-equation residual = 1.42e-14
max derivative error = 2.47e-8
max threshold-continuity error = 1.07e-14
```

脚本正确检查了：

- \(D_0,D_1>0\)；
- income fixed point；
- active/inactive free-entry profit conditions；
- \(dY/d\lambda\)；
- \(\lambda^*\) 两侧收入连续；
- income kink 的方向；
- 正进入后的 \(dn/d\lambda>0\) 解析式；
- endogenous entry 相对于 fixed seller mass 的额外放大。

独立的 100,000 组随机核验还得到：

```text
max full-ledger conservation residual = 5.68e-14
max free-entry profit residual = 8.88e-16
max nF - mu*(seller payout) residual = 2.84e-14
max branch-identity residual = 4.55e-13
max lambda-threshold continuity residual = 4.26e-14
max no-respending change in n = 0
```

### 7.2 脚本仍缺少的硬检查

当前脚本的 `income_rhs` 只检查本地收入方程，不检查式（R2）的外部接收账户。它也没有程序化检查：

1. \(I_L+I_H=Y+E\) 的完整守恒；
2. \(nF=\mu(1-\tau)\theta Q\) 的 fixed-cost decomposition；
3. 式（R5）的 branch identity；
4. \(Q_0(0)<Q_E<Q_0(1)\) 与 \(0<\lambda^*<1\) 的双向等价；
5. \(dn/d\lambda\) 的有限差分，而不只是断言解析式为正；
6. no-respending 下在不同 \(\lambda\) 取值上 \(n\) 完全相同。

这些不影响本轮代数判定，但在候选升级为正式模型前应补入验证脚本。

## 8. 离散候选在 CES business stealing 下的判定

离散候选一般化为 per-seller order density \(h(n)\) 后，给定 \(n\) 的收入和每个 seller payoff 为

\[
Y(n)=
\frac{B+[\ell+unh(n)]A}
{d_0-\chi u n h(n)},
\]

\[
q(n)=
\frac{u h(n)Q}
{d_0-\chi u n h(n)},
\qquad
Q=(1-\beta)A+\chi B.
\]

entry payoff 上升的局部必要条件是

\[
\varepsilon_b(n)
\equiv-\frac{nh'(n)}{h(n)}
<
\frac{\chi u n h(n)}{d_0}.
\tag{R8}
\]

若

\[
h(n)=\frac1{n+\nu},
\]

则 \(\varepsilon_b=nh(n)\)。式（R8）要求 \(d_0<\chi u\)，但合法支出份额必然给出

\[
d_0-\chi u
=1-\beta-\chi(\ell+u)
\geq1-\beta-\chi>0.
\]

所以 \(q'(n)<0\) 对所有 \(n>0\) 成立。entry map 弱下降而 identity map 严格上升，fixed point 唯一。no-entry 与 full-entry corners 不可能共存。

**判定：标准对称 CES/routing business stealing 必然消除离散候选的 multiplicity 和 hysteresis。** 该候选只有在可证明订单品类近似隔离、seller entry 不显著稀释 per-seller orders 时才可能恢复，不适合作为当前 EL 基准。

相比之下，spatial-rent-receipt 候选本身采用

\[
q=\frac{Q}{n+\chi},
\]

即标准 business stealing。它不依赖 strategic complementarity 或多重均衡；其结果是唯一均衡中的 active-set threshold 和 kink。因此 CES robustness failure 不推翻新候选，反而说明选择唯一阈值而放弃 hysteresis 是正确的模型收缩。

## 9. Economics Letters 篇幅

该候选可以在约 2,000 词内自足，但只能完全替换当前论文，不能追加到现有 scalar model 后面。建议主文预算：

| 部分 | 目标词数 |
|---|---:|
| Abstract | 80--90 |
| Introduction 与制度事实 | 300--350 |
| Environment、ledger 与 free entry | 550--600 |
| Lemma、Proposition 与 kink | 550--600 |
| no-respending falsification | 180--220 |
| Discussion/Conclusion | 100--130 |

总计约 1,760--1,990 词。必须删除：

- 完整 CES 家庭优化；
- 原 recursive-retention multiplier proposition；
- finite \(z\) regions；
- \(s^\dagger<1/2\)；
- 离散 hysteresis；
- 两地区矩阵；
- 平台最优 \((\tau,\lambda)\)。

正文把 \(s\in(0,1)\) 作为给定的内生渠道份额或预定状态即可。若为了挽救 \(\lambda\) 必须再内生 local terminal effort、平台最优 payout、消费者采用和服务质量，模型将超出 EL 篇幅，应并回大论文。

## 10. 必须修正项与最终 gate

### 阻断项

1. **冻结 \(\lambda\) 的唯一制度解释。** 推荐改成 local transaction-service payout \(r=\lambda\tau\)，并说明总 take rate 固定、HQ 收取 \(\tau-r\)、服务基础设施与质量在比较中固定。
2. **证明不是任意 transfer。** 用 Couture 的 terminal-manager 3--5% transaction reward 作为制度事实，并明确预测只适用于 transaction-attributed local payout；若只剩无条件地方返还，停止独立 EL。
3. **完成直接 prior-art audit。** 首先逐式核查 Li 最新版本，再查 platform affiliate/revenue-sharing 与 local franchise payment 文献。
4. **限定 necessity claim。** 写成“在保持 \((s,E,F,\mu,\chi,\tau)\) 不变的 receipt-only counterfactual 中，respending 是必要通道”，不能写成普遍必要性。
5. **完整收入守恒。** 正文或附录加入外部账户和式（R4），并明确所有 seller inputs 的所在地。

### 重要但机械的修正

6. 修正式（22）中遗漏的 `\phi` 反斜线；
7. 补正进入分支 numerator 为正的证明；
8. 将“全局稳定”限定为 income iteration；
9. 把 owner income 改为 fixed/variable local factor income；
10. 在验证脚本中加入第 7.2 节的六项检查。

### 最终决策规则

- 五项阻断项全部通过：`GO_TO_FORMAL_REWRITE`；
- \(\lambda\) 只能解释成任意总部返还，或必须内生服务质量才能成立：`NO_GO_FOR_EL, MERGE_INTO_LARGE_PAPER`；
- 当前状态：`CONDITIONAL_GO, MAIN_TEX_REMAINS_FROZEN`。
