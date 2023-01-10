#include <Python.h>
#include "Utils.h"
#include <assert.h>

/**
 * Register an external printFunction
 */
PyObject *printFunction = NULL;
void registerPrintFunction(PyObject *pF){
    Py_XINCREF(pF);             /* Add a reference to new callback */
    Py_XDECREF(printFunction);  /* Dispose of previous callback */
    printFunction = pF;         /* Remember new callback */
}


/**
 * Output the message to a file...
 */
int tvprintf(const char *format, va_list vl){
    static char message[1024];
    message[0] = '\0';

	vsprintf(message, format, vl);

	if ( printFunction == NULL ) {
		printf( "%s", message );
		return -1;
    }
	else {
        //printf( "%s", message );  // debug
		PyObject *arglist;
		PyObject *result;
		arglist = Py_BuildValue("(s)", message);
		result = PyEval_CallObject(printFunction, arglist);
		Py_DECREF(arglist);
		if (result == NULL) {
			// Unbind function
			registerPrintFunction(NULL);
			throwError( "The Python print function threw an exception!" );
		}
		Py_DECREF(result);
	}
    return 0;
}


/**
 * Output the message to a file...
 */
int tprintf(const char *format, ...){
    int result;
    va_list vl;

    if ( format == NULL || strlen(format) < 1 ) {
        throwError( "tprintf: Missing format." );
        return -1;
    }

	va_start(vl, format);
	result = tvprintf(format, vl);
	va_end(vl);

	return result;
}


/**
 * Test tprintf...
 */
void test() {
    int result;
    const char* fmt1 = "test:  fmt1 \"%s\"  s \"%s\"  d %d  lf %lf\n";
    const char* sfmt1 = "test:  fmt1 \"%s\"  s \"%s\"  d %d  lf %lf\\n";

    const char* fmt2 = "test:  fmt2 \"%s\"  %.*s\n";
    const char* sfmt2 = "test:  fmt2 \"%s\" %.*s\\n";

    result = tprintf(fmt1, sfmt1, "one", int(1.0f), 1.0f);
    assert ((result == -1) || (result == 0));

    result = tprintf(fmt2, sfmt2, 6, "=========");
    assert ((result == -1) || (result == 0));
}
