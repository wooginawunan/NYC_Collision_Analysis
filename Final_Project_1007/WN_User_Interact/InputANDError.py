'''
Created on Dec 3, 2016

@author: apple
'''
from WN_User_Interact.HelpMenu import HelpMainCall

class ExitALLProgram(Exception):
    pass

def InputCheck(avalibleSet,input):
    if input=='Help':
        HelpMainCall()
        return -2
    else:
        if input=='Exit':
            raise ExitALLProgram
        if input=='Back':
            return -1
        else:
            try:
                if (int(input) in avalibleSet):
                    return int(input)
                else:
                    print('Invalid Input!')
                    return -2
            except ValueError:
                print('Invalid Input!')
                return -2
def NameCheck(availableSet,input):
    if input=='Help':
        HelpMainCall()
        return -2
    else:
        if input=='Exit':
            raise ExitALLProgram
        if input=='Back':
            return -1
        else:
            if input in availableSet:
                return input
            else:
                print('Invalid Input!')
                return -2
           
    