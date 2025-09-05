print('Maria: Welcome to our family! What is your name?')

my_name = input()

while my_name == '':
    print('Maria: Oh... so you don\'t have name? Try again!')
    my_name = input()

print(my_name + ': Hi, my name is ' + my_name + '! What about yours?')
print('Maria: Nice to meet you ' + my_name + '. I am Maria! I will order coffee, what coffee would you like?')
print(my_name + ': I want a cappuccino assassino!')
print('Maria: ' + 'HA' * 3 + '! Anyway... we do a test to newcommers! First, tell me the length of your name!')

length_of_name = len(my_name)

print(my_name +': It\'s ' + str(length_of_name) + '!')

if length_of_name < 10:
    print('Maria: Oh, you\'re a Jedi!')

    force_counter = 0

    while counter < 3:
        print(my_name + ': May the force be with you!')
        force_counter = force_counter + 1
else:
    print('Maria: Oh, you\'re a Sith!')
