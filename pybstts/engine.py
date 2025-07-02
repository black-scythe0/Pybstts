import importlib
from .checktts import TTS



class Engine:
    '''
    pybstts Engine:

    Methods:
    init();       to initialize Engine
    speak();      after initialization to speak.
    get_info();   to get info about the tts
    voice();      to change voice 
    '''
    def __init__(this,
             tts: str,
            TTS=TTS(),
           _Exceptions= importlib
                               .import_module('pybstts.tts._Exceptions')
                  ) -> None:

        this.tts :str = tts
        this._tts = TTS.load_tts(tts)
        this.tts_engine = None;        
        this._Exceptions = _Exceptions
    def init(this) -> None:
        '''
        initialize the Engine
        '''
        if this.tts == '_espeak':
            this.tts_engine = this._tts.Espeak()
            this.tts_engine.check_lib()
            this.tts_engine.load_lib()
            this.tts_engine.lib_init()
        else:
            raise this._Exceptions.EngineNotInitialized  

    def get_info(this):  #get info of the model used here
        '''
        get information about the tts.
        '''
        return [
        f'lib: pybstts', 
        f'tts: {self.tts}'
        ]

    def voice(this):
        pass   #Take arguements to select voices available in the engine.

    def speak(this, text: str | None) -> None: #take arguements to speak.
        '''
        Takes string arguements to speak.

        '''  
        try: 
            if text != None :       
                this.tts_engine.speak(text)
            else:
                pass            
        except: 
            raise this._Exceptions.EngineNotInitialized
    def __repr__(this):
        '''
        return string regarding Engine
        '''
        return '\'Engine\' from pybstts'
        
    def __dir__(this):
        return [
            'init',
            'get_info',
            'voice',
            'speak'
        ]
