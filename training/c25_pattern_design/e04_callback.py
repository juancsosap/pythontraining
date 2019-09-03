class Provider:
    def get(self, path, cbf):
        with open(path) as file:
            text = file.read()
            result = self.analyze(text)
            cbf(result)
    
    def word_count(self, text):
        split_text = text.lower().split(' ')
        words = len(set(split_text))
        count = len(split_text) 
        return (words, count)
    
    def char_count(self, text):
        characters = len(set(text))
        count = len(text)
        return (characters, count)
    
    def analyze(self, text):
        word_info = self.word_count(text)
        char_info = self.char_count(text)
        return (word_info, char_info)

class Requester:
    def make(self, path):
        p = Provider()
        p.get(path, self.done)

    def done(self, result):
        print(result)

if __name__ == "__main__":
    basedir = __file__[:__file__.rfind('/')+1]
    r = Requester()
    r.make(basedir + 'data.txt')