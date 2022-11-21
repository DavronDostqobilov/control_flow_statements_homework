def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x=0
    if a>0:
        x+=1
    if b>0:
        x+=1
    if c>0:
        x+=1
    z=0
    if a<0:
        z+=1
    if b<0:
        z+=1
    if c<0:
        z+=1

    return z<x
j=main(12,-1,-23)
if j==True:
   print('there are a lot of positive numbers')
if j==False:
    print('there are a lot of negative numbers')