'''
Created on Dec 1, 2016

@author: apple
'''
import sys
import os
from CheckandError.DefinedError import ExitALLProgram
if __name__ == '__main__':
    try:
        print(os.getcwd())
        import WN_User_Interact
    except ExitALLProgram:
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
        