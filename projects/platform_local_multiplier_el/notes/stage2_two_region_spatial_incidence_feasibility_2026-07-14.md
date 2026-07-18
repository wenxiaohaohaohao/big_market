# Stage 2：两地区 spatial-incidence 解析模型可行性检验

日期：2026-07-14  
性质：内部解析建模备忘录，不是正式稿，不构成创新性优先权声明  
范围：只测试一个最小的两地区收入归属系统能否产生当前标量留值模型无法表达的空间结果。本文不建立 full spatial GE，不内生化平台定价、生产区位、工资、税收或人口流动。

## 一、结论先行

最小的两地区扩展是可解的，而且确实增加了当前单地区标量模型没有的对象：

1. 同一笔外围地区支出在外围地区 \(L\) 与平台总部地区 \(H\) 之间的收入归属向量；
2. 两地收入通过各自后续支出形成的回流网络；
3. 平台化对 \(L\)、\(H\) 和全国总收入的不同影响；
4. 在价格和平台份额完全不变时，平台租金归属改变两地收入的纯 spatial-incidence 效应。

在这个系统中，平台化可以使 \(L\) 的收入和本地 multiplier 下降、\(H\) 的收入和外地 multiplier 上升，同时全国总收入不变；若 \(H\) 的后续支出倾向高于 \(L\)，全国总收入甚至可以提高。这个结论不能由只报告 \(L\) 的标量留值率和标量收入方程完整表达，因为它还取决于 \(H\) 的支出倾向以及 \(H\) 支出回流到 \(L\) 的比例。

但是，必须保留一个严格边界：给定价值归属矩阵后的固定点、Leontief inverse、存在唯一性以及零和收入归属冲击的网络传播，都是标准 Leontief、SAM 或 MRIO 代数。仅把标量 \(\omega\) 换成 \(2\times2\) 矩阵并不足以形成新的理论贡献。潜在的增量来自三项结构的联合：价格诱导的内生渠道替代、渠道特定的收入归属列、以及可在价格和渠道份额不变时单独改变的租金所有权参数。是否足以发表，仍需 equation-level prior-art audit。

## 二、原始对象与时序

### 2.1 地区与收入

经济中有两个地区：

- \(L\)：外围消费地；
- \(H\)：平台总部和主要外部收入接收地。

令

\[
\mathbf y=
\begin{pmatrix}
y_L\\
y_H
\end{pmatrix},
\qquad
\mathbf b=
\begin{pmatrix}
b_L\\
b_H
\end{pmatrix},
\qquad b_L,b_H>0.
\]

\(b_i\) 是在所建模的重复零售支出循环之外形成的自主收入。地区 \(i\) 将收入的比例 \(c_i\) 用于进入本模型的零售支出：

\[
C=
\begin{pmatrix}
c_L&0\\
0&c_H
\end{pmatrix},
\qquad 0\leq c_L,c_H<1.
\]

其余收入用于模型外商品、储蓄或其他不再产生本模型收入的用途。这个楔子保证循环不会无限扩张。

### 2.2 平台渠道份额

外围地区 \(L\) 的居民在本地代理渠道 \(A\) 与平台渠道 \(P\) 之间选择。为了与当前 CES 稿件兼容，令

\[
s(z)=
\frac{a p_P(z)^{1-\eta}}
{(1-a)p_A^{1-\eta}+a p_P(z)^{1-\eta}},
\qquad
p_P(z)=\bar p_Pe^{-z},
\]

其中 \(a\in(0,1)\)、\(\eta>1\)、\(p_A,\bar p_P>0\)。因此，对有限 \(z\)，

\[
0<s(z)<1,
\qquad
s'(z)=(\eta-1)s(z)[1-s(z)]>0.
\]

