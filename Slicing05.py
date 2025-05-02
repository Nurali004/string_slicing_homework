def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[n:-1]

s="whatareyoudoing"
n=int(input("sonni kiriting:"))
print(main(s,n))