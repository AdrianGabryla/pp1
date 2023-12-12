import re
def f(first_letter, last_letter):
    x = open("data.txt", "r", encoding="utf8")
    f = x.read()
    words = []
    for i in f.split():
        if i[0] == first_letter and i[-1] == last_letter:
            words.append(i)
        if i[-1] == "." or i[-1] == "," or i[-1] == '"':
            if i[0] == first_letter and i[-2] == last_letter:
                if "-" in i:
                    continue
                else:
                    words.append(i)
    x.close()
    return len(words)

if __name__=="__main__":
    print(f("w","d"))