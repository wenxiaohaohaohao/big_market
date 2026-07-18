# M1--M3 修订基线

日期：2026-07-17  
用途：记录正式实施有限能力阈值、一般 share-speed 单峰和 increasing differences 之前的可恢复状态。

## 源文件 SHA-256

| 文件 | SHA-256 |
|---|---|
| `paper/main.tex` | `413563BB8419739C0D0788986A2925B9A9E0AFBF68E47232DD3577E220E3CAD7` |
| `paper/appendix.tex` | `E79671921F6B52410C4ACF89996281CDA6F1918FEC62CD41979FA9EB92BCDFFF` |
| `code/verify_model.py` | `BBA005B39752B761AA345B4CEEAA1C7FC47FDE160F3BB305CBC6194A027B4430` |
| `code/make_mechanism_figure.py` | `46D5C03C1075CFA28E062406DC6DE37CF7544D952024A2381D703B28314C2493` |

## 基线验证

- `python code/verify_model.py`：通过。
- 随机均衡：10,000 组，固定 seed `20260714`。
- CES 峰值：5,000 组满足 `Delta(kappa)>0` 的参数。
- 最大 fixed-point residual：`2.842e-14`。
- 最大 `z` derivative residual：`4.438e-10`。
- 最大 `kappa` derivative residual：`4.295e-10`。
- MiKTeX 完整编译：通过，生成 11 页 `output/paper.pdf`。
- 主文 `texcount -sum`：1,633。
- 主文加附录的既有记录：2,362。

MiKTeX 在尝试写用户级日志时报告 `C:\Users\dongw\AppData\Local\MiKTeX` 拒绝访问，但项目编译脚本已把 `TEMP` 和 `TMP` 指向项目内 `tmp/latex`，该警告没有影响 PDF、BibTeX 或交叉引用生成。

