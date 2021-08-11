import os, re

basedir = __file__[:__file__.rfind('\\')+1]
if basedir != '': os.chdir(basedir)


def get_data(line, pattern):
    result = []
    
    regex = re.compile(pattern)
    if regex.groups > 0:
        match = regex.match(line)
        for group in match.groups():
            result.append(group)
    
    return result

def get_block(text, tag, level=0, end='exit', data=[]):
    inipattern = f'^\\s{{{ level*4 }}}{ tag }$'
    iniregex = re.compile(inipattern)
    endpattern = f'^\\s{{{ level*4 }}}{ end }$'
    endregex = re.compile(endpattern)

    active = False
    result = ''
    for line in text.splitlines(True):
        if iniregex.match(line): 
            active = True
            data.extend(get_data(line, inipattern))
        if active: result += line
        if endregex.match(line): active = False
    
    return (result, data)

def get_blocks(text, path):
    tags = path.split('|')
    data = []
    for level, tag in enumerate(tags):
        text, data = get_block(text, tag, level, data=data)
    
    print(data)
    return text

if __name__ == "__main__":
    path = 'configure|router (.*)|interface (.*)'

    result = get_blocks(text, path)
    print(result)
