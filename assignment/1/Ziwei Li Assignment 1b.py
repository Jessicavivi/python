# Ziwei Li Assignment 1B
b = float(input('Please enter the starting balance ($):'))
t = float(input('Enter the term (years):'))
r = float(input('Enter the interest rate (%):'))
f = float(input('Enter the compounding frequency (times/year):'))
E = b *(1 + 0.01*r/f) ** (f * t)
print('An initial investment of',b,',in',t,'years, at an interest rate of',r,',compounded at',f,' times per year, will be worth',E)







