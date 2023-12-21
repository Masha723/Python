"""
The Alphabet class generates iterators and its constructor takes one argument:

language — language code: ru — Russian, en — English
The Alphabet() class iterator cycles through a sequence of lowercase letters:

Russian alphabet, if language has the meaning ru
English alphabet if language is en

"""






class Alphabet:
    def __init__(self,language):
        self.d={'ru': [chr(i) for i in range(1072, 1104)], 'en':[chr(i) for i in range(97, 123)]}
        self.language=self.d[language]
        self.index=-1
        pass

    def __iter__(self):
        return self

    def __next__(self):
                self.index+=1
                if self.index>=len(self.language):
                    self.index=0
                    return self.language[self.index]  
                else:
                    return self.language[self.index]

"""
Test samples
"""

ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

en_alpha = Alphabet('en')

for _ in range(100):
    print(next(en_alpha))

ru_alpha = Alphabet('ru')

for _ in range(50):
    print(next(ru_alpha))
