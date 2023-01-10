#pragma once

// Reference: https://gcc.gnu.org/wiki/Visibility

#ifndef PHYSICS_DECLSPEC
  #if defined _WIN32 || defined __CYGWIN__
	#ifdef PHYSICS_EXPORTS
		#define PHYSICS_DECLSPEC    __declspec(dllexport)
		#define PHYSICS_TEMPLATE(x) template class __declspec(dllexport) x;
	#else
		#define PHYSICS_DECLSPEC    __declspec(dllimport)
		#define PHYSICS_TEMPLATE(x) template class __declspec(dllimport) x;
	#endif
  #else
    #if (__GNUC__ >= 4) || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4)
      #ifdef PHYSICS_EXPORTS
        //#define PHYSICS_DECLSPEC __attribute__ ((visibility ("default")))
		//#define PHYSICS_TEMPLATE(x) template class __attribute__ ((visibility ("default"))) x;
        #define PHYSICS_DECLSPEC
	    #define PHYSICS_TEMPLATE(x) template class x;
	  #else
        //#define PHYSICS_DECLSPEC __attribute__ ((visibility ("default")))
		//#define PHYSICS_TEMPLATE(x) extern template class __attribute__ ((visibility ("default"))) x;
        #define PHYSICS_DECLSPEC
	    #define PHYSICS_TEMPLATE(x) extern template class x;
	  #endif
	#else
	  #define PHYSICS_DECLSPEC
	  #define PHYSICS_TEMPLATE(x) template class x;
	#endif
  #endif
#endif
