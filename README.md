# Python_Binding

It now provide C mapping with Python/C or cython api, and C++ binding will Pybind11.

The The default parsing method is **Python/C API**.

To use it:
**python3 evaluate.py target**

If you want to use pybind 11:
**python3 evaluate.py -c pybind11 target**

If you want to use cython:
**python3 evaluate.py -c cython target**
**To use cython, you should download the cython package. pip install cython**

**The target can be file or folder.**
