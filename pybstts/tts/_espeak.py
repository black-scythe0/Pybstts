import os
import sys
import ctypes
from ._Exceptions import (LibraryNotFound,
                      LibraryFailedToLoad,
                      )

class Espeak:
    def __init__(self) -> None:
        self.libespeak = None
        self.lib_espeak_posix :str = 'libespeak-ng.so'
        self.lib_path :str = ''
        self.lib_paths = [

            # Termux
            '/data/data/com.termux/files/usr/lib/libespeak-ng.so',
            '/data/data/com.termux/files/usr/local/lib/libepeak-ng.so'
        ]

    def check_lib(self) -> int:
        for lib_path in self.lib_paths:
            if os.path.isfile(lib_path):
                self.lib_path=lib_path    
                return lib_path   

        else:
            raise LibraryNotFound(self.lib_espeak_posix) 

    def load_lib(self) -> None:

        try:
            self.libespeak = ctypes.cdll.LoadLibrary(self.lib_path)
        except:
            LibraryFailedToLoad(self.lib_espeak_posix)
            
    def lib_init(self, lang=None) -> None:


        self.libespeak.espeak_Initialize.argtypes = [ctypes.c_int,
                                                ctypes.c_int,
                                                ctypes.c_char_p,
                                                ctypes.c_void_p]
                                       
        self.libespeak.espeak_Initialize(0,0,None, None)
        self.libespeak.espeak_SetVoiceByName(b'en')
     
    def speak(self,text: str) -> None:     
        text_bytes = text.encode('utf-8')
        self.libespeak.espeak_Synth(text_bytes, len(text_bytes), 0, 0, 0, 0, None, None)
        self.libespeak.espeak_Synchronize()
                         


if __name__ == '__main__':

    check = Espeak()

    check.check_lib()
    check.load_lib()
    check.lib_init()
    check.speak('hello')    
    
