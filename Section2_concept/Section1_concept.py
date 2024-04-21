# q2.1
input_str = "foundation"

output = input_str[:7:2]
print(output)   # output 'fudt'


# q2.2
squares = [i ** 2 for i in range(6)]

# for i in range(6):
#     squares.append(i**2)

print(squares)


# q2.3
set_one = {1, 2, 3, 4, 5, 6}
set_two = {1, 2, 3, 4, 5, 6, 7, 8}


def sub_set_function(set1, set2):
    for num in set1:
        if num in set2:
            continue
        else:
            return False
    return True


print(sub_set_function(set_one, set_two))

# q2.4
list_of_names = {'John', 'John', 'Sarah', 'Jack', 'Sam'}


def unique_names(name_list):
    return len(set(name_list))


print(unique_names(list_of_names))

# q2.5
vowel_list = ['a', 'e', 'i', 'o', 'u']
count = 0

with open('input.txt') as file:
    for line in file.readlines():
        #print(line, type(line))
        for word in line.split():
            for char in word:
                if char.lower() in vowel_list:
                    count += 1

print(count)
