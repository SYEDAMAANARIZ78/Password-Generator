import random
upper_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
              'n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9','0']
spl_char = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_',
            '=','<','>','?','+']

password = (random.choice(upper_char) + random.choice(lower_char) + random.choice(lower_char) + random.choice(lower_char) + 
           random.choice(lower_char) +random.choice(spl_char) + random.choice(number) + random.choice(number))
print(password)