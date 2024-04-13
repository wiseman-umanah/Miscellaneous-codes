
##from math import factorial
##import random
##
##
##def main():
##    word = input()
##    temp = word
##    unique_word = set(word)
##    word_list = []
##    count = 1
##
##    for i in unique_word:
##        num = word.count(i)
##        count *= factorial(num)
##    
##    iterate = factorial(len(word))/count
##
##    i = 0
##    while i < iterate:
##        word = ''.join(random.sample(word, len(word)))
##        if word in word_list:
##            iterate += 1
##        else:
##            word_list.append(word)
##        i += 1
##
##    print((sorted(word_list)).index(temp) + 1)    
##
##
##main()


##import itertools
##
##def word_generator(chars, len):
##    for i in range(len, len + 1):
##        for s in itertools.permutations(chars, len):
##            yield ''.join(s)    
##
##str_in = str(input())
##words = set()
##
##for word in word_generator(str_in, len(str_in)):
##    words.add(word)
##
##sorted_words = list(words)
##sorted_words.sort()
##print(sorted_words.index(str_in) + 1)

def infinite():
    x_2 = 0

    yield x_2

    for i in range(10):
        yield x_2 + 1
        x_2 += 1


