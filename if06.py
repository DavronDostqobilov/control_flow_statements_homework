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
    d=3-x
    if x>d:
        return 'there are a lot of positive numbers'
    if x<d:
        return 'there are a lot of negative numbers'
print(main(12,-2,34))