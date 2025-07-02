import importlib


class TTS:
    def __init__(this) -> None:
        this._Exceptions = importlib.import_module('pybstts.tts._Exceptions')
          
    def load_tts(this, tts: str):
        try:
            return (load_tts := importlib.import_module(f'pybstts.tts.{tts}'))
        except:
            raise this._Exceptions.EngineFailedToLoad
