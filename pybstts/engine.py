import os
import importlib
from .checktts import TTS
_Exceptions = importlib.import_module('pybstts.tts._Exceptions')


class Engine:

    def __init__(self, tts: str, TTS=TTS(), _Exceptions=_Exceptions) -> None:
        self.tts :str = tts
        self._tts = TTS.load_tts(tts)
        self.tts_engine = None;        

    def init(self) -> int:
        if self.tts == '_espeak':
            self.tts_engine = self._tts.Espeak()
            self.tts_engine.check_lib()
            self.tts_engine.load_lib()
            self.tts_engine.lib_init()
        else:
            raise _Exceptions.EngineNotInitialized  
        return 21
    def get_info(self):  #get info of the model used here
        return [
        f'lib: pybstts', 
        f'tts: {self.tts}'
        ]

    def voice():
        pass   #Take arguements to select voices available in the engine.

    def speak(self, text: str | None) -> None: #take arguements to speak.
        try: 
            if text != None :       
                self.tts_engine.speak(text)
            else:
                pass            
        except:
            raise _Exceptions.EngineNotInitialized
    def __repr__(self):
        return '\'Engine\' from pybstts '
        
    def __dir__():
        return [
            'init',
            'get_info',
            'voice',
            'speak'
        ]
