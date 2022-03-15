from students import *
from util import *
student=Student
util=Util
while True:
    print("\n\n\t\tMain Menu\n\n")
    print("\t1)Add Student\n")
    print("\t2)Remove Student\n")
    print("\t3)Update Score\n")
    print("\t4)Get Student Score\n")
    print("\t5)Display Student Records\n")
    print("\t6)Exit\n")
    option=int(input("\tEnter Your Option : "))
    if option==1:
        name=input("\tEnter Student Name : ")
        score=int(input("\tEnter Student Score : "))
        student.addUser(name,score)
    elif option==2:
        name=input("\tEnter Student Name : ")
        student.delUser(name)
    elif option==3:
        name=input("\tEnter Student Name : ")
        score=int(input("\tEnter Student Score : "))
        util.setScore(name,score)
    elif option==4:
        name=input("\tEnter Student Name : ")
        print("\n\t",name,":",util.getScore(name))
    elif option==5:
        student.display()
        break
    elif option==6:
        exit(0)
