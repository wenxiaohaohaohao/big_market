# M1--M3 正式数学合同

日期：2026-07-17  
用途：在修改正式稿前冻结命题范围、必要假设、等号边界和不允许的外推。

## M1：有限冲击下的能力双阈值

设 (G=0)、(z_1>z_0)、(0<s_0<s_1<1) 且
(0<\mathcal P=P_{M1}/P_{M0}<1)。组织能力只改变平台交易的本地留值率，
不改变 (B_j)、(s_j) 或 (P_{Mj})。定义

\[
d_A=1-\beta-\alpha\rho_A>0,\qquad
\Delta(\kappa)=\Delta_0-\delta_\rho\kappa,
\]

\[
D_j(\kappa)=d_A+\alpha s_j\Delta(\kappa),\qquad
\mathcal D(\kappa)=\frac{D_1(\kappa)}{D_0(\kappa)}.
\]

由于

\[
\frac{\partial\ln\mathcal D}{\partial\kappa}
=-
\frac{\alpha\delta_\rho d_A(s_1-s_0)}
{D_1(\kappa)D_0(\kappa)}<0,
\]

(\mathcal D) 在 ([0,1]) 上连续且严格下降。若

\[
\mathcal D(0)>
q_R^F\equiv\frac{\mathcal B}{\mathcal P^\alpha}
>
q_Y^F\equiv\mathcal B
>
\mathcal D(1),
\]

则存在唯一且有序的 (0<\kappa_R^F<\kappa_Y^F<1)，其中

\[
\kappa(q)=\frac{1}{\delta_\rho}
\left[
\Delta_0-
\frac{(q-1)d_A}{\alpha(s_1-qs_0)}
\right].
\]

三个严格区间依次为：两种收入均下降、只有实际收入上升、两种收入均上升。
在 (\kappa_R^F) 处实际收入不变且名义收入下降；在
(\kappa_Y^F) 处名义收入不变且实际收入上升。该命题不要求全域
(\Delta(\kappa)>0)。

## M2：一般凹 share-speed 下的唯一峰值

主文采用可微且 homothetic 的两渠道需求。沿 integration path，平台支出份额
(s) 满足

\[
\frac{d\ln P_M}{dz}=-s,\qquad \frac{ds}{dz}=g(s),
\]

其中 (g\in C^2([0,1])) 与 (\kappa) 无关，并满足

\[
g(0)=g(1)=0,\qquad g(s)>0\ (s\in(0,1)),\qquad
g''(s)<0\ (s\in(0,1)).
\]

固定 (\Delta(\kappa)>0)，令 (b=\alpha\Delta(\kappa)) 并定义

\[
\Lambda_g(s,\kappa)=\frac{b g(s)}{d_A+bs}.
\]

一阶导数的符号由

\[
F(s,b)=g'(s)(d_A+bs)-bg(s)
\]

决定，且 (F_s=g''(s)(d_A+bs)<0)、(F(0,b)>0>F(1,b))。因此
(\Lambda_g) strictly single-peaked，并有唯一内部最大点 (s^*(\kappa))。
若 (g(s)=g(1-s))，则 (s^*<1/2)。此外

\[
\frac{\partial s^*}{\partial\kappa}
=-
\frac{\alpha\delta_\rho d_Ag(s^*)}
{g''(s^*)[d_A+bs^*]^2}>0,
\]

\[
\frac{\partial\Lambda_g^{\max}}{\partial\kappa}
=-
\frac{\alpha\delta_\rho d_Ag(s^*)}
{[d_A+bs^*]^2}<0.
\]

一般 (g) 不允许声称 (\Lambda_g) strictly concave。非对称 (g) 不允许声称峰值
低于 (1/2)。(\Delta=0) 时 (\Lambda_g\equiv0)，没有唯一峰值；
(\Delta<0) 时该 capture-drag 命题不适用。CES
(g(s)=(\eta-1)s(1-s)) 仅作为附录 specialization。

## M3：integration--capacity increasing differences

在 (G=0)、(s_z>0) 且 (P_M,B,s) 不受 (\kappa) 影响时，

\[
\frac{\partial^2\ln Y}{\partial z\,\partial\kappa}
=
\frac{\partial^2\ln R}{\partial z\,\partial\kappa}
=
\frac{\alpha\delta_\rho d_A s_z}{D^2}>0.
\]

该结论只表示 (\ln Y) 与 (\ln R) 对 integration 和 organizational capacity
具有 strict increasing differences。不得改写为 level-income 交叉偏导必为正，也不得在
没有 capacity-choice problem 的情况下声称最优 (\kappa^*(z)) 上升。
