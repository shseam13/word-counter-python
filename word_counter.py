search_words = ["Python", "C", "OOP", "Hello", "Java"]

with open('words.txt') as file_object:
    lines = file_object.readlines()

# removing newline and whitespaces
stripped_words = []
for line in lines:
    stripped_words.append(line.strip('\n').lower())

print('\nSearch Result:')
# searching word
for value in search_words:
    counter = 0
    for word in stripped_words:
        if value.lower() == word:
            counter +=1
        else:
            counter += 0
    print(f"{value} -> {counter}")
print('\n')