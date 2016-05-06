'''\
Rev: 2
Name: silentshadow
Description: Letting the user decide when to stop the quiz 
Reference: listing 5.3
Page: 139 (PDF 159)
'''

import random, time

correct = 0
count   = 0
questns = 0
sTime   = time.time()
playon  = 'y'

while playon == 'y':
    num1 = random.randint( 0, 9)
    num2 = random.randint( 0, 9)
    
    if num1 < num2:
        num1, num2 = num2, num1
        
    answer =  int( input( "What is {} - {}  >".format( num1, num2)))
    
    if num1 - num2 == answer:
        print( "\tCorrect")
        correct += 1
        questns += 1
    else:
        print( "\tIncorrect")
        questns += 1
        
    playon = input( "Do you want another question? [y/n]  >")
    count += 1
        
endTime = time.time()
tstTime = int( endTime - sTime)
score   = correct / questns

print( "\n{:-^30}".format("Stats"))
print( "Correct:{:.>22} \nTotal:{:.>24} \nScore:{:.>24.2%} \nTime:{:.>25}".format( correct, questns, score, tstTime))
