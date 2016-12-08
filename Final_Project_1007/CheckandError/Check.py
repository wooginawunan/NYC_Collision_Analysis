'''
Created on Dec 5, 2016

@author: apple
'''
from WN_User_Interact.HelpMenu import HelpMainCall
from CheckandError.DefinedError import ExitALLProgram,InvalidDate,DATEEndBeforeBegin,GoingBack,InvalidInput
def GeneralCheck(Input):
    ExitCheck(Input)
    HelpMenuCheck(Input)
    
def ExitCheck(Input):
    if Input=='Exit':
        raise ExitALLProgram

def HelpMenuCheck(Input):
    if Input=='Help':
        HelpMainCall()

def OneDateCheck(Input):
    availbleset = list(map(lambda x,y:str(x)+str(y).zfill(2),sorted(['2015','2016']*12),list(range(1,13))*2))
    if Input in availbleset:
        return Input
    else:
        raise InvalidDate

def TwoDateCheck(begintime,endtime):
    if begintime<=endtime:
        return [int(begintime[0:4]),int(begintime[4:6])], [int(endtime[0:4]),int(endtime[4:6])] 
    else:
        raise DATEEndBeforeBegin
    
def IntInputCheck(avalibleSet,Input):
    if Input=='Back':
        return -1
    else:
        try:
            if (int(Input) in avalibleSet):
                return int(Input)
            else:
                raise InvalidInput
        except ValueError:
            raise InvalidInput


def StringInputCheck(availableSet,Input):
    if Input=='Back':
        raise GoingBack
    else:
        if Input in availableSet:
            return Input
        else:
            print('Invalid Input!')
            raise InvalidInput

    
        