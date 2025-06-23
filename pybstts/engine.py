import os
import importlib
Exceptions = importlib.import_module(f'tts._Exceptions')

class Engine:

    def __init__(self, tts: str) -> None:
        self.tts = tts
        self._tts = importlib.import_module(f'tts.{tts}')
        

    def init(self) -> None:
        if self.tts == '_espeak':
            self.tts = self._tts.Espeak()
            self.tts.check_lib()
            self.tts.load_lib()
            self.tts.lib_init()
                      

    def get_info():  #get info of the model used here
        pass

    def voice():
        pass   #Take arguements to select voices available in the engine.

    def speak(self, text: str | None) -> None: #take arguements to speak.

        self.tts.speak(text) if text != None else None

    def __repr__():
        pass
        
    def __dir__():
        return [
            'init',
            'get_info',
            'voice',
            'speak'
        ]
