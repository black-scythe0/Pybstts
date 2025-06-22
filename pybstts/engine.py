import os
from tts import Exceptions

class Engine:

    def __init__():
        pass

    def init(): #initialize the engine, may take arguements ,
                # if no arguements are given then figure out it self which engine to use.
        pass      

    def get_info():  #get info of the model used here
        pass

    def voice():
        pass   #Take arguements to select voices available in the engine.

    def speak(text): #take arguements to speak.
        pass

    def __repr__():
        pass
        
    def __dir__():
        return [
            'init',
            'get_info',
            'voice',
            'speak'
        ]
