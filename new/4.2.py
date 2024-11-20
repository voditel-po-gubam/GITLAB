with open('dictionary.txt', encoding='UTF-8') as file:
    dictionary = [sub.split('|')[:-1] for sub in file.readlines()]

def shuffle(words):
    ans = []
    the_set = set(str(i) for i in range(100))
    for e in the_set:
        ans += [words[int(e)]]
    return ans
    
def fguess(word):
    print(word[1])
    guess = '*' * len(word[0])
    boofer = ''
    guessed = []
    while guess != word[0]:
        print(guess + '\n')
        letGuess = input('Угадайте букву или слово целиком: ')
        if letGuess == word[0]:
            guess = word[0]
        elif letGuess in word[0]:
            guessed += [letGuess]
            for i in range(len(guess)):
                if word[0][i] in guessed:
                    boofer += word[0][i]
                else:
                    boofer += '*'
            guess, boofer = boofer, ''
    print(letGuess)
    print('Поздравляем!!!')
    print('\n' * 33)

for i in range(100):
    fguess(shuffle(dictionary)[i])
