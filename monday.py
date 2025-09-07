print('Maria: Welcome to our family! What is your name?')

my_name = input()

while not my_name:
    print('Maria: Oh... so you don\'t have a name? Try again!')
    my_name = input()

print(my_name + ': Hi, my name is ' + my_name + '! What about yours?')
print('Maria: Nice to meet you ' + my_name + '. I am Maria! I will order coffee, what coffee would you like?')
print(my_name + ': I want a cappuccino assassino!')
print('Maria: ' + 'HA' * 3 + '! Anyway... we do a test to newcommers! Tell me the length of your name!')

length_of_name = len(my_name)

print(my_name +': It\'s ' + str(length_of_name) + '!')
line = ''

if length_of_name < 10:
    line = 'May the force be with you'
    print('Maria: Oh, you\'re a Jedi! This means that you have to say ' + str(length_of_name) + ' times "' + line + '"!')

    for _ in range(length_of_name):
        print(my_name + ': ' + line + '!')
else:
    line = 'Infinite POWER'
    print('Maria: Oh, you\'re a Sith! This means that you have to say ' + str(length_of_name) + ' times "' + line + '"!')

    for _ in range(length_of_name):
        print(my_name + ': ' + line + '!')

print('Maria: Yey! Oh... the coffee arrived! Let me count my money...')
for i in range(2, 10, 2):
    print('Maria: ' + str(i) + '.')
