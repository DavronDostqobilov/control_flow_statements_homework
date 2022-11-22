def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x=a%10
    x1=a//10
    d=x*10+x1
    if a>=d:
        return True
    if a<d:
        return False
print(main(12)) 