words_counted = {}
text_string = str(input("Text: "))
test = text_string.split(" ")
for word in test:
    print("{} : {}".format(word, len(word)))