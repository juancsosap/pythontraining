import numpy as np


# Present Value
# Anual rate (4.5%) to month
rate = (4.5 / 100) / 12
# Number of periods (15 years) to month
nper = 15 * 12
# Monthly investment ($200) out of cash payment
pmt = -200
# Future Value ($150.000)
fv = 150_000
# When will be made the investment each Month
# 'begin' = 1 , 'end' = 0
when = 'begin'

# The result represent the initial amound that must be invested today to
# receive the FV ($150.000) expected after 15 years, with an investment
# of $200 at the begining of each month
pv = np.pv(rate, nper, pmt, fv, when)
print('PV: {pvv:,.2f}$'.format(pvv=pv))
# As it is an investment the result is negative (-$50.227,88)

# Present Value
# Anual rate (5%) to month
rate = (5 / 100) / 12
# Number of periods (10 years) to month
nper = 10 * 12
# Monthly investment ($100) out of cash payment
pmt = -100
# Future Value ($15.692,93)
fv = 15692.93
# When will be made the investment each Month
# 'begin' = 1 , 'end' = 0
when = 'end'

# The result represent the initial amound that must be invested today to
# receive the FV ($15.692,93) expected after 10 years, with an investment
# of $100 at the end of each month
pv = np.pv(rate, nper, pmt, fv, when)
print('PV: {pvv:,.2f}$'.format(pvv=pv))
# As it is an investment the result is negative (-$100)

# Future Value
# Anual rate (4.5%) to month
rate = (4.5 / 100) / 12
# Number of periods (15 years) to month
nper = 15 * 12
# Monthly investment ($200) out of cash payment
pmt = -200
# Present Value ($50.227,88)
pv = -50227.88
# When will be made the investment each Month
# 'begin' = 1 , 'end' = 0
when = 'begin'

# The result represent the future amound that will be receive after 15 years
# if today is invested the PV (-$50.000), with an investment of $200 at the
# begining of each month
fv = np.fv(rate, nper, pmt, pv, when)
print('FV: {fvv:,.2f}$'.format(fvv=fv))
# As it is an return of investment the result is positive ($149.553)

# Future Value
# Anual rate (5%) to month
rate = (5 / 100) / 12
# Number of periods (10 years) to month
nper = 10 * 12
# Monthly investment ($100) out of cash payment
pmt = -100
# Present Value ($100)
pv = -100
# When will be made the investment each Month
# 'begin' = 1 , 'end' = 0
when = 'end'

# The result represent the future amound that will be receive after 10 years
# if today is invested the PV (-$100), with an investment of $100 at the
# end of each month
fv = np.fv(rate, nper, pmt, pv, when)
print('FV: {fvv:,.2f}$'.format(fvv=fv))
# As it is an return of investment the result is positive ($15.692,93)

# Next Present Value
# Initial investment ($0) out of cash payment
inve = 0
# Discount rate (10%)
rate = 10 / 100
# Anual Cash Flows
cf_yr1 = -25_000
cf_yr2 = -10_000
cf_yr3 = 0
cf_yr4 = 10_000
cf_yr5 = 30_000
cf_yr6 = 100_000

# A positive result represent a good option to invest
npv = np.npv(rate, [inve, cf_yr1, cf_yr2, cf_yr3, cf_yr4, cf_yr5, cf_yr6])
print('NPV: {npvv:,.2f}$'.format(npvv=npv))

# Next Present Value
# Initial investment ($10.000) out of cash
inve = -10_000
# Discount rate (10%)
rate = 10 / 100
# Anual Cash Flows
cf_yr1 = 2_000
cf_yr2 = 2_000
cf_yr3 = 4_000
cf_yr4 = 4_000
cf_yr5 = 5_000

# A positive result represent a good option to invest
npv = np.npv(rate, [inve, cf_yr1, cf_yr2, cf_yr3, cf_yr4, cf_yr5])
print('NPV: {npvv:,.2f}$'.format(npvv=npv))

# Internal Return Rate
# Initial investment ($0) out of cash payment
inve = 0
# Anual Cash Flows
cf_yr1 = -25_000
cf_yr2 = -10_000
cf_yr3 = 0
cf_yr4 = 10_000
cf_yr5 = 30_000
cf_yr6 = 100_000

# The result represent the rate required to obtain a NPV of $0
# in the defined amount of years
irr = np.irr([inve, cf_yr1, cf_yr2, cf_yr3, cf_yr4, cf_yr5, cf_yr6])
print('IRR: {irrv:.2f}%'.format(irrv=(irr * 100)))

# Internal Return Rate
# Initial investment ($10.000) out of cash
inve = -10_000
# Anual Cash Flows
cf_yr1 = 2_000
cf_yr2 = 2_000
cf_yr3 = 4_000
cf_yr4 = 4_000
cf_yr5 = 5_000

# The result represent the rate required to obtain a NPV of $0
# in the defined amount of years
irr = np.irr([inve, cf_yr1, cf_yr2, cf_yr3, cf_yr4, cf_yr5])
print('IRR: {irrv:.2f}%'.format(irrv=(irr * 100)))
