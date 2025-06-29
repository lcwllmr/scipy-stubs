from _typeshed import Incomplete
from collections.abc import Callable
from typing import Final

import numpy as np
import optype.numpy as onp

###

__f2py_numpy_version__: Final[str] = ...  # undocumented

# NOTE: The callables below cannot be annotated as functions because of stubtest limitations.

###
# level 1

# (x, [n, offx, incx]) -> s
sasum: Final[Callable[..., Incomplete]] = ...
dasum: Final[Callable[..., Incomplete]] = ...
scasum: Final[Callable[..., Incomplete]] = ...
dzasum: Final[Callable[..., Incomplete]] = ...

# (x, [n, offx, incx]) -> k
isamax: Final[Callable[..., Incomplete]] = ...
idamax: Final[Callable[..., Incomplete]] = ...
icamax: Final[Callable[..., Incomplete]] = ...
izamax: Final[Callable[..., Incomplete]] = ...

# (x, [n, offx, incx]) -> n2
snrm2: Final[Callable[..., Incomplete]] = ...
dnrm2: Final[Callable[..., Incomplete]] = ...
scnrm2: Final[Callable[..., Incomplete]] = ...
dznrm2: Final[Callable[..., Incomplete]] = ...

# (x, y, [n, offx, incx, offy, incy]) -> xy
sdot: Final[Callable[..., Incomplete]] = ...
ddot: Final[Callable[..., Incomplete]] = ...
cdotc: Final[Callable[..., Incomplete]] = ...
zdotc: Final[Callable[..., Incomplete]] = ...
cdotu: Final[Callable[..., Incomplete]] = ...
zdotu: Final[Callable[..., Incomplete]] = ...

# (a, b) -> (c, s)
srotg: Final[Callable[[Incomplete, Incomplete], tuple[Incomplete, Incomplete]]] = ...
drotg: Final[Callable[[Incomplete, Incomplete], tuple[Incomplete, Incomplete]]] = ...
crotg: Final[Callable[[Incomplete, Incomplete], tuple[Incomplete, Incomplete]]] = ...
zrotg: Final[Callable[[Incomplete, Incomplete], tuple[Incomplete, Incomplete]]] = ...

# (d1, d2, x1, y1) -> param
srotmg: Final[Callable[[Incomplete, Incomplete, Incomplete, Incomplete], onp.ArrayND[np.float32]]] = ...
drotmg: Final[Callable[[Incomplete, Incomplete, Incomplete, Incomplete], onp.ArrayND[np.float64]]] = ...

# (x, y, param, [n, offx, incx, offy, incy, overwrite_x, overwrite_y]) -> (x, y)
srotm: Final[Callable[..., tuple[onp.ArrayND[np.float32], onp.ArrayND[np.float32]]]] = ...
drotm: Final[Callable[..., tuple[onp.ArrayND[np.float64], onp.ArrayND[np.float64]]]] = ...

# (x, y, c, s, [n, offx, incx, offy, incy, overwrite_x, overwrite_y]) -> (x, y)
srot: Final[Callable[..., tuple[onp.ArrayND[np.float32], onp.ArrayND[np.float32]]]] = ...
drot: Final[Callable[..., tuple[onp.ArrayND[np.float64], onp.ArrayND[np.float64]]]] = ...
csrot: Final[Callable[..., tuple[onp.ArrayND[np.complex64], onp.ArrayND[np.complex64]]]] = ...
zdrot: Final[Callable[..., tuple[onp.ArrayND[np.complex128], onp.ArrayND[np.complex128]]]] = ...

# (x, y, [n, offx, incx, offy, incy]) -> (x, y)
sswap: Final[Callable[..., tuple[onp.ArrayND[np.float32], onp.ArrayND[np.float32]]]] = ...
dswap: Final[Callable[..., tuple[onp.ArrayND[np.float64], onp.ArrayND[np.float64]]]] = ...
cswap: Final[Callable[..., tuple[onp.ArrayND[np.complex64], onp.ArrayND[np.complex64]]]] = ...
zswap: Final[Callable[..., tuple[onp.ArrayND[np.complex128], onp.ArrayND[np.complex128]]]] = ...

