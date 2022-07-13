import cv2
import numpy as np

img = cv2.imread('104.png', -1)                            # -1はAlphaを含んだ形式(0:グレー, 1:カラー)
img[:, :, 3] = np.where(np.all(img == 255, axis=-1), 0, 255)  # 白色のみTrueを返し、Alphaを0にする
                                                             # 画像保存
cv2.imwrite('/Users/taisho/Desktop/Soyamax/vanish.png', img) 
cv2.imshow('img', img) 