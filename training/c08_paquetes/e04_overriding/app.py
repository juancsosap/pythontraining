# Import conflict
#from printer.line import show
#from printer.text import show

# Import method rename
#from printer.line import show as showl
#from printer.text import show as showt

# Import module rename
#import printer.line as pl
#import printer.text as pt

import printer as pr

if __name__ == "__main__":
    #showt('hola')
    #showl(5)
    
    #pt.show('hola')
    #pl.show(5)

    pr.showt('hola')
    pr.showl(5)