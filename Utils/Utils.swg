#ifndef SWIG_UTILS_SWG
#define SWIG_UTILS_SWG

%module(directors="1") Utils

%begin %{
// VC++ issues those warnings when compiling templates
#ifdef _MSC_VER
#pragma warning (disable : 4275 4251)
#endif
%}

%{
#include "Utils.h"
#include "RegisterPrintFunction.h"
#include "Observer.h"
#include "Observable.h"
%}

// SWIG compiler does not support VC++ declspec
#define CW_SWIG_INCLUDE
#define UTILS_DECLSPEC
#define UTILS_TEMPLATE(x)

%feature("director") Observer;
%include "std_vector.i"
%include "Utils.h"
%include "RegisterPrintFunction.h"
%include "Observer.h"
%include "Observable.h"

namespace std {
	%template(DynamicArrayDouble) DynamicArray<double>;
};

#endif // SWIG_UTILS_SWG
