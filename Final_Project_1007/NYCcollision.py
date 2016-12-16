'''
Created on Dec 1, 2016

@author: apple
'''
import sys
import os
from CheckandError.DefinedError import ExitALLProgram
import WN_User_Interact
if __name__ == '__main__':
    try:
        dirname, filename = os.path.split(os.path.abspath(__file__))
        WN_User_Interact.User_Interaction(dirname)
    
    except ExitALLProgram:
        print('Exiting...')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        