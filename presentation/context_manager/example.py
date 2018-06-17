from contextlib import contextmanager

class MyFile():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

@contextmanager
def MyFile_2(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

with MyFile_2('foo.txt','a') as file:
    file.write('mithil')