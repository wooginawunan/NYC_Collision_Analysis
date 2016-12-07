'''
Created on Dec 5, 2016

@author: apple
'''
from WN_User_Interact.HelpMenu import HelpMainCall
from CheckandError.DefinedError import ExitALLProgram,InvalidDate,DATEEndBeforeBegin,InvalidFirst,GoingBack
def DateCheck(begintime,endtime):

    availbleset = list(map(lambda x,y:str(x)+str(y).zfill(2),sorted(['2015','2016']*12),list(range(1,13))*2))
    if ((begintime in availbleset) and (endtime in availbleset)):
        if begintime<=endtime:
            return [int(begintime[0:4]),int(begintime[4:6])], [int(endtime[0:4]),int(endtime[4:6])] 
        else:
            raise DATEEndBeforeBegin
    else:
        raise InvalidDate
def InputCheck(avalibleSet,Input):
    if Input=='Help':
        HelpMainCall()
        return -2
    else:
        if Input=='Exit':
            raise ExitALLProgram
        if Input=='Back':
            return -1
        else:
            try:
                if (int(Input) in avalibleSet):
                    return int(Input)
                else:
                    print('Invalid Input!')
                    return -2
            except ValueError:
                print('Invalid Input!')
                return -2
def NameCheck(availableSet,Input):
    if Input=='Help':
        HelpMainCall()
        return -2
    else:
        if Input=='Exit':
            raise ExitALLProgram
        if Input=='Back':
            return -1
        else:
            if Input in availableSet:
                return Input
            else:
                print('Invalid Input!')
                return -2

def FirstCheck(availableSet,Input):
    if Input=='Help':
        HelpMainCall()
        raise InvalidFirst
    else:
        if Input=='Exit':
            raise ExitALLProgram
        if Input=='Back':
            raise GoingBack
        else:
            if Input in availableSet:
                return Input
            else:
                print('Invalid Input!')
                raise InvalidFirst

    
        