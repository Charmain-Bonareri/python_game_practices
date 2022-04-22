"""
Creating the magic 8 game."""


import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


print('Hello World, I am the Magic 8 Ball, What is your name?')
name = input()
print('hello ' + name + ' , i hope you are having a gametastic day!')
print('That is a cheesy name')


def Magic8Ball():
   
    print('Ask me a question.')
    input()
    print(random.choice(answers) + "\n")
    print('I hope that answers your question!')
    Replay()
    
    
 #Asks if they want to play again


def Replay():
    print("Would you like to play again? (Y/N)")
    play = input()
    if play == "Y":
        Magic8Ball()
    elif play == "N":  
        exit()
    else:
        print("Nice try but wrong input, thank you for playing!")
        Replay()
        

Magic8Ball()
