# Internal Referee Audit

日期：2026-07-27
审查对象：`paper/main.tex`、`paper/appendix.tex`、Model Contract v3 和数值代码

## 总体判断

当前稿已经是一篇独立、完整的理论论文，而不是等待数据的理论框架。主问题仍是
platform access--local capture；NSE 用于解释生产机会如何转化为 viable entry、
organizational embeddedness 和 local income。论文适合用于内部讨论和征求 NSE
理论专家意见，但尚不能据此判断期刊接受概率。

## 主要审查问题及处理

### 1. 比较优势是否被错误定义为 \(1/c\)

**风险：** 单一单位成本只表示绝对成本或盈利能力，不是比较优势。

**处理：** 正文使用地区、产业双重相对生产成本
\(\mathcal C^P_{ij}\) 定义 LCA；\(c\) 仅作为保持参照成本不变时的单调充分统计量。
ACA、viability 和 realization 分开定义。

ACA 进一步写成现实双重相对交付成本指数
\(\mathcal C^A_{ijr}=\tau_O(c+d_r)/\bar c_h^A\)，并单独生成 \(G_A\)。
\(G_A\) 不含固定成本，\(G_E\) 含固定成本；稿件不再用盈利进入替代 ACA。

### 2. NSE 是否替代了原始平台问题

**风险：** 论文可能退化为一般 LCA--ACA 模型。

**处理：** consumer platform price、platform expenditure share、
producer market access、channel displacement、producer payment incidence 和 EL
income propagation 均保留。四个 NSE 门槛最终都进入 access--capture 结果。

### 3. 组织选择是否只是人为增加变量

**风险：** \(P/L\) 选择若不改变支付位置，就只是额外成本排序。

**处理：** 组织方式由同一利润比较生成，并改变
\(\rho_r,B_j^r\)、local service income 和 external payment。平台依赖区间只在
\(F>\bar F\) 时存在；\(F\leq\bar F\) 的反例已正式报告。

### 4. 固定成本和地方收入是否重复扣除

**风险：** 将本地固定成本既当作企业成本又从地方收入扣除会双重计算。

**处理：** \(f,F\) 决定利润和组织选择。基准中它们由本地要素和服务提供，因此是
本地内部支付，不再从 local income 扣除。外部单位平台支付只通过 \(\rho_P\)
扣除一次。

### 5. 背景产业收入和候选产业收入的边界

**风险：** focal-region partial equilibrium 没有完整求解候选产业对背景产业的
要素挤出。

**处理：** 正文明确候选产业面对背景部门给出的固定机会成本，地方收入是短期
transaction-related income，不是完整福利。该设定要求边际要素或闲置能力在相关
区间可按固定机会成本供给。若研究长期充分就业资源重配，必须建立完整两部门 GE，
不属于当前小模型。

### 6. \(G_R<G_Y\) 是否被无条件声称

**风险：** 离散 entry 或 organization switch 可以使两个最小阈值重合。

**处理：** 正式结果为 \(G_R\leq G_Y\)。只有两个根位于同一连续组织区间时才声称
严格排序；共同离散跳跃导致 \(G_R=G_Y\) 的边界已证明。

### 7. facilitating state 是否等于任意补贴

**风险：** 若政府只是机械降低成本，政策结论是预设的。

**处理：** 政府参与只降低共享基础设施的融资楔子；基础设施提供者有独立、严格
凹的选择问题。论文不求全国最优 \(\vartheta\)。保护通过提高外部渠道成本建模，
并被证明同时损害 consumer access 和 marginal entry。

### 8. 数值练习是否被误称为校准

**处理：** 正文、图注和附录均称 illustrative numerical exercises；参数只用于
证明相关区域非空。代码输出每张图的 PDF、PNG 和 CSV。

### 9. outbound iceberg cost 是否错误地低于 1

**风险：** 直接把 \(\exp[-(\gamma+\chi z)G]\) 称为 iceberg cost，会在正的
\(G\) 下低于 1。

**处理：** 完整成本改为
\(\tau_O=\bar\tau_O\exp[-(\gamma+\chi z)G]\geq1\)。不随政策变化的
\(\bar\tau_O^{1-\sigma}\) 吸收到 \(\mathcal M_0\)，所以所有利润、阈值和数值结果
保持不变，但 iceberg cost 的经济含义得到恢复。

### 10. 数值练习是否真正展示正文机制

**风险：** 旧基准在 \(c=0.8\) 时进入和组织门槛大多接近零，政府参与度
\(0.1,0.5,0.9\) 也没有分别覆盖“不进入—平台依赖—本地嵌入”三个状态；这虽不
构成计算错误，却削弱了数值练习的说明力。旧代码还用 \(G_X\) 无条件定义
\(G_L\)，在 \(F\leq\bar F\) 的反例中不正确。

**处理：** 基准改为 \(c=0.9,\kappa_g=0.3\)，并使用
\(\vartheta=0.05,0.50,0.95\)。五个门槛和对应政府参与门槛均在图示范围内。
\(G_L\) 现按均衡选择分段定义：三状态区域使用 \(G_X\)，平台中间区消失时使用
\(G_L^0\)。验证脚本同时检查两个参数区域。另新增同一本地化结果下的
facilitation--protection CSV 对照，避免只在正文声称而没有数值 artifact。

## 仍需在对外版本声明的限制

1. 背景部门与候选产业之间的长期资源重配未求解；
2. 参照地区成本和全国市场规模外生；
3. 平台价格与平台费不由平台最优化决定；
4. 无企业异质性、迁移、集聚或全国福利；
5. 无实际数据，因此不能对中国效应大小作数量判断。

这些限制不使当前理论稿成为未完成品，但决定了论文可以回答的是结构性门槛和机制，
而不是全国政策最优或定量福利。
