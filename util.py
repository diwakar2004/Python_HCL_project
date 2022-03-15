from students import *
class Util:
    def getScore(name):
        for user in users:
            if user == name:
                return users[user]
            else:
                return "No Student named " + name
    def setScore(name,score):
        for user in users:
            if user == name:
                users.update({user:score})
            else:
                return "No Student named " + name