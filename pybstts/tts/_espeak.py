import os
import sys



class Espeak:
    def __init__():
        pass

    def check_lib():
        
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
            return "error occured"  # something unexpected  happen.


