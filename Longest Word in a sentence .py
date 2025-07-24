Problem: Ekta sentence e je word ta shobcheye boro, seta ber koro.

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)
