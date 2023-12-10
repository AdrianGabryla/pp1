import re
def f(first_letter, last_letter):
    x = open("data.txt", "r", encoding="utf8")
    f = x.read()
    words = re.findall("^{first_letter}.{last_letter}&", f)
    x.close()
    return words

if __name__=="__main__":
    print(f("w","d"))