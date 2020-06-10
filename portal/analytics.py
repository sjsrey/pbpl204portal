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

    HHI is an index of market concentration. In other words, a higher value of HHI points to more concentration or activity in a specific sector and lower diversification
    while a low value means lower concentration and more diversification. Measure based on the economy as a whole, not individual sectors.

    
    Parameters
    ----------
    e: array-like
       vector of n values, one for each sector. Can be employment, income, wages, profits

    Return
    ------------
    Returns index 

      
    
    Notes
    ----------
    Based on Sergio J. rey <srey@asu.edu>
    """
    e=np.asarray(e)
    s = 100 * e / e.sum()

    s = np.rint(s).astype('i')

    return (s**2).sum()


def lq(region, base):
    """
    Location Quotient
    
    a way of quantifying how concentrated a particular industry, cluster, occupation, or demographic group is in a region as compared to the nation. 
    It can reveal what makes a particular region “unique” in comparison to the national average.
    In more exact terms, location quotient is a ratio that compares a region to a larger reference region according to some characteristic or asset. 
    Suppose X is the amount of some asset in a region (e.g., manufacturing jobs), and Y is the total amount of assets of comparable types in the region (e.g., all jobs). 
    X/Y is then the regional “concentration” of that asset in the region. If X’ and Y’ are similar data points for some larger reference region (like a state or nation),
    then the LQ or relative concentration of that asset in the region compared to the nation is (X/Y) / (X’/Y’). 

    Parameters
    ----------
    region: array-like
            list of characteristics such as employment in various sectors
    region of interest Ex: CA

    base: array-like
          list of characteristics such as employment in various sectors
    base comparison Ex: US

    Returns:
    -----------
   location quotients for each characteristic of comparison

    location quotient coefficient or ratio of comparison    
    """
    region=np.asarray(region)
    base=np.asarray(base)
    Pi = base/base.sum()
    pi = region/region.sum()
    return pi/Pi

def basic(region, base):
    """
    Basic Employment
    
    Defines a sector as basic employment if its location coefficient is greater than 1, all employment in such a sector will be designated basic employment

    Parameters
    ----------
    region: array-like
            list of characteristics such as employment in various sectors
    base: array-like
          list of characteristics such as employment in various sectors

    Returns
    ----------
    basic: returns an estimate of the basic employment in sectors whose location quotients are greater than 1

    """
    region=np.asarray(region)
    base=np.asarray(base)
    lq_est = lq(region, base)
    return (lq_est>1)*1 * region


def eb_multiplier(region, base):
    """
    Economic Base Multiplier

     A measure that provides a rough estimate of how changes in basic employment will affect total employment in a given region
     Ratio of the total number of jobs created to the number of basic jobs created. 
     A higher economic base multiplier implies a larger effect of the basic job creator on the total number of jobs.

    Read more: http://www.businessdictionary.com/definition/economic-base-multiplier.html

    Parameters
    ----------
    region: array-like
            employment vector for the region of interest
    base: array-like
            base vector for the specific sector or job of interest

    Return:
 *   eb_multiplier: float, 
                    returns a value that represents how much employment is going to grow based on the base, usually greater than 1 suggesting one job will bring in x amount more jobs to the region.
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

