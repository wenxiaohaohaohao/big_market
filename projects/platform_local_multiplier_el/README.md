# platform_local_multiplier_el

这是 `big_market` 下拟投 *Economics Letters* 的独立理论短文子项目。

## 固定题目

中文：**统一市场、平台化与地方乘数：价值捕获的空间重组**

英文：**Market Integration, Platformization, and Local Multipliers: The
Spatial Reorganization of Value Capture**

题目与研究主线已经冻结。除非两位作者共同作出新的书面决定，不再以
“retail channel substitution”“seller entry”或“transaction-service
payout”重新命名论文；这些对象至多是解释平台中介重组的模型部件。

## 研究问题

市场一体化何时主要产生 market-access gain，何时因平台中介重组降低
local value capture；本地组织能力如何决定一个地区能否把平台扩张
转化为本地收入和地方乘数？

固定机制链条是“市场一体化与平台扩张 → 交易渠道和中介组织重组 →
本地价值捕获变化 → 本地收入与非贸易部门需求变化 → 有效地方乘数变化”。

## 最小模型

- 一般 homothetic 两渠道需求与相应的消费价格指数；
- CES 作为 Supplement 中的嵌套特例和数值示意；
- 市场一体化带来的消费端价格改善与生产端基础收入扩张；
- 平台渠道与本地代理渠道之间的交易组织重组；
- 本地组织能力决定平台交易中工资、当地所有者利润与服务收入的留存；
- 本地收入通过非贸易品需求继续传播，形成 Moretti 型地方乘数；
- 小型开放地区的短期地方收入均衡，而非完整多地区空间 GE。

## 模型版本决定

