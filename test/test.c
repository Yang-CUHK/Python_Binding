// test.c

#include <Python.h>

// Implementation of mypow function
int mypow(int x, int y) {
    int result = 1;
    for (int i = 0; i < y; ++i) {
        result *= x;
    }
    return result;
}

// Implementation of myadd function
int myadd(int x, int y) {
    return x + y;
}

// Python binding for mypow function
static PyObject* py_mypow(PyObject* self, PyObject* args) {
    int x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;
    }
    int result = mypow(x, y);
    return PyLong_FromLong(result);
}

// Python binding for myadd function
static PyObject* py_myadd(PyObject* self, PyObject* args) {
    int x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;
    }
    int result = myadd(x, y);
    return PyLong_FromLong(result);
}

// Method definitions table
static PyMethodDef test_methods[] = {
    {"mypow", py_mypow, METH_VARARGS, "Calculate x^y."},
    {"myadd", py_myadd, METH_VARARGS, "Calculate x + y."},
    {NULL, NULL, 0, NULL} // Sentinel to indicate end of methods
};

// Module definition
static struct PyModuleDef testmodule = {
    PyModuleDef_HEAD_INIT,
    "test",   // Module name
    NULL,     // Module documentation, may be NULL
    -1,       // Size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
    test_methods
};

// Module initialization function
PyMODINIT_FUNC PyInit_test(void) {
    return PyModule_Create(&testmodule);
}
