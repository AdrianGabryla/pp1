def num_of_words(text):
    spaces = 0
    for i in text:
        if i == " ":
            spaces += 1
    return spaces+1
def orderd(text):
    text = text.split()
    for j in range(len(text)-1):
        for i in range(len(text)-j-1):
            if len(text[i+1]) > len(text[i]):
                text[i+1], text[i] = text[i], text[i+1]
    return text
def alphabet(text):
    text = text.split()
    text = sorted(text)
    return text

if __name__=="__main__":
    print(num_of_words("An apple a day keeps the doctor away"))
    print(orderd("An apple a day keeps the doctor away"))
    print(alphabet("An apple a day keeps the doctor away"))