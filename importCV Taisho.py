import cv2
import glob
import os
import numpy as np

#関数を作るお！
def mask(path):
     img = cv2.imread(path, 1)  
     lower = np.array([n, n, n])  n=[90,60,30]                         # Define lower and uppper limits
     upper = np.array([255, 255, 255])
     thresh = cv2.inRange(img, lower, upper)                           # Create mask to only select black
     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))      # apply morphology
     morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
     mask = 255 - morph                                                # invert morp image
     result = cv2.bitwise_and(img, img, mask=mask)                     # apply mask to image
     return img


def bundle_mask(dir):
    path_list = glob.glob(dir + '\*')       # 指定されたディレクトリ内の全てのファイルを取得
    name_list = []                          # ファイル名の空リストを定義
    ext_list = []  


    for i in path_list:
          file = os.path.basename(i)          # 拡張子ありファイル名を取得
          name, ext = os.path.splitext(file)  # 拡張子なしファイル名と拡張子を取得
          name_list.append(name)              # 拡張子なしファイル名をリスト化
          ext_list.append(ext)                # 拡張子をリスト化
 
          out_path = os.path.join(*[dir, name + '_resize' + ext]) # 保存パスを作成
 
          img = mask(i)                     # mask関数を実行
          cv2.imwrite(out_path, img)          # 画像を保存
    return



bundle_mask('dir')









##############これ以降は消して実行#############


# Read image
path_name = '/Users/taisho/Desktop/Soyamax/'
file_name = '101.jpg'
img = cv2.imread(path_name + file_name)
cv2.imshow("image", img)
hh,ww = img.shape[:2]

# threshold on white
# Define lower and uppper limits
lower = np.array([90, 90, 90])
upper = np.array([255, 255, 255])

# Create mask to only select black
thresh = cv2.inRange(img, lower, upper)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# invert morp image
mask = 255 - morph

# apply mask to image
result = cv2.bitwise_and(img, img, mask=mask)



# save results
cv2.imshow("img", img)
cv2.imwrite(('/Users/taisho/Desktop/Soyamax/'+ str(file_name) +'thresh.png'), thresh)
cv2.imwrite(('/Users/taisho/Desktop/Soyamax/' + file_name+'pills_morph.png'), morph)
cv2.imwrite('/Users/taisho/Desktop/Soyamax/pills_mask.png', mask)
cv2.imwrite('/Users/taisho/Desktop/Soyamax/pills_result.png', result)
print("???")

cv2.imshow('thresh', thresh)
cv2.imshow('morph', morph)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()