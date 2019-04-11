words_counted = {}
text_string = str(input("Text: "))
test = text_string.split(" ")
for word in test:
    frequency = words_counted.get(word, 0)
    words_counted[word] = frequency + 1
test = list(words_counted.keys())
test.sort()

length_calculator = max(len(i) for i in test)
for i in test:
    print("{:{}} : {}".format(i, length_calculator, words_counted[i]))
