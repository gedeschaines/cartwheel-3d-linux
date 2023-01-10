#include "MathLib/Vector3d.h"
#include <cstdio>

int main(int argc, char* argv[])
{
   Vector3d vecA = Vector3d(1.0, 2.0, 3.0);

   /* Test Vector3d element indexing.
   */
   printf("(vecA.x,  vecA.y,  vecA.z ) = (%lf, %lf, %lf)\n", vecA.x, vecA.y, vecA.z);
   printf("(vecA[0], vecA[1], vecA[2]) = (%lf, %lf, %lf)\n", vecA[0], vecA[1],vecA[2]);

   return 0;
}

