'''
Author: jhont.tao
Date: 2022-03-21 21:16:52
LastEditTime: 2022-03-21 21:21:32
Description: 
'''

## mian.py
import os
import matplotlib.plt as plt
## linux 下，给 $DISPLAY 分配一个变量，以防窗口无法弹出
if __name__ == "__main__":
    os.system('export DISPLAY=:0.0')
    x = [0, 1]
    plt.plot(x)
    print('test matplot')