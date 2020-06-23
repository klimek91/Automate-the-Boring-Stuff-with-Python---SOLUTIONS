text = 'My name is AL SWEIGART and I am 4,000 years old.'

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatina = []
words = text.split(' ')

for word in words:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatina.append(prefixNonLetters)
        continue

    sufixNonLetters = ''
    while len(word) > 0 and not word[-1].isalpha():
        sufixNonLetters += word[-1]
        word = word[:-1]