import random

wordlist = []
spl_char = ['~','!','@','#','$','%','^','&','*','-','_',
            '=','?','+']

with open("Text_input.txt", 'r') as file:
    data = file.readlines()
    
    for line in data:
        words = line.split()
        
        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())
                
word = random.choice(wordlist)
schar = random.choice(spl_char)
num = str(random.randint(10, 99))

password = word + schar + num
print(password)