
correct = 0
def quiz(correct):

    win = True

    q1 = input('What is my last name?\n ANSWER: ')
    if q1 == 'Kahn' or q1 == 'kahn':
        print('Correct!\n')
        correct += 1
    else:
        print('oooh shucks......\n')



    q2 = input('If Johny has four chairs and he throws one out of the window, how many chairs does Johny own?\n1. Zero, they are his mom\'s and she is very angry with him\n2. Three, someone stole the chair he threw out the window\n3. Two, one of the chairs ran away when they saw what happened to their kin\n4. Four, but one is very broken now\nANSWER: ')
    if q2 == '1':
        print('Correct! Poor Johny, he just wanted to throw a chair out his window and now his mom is mad at him :(\n')
        correct += 1
    else:
        print('damn.... maybe next time\n')

    q3 = input('What number is after 3?\n1. 2\n2. 3+2-1+4-2+3-5\n3. FOUR\n4. three\nANSWER: ')
    if q3 == '4':
        print('Suspiciously correct... I\'ll trick you next time\n')
        correct += 1
    else:
        print('Come on now... you don\'t know what number is after 3?\n')

    q4 = input('What date was the civil war?\nANSWER: ')
    if q4 == 'April 12, 1861' or q4 == 'April 12 1861' or q4 == 'april 12, 1861' or q4 == 'april 12 1861':
        print('NICE JOB!\n')
        correct += 1
    else:
        print('Don\'t worry this test is almost done\n')

    q5 = input('Is this test impossible?Answer is either 1 or 2.\n1. Yes\n2. No\nANSWER: ')
    if q5 == 'either 1 or 2' or q5 == 'either 1 or 2.':
        print('YOU GOT IT!!!')
        correct += 1
    else:
        print('WRONG')


    if correct == 5:
        print('CONGRATS YOU HAVE BEATEN THE almost IMPOSSIBLE QUIZ')

    if correct < 5:
        print(f'You have finished THE IMPOSSIBLE QUIZ!!\nSCORE:{(correct/5)*100}')







quiz(correct)
