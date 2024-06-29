// mypow.c

#include <Python.h>

// 定义你的函数 mypow
int mypow(int x, int y) {
    return x * y;
}

// Python/C API 调用接口
static PyObject* wrap_mypow(PyObject* self, PyObject* args) {
    int x, y;

    // 解析 Python 传入的参数
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;  // 解析失败，返回错误
    }

    // 调用 C 函数并返回结果
    return PyLong_FromLong(mypow(x, y));
}

// 方法列表，将 Python 函数名与 C 函数绑定
static PyMethodDef MyPowMethods[] = {
    {"mypow", wrap_mypow, METH_VARARGS, "Calculate x * y"},
    {"__reduce__",
        (PyCFunction)arraydescr_reduce,
        METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}  // 结束标志
};

// 模块定义，初始化模块名和方法列表
static struct PyModuleDef mypowmodule = {
    PyModuleDef_HEAD_INIT,
    "mypow",   // 模块名
    NULL,      // 模块文档
    -1,        // 模块状态 -1 表示全局变量
    MyPowMethods  // 方法列表
};

// 模块初始化函数，Python 解释器会自动调用此函数
PyMODINIT_FUNC PyInit_mypow(void) {
    return PyModule_Create(&mypowmodule);
}
