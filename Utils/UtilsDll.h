#pragma once

// Reference: https://gcc.gnu.org/wiki/Visibility

#ifndef UTILS_DECLSPEC
  #if defined _WIN32 || defined __CYGWIN__
	#ifdef UTILS_EXPORTS
		#define UTILS_DECLSPEC    __declspec(dllexport)
		#define UTILS_TEMPLATE(x) template class __declspec(dllexport) x;
	#else
		#define UTILS_DECLSPEC    __declspec(dllimport)
		#define UTILS_TEMPLATE(x) extern template class __declspec(dllimport) x;
	#endif
  #else
    #if (__GNUC__ >= 4) || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4)
      #ifdef UTILS_EXPORTS
        //#define UTILS_DECLSPEC __attribute__ ((visibility ("default")))
		//#define UTILS_TEMPLATE(x) template class __attribute__ ((visibility ("default"))) x;
        #define UTILS_DECLSPEC
	    #define UTILS_TEMPLATE(x) template class x;
	  #else
        //#define UTILS_DECLSPEC __attribute__ ((visibility ("default")))
		//#define UTILS_TEMPLATE(x) extern template class __attribute__ ((visibility ("default"))) x;
        #define UTILS_DECLSPEC
	    #define UTILS_TEMPLATE(x) extern template class x;
	  #endif
	#else
	  #define UTILS_DECLSPEC
	  #define UTILS_TEMPLATE(x) template class x;
	#endif
  #endif
#endif

#include <Utils/UtilsTemplates.h>
