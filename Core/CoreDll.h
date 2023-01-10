#pragma once

// Reference: https://gcc.gnu.org/wiki/Visibility

#ifndef CORE_DECLSPEC
  #if defined _WIN32 || defined __CYGWIN__
	#ifdef CORE_EXPORTS
		#define CORE_DECLSPEC    __declspec(dllexport)
		#define CORE_TEMPLATE(x) template class __declspec(dllexport) x;
	#else
		#define CORE_DECLSPEC    __declspec(dllimport)
		#define CORE_TEMPLATE(x) template class __declspec(dllimport) x;
	#endif
  #else
    #if (__GNUC__ >= 4) || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4)
      #ifdef CORE_EXPORTS
        //#define CORE_DECLSPEC __attribute__ ((visibility ("default")))
		//#define CORE_TEMPLATE(x) template class __attribute__ ((visibility ("default"))) x;
        #define CORE_DECLSPEC
	    #define CORE_TEMPLATE(x) template class x;
	  #else
        //#define CORE_DECLSPEC __attribute__ ((visibility ("default")))
		//#define CORE_TEMPLATE(x) extern template class __attribute__ ((visibility ("default"))) x;
        #define CORE_DECLSPEC
	    #define CORE_TEMPLATE(x) extern template class x;
	  #endif
	#else
	  #define CORE_DECLSPEC
	  #define CORE_TEMPLATE(x) template class x;
	#endif
  #endif
#endif
