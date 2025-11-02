import numpy as np

G = 9.81

def period(L):
    L=np.asarray(L, dtype=float)
    return 2 *np.pi*np.sqrt(L / G)
def find_period(L0, L1):
    if not (isinstance(L0, int) and isinstance(L1, int)):
       raise TypeError("L0 ve L1 tamsayı olmalı.")
    if not (L1 > L0 > 0):
       raise ValueError("L1 > L0 > 0 olmalı.")
       Ls = np.arange(L0, L1 + 1, dtype=float)
       Ts = period(Ls)  
       for L, T in zip(Ls, Ts):
        print("When L = %5.1f m,  T = %4.1f s" % (L, T))
        return float(Ts[0]), float(Ts[-1]) 
