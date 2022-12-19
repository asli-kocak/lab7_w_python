# To do:
# --> get file name / file pointer from c++ code--> howw
# --> open file, check if file is corrupt
# --> close file
# --> write a fake empty file.. bc.. yk ....--
#    at this point, we have a problem. We need to go from jpeg to pnm
# 
# 

import sys
import os
import cv2


def main():


    path = '/Users/aslikocak/Desktop/comp-graphs/Lab7/data'
    dir_list = os.listdir(path) 
    with open('normal_map.ppm', 'w') as fp0:
        fp0.write("New file created")
    
    fp0.close()
    
    with open('texture.ppm', 'w') as fp1:
        fp1.write("New file created")
        fp1.write(sys.argv[1])

    fp1.close()
    # Open the file and read its contents
    # print(sys.argv[1])
    
    # Read the JPEG image
    image = cv2.imread('image.jpeg')

    # Save the image in PPM format
    cv2.imwrite('image.ppm', image)
        
    

if __name__ == '__main__':
    main()