本备忘录只需要 \(s'(z)>0\)。CES 负责把 integration shock \(z\) 映射为渠道份额变化；收入归属由下一部分决定。

### 2.3 渠道收入归属与平台租金

令：

- \(\ell_A\in[0,1]\)：一元 \(L\) 地代理渠道支出最终成为 \(L\) 收入的份额；
- \(\ell_P^0\in[0,1]\)：不含可重新分配的平台租金时，一元平台支出成为 \(L\) 收入的份额；
- \(\kappa\in[0,1]\)：一元平台支出中的平台租金份额；
- \(\lambda\in[0,1]\)：平台租金中归 \(L\) 所有者或返还 \(L\) 的比例。

要求

\[
0\leq\ell_P^0,\quad 0\leq\kappa,\quad
\ell_P^0+\kappa\leq1.
\]

平台渠道的一元支出在 \(L\) 形成的收入份额为

\[
\ell_P(\lambda)=\ell_P^0+\lambda\kappa.
\]

在给定平台份额 \(s\) 时，\(L\) 地零售支出的平均本地归属份额为

\[
\omega(s,\lambda)
=(1-s)\ell_A+s\ell_P(\lambda).
\]

基准条件是

\[
\ell_A>\ell_P(\lambda),
\]

因而

\[
\omega_z
=s'(z)[\ell_P(\lambda)-\ell_A]<0,
\qquad
\omega_\lambda=s\kappa\geq0.
\]

\(\lambda\) 只改变平台租金的空间所有权，不改变 \(p_P\) 或 \(s\)。因此，它可以用于识别纯收入归属效应。

### 2.4 总部地区支出的回流

令 \(r\in[0,1]\) 表示一元 \(H\) 地零售支出中最终成为 \(L\) 收入的份额。它可以代表 \(H\) 对 \(L\) 的商品、履约或服务采购。其余 \(1-r\) 成为 \(H\) 收入。

于是，渠道份额和收入归属共同生成价值归属矩阵

\[
\Gamma(\omega,r)=
\begin{pmatrix}
\omega&r\\
1-\omega&1-r
\end{pmatrix}.
\]

列表示支出发生地，行表示收入形成地。每列和为一：

\[
\mathbf 1^\top\Gamma=\mathbf 1^\top.
\]

第一列是平台化改变的 \(L\) 地支出归属；第二列是总部地区支出向外围地区的回流。当前单地区模型相当于只保留第一列的第一个元素 \(\omega\)，并把 \(1-\omega\) 作为不再追踪的外流。

## 三、地方收入固定点

两地诱发零售支出为 \(C\mathbf y\)。收入固定点是

\[
\mathbf y
=\mathbf b+\Gamma(\omega,r)C\mathbf y.
\tag{1}
\]

令

\[
M(\omega,r)=\Gamma(\omega,r)C
=
\begin{pmatrix}
\omega c_L&r c_H\\
(1-\omega)c_L&(1-r)c_H
\end{pmatrix}.
\]

式（1）可以写为

\[
\mathbf y=\mathbf b+M\mathbf y.
\]

它同时包含四类路径：

1. \(L\to L\)：外围收入经外围支出再次形成外围收入；
2. \(L\to H\)：外围支出经平台和外部供给形成总部地区收入；
3. \(H\to L\)：总部地区收入通过 \(r\) 回流外围；
4. \(H\to H\)：总部地区收入继续在总部地区循环。

## 四、存在性、唯一性与闭式解

### Lemma 1：存在性与唯一性

在 \(0\leq c_L,c_H<1\)、\(\omega,r\in[0,1]\) 和 \(\mathbf b\gg0\) 下，式（1）存在唯一正解，并且从任意非负初值开始的迭代

\[
\mathbf y^{(n+1)}=\mathbf b+M\mathbf y^{(n)}
\]

收敛到该解。

### 证明

\(M\) 非负，其两列的列和分别为 \(c_L\) 和 \(c_H\)。因此

\[
\lVert M\rVert_1=\max\{c_L,c_H\}<1,
\]

从而

\[
\rho(M)\leq\lVert M\rVert_1<1.
\]

所以 \(I-M\) 可逆，

\[
(I-M)^{-1}
=\sum_{k=0}^{\infty}M^k\geq0,
\]

且唯一解为

\[
\mathbf y=(I-M)^{-1}\mathbf b\gg0.
\]

同一条件也保证固定点迭代全局收敛。证毕。

定义

\[
D(\omega,r)
=\det(I-M).
\]

直接展开得

\[
D
=
[1-\omega c_L][1-(1-r)c_H]
-r c_H(1-\omega)c_L
\]

以及等价表达

\[
D
=1-(1-r)c_H-r c_Hc_L-\omega c_L(1-c_H)>0.
\tag{2}
\]

闭式解是

\[
y_L
=
\frac{
[1-(1-r)c_H]b_L+r c_Hb_H
}{D},
\tag{3}
\]

\[
y_H
=
\frac{
[1-\omega c_L]b_H+(1-\omega)c_Lb_L
}{D}.
\tag{4}
\]

对应的收入 multiplier matrix 为

\[
\mathcal R(\omega,r)
\equiv
\frac{\partial\mathbf y}{\partial\mathbf b^\top}
=(I-M)^{-1}
=\frac1D
\begin{pmatrix}
1-(1-r)c_H&r c_H\\
(1-\omega)c_L&1-\omega c_L
\end{pmatrix}.
\tag{5}
\]

式（5）不仅给出一地自己的 multiplier，也给出一地自主收入在另一地形成的 cross-region multiplier。

## 五、解析结果

### Proposition 1：平台化引起 multiplier 的空间转移

给定 \(0<c_L<1\)、\(0\leq c_H<1\)、\(r\)、\(\mathbf b\) 和 \(\lambda\)，把 \(\omega\) 看作平台化改变的收入归属状态。则

\[
\frac{\partial y_L}{\partial\omega}
=
\frac{c_Ly_L(1-c_H)}D>0,
\tag{6}
\]

\[
\frac{\partial y_H}{\partial\omega}
=
-\frac{c_Ly_L(1-c_L)}D<0,
\tag{7}
\]

\[
\frac{\partial(y_L+y_H)}{\partial\omega}
=
\frac{c_Ly_L(c_L-c_H)}D.
\tag{8}
\]

若 \(\ell_A>\ell_P(\lambda)\)，则 \(\omega_z<0\)。因此，仅通过收入归属渠道，平台化严格降低 \(L\) 收入并严格提高 \(H\) 收入。全国总收入的方向取决于两地在本模型中的后续支出倾向：

- 若 \(c_L=c_H\)，全国总收入不变；
- 若 \(c_H>c_L\)，全国总收入提高，同时 \(L\) 收入下降；
- 若 \(c_H<c_L\)，全国总收入下降，同时收入向 \(H\) 转移。

### 证明

对式（1）关于 \(\omega\) 求导。令

\[
\mathbf u=
\begin{pmatrix}
1\\
-1
\end{pmatrix},
\qquad
\frac{\partial\Gamma}{\partial\omega}
=\mathbf u
\begin{pmatrix}
1&0
\end{pmatrix}.
\]

于是

\[
\frac{\partial\mathbf y}{\partial\omega}
=(I-M)^{-1}\mathbf u\,c_Ly_L.
\tag{9}
\]

由式（5），

\[
(I-M)^{-1}\mathbf u
=\frac1D
\begin{pmatrix}
1-c_H\\
-(1-c_L)
\end{pmatrix}.
\]

代回式（9）即得式（6）至式（8）。再利用 \(\omega_z<0\) 即得平台化比较静态。证毕。

### Corollary 1：全国 multiplier 不变但由 \(L\) 转向 \(H\)

若 \(c_L=c_H=c\in(0,1)\)，则

\[
y_L+y_H=\frac{b_L+b_H}{1-c},
\tag{10}
\]

与 \(\omega\)、\(r\) 和渠道份额无关。对 \(L\) 自主收入冲击的两地 multiplier 为

\[
m_{LL}
=\frac{1-(1-r)c}
{(1-c)[1+c(r-\omega)]},
\]

\[
m_{HL}
=\frac{(1-\omega)c}
{(1-c)[1+c(r-\omega)]},
\]

并且

\[
m_{LL}+m_{HL}=\frac1{1-c}.
\tag{11}
\]

当平台化降低 \(\omega\) 时，\(m_{LL}\) 下降、\(m_{HL}\) 上升，二者变化一一抵消。平台化没有改变全国 multiplier 的大小，但改变了该 multiplier 在外围地区和总部地区之间的归属。

这正是标量 \(L\) 模型无法报告的结果：标量模型只能看到 \(m_{LL}\) 减弱，看不到同一冲击在 \(H\) 形成的 \(m_{HL}\)。

### Corollary 2：全国增长与外围损失可以同时发生

若 \(c_H>c_L\) 且平台化降低 \(\omega\)，由式（6）至式（8）可得

\[
\frac{dy_L}{dz}<0,
\qquad
\frac{dy_H}{dz}>0,
\qquad
\frac{d(y_L+y_H)}{dz}>0.
\]

所以全国总收入上升不能推出外围地区受益。平台化把收入转向具有更强后续支出反馈的总部地区时，全国 multiplier 可以扩大，同时地方 multiplier 和地方收入下降。

### Proposition 2：租金地方化的纯 spatial-incidence 效应

固定 \(z\)、平台价格和平台份额 \(s\)。若 \(\kappa>0\)，提高平台租金地方化比例 \(\lambda\) 不改变价格或渠道配置，但

\[
\frac{\partial\omega}{\partial\lambda}=s\kappa>0.
\]

因此

\[
\frac{\partial y_L}{\partial\lambda}
=
s\kappa
\frac{c_Ly_L(1-c_H)}D>0,
\tag{12}
\]

\[
\frac{\partial y_H}{\partial\lambda}
=
-s\kappa
\frac{c_Ly_L(1-c_L)}D<0,
\tag{13}
\]

\[
\frac{\partial(y_L+y_H)}{\partial\lambda}
=
s\kappa
\frac{c_Ly_L(c_L-c_H)}D.
\tag{14}
\]

若 \(c_L=c_H\)，租金地方化在全国总收入不变时把收入和 multiplier 从 \(H\) 转回 \(L\)。若 \(c_L>c_H\)，租金地方化还提高全国总收入；若 \(c_L<c_H\)，则全国总收入下降。最后两种情况不是资源凭空增加或减少，而是收入归属改变后，两地不同的后续支出倾向改变了被本模型计入的循环轮次。

### 证明

价格和 \(s\) 固定时，\(\lambda\) 只通过 \(\omega\) 进入 \(\Gamma\)。将
\(\omega_\lambda=s\kappa\) 乘入 Proposition 1 的三个导数即可。证毕。

## 五-A、强候选：双向 access–capture threshold

上一模型把两地后续支出倾向写成 \(c_L\) 与 \(c_H\)。为了更直接地
对应当前稿件的 \(\alpha\) 和 \(\beta\)，并同时表示 outward access 与
headquarters capture，考虑下面的共同支出结构。

两地居民都将收入份额 \(\beta\) 花在只形成当地收入的非贸易品，将
收入份额 \(\alpha\) 花在存在跨地区收入归属的零售品，并满足

\[
\alpha,\beta>0,\qquad
d\equiv1-\alpha-\beta>0.
\]

定义双向收入归属矩阵

\[
\Pi(q,r)=
\begin{pmatrix}
1-q&r\\
q&1-r
\end{pmatrix},
\qquad q,r\in[0,1].
\tag{17}
\]

其中：

- \(q(z)\) 是一元 \(L\) 地零售支出最终在 \(H\) 形成收入的份额，表示
  headquarters capture、外部供货和平台租金外流；
- \(r(z)\) 是一元 \(H\) 地零售支出最终在 \(L\) 形成收入的份额，表示
  \(L\) 通过市场一体化获得的 outward access。

收入固定点为

\[
\mathbf Y
=\mathbf B+\beta I\mathbf Y+\alpha\Pi(q,r)\mathbf Y.
\tag{18}
\]

因为 \(\beta I+\alpha\Pi\) 的两列和均为 \(\alpha+\beta<1\)，存在
唯一正解。令

\[
K(q,r)=d+\alpha(q+r)>0.
\]

则

\[
I-\beta I-\alpha\Pi
=
\begin{pmatrix}
d+\alpha q&-\alpha r\\
-\alpha q&d+\alpha r
\end{pmatrix},
\]

\[
\det(I-\beta I-\alpha\Pi)=dK,
\]

并且

\[
Y_L
=
\frac{dB_L+\alpha r(B_L+B_H)}{dK},
\qquad
Y_H
=
\frac{dB_H+\alpha q(B_L+B_H)}{dK}.
\tag{19}
\]

加总式（18）得到

\[
Y_L+Y_H=\frac{B_L+B_H}{d}.
\tag{20}
\]

全国总收入只由共同的总支出倾向 \(\alpha+\beta\) 决定，而 \(q\) 与
\(r\) 决定 multiplier 在两地之间如何分布。

### Proposition 3：outbound access 与 headquarters capture 的精确阈值

假定 \(q(z)\) 与 \(r(z)\) 可微。双向市场一体化的地区收入效应为

\[
\frac{dY_L}{dz}
=
-\frac{\alpha[q'(z)Y_L-r'(z)Y_H]}
{d+\alpha(q+r)},
\tag{21}
\]

\[
\frac{dY_H}{dz}
=-\frac{dY_L}{dz},
\qquad
\frac{d(Y_L+Y_H)}{dz}=0.
\tag{22}
\]

因此，

\[
\frac{dY_L}{dz}>0
\quad\Longleftrightarrow\quad
r'(z)Y_H>q'(z)Y_L.
\tag{23}
\]

外围地区能否把 market integration 转化为地方收入，不取决于
access 或 capture 的单独变化，而取决于：

\[
\text{新增 outward access 作用于总部收入基数}
\quad\text{是否超过}\quad
\text{新增 HQ capture 作用于外围收入基数}.
\]

平台化可以同时提高 \(q\) 和 \(r\)。即使 \(r'>0\)，只要
\(q'Y_L>r'Y_H\)，\(L\) 收入仍然下降；反之，即使平台带来 HQ
capture，只要 outward access 足够强，\(L\) 仍然受益。

### 证明

令

\[
A(z)=\beta I+\alpha\Pi[q(z),r(z)],
\qquad
\mathbf u=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]

对式（18）求导：

\[
\mathbf Y_z=(I-A)^{-1}A_z\mathbf Y.
\]

定义

\[
g(z)=q'(z)Y_L-r'(z)Y_H.
\]

直接计算得到

\[
A_z\mathbf Y=-\alpha g(z)\mathbf u.
\]

又因为

\[
(I-A)^{-1}\mathbf u
=\frac{\mathbf u}{d+\alpha(q+r)},
\]

代回即得式（21）和式（22）。式（23）随即成立。证毕。

### Corollary 3：HQ rent localization

令平台租金地方化只降低 \(L\to H\) 的收入外流：

\[
q(z,\lambda)
=\bar q(z)-s(z)\kappa\lambda,
\qquad
r_\lambda=0,
\]

并在给定 \(z\) 时保持平台价格、平台份额和 \(\kappa>0\) 不变。于是

\[
q_\lambda=-s\kappa<0
\]

且

\[
\frac{\partial Y_L}{\partial\lambda}
=
\frac{\alpha s\kappa Y_L}
{d+\alpha(q+r)}>0,
\qquad
\frac{\partial Y_H}{\partial\lambda}
=-\frac{\partial Y_L}{\partial\lambda},
\tag{24}
\]

\[
\frac{\partial(Y_L+Y_H)}{\partial\lambda}=0.
\]

这是一个价格、渠道份额和全国总 multiplier 均不改变，只改变
地区收入归属的反事实。

### 这一强候选是否真的新增 feedback state

相对于当前单地区标量模型，答案是“是，但仍不充分”。

- **是：** 式（21）的符号取决于 \(q'Y_L-r'Y_H\)。\(H\) 的当前收入
  \(Y_H\)、由 \(H\) 支出形成的回流 \(r\) 及其变化 \(r'\) 都是
  单地区 \(\omega_L\) 方程中不存在的均衡对象。只有在
  \(r=r'=0\) 时，结果才退化为单向 leakage 模型。
- **仍不充分：** 给定 \(\Pi(q,r)\) 后，式（18）至式（23）仍是一个
  两部门或两地区 MRIO/SAM comparative static。threshold 的闭式形式
  来自 \(2\times2\) 列随机矩阵和共同支出倾向，并不是新的矩阵定理。
  可主张的潜在增量只能是平台渠道选择如何共同生成 \(q(z)\) 与
  \(r(z)\)，以及为什么 rent localization 只移动 \(q\) 而不改变价格
  与份额。若 \(q\) 和 \(r\) 继续完全 reduced form，创新性风险仍然高。

## 六、回流与网络反馈

Neumann 展开给出

\[
\mathbf y
=
\mathbf b+M\mathbf b+M^2\mathbf b+\cdots.
\tag{15}
\]

当 \(r=0\) 时，所有 \(H\to L\) 路径消失；当 \(r>0\) 时，\(L\to H\to L\)、\(H\to L\to H\) 以及更长路径进入式（15）。因此，相同的 \(L\) 地留值率 \(\omega\) 并不足以确定两地均衡。

对一个给定规模的第一轮零和收入归属变化 \(\delta\mathbf u\)，完整网络响应为

\[
d\mathbf y
=(I-M)^{-1}\mathbf u\,\delta
=
\frac{\delta}{D}
\begin{pmatrix}
1-c_H\\
-(1-c_L)
\end{pmatrix}.
\tag{16}
\]

这里 \(r\) 通过 \(D\) 改变后续传播。由于

\[
\frac{\partial D}{\partial r}=c_H(1-c_L)>0,
\]

对固定的第一轮转移 \(\delta\)，更强的 \(H\to L\) 回流会缩小式（16）中最终两地收入变化的绝对值。经济含义是，原本已经存在的跨区回流抵消了部分初始空间重分配。

但是，对一个由平台份额变化内生生成的冲击，第一轮转移本身等于
\(c_Ly_L\,d\omega\)，而 \(y_L\) 也随 \(r\) 变化。因此，平台化总效应对 \(r\) 的比较静态一般不具有无条件单调性。不能把“回流一定缓冲平台冲击”写成一般命题。

式（15）和式（16）是标准网络 multiplier 结果。它们的用途是明确渠道收入归属冲击如何进入网络，而不是宣称发现了新的 Leontief 性质。

## 七、为什么它不能还原为单一标量 \(\omega\)

有三种意义上的不可还原性。

### 7.1 同一 \(\omega\)，不同回流网络

给定相同的 \(L\) 地留值率，\(r\) 不同会改变 \(L\) 和 \(H\) 的收入。单地区方程没有 \(H\to L\) 的支出列，无法区分这两个经济。

### 7.2 同一 \(L\) 损失，不同全国结果

平台化降低 \(\omega\) 时，\(L\) 收入总是下降、\(H\) 收入总是上升；但全国总收入的符号由 \(c_L-c_H\) 决定。单地区方程只能报告 \(L\) 的损失，不能判断全国总 multiplier 是不变、扩大还是缩小。

### 7.3 同一价格和渠道份额，不同空间收入归属

\(\lambda\) 改变平台租金归属而不改变 \(p_P\) 或 \(s\)。因此，价格可及性、渠道选择和收入归属可以被严格分开。单一 \(\omega\) 方程可以做这一比较静态，但无法同时报告收入从哪个地区转向哪个地区，也无法追踪转移后的回流。

需要同时承认：两地区模型仍可写为一个 \(2\times2\) Leontief system。从线性代数上，它当然可以被消元为关于 \(y_L\) 的单个分式方程。这里所说的“不能还原为标量重算”，是指一个只使用 \(L\) 的 \(\omega\)、\(c_L\) 和 \(b_L\) 的经济模型无法恢复 \(H\) 的归属、全国效应和回流路径；并不是声称二维线性系统不能被代数消元。

## 八、边界与特殊情形

1. **有限 CES 份额。** 对有限 \(z\)，\(s\in(0,1)\)。\(s\to0\) 和 \(s\to1\) 只作为极限。
2. **渠道无归属差异。** 若 \(\ell_A=\ell_P(\lambda)\)，则 \(\omega_z=0\)，integration 不通过收入归属矩阵产生空间转移。
3. **无平台租金。** 若 \(\kappa=0\) 或 \(s=0\)，\(\lambda\) 无实际作用。
4. **无回流。** 若 \(r=0\)，\(H\) 支出不再形成 \(L\) 收入，矩阵变为单向网络，但 \(L\to H\) 仍存在。
5. **完全回流。** 若 \(r=1\)，所有 \(H\) 地模型内支出形成 \(L\) 收入；只要 \(c_L,c_H<1\)，均衡仍唯一。
6. **无诱发支出。** 若 \(c_L=c_H=0\)，则 \(\mathbf y=\mathbf b\)，渠道收入归属只在有外部 gross-spending injection 时才产生效应。
7. **共同支出倾向。** 若 \(c_L=c_H=c\)，全国总 multiplier 是 \(1/(1-c)\)，空间矩阵只分配而不改变全国总量。
8. **支出倾向接近一。** 当 \(\max\{c_L,c_H\}\uparrow1\) 时，当前的充分收敛界失效。若 \(c_L=c_H=1\)，\(\Gamma\) 为列随机矩阵，\(\rho(M)=1\)，正的自主收入下不存在有限固定点。
9. **全国之外的漏出。** 当前假定每列和为一，即每一元模型内零售支出都在 \(L\) 或 \(H\) 形成收入。若还存在国外利润、储蓄性抽取或模型外税收，可令列和小于一；存在性更容易，但全国总量不再满足式（10）。
10. **平台价格和收入归属独立。** Proposition 2 需要维持 \(\lambda\) 不影响价格、佣金率和渠道需求。若租金地方化改变平台成本或定价，必须重新求解 \(s\)，纯 incidence 解释不再成立。

## 九、代数与数值核验

### 9.1 中心差分核验

取

\[
c_L=0.4,\quad c_H=0.6,\quad r=0.2,\quad
\omega=0.55,\quad b_L=b_H=1.
\]

解析导数为

\[
\frac{\partial(y_L,y_H)}{\partial\omega}
=(0.69444444,-1.04166667),
\]

中心差分步长 \(10^{-6}\) 得到完全相同的八位小数结果。总收入导数为

\[
-0.34722222
=
\frac{c_Ly_L(c_L-c_H)}D,
\]

也与中心差分一致。

另外使用固定随机种子 20260714，在允许参数域内抽取 10,000 组
\((c_L,c_H,r,\omega,b_L,b_H)\)。所有抽样均满足 \(D>0\)、
\(y_L>0\) 和 \(y_H>0\)；式（6）与式（7）相对中心差分的最大绝对
误差为 \(6.93\times10^{-8}\)，未发现符号或闭式解违例。

### 9.2 平台化的三种全国结果

令 \(r=0.2\)、\(b_L=b_H=1\)，并把 \(\omega\) 从 \(0.7\) 降至 \(0.4\)。

| \((c_L,c_H)\) | \((y_L,y_H)\) at \(\omega=0.7\) | \((y_L,y_H)\) at \(\omega=0.4\) | 全国总收入变化 |
|---|---:|---:|---:|
| \((0.5,0.5)\) | \((1.8667,2.1333)\) | \((1.5556,2.4444)\) | \(4.0000\to4.0000\) |
| \((0.4,0.6)\) | \((1.7778,2.3333)\) | \((1.5686,2.6471)\) | \(4.1111\to4.2157\) |
| \((0.6,0.4)\) | \((2.0000,2.0000)\) | \((1.5574,2.2951)\) | \(4.0000\to3.8525\) |

三行都出现 \(L\) 下降和 \(H\) 上升；全国总收入分别不变、提高和下降，与 Proposition 1 完全一致。

### 9.3 相同 \(\omega\) 但不同回流网络

取

\[
c_L=0.6,\quad c_H=0.4,\quad \omega=0.5,\quad b_L=b_H=1.
\]

| \(r\) | \(D\) | \(y_L\) | \(y_H\) | \(y_L+y_H\) |
|---:|---:|---:|---:|---:|
| \(0\) | \(0.4200\) | \(1.4286\) | \(2.3810\) | \(3.8095\) |
| \(0.3\) | \(0.4680\) | \(1.7949\) | \(2.1368\) | \(3.9316\) |

两组经济有完全相同的 \(L\) 地标量留值率 \(\omega\)，但均衡不同。这直接证明 \(L\) 的 \(\omega\) 不是两地区结果的充分统计量。

### 9.4 双向 access–capture threshold 核验

取

\[
\alpha=0.3,\quad\beta=0.4,\quad d=0.3,\quad
q=0.25,\quad r=0.10,\quad B_L=1,\quad B_H=2,
\]

\[
q'=0.05,\qquad r'=0.02.
\]

式（19）给出

\[
(Y_L,Y_H)=(3.20987654,6.79012346),
\qquad
Y_L+Y_H=10=\frac{B_L+B_H}{d}.
\]

式（21）给出

\[
\left(\frac{dY_L}{dz},\frac{dY_H}{dz}\right)
=(-0.01828989,0.01828989).
\]

令 \(q(z)=q+q'z\)、\(r(z)=r+r'z\)，使用步长 \(10^{-6}\) 的中心
差分得到 \((-0.01828989,0.01828990)\)，与解析式一致。该例中
\(q'Y_L>r'Y_H\)，所以 headquarters capture 超过 outward access，
全国总收入不变但收入从 \(L\) 转向 \(H\)。

进一步在 \(\alpha+\beta<1\)、\(q,r\in[0,1]\) 的参数域内使用同一
固定随机种子抽取 10,000 组参数。式（21）与中心差分的最大绝对误差
为 \(1.13\times10^{-8}\)，式（20）的最大绝对误差为
\(2.85\times10^{-14}\)，没有出现正性或分母违例。

## 十、哪些是标准结果，哪些是待检验的增量

| 内容 | 性质 | 是否可以单独主张创新 |
|---|---|---|
| \(\mathbf y=(I-\Gamma C)^{-1}\mathbf b\) | 标准 Leontief/SAM/MRIO fixed point | 否 |
| 谱半径小于一时存在唯一解 | 标准非负矩阵结果 | 否 |
| Neumann series 表示多轮支出路径 | 标准 multiplier 解释 | 否 |
| 固定零和收入转移经网络放大 | 标准 network incidence | 否 |
| 列随机矩阵与相同 \(c\) 下全国总 multiplier 不变 | 标准加总恒等式 | 否 |
| CES 降价内生提高平台份额 | 标准 CES demand | 否 |
| 渠道替代内生改变价值归属矩阵的特定一列 | 平台化与 spatial incidence 的结合 | 可能，但需查重 |
| 平台化使全国总收入不变或提高时外围收入下降、总部收入提高 | 联合结构的解析符号结果 | 可能，但仍可被视为矩阵 comparative statics |
| 租金地方化在价格和份额不变时改变两地收入及其反馈 | 平台所有权与空间归属的机制关闭 | 可能，需与 ownership 和 regional multiplier 文献逐式比较 |
| 同一 \(\omega_L\) 因回流列不同而产生不同均衡 | 反对标量 sufficient-statistic 的明确结果 | 有用的理论边界，但不足以单独支撑论文 |
| \(r'Y_H\) 与 \(q'Y_L\) 的 access–capture threshold | 双向收入归属矩阵的 \(2\times2\) comparative static | 比标量模型更贴合原项目，但仍需排除 MRIO/SAM 先例 |

## 十一、可行性判定与推荐

### 11.1 可行性判定

这个最小模型满足本次测试的三项目标：

1. **全国总收入不变或提高，同时 multiplier 从 \(L\) 转向 \(H\)：通过。**
2. **租金地方化在价格和渠道份额不变时改变地区收入：通过。**
3. **加入 \(H\to L\) 回流后的网络反馈：通过。**
4. **共同 \(\alpha,\beta\) 下的 \(r'Y_H\) 对 \(q'Y_L\) 阈值：通过。**

它也证明当前标量 \(\omega\) 不是两地区均衡的充分统计量。但它没有自动解决创新性问题，因为固定点和矩阵传播仍属于标准 Leontief/SAM/MRIO。

### 11.2 推荐的最小恢复机制

若决定修改 Economics Letters 模型，推荐只恢复以下结构，不加入 full GE：

1. 保留当前 CES 渠道选择，使 \(z\to s(z)\)；
2. 优先考虑式（17）的 \(\Pi[q(z),r(z)]\)，同时表示 HQ capture 与
   outward access，而不是只把 \(\omega\) 改名为矩阵元素；
3. 保留 \(H\to L\) 回流状态 \(rY_H\)，使空间网络不能被外围地区单独闭合；
4. 加入租金归属参数 \(\lambda\)，构造价格和渠道份额不变的 incidence counterfactual；
5. 将正文主结果改为 multiplier 的空间转移和全国—地方符号分离，而不是再次强调重复漏出本身。

不建议同时加入企业区位、税收预算、平台最优收费、迁移或住房。那些机制会迅速超过 Letter 的篇幅，也不能自动使一个标准矩阵 fixed point 变成新理论。

### 11.3 下一道停止规则

在修改正式稿前，应先完成 Type-II/SAM/Miyazawa、regional ownership multiplier、MRIO、platform rent incidence 以及 headquarters concentration 文献的 equation-level comparison。若相邻文献已经包含“内生渠道份额改变收入归属矩阵，并推出全国 multiplier 不变或上升但外围 multiplier 下降”的同一命题，则该两地区扩展不能承担独立 Economics Letters 贡献。

## 十二、文件边界

本次仅新增这份 feasibility note。没有修改 main.tex、appendix.tex、references.bib、verify_model.py 或 output/paper.pdf。
