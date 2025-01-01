def length(words):
    return max(len(word)for word in words)
words_list=input("Enter a list of words seperated by spaces:").split()
print("length of longest word:",length(words_list))