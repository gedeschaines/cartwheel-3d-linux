#pragma once
#include <Python.h>

// This makes it possible to redirect printing (tprintf) to a Python function
UTILS_DECLSPEC
void registerPrintFunction(PyObject * printFunction);
