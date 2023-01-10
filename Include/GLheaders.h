#ifdef __linux__
  #include <GL/glu.h>
  #include <GL/gl.h>
#else
  #define WIN32_LEAN_AND_MEAN
  #include <windows.h>		// The windows header file needs to be here...
  #include <gl/gl.h>		// Header file for The OpenGL32 library
  #include <gl/glu.h>		// Header file for the GLu32 library
#endif

