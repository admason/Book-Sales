#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Stock analysis: Including Sales 
#  Note: Sales Forecast will be obtained by another code
#  Enter total stock, back orders and quantity in transit
# The output advises further action
# Total Stock:   ts
# Back Orders:   b
# In Transit:    t
# Forecast Sales:s


ts=100
b=0
t=110
s=200

net=ts-b-s
nt=net+t

if net<0 and nt<0:
    print(f" Forecasted post sales Net stock is {nt}, with {p} in transit, order at least {-1*nt}.")
elif net<0 and nt>=0:
    print(f" Stock okay, there are {t} copies due.")
else:
    print(f" Forecasted net stock of {net} , do not order.")


# In[ ]:




