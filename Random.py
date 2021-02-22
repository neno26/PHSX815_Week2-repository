#! /usr/bin/env python
import math
import numpy as np

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed         #Creates class with variable seed
        self.m_v = np.uint64(4101842887655102017) #defines three numbers(vector) (one is orders 10^-9)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v  #Transformation relationships defines between the 3 numbers (vector)
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'): #Computer error control
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087)) #transformation relation
        self.m_v ^= self.m_v >> np.uint64(17) #bitwise manipulation of the contents of the 3 numbers (vectors)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8) #Overal bit shifting of 31-17-8 = 6 to the left
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
   # Bit wise operation. Creates 64 bit, multiplies it by itself (having checked to see that it's value hadn't overflown)
   # Add to that another 64 bit integer of size itself bitshifted by 32 to the right.
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21))) #creates variabe X of size number(vector) with an Exor btw bits
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4) #overal bit shifting of 231 to the right.
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w #returns transformed it according to relation above. 

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64() #"random number" generated mainly by int64 function..

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            return 1
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0

    # function returns a random double (0 to infty) according to an exponential distribution
    def Exponential(self, beta=1.):
      # make sure beta is consistent with an exponential
        if beta <= 0.:
            beta = 1.

        R = self.rand();

        while R <= 0.:
            R = self.rand()

        X = -math.log(R)/beta

        return X
    
      # function that returns a random double between (0,1) according to an geometric distribution
    def Geometric(self, p = 0.5):
        if p < 0. or p > 1.:
            return 1
            
        R = self.rand()
        X = math.log(R*(1-p)/p)/math.log(1-p)
        
        if p <= 0.5:
            while R > p:
                R = self.rand()
                y = self.int64()*10**-19
                RR= math.log(R*(1-p)/p)/math.log(1-p)
                YY= math.log(y*(1-p)/p)/math.log(1-p)
                if np.abs(RR) > np.abs(YY):                                         
                    return (1)
                else:
                    return (0)
        elif p > 0.5:
            while R < p:
                R  = 1-self.rand()
                RR = math.log(R*(1-p)/p)/math.log(1-p)
                Y  = np.abs(1-self.int64())*10**-19
                YY = math.log(Y*(1-p)/p)/math.log(1-p)
                if np.abs(YY) < np.abs(RR):
                    return (0)
                else:
                    return (1)
        return (1)