import importlib


class TTS:
    def __init__(self) -> None:
        self._Exceptions = importlib.import_module('pybstts.tts._Exceptions')
          
    def load_tts(self, tts: str):
        try:
            return (load_tts := importlib.import_module(f'pybstts.tts.{tts}'))
        except:
            raise self._Exceptions.EngineFailedToLoad

if __name__ == '__main__':    
    a = importlib.import_module('tts._Exceptions')
    print(TTS.load_tts('_espeak'))    

