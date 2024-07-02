def say_hello_to(name):
    print("Hello %s!" % name)

cdef extern from "./a.h":
    int test(int a)

cdef int myfunc(int var):
    return test(var)

def pyfun(v):
    return myfunc(v)