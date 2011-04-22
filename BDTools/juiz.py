#!/usr/bin/env python
# Copyright (C) 2008 Instituto Nokia de Tecnologia. All rights reserved.
# Contact: Ian Lawrence root@ianlawrence.info
#
# This software, including documentation, is protected by copyright
# controlled by Instituto Nokia de Tecnologia. All rights are reserved.
# Copying, including reproducing, storing, adapting or translating, any
# or all of this material requires the prior written consent of
# Instituto Nokia de Tecnologia. This material also contains
# confidential information which may not be disclosed to others without
# the prior written consent of Instituto Nokia de Tecnologia.
#
#===========================================================================


'''
A set of functions for quick analysis of an investment 
opportunity and a series of projected cashflows.

For further details and pros/cons of each function please refer
to the respective wikipedia page:

    payback_period 
        http://en.wikipedia.org/wiki/Payback_period
    
    net present value 
        http://en.wikipedia.org/wiki/Net_present_value
        
    internal rate of return
        http://en.wikipedia.org/wiki/Internal_rate_of_return
        
    efficiency of investment
        net present value/cost -> the return to be expected per unit of investment
        
Works according to http://www.datadynamica.com/irr.asp

'''

import sys, locale

def payback_of_investment(investment, cashflows):
    """The payback period refers to the length of time required 
       for an investment to have its initial cost recovered.
       
       >>> payback_of_investment(200.0, [60.0, 60.0, 70.0, 90.0])
       3.1111111111111112
    """
    total, years, cumulative = 0.0, 0, []
    if not cashflows or (sum(cashflows) < investment):
        raise Exception("insufficient cashflows")
    for cashflow in cashflows:
        total += cashflow
        if total < investment:
            years += 1
        cumulative.append(total)
    A = years
    B = investment - cumulative[years-1]
    C = cumulative[years] - cumulative[years-1]
    return A + (B/C)

def payback(cashflows):
    """The payback period refers to the length of time required
       for an investment to have its initial cost recovered.
       
       (This version accepts a list of cashflows)
       
       >>> payback([-200.0, 60.0, 60.0, 70.0, 90.0])
       3.1111111111111112
    """
    investment, cashflows = cashflows[0], cashflows[1:]
    if investment < 0 : investment = -investment
    return payback_of_investment(investment, cashflows)

def npv(rate, cashflows):
    """The total present value of a time series of cash flows.
    
        >>> npv(0.1, [-100.0, 60.0, 60.0, 60.0])
        49.211119459053322
    """
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate)**i
    return total

def irr(cashflows, iterations=100):
    """The IRR or Internal Rate of Return is the annualized effective 
       compounded return rate which can be earned on the invested 
       capital, i.e., the yield on the investment.
       
       >>> irr([-100.0, 60.0, 60.0, 60.0])
       0.36309653947517645

    """
    rate = 1.0
    investment = cashflows[0]
    for i in range(1, iterations+1):
        rate *= (1 - npv(rate, cashflows) / investment)
    return rate


# enable placing commas in thousands
locale.setlocale(locale.LC_ALL, "")
# convenience function to place commas in thousands
format = lambda x: locale.format('%d', x, True)

def investment_analysis(discount_rate, cashflows, resources):
    """Provides summary investment analysis on a list of cashflows
       and a discount_rate.
       
       Assumes that the first element of the list (i.e. at period 0) 
       is the initial investment with a negative float value."""
    
    NPV = npv(discount_rate, cashflows)
    #ts = [('year', 'cashflow')] + [(str(x), format(y)) for (x,y) in zip(
         #  range(len(cashflows)), cashflows)]
    IRR = (irr(cashflows) * 100)
    IE = (NPV/resources)
    return (IRR, NPV, IE)
           
        
    """print "-" * 70
    for y,c in ts:
        print y + (len(c) - len(y) + 1)*' ',
    print
    for y,c in ts:
        print c + ' ',
    print
    print
    print "Discount Rate: %.1f%%" % (discount_rate * 100)
    print "Remaining Expenses: %s" % resources 
    print
    #print "Payback: %.2f years" % payback(cashflows)
    print "    IRR: %.2f%%" % (irr(cashflows) * 100)
    print "    NPV: %s" % format(_npv)
    print "    IE: %s" % (_npv/resources)
    print 
    print "==> %s opportunity which has a one time fixed cost of %s" % (
        ("Approve this" if _npv > 0 else "Do Not Approve this"), format(-cashflows[0]))
    print "-" * 70"""

def main(inputs):
    """commandline entry point
    
    usage = '''Provides analysis of a business opportunity from a series of cashflows.
    
    usage: juiz WACC [cashflow0, cashflow1, ..., cashflowN] Remaining Expenses
        where 
            WACC is Weighted Average Cost of Capital
            cashflow0 is the investment amount (always a negative value)
            cashflow1 .. cashflowN values can be positive (net inflows)
                                                 or
                                                 negative (net outflows)
            Remaining Expenses is the capital which remains to be spent on the project
             
    for example:
        ./juiz.py 0.09 -849600 4332568.47 1299000"""
    
    
    try:
        rate, cashflows, resources = inputs[0], inputs[1:-1], inputs[-1]
        investment_analysis(float(rate), [float(c) for c in cashflows], float(resources))
    except IndexError:
        print usage
        sys.exit()

if __name__ == '__main__':
    debug = False
    if debug:
        import doctest
        doctest.testmod()
    else:
        main(sys.argv[1:])
