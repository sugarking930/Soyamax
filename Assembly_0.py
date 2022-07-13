
'''
Into_Gray_Scale と　Transparent の親です
息子がいつも大変お世話になっております。
'''

import Into_Gray_Scale as IGS
import Transparent 
import os


if __name__ == '__main__':
    
    #Modify below path to work
    input_path = "/Users/taisho/Desktop/Soyamax/TW_FN200"
    dir_path = os.listdir(input_path)
    for i in range(len(dir_path)):
        if dir_path[i].endswith("png"):
            print(input_path + "/" + str(dir_path[i]))
            IGS.IntoGray(input_path, str(dir_path[i]))
            print(input_path + "/" + str(dir_path[i]))
            print(input_path + '/Res/'+ str(dir_path[i]) + 'thresh.png')
            input_trans_path = (input_path + '/Res/')
            input_trans_file = str(dir_path[i]) + 'thresh.png'
            Transparent.convertImage(input_trans_path, input_trans_file)
