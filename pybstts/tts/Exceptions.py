class 




class LibraryNotFound(Exception):
    def __init__(self, lib, raise_msg= 'Not found library'):
        self.raise_msg = raise_msg
        self.lib = lib
        super().__init__(f'{self.raise_msg}: {lib}')



class LibraryFailedToLoad(Exception):
    def __init__(self, lib, raise_msg= 'Failed to load'):
        self.raise_msg = raise_msg
        self.lib =  lib
        super().__init__(f'{self.raise_msg}: {lib}')

if __name__ == '__main__':
    raise LibraryFailedToLoad("library")
    raise LibraryNotFound("library")
