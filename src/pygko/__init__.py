import cppyy
import os
import sys
from pathlib import Path

gko_path = Path(os.environ.get("GKO_ROOT"))
if not gko_path:
    print("[PyGKO] GKO_ROOT enviroment variable not set")
    sys.exit(-1)


gko_incl_path = gko_path / "include"
cppyy.add_include_path(gko_incl_path)
# TODO find gko version
# define GKO_VERSION_MAJOR 1
# define GKO_VERSION_MINOR 5
# define GKO_VERSION_PATCH 0

gko_major_version = 1
gko_minor_version = 5
gko_patch_version = 0

if os.exists(gko_incl_path / "ginkgo" / "ginkgo.hpp"):
    print("[PyGKO] found Ginkgo version {}{}{}".format(gko_major_version, gko_minor_version, gko_patch_version))

# cppyy.include('ginkgo/ginkgo.hpp')
# cppyy.load_library('libginkgo')
# from cppyy.gbl import gko
# from cppyy.gbl.std import ifstream

# omp = gko.OmpExecutor.create()
# csr = gko.matrix.Csr['double', 'int']
# A = gko.read[csr](ifstream("ginkgo/examples/simple-solver/data/A.mtx"), omp.__smartptr__())
# B = gko.share(cppyy.gbl.std.move(A.__smartptr__()))
# dense = gko.matrix.Dense['double']
# x = gko.read[dense](ifstream("ginkgo/examples/simple-solver/data/x0.mtx"), omp.__smartptr__())
# b = gko.read[dense](ifstream("ginkgo/examples/simple-solver/data/b.mtx"), omp.__smartptr__())
# iters = gko.stop.Iteration.build().with_max_iters(20).on(omp)
# iters_s = gko.share(cppyy.gbl.std.move(iters.__smartptr__()))
# solver_gen = gko.solver.Cg['double'].build().with_criteria(iters_s.__smartptr__()).on(omp)
# solver = solver_gen.generate(B.__smartptr__())
# solver.apply(b, x)
__version__ = '0.0.0'
try:
    from ._pygko import longest  # noqa
except ImportError:

    def longest(args):
        return max(args, key=len)
