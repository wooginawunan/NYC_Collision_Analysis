'''
Define Error
Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''


class ExitALLProgram(Exception):
    '''
    Check input "Exit", anytime user input a Exit, this error will be raise and exit the whole program.
    '''
    pass
class InvalidDate(Exception):
    '''
    Raise when The Input Date are not available.
    '''
    pass
class DATEEndBeforeBegin(Exception):
    '''
    Raise when timeend are earlier than timestart
    '''
    pass
class GoingBack(Exception):
    '''
     Check input "Back", anytime user input a Back, this error will be raise and go to the upper level of menu.
    '''
    pass
class InvalidInput(Exception):
    '''
    Raise when input are invalid
    '''
    pass

class WrongFilePathError(Exception):
    """Raised when the path given is invalid (not in local directory.) or does not contain completed files required"""

    def __init__(self, FilePath):
        self.file_name = FilePath

    def __str__(self):
        return "FILE NOT FOUND! or FILE INCOMPLETED! in the Given Path" \
               "Make sure you run `python NYCcollision.py` from the appropriate directory. or reset the Data Path here".format(self.file_name)
