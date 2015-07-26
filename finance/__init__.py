from __future__ import division
from collections import namedtuple

version_info = namedtuple("version_info", ["major", "minor", "patch"])
version = version_info(0, 0, 1)

__title__ = "finance-helper"
__author__ = "Evan Briones"
__copyright__ = "Copyright 2015 Evan Briones"
__license__ = "BSD LICENSE"
__version__ = "{0.major}.{0.minor}.{0.patch}".format(version)


def PV(rate, period, pmt=None, FV=None):
    '''
    Returns the present value given either the payment or future value.
    '''
    if FV:
        return -FV / (1 + rate) ** period
    elif pmt:
        return (-pmt * sum([(1.0 + rate) ** i for i in range(period)])
                / (1 + rate) ** period)

def FV(rate, period, pmt=None, PV=None):
    '''
    Returns the future value given either the payment or present value.
    '''
    if PV:
        return -PV * (1 + rate) ** period
    elif pmt:
        return (-pmt * sum([(1.0 + rate) ** i for i in range(period)]))

def PMT(rate, period, PV=None, FV=None):
    '''
    Returns the payment given either the present value or future value.
    '''
    if PV:
        return ((-PV * (1 + rate) ** period) /
                sum([(1.0 + rate) ** i for i in range(period)]))
    elif FV:
        return -FV / sum([(1.0 + rate) ** i for i in range(period)])

def NPV(rate, values=None):
    '''
    Returns the NPV of a given set of values.
    '''
    return sum(PV(rate, year, FV=value) for (year, value)
            in enumerate(values, start=1))

def NFV(rate, values=None):
    '''
    Returns the NFV of a given set of values.
    '''
    return sum(FV(rate, year, PV=value) for (year, value)
            in enumerate(reversed(values), start=1))

def IRR(values, guess=None):
    '''
    Return the internal rate of return.
    '''

def EAR(rate):
    '''
    Returns the effective annual rate.
    '''
    return _ER(rate, 12)

def EADR(rate):
    '''
    Returns the effective annaul rate given daily rates.
    '''
    return _ER(rate, 365)

def _ER(rate, period):
    '''
    Returns the effective rate given the desired period.
    '''
    return (1 + rate / period) ** period - 1
