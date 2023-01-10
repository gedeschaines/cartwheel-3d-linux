#ifndef TYPENAME_H
#define TYPENAME_H

/** Reference:
 *  https://stackoverflow.com/questions/281818/unmangling-the-result-of-stdtype-infoname
 */

#include <Utils/UtilsDll.h>
#include <typeinfo>

const char * demangle(const char* name);

template <class T>
const char * classType(const T& t) {

    return demangle(typeid(t).name());
}

#endif

