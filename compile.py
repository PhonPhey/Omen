""" Compile module """


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("build.data_db", ["data_db.py"]),
    ]

setup(
    name = 'omen',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
