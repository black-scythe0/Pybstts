
# Colours 
yellow = '\033[93m'
white = '\033[0m'

class EngineNotInitialized(Exception):
    def __init__(this, raise_msg='you forgot to initialize engine ?'):
        this.raise_msg = raise_msg
        super().__init__(f'{yellow}{this.raise_msg}?{white}')

class EngineFailedToLoad(Exception):
    def __init__(this, raise_msg='Engine failed to Load!'):
        this.raise_msg = raise_msg
        super().__init__(f'{yellow}{this.raise_msg}{white}')

class EngineNotFound(Exception):
    def __init__(this, raise_msg= 'Engine not found'):
        this.raise_msg = raise_msg
        super().__init__(f'{yellow}{this.raise_msg}{white}')


class LibraryNotFound(Exception):
    def __init__(this, lib, raise_msg= 'Not found library'):
        this.raise_msg = raise_msg
        this.lib = lib
        super().__init__(f'{yellow}{this.raise_msg}: {lib}{white}')



class LibraryFailedToLoad(Exception):
    def __init__(this, lib, raise_msg= 'Failed to load'):
        this.raise_msg = raise_msg
        this.lib =  lib
        super().__init__(f'{yellow}{this.raise_msg}: {lib}{white}')

if __name__ == '__main__':
#   raise LibraryFailedToLoad("library")
#    raise LibraryNotFound("library")
    raise EngineNotInitialized
    raise EngineFailedToLoad
