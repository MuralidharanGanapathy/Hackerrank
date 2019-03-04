def swap_case(s):
    s = "".join(c.lower() if c.isupper() else c.upper() for c in s)
    return s

