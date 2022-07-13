import cv2
import numpy as np
 
#読み込む画像のカラースケールがRGBでない場合読み込むことができない
#グレイとなっている場合は何らかの手を加える必要があり
#この手法はRGBを抽出しているから

img = cv2.imread('/Users/taisho/Desktop/Soyamax/練習ファイル/8060.png', 1)                       # -1はAlphaを含んだ形式(0:グレー, 1:カラー)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
color_lower = np.array([0, 0, 0, 255])                 # 抽出する色の下限(BGR形式)
color_upper = np.array([255, 255, 255, 255])                 # 抽出する色の上限(BGR形式)
img_mask = cv2.inRange(hsv, color_lower, color_upper)    # 範囲からマスク画像を作成
img_bool = cv2.bitwise_not(hsv, mask=img_mask)      # 元画像とマスク画像の演算　　　背景を白く　
     

cv2.imwrite('/Users/taisho/Desktop/Soyamax/vanish.png', img_bool) 
cv2.imshow('img_bool', img_bool)   
cv2.imshow('img_mask', img_mask)          
cv2.waitKey(0)





#####not use