basedir = __file__[:__file__.rfind('/')+1]

import textanalizer as ta

path = basedir + 'data.txt'

if __name__ == "__main__":
   with open(path) as file:
      text = file.read()

      result = ta.top(text, 10)
      print(result)

      result = ta.top(text, 10, chars=True)
      print(result)
