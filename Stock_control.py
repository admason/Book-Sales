#!/usr/bin/env python
# coding: utf-8

# In[36]:


a=6
b=8
if a>b:
    a = a+2
    b = b+2
    print('The larger vale is a=', a)
else:
    a = a+2
    b = b+2
    print('The larger value is b=',b)


# In[38]:


if True:
    print("It's true")


# In[40]:


x=True

if x:
    print('x was true')
else:
##    print('x not true')


# In[118]:


## Stock analysis:
#  Enter total stock, back orders and quantity in transit
# The output advises further action

totalstock=10
backorder=50
transit=40

netstock=totalstock-backorder
net_plus_transit=totalstock-backorder+transit

if netstock<=0 and net_plus_transit<=0:
    print(f" Net stock is {netstock}, with {transit} in transit, order at least {-1*net_plus_transit}")
elif net<=0 and nt>=0:
    print(f" Stock okay, there are {transit} copies due")
else:
    print(f" stock level= {netstock}, but {transit} on the way, do not order")


# In[45]:


num=100
root=2
squareroot=(num)**(1/root)
sol=1
dp=50

print(f" The {dp} decimal point solution for the square root of {num!s} is : {squareroot:{sol}.{dp+3}}")


# In[87]:


## Stock analysis:
#  Enter total stock, back orders and quantity in transit
# The output advises further action

ts=1
b=20
p=5

net=ts-b
nt=ts-b+p

if net<0 and nt<0:
    print(f" Net stock is {net}, with {p} in transit, order at least {-1*nt}")
elif net<0 and nt>=0:
    print(f" Stock okay, there are {p} copies due")
else:
    print(f" {net} in stock, do not order")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




