import os
from tts import _espeak

class Engine:

    def __init__():
        pass

    def init():

        lib = _espeak.Espeak.check_lib()
        if lib != 1:
        
            try:
                os.system('espeak initialize')
                return 'successfully initialize'
           # assert os.system('echo $?') !
            except:
                return 'failed to initialize '
        return 0        




