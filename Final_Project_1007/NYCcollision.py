'''
Created on Dec 1, 2016

@author: apple
'''
import sys
import os
if __name__ == '__main__':
    try:
        import WN_User_Interact
    
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        