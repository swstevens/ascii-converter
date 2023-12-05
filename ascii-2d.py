import numpy as np
from PIL import Image
import sys

output_array_block = ['∙','■','▀','▄','▐','▌','░','▒','▓','█'] 
output_array_nums = [1,2,3,4,5,6,7,8,9,0] 
output_array_symbols = [' ','∙',':','-','+','*','=','%','@','#']
output_array_symbols.reverse() 
def main():
    # print("input file location: ")
    for line in sys.stdin:
        if line == 'q\n' or line == '\n':
            break
        try:
            im = np.array(Image.open(line.rstrip()).convert('L'))
            # resize?
            for x in im[::4]: # works but getting fuzz because i'm not smoothing
                for y in x[::2]:
                    val = round(y/255*10)
                    print(output_array_symbols[val-1],end='')
                print()

        except:
            print('invalid file')
    return

if __name__ == '__main__':
    main()