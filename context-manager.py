from contextlib import contextmanager, ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self
    
    def __exit__(self, *exc):
        print('</p>')
        return self

@makeparagraph()
def my_html():
    print('Hello world')
    print('my bad')


my_html()
