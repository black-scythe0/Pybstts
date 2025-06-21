import os
import sys
import ctypes
from Exceptions import LibraryNotFound, LibraryFailedToLoad


class Espeak:
    def __init__():
        pass

    def check_lib():
        global lib_espeak_posix
        lib_espeak_posix='libespeak-ng.so'
          
        lib_path = [

         # Termux
        '/data/data/com.termux/files/usr/lib/libespeak-ng.so',
        '/data/data/com.termux/files/usr/local/lib/libespeak-ng.so'     
        
            ]
        try:
            for lib in lib_path:
                if os.path.isfile(lib):
                    return lib     # will return library path if found

            return 1  # return 1 if not found               
        except:
            raise LibraryNotFound(lib_espeak_posix)  # something unexpected  happen.

    def load_library(lib):
         try:
             libespeak = ctypes.cdll.LoadLibrary(lib)
             libespeak.espeak_Initialize.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p]
             libespeak.espeak_Initialize(0,0,None, None)

             libespeak.espeak_SetVoiceByName(b'en')

             def speak(text):
                 text_bytes = text.encode('utf-8')
                 libespeak.espeak_Synth(text_bytes, len(text_bytes), 0, 0, 0, 0, None, None)
                 libespeak.espeak_Synchronize()
                         
                     
          
             speak("")
             print("successfully loaded library")
         except:
             raise LibraryFailedToLoad(lib_espeak_posix)



