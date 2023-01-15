#pragma once

#ifdef USE_SYSTEM_GSL
#include <gsl/gsl_matrix.h>

// The function gsl_matrix_add_scaled does not exist in standard GSL, so we
// need to add it herein.
int gsl_matrix_add_scaled(gsl_matrix * a, const gsl_matrix * b, double scaleA, double scaleB);

#endif // USE_SYSTEM_GSL

