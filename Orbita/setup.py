# Fichero para la creacion del objeto Compartido 

from distutils.core import setup , Extension
from Cython.Build import cythonize

exts = (cythonize ("cy_orb.pyx"))

setup(ext_modules=exts)
