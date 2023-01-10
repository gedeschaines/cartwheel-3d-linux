#pragma once

// Reference: https://gcc.gnu.org/wiki/Visibility

#ifndef MATHLIB_DECLSPEC
  #if defined _WIN32 || defined __CYGWIN__
	#ifdef MATHLIB_EXPORTS
		#define MATHLIB_DECLSPEC    __declspec(dllexport)
		#define MATHLIB_TEMPLATE(x) template class __declspec(dllexport) x;
	#else
		#define MATHLIB_DECLSPEC    __declspec(dllimport)
		#define MATHLIB_TEMPLATE(x) template class __declspec(dllimport) x;
	#endif
  #else
    #if (__GNUC__ >= 4) || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4)
      #ifdef MATHLIB_EXPORTS
        //#define MATHLIB_DECLSPEC __attribute__ ((visibility ("default")))
		//#define MATHLIB_TEMPLATE(x) template class __attribute__ ((visibility ("default"))) x;
        #define MATHLIB_DECLSPEC
	    #define MATHLIB_TEMPLATE(x) template class x;
	  #else
        //#define MATHLIB_DECLSPEC __attribute__ ((visibility ("default")))
		//#define MATHLIB_TEMPLATE(x) extern template class __attribute__ ((visibility ("default"))) x;
        #define MATHLIB_DECLSPEC
        #define MATHLIB_TEMPLATE(x) extern template class x;
	  #endif
	#else
	  #define MATHLIB_DECLSPEC
	  #define MATHLIB_TEMPLATE(x) template class x;
	#endif
  #endif
#endif