# (a, x, [n, offx, incx]) -> x
sscal: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dscal: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cscal: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zscal: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (a, x, [n, offx, incx, overwrite_x]) -> x
csscal: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zdscal: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (x, y, [n, offx, incx, offy, incy]) -> y
scopy: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dcopy: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ccopy: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zcopy: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (x, y, [n, a, offx, incx, offy, incy]) -> z
saxpy: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
daxpy: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
caxpy: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zaxpy: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

###
# level 2

# (a, x, [offx, incx, lower, trans, diag, overwrite_x]) -> x
strmv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dtrmv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ctrmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztrmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (a, x, [incx, offx, lower, trans, diag, overwrite_x]) -> xout
strsv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dtrsv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ctrsv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztrsv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, a, x, [beta, y, offx, incx, offy, incy, trans, overwrite_y]) -> y
sgemv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dgemv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cgemv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zgemv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
ssymv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsymv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
chemv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zhemv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, x, [lower, incx, offx, n, a, overwrite_a]) -> a
ssyr: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsyr: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
csyr: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zsyr: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
cher: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zher: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (k, a, x, [incx, offx, lower, trans, diag, overwrite_x]) -> xout
stbsv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...  # undocumented
dtbsv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...  # undocumented
ctbsv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztbsv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (n, ap, x, [incx, offx, lower, trans, diag, overwrite_x]) -> xout
stpsv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dtpsv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ctpsv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztpsv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...  # undocumented

# (k, a, x, [incx, offx, lower, trans, diag, overwrite_x]) -> xout
stbmv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dtbmv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ctbmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztbmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (n, ap, x, [incx, offx, lower, trans, diag, overwrite_x]) -> xout
stpmv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...  # undocumented
dtpmv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...  # undocumented
ctpmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztpmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, x, y, [incx, incy, a, overwrite_x, overwrite_y, overwrite_a]) -> a
sger: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dger: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cgerc: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zgerc: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
cgeru: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zgeru: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, x, y, [lower, incx, offx, incy, offy, n, a, overwrite_a]) -> a
ssyr2: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsyr2: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cher2: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zher2: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (n, alpha, x, ap, [incx, offx, lower, overwrite_ap]) -> apu
sspr: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dspr: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cspr: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...  # undocumented
zspr: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...  # undocumented
chpr: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zhpr: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (n, alpha, x, y, ap, [incx, offx, incy, offy, lower, overwrite_ap]) -> apu
sspr2: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dspr2: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
chpr2: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zhpr2: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (k, alpha, a, x, [incx, offx, beta, y, incy, offy, lower, overwrite_y]) -> yout
ssbmv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsbmv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
chbmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zhbmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (m, n, kl, ku, alpha, a, x, [incx, offx, beta, y, incy, offy, trans, overwrite_y]) -> yout
sgbmv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dgbmv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cgbmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zgbmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (n, alpha, ap, x, [incx, offx, beta, y, incy, offy, lower, overwrite_y]) -> yout
sspmv: Final[Callable[..., onp.ArrayND[np.float32]]] = ...  # undocumented
dspmv: Final[Callable[..., onp.ArrayND[np.float64]]] = ...  # undocumented
cspmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...  # undocumented
zspmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...  # undocumented
chpmv: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zhpmv: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

###
# level 3

# (alpha, a, [beta, c, trans, lower, overwrite_c]) -> c
ssyrk: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsyrk: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
csyrk: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zsyrk: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
cherk: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zherk: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, a, b, [beta, c, trans, lower, overwrite_c]) -> c
ssyr2k: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsyr2k: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
csyr2k: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zsyr2k: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
cher2k: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zher2k: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, a, b, [beta, c, side, lower, overwrite_c]) -> c
ssymm: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dsymm: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
csymm: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zsymm: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
chemm: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zhemm: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, a, b, [beta, c, trans_a, trans_b, overwrite_c]) -> c
sgemm: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dgemm: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
cgemm: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
zgemm: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, a, b, [side, lower, trans_a, diag, overwrite_b]) -> b
strmm: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dtrmm: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ctrmm: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztrmm: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...

# (alpha, a, b, [side, lower, trans_a, diag, overwrite_b]) -> x
strsm: Final[Callable[..., onp.ArrayND[np.float32]]] = ...
dtrsm: Final[Callable[..., onp.ArrayND[np.float64]]] = ...
ctrsm: Final[Callable[..., onp.ArrayND[np.complex64]]] = ...
ztrsm: Final[Callable[..., onp.ArrayND[np.complex128]]] = ...
