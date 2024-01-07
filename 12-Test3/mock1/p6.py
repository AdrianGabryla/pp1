def f(vname):
    import re
    x = re.search("^[a-zA-z]|_.+[a-zA-z].?_", vname)
    if x:
        return True
    return False

if __name__=="__main__":
    print(f("abc"))
    print(f("abcdef"))
