def main():
     print ('hi, please answer on 20 question by t or f')
     name= input('enter your name: ')
 
     questions(name)
def questions(n):
    c = 0
    questions=open("aa.txt",'r')
    R = [line.rstrip().split(',') for line in questions]
    for j in R:
        print(j[0])
        s=input()
        if s==j[1]:
             c+=1
    W=open("abd.txt","w")
    print (n + '  the correct answers:' + str (c)) 
    W.write(n + 'the correct answers:' + str(c))
    questions.close
    W.close
main()
