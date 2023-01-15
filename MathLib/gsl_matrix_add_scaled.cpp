#ifdef USE_SYSTEM_GSL
#include "gsl_matrix_add_scaled.h"
#include <gsl/gsl_errno.h>

// The function gsl_matrix_add_scaled does not exist in standard GSL, so we
// need to add it herein.
int gsl_matrix_add_scaled(gsl_matrix * a, const gsl_matrix * b, double scaleA, double scaleB)
{
    const size_t M = a->size1;
    const size_t N = a->size2;

    if (b->size1 != M || b->size2 != N)
    {
        GSL_ERROR ("matrices must have same dimensions", GSL_EBADLEN);
    }
    else 
    {
        const size_t tda_a = a->tda;
        const size_t tda_b = b->tda;

        size_t i, j;

        for (i = 0; i < M; i++)
        {
            for (j = 0; j < N; j++)
            {
                a->data[i * tda_a + j] = scaleA * a->data[i * tda_a + j] +scaleB * b->data[i * tda_b + j];
            }
        }      
        return GSL_SUCCESS;
    }
}

#endif // USE_SYSTEM_GSL

