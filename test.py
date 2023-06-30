import time 

class Question:
  def __init__(self, msg, goodAnswers):
    self.msg = msg
    self.goodAnswers = goodAnswers

  def __str__(self):
    return self.msg

  def quit():
    raise EOFError

print(
  '\n***********************************************************************'
  '\n--------|| Welcome to the game Who Wants to Be a Millionaire ||--------'
  '\n***********************************************************************'
  )
promt = '> '
player = input(" \n Enter your name? \n " + promt )
print (
  '\nHello ' + player  + 
  ' Lets start the game' + 
  ' you will get 15 questions with respect'
  '\nto difficulty level of the game. Begining of the game you will get'
  '\nsimpler questions and the level will go harder and harder as you go on'
  '\ntill the end and if you could able to answer all of them you will be'
  '\nwinner and can win $1,000,000!' + 
  '\n                          \U0001f631' + ' HURRAY ' + '\U0001f631\n'
  )
enter = input('\nPress Enter to start the game \n')

print('\nSo let the game begin\n')


print('\nHere is the first question for you\n')
 
questions = [
  Question(
    '\n=========================================================================' +
    '\n 1. who is allah ?' +
    '\n=========================================================================\n',
    {
      'God': 'Good Job! You got it right Congratualtions You won $100.',
      'almighty': 'Good Job! You got it right Congratualtions You won $100.'
    }
    ),
  Question(
    '\n=========================================================================' +
    '\n who was first khalif ?' +
    '\n=========================================================================\n',
    {
      'abu bakr': 'Good Job! You got it right Congratualtions You won $200.',
      'abu': 'Good Job! You got it right Congratualtions You won $200.'
    }
    ),
  Question(
    '\n=========================================================================' +
    '\n who was second khalif ?' +
    '\n=========================================================================\n',
    {
      'abu bakr': 'Good Job! You got it right Congratualtions You won $300.',
      'umar': 'Good Job! You got it right Congratualtions You won $300.',
      'Umar': 'Good Job! You got it right Congratualtions You won $300.'
    }
    ),

]


try :
  level = 0  
  unknown = 'Your answer is wrong please try next time'
  while True:
    q = questions[level]
    print(q)
    useranswer = input(promt)
    if useranswer == 'quit':
      break
    response = q.goodAnswers.get(useranswer, unknown)
    print(response)
    if response != unknown:
      level += 1
    else:
      break

except EOFError:
  pass

print('Game over, ' + player + ' Sorry You won nothing.\U0001f614 \nThanks for playing the game hope to see you next time.\U0001f642')
