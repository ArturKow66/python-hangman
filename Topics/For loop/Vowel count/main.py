string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowels_sum = 0
string_size = len(string)

for i in range(string_size):
    if string[i] in vowels:
        vowels_sum += 1

print(vowels_sum)
