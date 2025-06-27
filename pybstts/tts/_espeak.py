import os
import sys
import ctypes
from ._Exceptions import (LibraryNotFound,
                      LibraryFailedToLoad,
                      )

class Espeak:
    def __init__(this) -> None:
        this.libespeak: None = None
        this.lib_espeak_posix :str = 'libespeak-ng.so'
        this.lib_path :str = ''
        this.lib_paths = [

            # Termux
            '/data/data/com.termux/files/usr/lib/libespeak-ng.so',
            '/data/data/com.termux/files/usr/local/lib/libepeak-ng.so'
        ]

    def check_lib(this) -> str:
        for lib_path in this.lib_paths:
            if os.path.isfile(lib_path):
                this.lib_path=lib_path    
                return lib_path   

        else:
            raise LibraryNotFound(this.lib_espeak_posix) 

    def load_lib(this) -> None:

        try:
            this.libespeak = ctypes.cdll.LoadLibrary(this.lib_path)
        except:
            LibraryFailedToLoad(this.lib_espeak_posix)
            
    def lib_init(this, lang=None) -> None:


        this.libespeak.espeak_Initialize.argtypes = [ctypes.c_int,
                                                ctypes.c_int,
                                                ctypes.c_char_p,
                                                ctypes.c_void_p]
                                       
        this.libespeak.espeak_Initialize(0,0,None, None)
        this.libespeak.espeak_SetVoiceByName(b'en')
     
    def speak(this,text: str) -> None:     
        text_bytes = text.encode('utf-8')
        this.libespeak.espeak_Synth(text_bytes, len(text_bytes), 0, 0, 0, 0, None, None)
        this.libespeak.espeak_Synchronize()
                         


if __name__ == '__main__':

    check = Espeak()

    check.check_lib()
    check.load_lib()
    check.lib_init()
    check.speak('hello')    
    
