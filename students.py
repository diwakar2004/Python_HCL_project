users={"diwakar":90 ,"subasri":70 ,"karan":75 ,"kapil":65}
class Student:
    def addUser(name,score):
        users[name]=score
        return name

    def delUser(name):
        del users[name]

    def display():
        for user in users:
            print("\n\t"+user,"\t",users[user])
