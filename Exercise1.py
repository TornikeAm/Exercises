class Exercise1:
    def __init__(self,words):
        self.words = open(words,'r')

    def count(self):
        word = {}
        for w in self.words:
            w=w.strip()
            if w in word:
                word[w] = word[w] +1
            else:
                word[w] = 1
        print(f" Number of distinct words: {len(word)}")

        for key,value in word.items():
            print(str(value),end= ' ')
        return ''

def create_input_txt():
    f = open('./Inputs.txt', 'w+')
    check_count = int(input('Input maximum length of words(Number) : \n'))
    while True:
        inpt = input('Input words(if done input y) : \n')

        if inpt == 'y':
            break
        while len(inpt) > check_count or len(inpt) <1 :
            inpt = input(f"The lenght of the word was more than N or less than 1. please input word not longer than {check_count+1} \n")
        f.write(f"{inpt} \n")


create_input_txt()
get_word_count = Exercise1('./Inputs.txt')
print(get_word_count.count())
