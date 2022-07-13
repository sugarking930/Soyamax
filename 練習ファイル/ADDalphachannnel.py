import cv2
import numpy as np
import os
import glob

def filter(src_file, dst_file):
    print(src_file, dst_file)

    src = cv2.imread(src_file, 0)

    tmp = src.copy()

    dst = cv2.cvtColor(tmp, cv2.COLOR_GRAY2RGBA)
    print(dst.shape)
    cv2.imwrite(dst_file, dst)

if __name__ == 'cheng.jpg':
    list = ['/Users/taisho/Desktop/Soyamax']

    for src_dir in list:
        dst_dir = src_dir

        for s in sorted(glob.glob(os.path.join(src_dir, '*.png'))):
            dn = os.path.dirname(s)
            fn = os.path.basename(s)
            bn, ext = os.path.splitext(fn)
            d = os.path.join(dst_dir, bn + '.png')

            filter(s, d)