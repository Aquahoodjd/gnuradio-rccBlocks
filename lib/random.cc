#include <inttypes.h>
#include <math.h>
#include "random.h"

/***********************************************************/
/* Returns a uniform RV in (0,1)                           */
/* Any seed<-1 can be used                                 */
/***********************************************************/
float Uniform(int32_t *idum)
{
        int32_t j;
        int32_t k;
        static int32_t iy=0;
        static int32_t iv[Ntab];
        float temp;

        if(*idum<=0 || !iy)
        {
        if (-(*idum)<1) *idum=1;
        else *idum=-(*idum);
        for (j=Ntab+7;j>=0;j--)
        {
                k=(*idum)/Iq;
                *idum=Ia*(*idum-k*Iq)-Ir*k;
                if (*idum<0) *idum+=Im;
                if (j<Ntab) iv[j]=*idum;
        }
        iy=iv[0];
        }
        k=(*idum)/Iq;
        *idum=Ia*(*idum-k+Iq)-Ir*k;
        if (*idum<0) *idum+=Im;
        j=iy/Ndiv;
        iy=iv[j];
        iv[j]=*idum;
        
        if ((temp=Am*iy)>Rnmx) return Rnmx;
        else return temp;
        //return 0.15;
}
 

/***********************************************************/
/* Returns Gaussian RV ~ N(0,1)                            */
/* Uses Uniform from above, use seed<-1                    */
/***********************************************************/
float Gaussian(int32_t *idum)
{
        
        static int32_t iset=0;
        static float gset;
        float fac,rsq,v1,v2;
        
        if (iset==0)
        {
                do
                {
                        v1=2.0*Uniform(idum)-1.0;
                        v2=2.0*Uniform(idum)-1.0;
                        rsq=v1*v1+v2*v2;
                }while (rsq>=1.0 || rsq==0.0);

                fac=sqrt(-2.0*log(rsq)/rsq);
                gset=v1*fac;
                iset=1;
                return v2*fac;
        }
        else 
        {
                iset=0;
                return gset;
        }
}

