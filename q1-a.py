import pandas as pd 
d1 = {'ali':'graduated', 'sara':'graduated', 'samer':'not graduated', 'rana':'not graduated', 'yara':'graduated'}
while True:
    ename = input ('enter your name: ')
    if ename in d1.keys():
        if d1[ename]=='graduated':
            print (ename , 'graduated')
        else:
                print (ename , 'not graduated')
    else: print ('not found') 
          
