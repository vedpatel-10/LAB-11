f1 = open('8dirs/sample1.txt', 'r')
f2 = open('8dirs/sample2.txt', 'w+')

data = f1.read()
lst_data = data.split()
print("Original Words:", lst_data)

remove_words = ['a', 'an', 'the']

filtered_words = [word for word in lst_data if word.lower() not in remove_words]

output = ' '.join(filtered_words)

f2.write(output)

print("Filtered Words:", filtered_words)
print("Task done successfully")

f1.close()
f2.close()

#OUTPUT:
# Original Words: ['the', 'quick', 'brown', 'fox', 'jumps', 'all', 'over', 'a', 'lazy', 'dog', '.']
# Filtered Words: ['quick', 'brown', 'fox', 'jumps', 'all', 'over', 'lazy', 'dog', '.']
# Task done successfully
