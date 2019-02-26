def countVowels(txt):

    vowels = 'aeiou'
    newtxt = txt.lower()
    noduplicates = set(newtxt)
    duplication = len(newtxt)-len(noduplicates)
    vowelstring = ""

    for letter in vowels:
        if letter in noduplicates:
            vowelstring += str(letter)

    return (vowelstring, duplication)


if __name__ == "__main__":

    print(countVowels(input('Enter text: ')))
