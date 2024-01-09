def f(vname):
    import re
    x = re.search("^[a-zA-Z_][a-zA-Z0-9_]{0,4}$", vname)
    if x:
        return True
    return False

if __name__=="__main__":
    print(f("abc"))
    print(f("Abc"))
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))
    print(f("_4x"))
