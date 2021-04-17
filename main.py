# Work with Python long enough, and eventually you will encounter `*args` and `**kwargs`. These strange terms show up as parameters in function definitions. What do they do? Let's review a simple function:
def myfunc(a,b):
    return sum((a,b))*.05

print(myfunc(40,60))
# This function returns 5% of the sum of **a** and **b**. In this example, **a** and **b** are *positional* arguments; that is, 40 is assigned to **a** because it is the first argument, and 60 to **b**. Notice also that to work with multiple positional arguments in the `sum()` function we had to pass them in as a tuple.

# What if we want to work with more than two numbers? One way would be to assign a *lot* of parameters, and give each one a default value.
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

x=myfunc(40,60,20)
print(x)
# Obviously this is not a very efficient solution, and that's where `*args` comes in.

# ## `*args`

# When a function parameter starts with an asterisk, it allows for an *arbitrary number* of arguments, and the function takes them in as a tuple of values. Rewriting the above function: