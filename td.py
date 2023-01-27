import random
import time
import winsound
from datetime import date, datetime
import math

def print_menu():
    print('Menu')
    print('1. Password Generator')
    print('2. Password Strength Checker ')
    print('3. Random Colour Generator')
    print('4. Tip Calculator')
    print('5. Award Winner Picker')
    print('6. Guess Number Game')
    print('7. Rock Paper Scissors Game')
    print('8. Countdown Timer')
    print('9. Metronome (Works only on windows)')
    print('10. Leap year')
    print('11. Word reverser')
    print('12. HTML Template builder')
    print('13. CSS Template builder')
    print('14. Today date')
    print('15. Clock')
    print('16. Multiplication test')
    print('17. Addition test')
    print('18. Is Even?')
    print('19. Count vowels in string')
    print('20. Average')    
    print('21. Is prime?')    
    print('22. Is perfect?')    
    print('23. Is palindrome')    
    print('24. Longest word')    
    print('25. Rectangle area')    
    print('26. Count words')    
    print('27. Get sin')    
    print('28. Check Phone')    
    print('29. Get sum')    
    print('30. Find largest')    

def password_generator():    
    code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    password = ''

    for i in range(16):
        is_upper = random.randint(0, 1)
        randnum = random.randint(0, 14)

        password += code[randnum].upper() if is_upper == 1 else code[randnum]
    
    print(f'Your secure password: {password}')

def password_check():
    password = input('Please, enter your password: ')
    points = 0
    levels = ['low', 'medium', 'high']

    if(len(password) > 14): 
        points += 1
        print('point for lenght')

    for letter in password:
        if(letter.isnumeric()): 
            points += 1
            print('point for number')
            break

    for letter in password:
        if(letter.isupper()):
            points += 1
            print('point for upper')
            break

    print(f'Your password is {levels[points-1]} quality!') if len(password) > 7 else print('Your password is too short!')

    if(points < 3):
        print('Tips to make your password safe:')
        print('-at least 15 characters')
        print('-at least 1 number')
        print('-at least 1 letter in uppercase')

def colour_generator():
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    colour = '#'

    for i in range(6):
        colour += hex[random.randint(0, 16)]

    print(f'Random colour: {colour}')     

def tip_calculator():
    price = float(input('Price: $'))
    tip = float(input('Tip: %'))/100
    amount = tip * price
    total = price + amount
    print(f'Tip amount: {amount}, total: {total}')

def award_winner():
    def add_name():
        name = input('Enter new name: ')
        names.append(name)

    def delete_name():
        name = input('Enter name to remove: ')
        names.remove(name)
    
    def pick_winner():
        rand = random.randint(0, len(names)-1)
        winner = names[rand]
        print(f'==Winner is: {winner}==')


    names = []
    menu = {
        '1': add_name,
        '2': delete_name,
        '3': pick_winner,
    }
    
    while True:
        print(f'list of names: {names}')
        print('1. Add name')
        print('2. Delete name')
        print('3. Pick winner')
        print('4. Stop')
        choice = input('Enter your choice: ')

        if(choice == '4'):
            break
        elif choice not in menu:
            print('Invalid choice!')
        else:
            menu[choice]()

def guess_number():
    tries = int(input('How many tries you want?: '))
    number = random.randint(1,100)

    while(tries>0):
        print(f'You have {tries} tries left!')
        user_number = int(input('Guess a random number between 1 and 100: '))
        
        if(user_number == number):
            print('You won!')
            break
        elif(user_number > number):
            print('Less!')
            tries -= 1
        elif(user_number < number):
            print('More!')
            tries -= 1

        if(tries == 0):
            print('You lost!')

def rock():
    choices = ['R', 'P', 'S']
    winning_settings = ['RS', 'PR', 'SP']
    choice = input('[R]ock [P]aper [S]cissors: ')

    if choice not in choices:
        print('Wrong choice!')
    else:
        computer_choice = random.choice(choices)
        setting = f'{choice}{computer_choice}'

        print(f'You:{choice}, Computer: {computer_choice}')

        if(choice==computer_choice):
            print('No contest!')
        elif(setting in winning_settings):
            print('You Won!')
        else:
            print('You lost!')
     
def countdown_timer():
    def fill(n):
        return str(n).zfill(2)

    def check(n): return 0 <= n < 60
    
    def print_timer(h, m, s):
        print(f'[{fill(h)}:{fill(m)}:{fill(s)}]')
 
    print('Countdown Timer')
    print('Press [CTRL] + [C] to stop the countdown!')

    while True:
        hours = int(input('h:'))
        minutes = int(input('m:'))
        seconds = int(input('s:'))

        clock = [hours, minutes, seconds]
        score = 0

        for i in range(3):
            if check(clock[i-1]): score += 1

        if(score == 3): break
        else: print('Numbers cannot be less than 0 or greater than 59!') 

    try:
        while True:
            for i in reversed(range(1, 3)):
                if clock[i] == -1: 
                    clock[i-1] -= 1
                    clock[i] = 59

            print_timer(clock[0], clock[1], clock[2])
            time.sleep(1)
            clock[2] -= 1

            if clock[0] < 1 and clock[1] < 1 and clock[2] < 1: break
    except KeyboardInterrupt:
        print('Countdown stopped!')

def metronome():
    bpm = int(input('Enter BPM: '))
    sleep_time = 60 / bpm
    arrow = 0

    while True:
        print('\\') if arrow == 0 else print('/')
        winsound.Beep(440, int(sleep_time * 1000))

        arrow = 1 if arrow == 0 else 0

def leap_year():
    year = int(input('Enter year : '))
 
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(year, 'is a leap year.')
    else:
        print(year, 'is not a leap year.')

def word_reverser():
    user_word = input('Enter your word: ')
    reversed_word = ''

    for i in reversed(range(0, len(user_word))):
        reversed_word += user_word[i]
    
    print(f'Reversed word: {reversed_word}')

def html_template():
    title = input('Enter your title: ')
    lang = input('Enter language of your page: ')

    print('Your page template: ')
    print(f'''
    <!DOCTYPE html>
    <html lang="{lang}">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
        </head>
        <body>
            My page
        </body>
    </html>
    ''')

def css_template():
    print('Your CSS template:')
    print('''
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body{
        width: 100%;
        min-height: 100vh;
    }
    ''')

def today_date():
    today = date.today()
    print(f'Todays date: {today}')

def clock():
    print('Clock')
    print('Press [CTRL] + [C] to exit clock!')

    try:
        while True:
            print(f'[{datetime.now().strftime("%H:%M:%S")}]')
            time.sleep(1)
    except KeyboardInterrupt:
        print('Clock stopped!')
    
def addition_test():
    def rand(r):
        return random.randint(1, r)
    
    print('Multiplication Test')
    rang = int(input('Range: '))

    score = 0
    for i in range(1, 11):
        n = [rand(rang), rand(rang)]
        answer = int(input(f'{i}. What is {n[0]} + {n[1]}?: '))
        print(f'Good answer: {n[0] + n[1]}')
        if n[0] + n[1] == answer: score += 1

    print(f'Your score: {score}')

def multiplication_test():
    def rand():
        return random.randint(1, 9)
    
    print('Multiplication Test')
    score = 0
    for i in range(1, 11):
        n = [rand(), rand()]
        answer = int(input(f'{i}. What is {n[0]} * {n[1]}?: '))
        print(f'Good answer: {n[0] * n[1]}')
        if n[0] * n[1] == answer: score += 1

    print(f'Your score: {score}')

def is_even():
    n = int(input('Number: '))
    print('even') if n % 2 == 0 else print('not even')

def count_vowels():
    s = input('Enter your word: ')
    vowels = 'aeiouAEIOU'
    count = 0

    for char in s:
        if char in vowels: count += 1

    print(f'Number of vowels: {count}')

def average():
    non = int(input('How many numbers do you want to average?: '))
    numbers = []
    average = 0
    
    for i in range(non):
        new = int(input(f'Enter {i+1}. number: '))
        numbers.append(new)

    for number in numbers: average += number

    average /= non

    print(f'Average: {average}')

def is_prime():
    def check(n):
        if n < 2: return False

        for i in range(2, n):
            if n % i == 0: return False

        return True

    number = int(input('Enter number: '))
    print('Prime') if check(number) else print('not Prime')

def is_perfect():   
    def check(n):
        dividers = []

        for i in range(1, n):
            if n % i == 0: dividers.append(i)

        return sum(dividers) == n

    number = int(input('Enter number: '))
    print('Perfect') if check(number) else print('not Perfect')

def is_palindrome():
    def check(s):
        return s[::-1] == s

    str = input('Enter string: ')
    print('Palindrome' if check(str) else print('not Palindrome'))

def longest_word():
    def check(t):
        words = t.split()
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word
        return longest
    
    text = input('Enter your text:')

    print(f'Longest word: {check(text)}')

def rectangle_area():
    lth = int(input('Enter length: '))
    wth = int(input('Enter width: '))
    print(f'Area: {lth * wth}')

def count_words():
    text = input('Your text: ')
    words = text.split()
    count = len(words)
    print(count)

def get_sin():
    number = float(input("Number: "))
    print(math.sin(number))

def check_phone():
    phone = input('Phone number:')
    print('Correct') if phone.isnumeric() and len(phone) == 9 else print('Incorrect')

def get_sum():
    numbers = []
    print('Add numbers or type [f] to sum get sum')

    while True: 
        n = input()

        if(n == 'f'): break
        numbers.append(float(n))

    print(f'Sum: {sum(numbers)}')

def find_largest():
    numbers = []
    print('Add numbers or type [f] to sum get largest')

    while True: 
        n = input()

        if(n == 'f'): break
        numbers.append(float(n))

    print(f'Sum: {max(numbers)}')

def main():
    menu = {
        '1': password_generator,
        '2': password_check,
        '3': colour_generator,
        '4': tip_calculator,
        '5': award_winner,
        '6': guess_number,
        '7': rock,
        '8': countdown_timer,
        '9': metronome,
        '10': leap_year,
        '11': word_reverser,
        '12': html_template,
        '13': css_template,
        '14': today_date,
        '15': clock,
        '16': multiplication_test,
        '17': addition_test,
        '18': is_even,
        '19': count_vowels,
        '20': average,
        '21': is_prime,
        '22': is_perfect,
        '23': is_palindrome,
        '24': longest_word,
        '25': rectangle_area,
        '26': count_words,
        '27': get_sin,
        '28': check_phone,
        '29': get_sum,
        '30': find_largest,
    }

    while True:
        print_menu()
        choice = input('Enter your choice: ')

        if choice not in menu:
            print('Invalid choice. Please try again.')
        else:
            menu[choice]()
        
        time.sleep(2)
        print('\n')
        # exit()


if __name__ == '__main__':
    main()