from textanalizer.charanalizer import CharAnalizer as ca
from textanalizer.wordanalizer import WordAnalizer as wa

def clean(text, chars=False):
    return ca.clean(text) if(chars) else wa.clean(text)
    
def set(text, chars=False):
    return ca.set(text) if(chars) else wa.set(text)

def list(text, chars=False):
    return ca.list(text) if(chars) else wa.list(text)

def count(text, chars=False):
    return ca.count(text) if(chars) else wa.count(text)

def top(text, limit=0, highest=True, chars=False):
    return ca.top(text, limit, highest) if(chars) else wa.top(text, limit, highest)

def length(text, limit=0, highest=True):
    return wa.top(text, limit, highest)