# Q89. Write a Python program to find words which are greater than a given length k.

def find_words_greater_than_k(words, k):
    result = []
    for word in words:
        if len(word) > k:
            result.append(word)
    return result

sentence = input("Enter a sentence: ")
k = int(input("Enter the value of k: "))
word_list = sentence.split()
result = find_words_greater_than_k(word_list, k)
print("Words greater than length", k, "in the sentence:", result)
