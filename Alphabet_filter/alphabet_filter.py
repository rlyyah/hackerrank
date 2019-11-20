import string
alphabet = string.ascii_lowercase
def alphabet_filter(word):
    vowels = 'aeiouy'
    constraints = 'bcdfghjklmnpqrstvwxz' 
    word_consonants = ''
    word_vowels = ''
    vowels_list = []
    consonants_list = []
    for letter in word:
        if letter in vowels:
            vowels_list.append(letter.lower())
        elif letter in constraints:
            consonants_list.append(letter.lower())
    word_consonants = ''.join(consonants_list)
    word_vowels = ''.join(vowels_list)
    
    return word_consonants, word_vowels

answer_list = alphabet_filter('abcdefghijklmnoprstAAAaaauwvxyz111')
print(alphabet)

print(f'consonants: {answer_list[0]}, vowels: {answer_list[1]}')