当前 *Economics Letters* 稿件采用方案 A：有限整合指数、正价格和
内部两渠道需求。主文使用可微、linearly homogeneous 的一般两渠道
unit-expenditure function，并假定平台支出份额满足 \(0<s(z)<1\)、
\(s'(z)>0\)。一般单峰结果进一步要求需求系统诱导的 share-speed
\(g(s)\) 在端点为零、内部为正且严格凹。CES
\(g(s)=(\eta-1)s(1-s)\) 只在 Supplement 中作为闭式特例，不再是主文
结论成立的必要条件。

方案 A 用 \(\kappa\in[0,1]\) 表示本地组织能力，并令平台交易的本地
留值率随 \(\kappa\) 提高。它只改变交易收入的空间归属，不改变平台
价格或消费者渠道偏好，因此能够分别识别 market access 与 local
capture。当前主文的核心结果是：有限整合冲击下唯一且有序的 nominal
local income/consumption-equivalent real income 能力阈值、一般严格凹
share-speed 下的
唯一 capture-drag 峰值，以及 integration 与 capacity 的 log-income
increasing differences。标准 multiplier 只作为 benchmark。

正式稿必须依次给出原始假设、家庭优化、均衡定义、存在性与唯一性、
解析解、Lemma/Proposition/Corollary、完整证明和边界分析。方案 A
是当前唯一进入 `paper/main.tex`、`paper/appendix.tex` 与核验代码的
模型版本。

## 未来扩展：方案 B

未来可以加入平台参与固定成本 \(F>0\)。它能够产生真正的无平台
corner \(s=0\)；一旦采用平台，家庭仍进入方案 A 的内部两渠道需求子问题。
但单独加入平台固定成本不会自动产生严格的完全平台化 corner
\(s=1\)。后者还需要 single-homing、本地渠道退出、另一项渠道固定
成本，或 \(\eta\to\infty\) 等额外结构。

方案 B 需要重新研究采用时序、采用阈值的存在与唯一性、不连续反应及
多重均衡。本项目当前不求解方案 B，也不在主文、附录或结论中把它引用
为已有结果；只有在方案 A 投稿稿完成后，才重新评估是否扩展。

## 计划成果

- 两个解析命题、一个推论及完整证明；
- 一张双 panel 主图及可追溯 source-data CSV；
- 约 2,000 英文词的主文；
- 可复现的示意性数值代码；
- 投稿所需摘要、highlights、JEL 和数据声明。

## 正式目录

```text
platform_local_multiplier_el/
├── paper/
│   ├── main.tex
│   ├── supplement.tex
│   ├── references.bib
│   └── appendix.tex
├── figures/
├── code/
├── notes/
├── literature/
├── output/
└── README.md
```

现有参考材料：

- `notes/EL_project_memo_zh.md`：供合作者讨论的完整中文项目备忘录，不是论文主稿；
- `output/EL_project_memo_zh.pdf`：备忘录的审阅版本，不是可编辑源文件。

## 唯一源文件规则

- `paper/main.tex` 是唯一正式主稿；
- `paper/supplement.tex` 是单独生成 PDF 的 Supplement wrapper；其主文
  交叉引用由构建脚本先编译 `paper/main.tex` 后提供；
- `paper/appendix.tex` 是由 Supplement 载入的证明正文；
- `paper/references.bib` 是唯一 BibTeX 文献库；
- `output/paper.pdf` 只由 LaTeX 编译生成，不能直接编辑；
- `output/supplement.pdf` 只由 LaTeX 编译生成，不能直接编辑；
- 网页端、Word、聊天记录和 PDF 只用于讨论与审阅，不维护第二份正式稿；
- 合作者的有效修改应统一写回上述 LaTeX/BibTeX 文件。

## 网页端与桌面 App 分工

网页端主要用于：

- 与合作者讨论研究问题；
- 文献查重、检索和定位；
- 阅读、批注 PDF；
- 比较不同版本；
- 决定模型机制、命题和写作取舍。

桌面 App 主要用于：

- 正式编辑 `paper/main.tex` 和 `paper/appendix.tex`；
- 维护 `paper/references.bib`；
- 推导和核验公式；
- 编写数值模拟与制图代码；
- 生成论文图形；
- 编译并逐页检查 `output/paper.pdf`。

手机 App 可以继续云端聊天与审阅文件，但不视为可以直接读写电脑本地论文目录。

## Library 里程碑存档

Library 已保存项目备忘录的 Markdown 和 PDF，作为跨端参考。后续只在以下节点新增存档：

1. 模型设定冻结版；
2. 第一版英文全文；
3. 合作者修改版；
4. 投稿版；
5. 最终代码与附录。

每份里程碑文件应注明日期、版本性质和对应 Git commit。Library 文件不直接续写；发现问题后，回到本地 LaTeX 或代码修改、重新编译和提交，再生成新的里程碑快照。

## 讨论成果回写顺序

1. 在网页端或聊天中形成明确决定；
2. 在桌面 App 中将决定写入 README、`notes/`、LaTeX 或代码；
3. 运行编译与必要验证；
4. 使用 Git 保存可追踪版本；
5. 仅在达到上述里程碑时更新 Library。

## 本机编译

需要重生成解析图形时，先从子项目根目录运行：

```powershell
python .\code\make_mechanism_figure.py
python .\code\make_supplementary_local_regions.py
```

第一条命令生成正文 Figure 1 及两份 panel CSV；第二条命令生成
Supplementary Figure S1 的 PDF、SVG、600 dpi PNG 和501行 source-data
CSV。两张图均由 `code/verify_model.py` 中的核验函数计算解析对象。

从子项目根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\code\build_paper.ps1
```

脚本依次编译主文与 Supplement，生成 `output/paper.pdf` 和
`output/supplement.pdf`，成功后清理 LaTeX 辅助文件。调试时可增加
`-KeepAux` 保留辅助文件。

## 当前状态与下一步

M1--M3 已按上述定义写入主文与 Supplement，验证脚本覆盖随机、有限
差分、闭式根、阈值排序、边界分类和 CES nesting；图 1 同步输出
PDF、SVG、600 dpi PNG 与 panel CSV。Supplementary Figure S1 单独保留
CES 特例下沿平台份额变化的局部收入符号区域，并同步输出 PDF、SVG、
600 dpi PNG 与 source-data CSV。投稿版完成条件是：MiKTeX 编译无错误、
未解析引用或 overfull box，主文不超过内部字数上限，并对两份 PDF
完成逐页检查。
