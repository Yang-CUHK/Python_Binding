#include <pybind11/pybind11.h>
// 定义两个简单的函数
int mypow(int x, int y) {
    return x * y;
}

int myadd(int x, int y) {
    return x + y;
}

// main.cpp



namespace py = pybind11;

PYBIND11_MODULE(example, m) {
    m.def("mypow", &mypow, "Calculate x raised to the power of y");
    m.def("myadd", &myadd, "Calculate sum of x and y");
}
