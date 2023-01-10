#include "TypeName.h"

/** Reference:
 *  https://stackoverflow.com/questions/281818/unmangling-the-result-of-stdtype-infoname
 */

#ifdef _MSC_VER
// do nothing
const char* demangle(const char* name) {
    return name;
}

#else
// invoke cxxabi demangle
#include <cxxabi.h>
const char* demangle(const char* name) {
    char buf[1024];
    unsigned int size = 1024;
    int status;

    char* res = abi::__cxa_demangle(name, buf, (size_t *)&size, &status);

    return (const char *)res;
}
#endif

