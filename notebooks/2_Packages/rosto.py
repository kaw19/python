# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
from pylab import imread, imshow, figure, subplot
from scipy.signal import sepfir2d, gaussian
from numpy import uint8, float32, array

def norm8(img):
  mn = img.min()
  mx = img.max()
  I = (img - mn)/(mx - mn)*255
  return I.astype(uint8)

filtro = gaussian(30, 20.0).astype(float32)
# possível solução
lena = array(imread('dat/lena.dat'))
face = lena[180:390,250:350]                             # rosto
figure(figsize=(10,8), dpi=80)
subplot(2,2,1); imshow(face)
emba = sepfir2d(lena[200:390,250:350], filtro, filtro)   # embaçamento
embb = norm8(emba)
subplot(2,2,2); imshow(embb)
#copia.setflags(write=1)
lena[200:390,250:350] = embb
subplot(2,1,2); imshow(lena)