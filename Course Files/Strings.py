from os import system
from time import sleep

system('clear')
#Escape Characters with Print Function
# \n -> New line | \t -> Tab | \\ -> Backslash | \b -> Backspace | \r -> Carriage Return | \a -> ASCII Bell | \x -> Character with Hex Value

print("I love Python. \nThis is one of the most simple Languages. \tTry these Escape (\\) characters. \n\"Hope you will have fun.\"")
input()
print("Octal Value: \101 \102")
input()
print("Hexa Decimal Value: \x29")
input()
system('clear')

## Prefix your string with "r" to make it Raw  (Escape Free)
print(r'C:\Program Files\Python 3.10')
input()
system('clear')





## Formatting String
'''Hello %s' % name    # C-style
'I love {1}, {0} {1}'.format('Any', 'Ice-Cream')  # Added in Python 3.0
f'I am {age} years old'  # f-string added in Python 3.6'''

s_name = 'Joseph K'
s_class = 4
s_marks = 99.88999
print(f'He is {s_name}. He is in the {s_class}th standar. He got {s_marks:.2f} in the last session.')

### Summarize Type Filtering sub types
'''
Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.
More details can be found here : https://docs.python.org/3/library/string.html#formatspec
'''
input()
system('clear')





## Using Separators and Flush
print('Print', 'with', 0, 'seapartor', sep='\n')
input()
for i in range(5):
    sleep(1)
    print('.', end='', flush=True)
input()
system('clear')


## Playing with Print
for x in range(5):
    for f in r'-\|/-\|/':
        print('\b', f, sep='', end='', flush=True)
        sleep(0.2)
print('\b ')

input()
system('clear')

def progress(percent=0, width=30):
    hashes = width * percent // 100
    blanks = width - hashes
    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)
print('This will take a moment')
for i in range(101):
    progress(i)
    sleep(0.1)

input()
system('clear')