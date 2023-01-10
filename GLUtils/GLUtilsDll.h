#pragma once

// Reference: https://gcc.gnu.org/wiki/Visibility

#ifndef GLUTILS_DECLSPEC
  #if defined _WIN32 || defined __CYGWIN__
	#ifdef GLUTILS_EXPORTS
		#define GLUTILS_DECLSPEC    __declspec(dllexport)
		#define GLUTILS_TEMPLATE(x) template class __declspec(dllexport) x;
	#else
		#define GLUTILS_DECLSPEC    __declspec(dllimport)
		#define GLUTILS_TEMPLATE(x) template class __declspec(dllimport) x;
	#endif
  #else
    #if (__GNUC__ >= 4) || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4)
      #ifdef GLUTILS_EXPORTS
        //#define GLUTILS_DECLSPEC __attribute__ ((visibility ("default")))
		//#define GLUTILS_TEMPLATE(x) template class __attribute__ ((visibility ("default"))) x;
        #define GLUTILS_DECLSPEC
	    #define GLUTILS_TEMPLATE(x) template class x;
	  #else
        //#define GLUTILS_DECLSPEC __attribute__ ((visibility ("default")))
		//#define GLUTILS_TEMPLATE(x) extern template class __attribute__ ((visibility ("default"))) x;
        #define GLUTILS_DECLSPEC
	    #define GLUTILS_TEMPLATE(x) extern template class x;
	  #endif
	#else
	  #define GLUTILS_DECLSPEC
	  #define GLUTILS_TEMPLATE(x) template class x;
	#endif
  #endif
#endif
