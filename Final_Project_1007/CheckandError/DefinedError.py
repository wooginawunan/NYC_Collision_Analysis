'''
Created on Dec 3, 2016

@author: apple
'''


class ExitALLProgram(Exception):
    pass
class InvalidDate(Exception):
    pass
class DATEEndBeforeBegin(Exception):
    pass
class GoingBack(Exception):
    pass
class InvalidInput(Exception):
    pass

class WrongFilePathError(Exception):
    """Raised when the path given is invalid (not in local directory.) or does not contain completed files required"""

    def __init__(self, FilePath):
        self.file_name = FilePath

    def __str__(self):
        return "FILE NOT FOUND! or FILE INCOMPLETED! in the Given Path" \
               "Make sure you run `python NYCcollision.py` from the appropriate directory. or reset the Data Path here".format(self.file_name)
