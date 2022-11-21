def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    x=0
    if a>0:
        x+=1
    if b>0:
        x+=1
    if c>0:
        x+=1
    
    return x
print(main(12,23,-1)) 