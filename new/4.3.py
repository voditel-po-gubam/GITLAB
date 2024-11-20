from random import choice

class word:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class password:
    def __init__(self, name):
        self.name = '*' * len(name)
    def reboot(self, name, shot, target):
        if shot == target:
            self.name = target
        else:
            for i in range(len(target)):
                if target[i] == shot or name[i] != '*':
                    self.name += target[i]
                else:
                    self.name += '*'
            self.name = self.name[len(target):]

class guess:
    def __init__(self, checked):
        self.flag = False
        self.checked = checked
        self.letter = input('Угадайте букву или слово целиком: ')
    def check(self, pw, w):
        if pw == w:
            print('Поздравляем!')
            print('\n' * 33)
            self.flag = True
        else:
            print('')

with open('dictionary.txt', encoding='UTF-8') as file:
    dictionary = [sub.split('|')[:-1] for sub in file.readlines()]
while True:
    w = choice(dictionary)
    w = word(w[0], w[1])
    p = password(w.name)
    print(w.desc)
    print(p.name + '\n')
    while True:
        g = guess(p.name)
        p.reboot(p.name, g.letter, w.name)
        print(p.name)
        g.check(p.name, w.name)
        if g.flag:
            break
