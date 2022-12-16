import mpmath as math
# rd = 2 
# g = 1/mpmath.sqrt(1+(3*rd*0.0057565**2)/(3.1415926**2))
# e = 1/(1+10**(-g * mpmath.sqrt((80)**2)+(150)**2)*(1400-1500)/400)
# print(e)
#
ri = 1400
rdi = 80
rj = 1500
rdj = 150

g = 1/math.sqrt(1+(3*(0.0057565**2)*(rdi**2))/(3.1415926**2))
print(g)
e0 = -g * (math.sqrt((rdi)**2)+(rdj)**2)*(ri-rj)/400
print(e0)
e1 = 1+10**e0
print(e1)
e2 = 1/e1
print(e2)