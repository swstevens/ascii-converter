import numpy as np
from PIL import Image
import sys

output_array = ['∙','■','▀','▄','▐','▌','░','▒','▓','█'] #TODO: better implementation of this array, maybe a hleper function?
output_array_nums = [1,2,3,4,5,6,7,8,9,0] #TODO: better implementation of this array, maybe a hleper function?
def main():
    print("input file location: ")
    for line in sys.stdin:
        if line == 'q\n' or line == '\n':
            break
        im = np.array(Image.open(line.rstrip()).convert('L'))
        # resize?
        for x in im[::2]:
            for y in x[::2]:
                val = round(y/255*10)
                print(output_array_nums[val-1],end='')
            print()
        # now we've got the 2d array getting parsed and printed. What about using the square of values to form an average?
        # it's easy to scale down but I want to do average stuff so that I can use some of the more interesting characters
        # some kind of blending effect would be nice
        # for i, j in [(0, 1), ('a', 'b')]:

        # so it's a 2d array based on the the values in im.shape
        # so to transform, take the value, divide by 255, round to one in array of characters
        # then print that character with either a space or nothing (end='')
        # then can possibly move onto complex simplifications like scale downs 
        # maybe output to a text file? then can be easier to ensure line accuracy
        print(im)
    return

if __name__ == '__main__':
    main()