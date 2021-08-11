import re

class RegexUtils:
    # load from the regex string a regex finder function
    @staticmethod
    def getter(regex):
        cre = re.compile(regex)
        return lambda text: cre.findall(text)
