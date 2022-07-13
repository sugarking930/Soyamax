
'''
Into_Gray_Scale と　Transparent の親です
息子がいつも大変お世話になっております。
'''

import Into_Gray_Scale as IGS
import Transparent 
import os


if __name__ == '__main__':
    
    #Modify below path to work
    input_path = "/Users/taisho/Desktop/Soyamax/"
    dir_path = os.listdir(input_path)
    for i in range(len(dir_path)):
        if dir_path[i].endswith("png"):
            print(input_path + "/" + str(dir_path[i]))
            IGS.IntoGray(input_path + "/" + str(dir_path[i]))
            print(input_path + "/" + str(dir_path[i]))
            Transparent.convertImage('/Users/taisho/Desktop/Soyamax/Res/' +  str(input_path + "/" + str(dir_path[i])) +'thresh.png')