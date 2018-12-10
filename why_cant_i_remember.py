#/home/h4ckfu/anaconda3/bin/python3
#04.21.18
# These are things that i've sadly looked up...
# Just notes essentially
# https://www.youtube.com/watch?v=Z3_lIPESVTw

test_string="Seether - Same Damn Life"
s='amn'

last_two_chars = test_string[-2:] # Get the end of a string

new_list = test_string.split(" ") # make a new list from a string
make_a_string = " ".join(new_list) # make a string from that new list

print(f'\n \t the last two characters of {test_string} (test_string[-2:]) are {last_two_chars}')
print(f' \t (test_string.split(" ")) makes a {type(new_list)} from test_string')
print(f' \t The first element of new_list is: {new_list[0]}')


print(f'\n \t and then " ".join(new_list) makes that new_list back into {type(make_a_string)}')

print(f'\n \t index {test_string.index(s)} and find {test_string.find(s)} are !=')

print(f'\n \t this round is a feature not a #BUG: round(12345.56, -2) {round(12345.56, -2)} \n')

# [sum(x) for x in zip(list1, list2)]
