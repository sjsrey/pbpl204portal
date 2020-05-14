"""
This is the analytic module for the portal project
I am planning on adding these:
1.Gini coefficients through inequality in pysal.explore
2.Location Quotient
3. Regional Diversification Index HHI
4. Economic base multiplier
5. basic employment

"""
version= '0.0.1'

import inequality 

import numpy as np

def hhi(e):
    """
    HHI Index
    """
    e=np.asarray(e)
    s = 100 * e / e.sum()

    s = np.rint(s).astype('i')

    return (s**2).sum()


def lq(region, base):
    """
    Location Quotient
    """
    region=np.asarray(region)
    base=np.asarray(base)
    Pi = base/base.sum()
    pi = region/region.sum()
    return pi/Pi

def basic(region, base):
    """
    Basic Employment
    """
    region=np.asarray(region)
    base=np.asarray(base)
    lq_est = lq(region, base)
    return (lq_est>1)*1 * region


def eb_multiplier(region, base):
    """
    Economic Base Multiplier
    """
    region=np.asarray(region)
    base=np.asarray(base)
    b = basic(region, base)
    T = region.sum()
    return T/b.sum()

def gini(x):
    """
    Memory efficient calculation of Gini coefficient in relative mean difference form
    Parameters
    ----------
    x:array-like

    Attributes
    ------------
    g:float
      Gini Coefficient
    
    Notes
    ----------
    Based on Sergio J. rey <srey@asu.edu>
    """
    return inequality.gini.Gini(x)
    
