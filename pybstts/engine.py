import os
import importlib
from .checktts import TTS
_Exceptions = importlib.import_module('pybstts.tts._Exceptions')


class Engine:

    def __init__(this, tts: str, TTS=TTS(), _Exceptions=_Exceptions) -> None:
        this.tts :str = tts
        this._tts = TTS.load_tts(tts)
        this.tts_engine = None;        

    def init(this) -> None:
        if this.tts == '_espeak':
            this.tts_engine = this._tts.Espeak()
            this.tts_engine.check_lib()
            this.tts_engine.load_lib()
            this.tts_engine.lib_init()
        else:
            raise _Exceptions.EngineNotInitialized  

    def get_info(this):  #get info of the model used here
        return [
        f'lib: pybstts', 
        f'tts: {self.tts}'
        ]

    def voice():
        pass   #Take arguements to select voices available in the engine.

    def speak(this, text: str | None) -> None: #take arguements to speak.
        try: 
            if text != None :       
                this.tts_engine.speak(text)
            else:
                pass            
        except: 
            raise _Exceptions.EngineNotInitialized
    def __repr__(this):
        return '\'Engine\' from pybstts '
        
    def __dir__():
        return [
            'init',
            'get_info',
            'voice',
            'speak'
        ]
