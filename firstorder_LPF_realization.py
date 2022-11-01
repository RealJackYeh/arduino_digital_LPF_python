from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
signalFreq = [2,50]
w0 = 2 * np.pi * 10  # filter cut-off frequency 5Hz
num = w0; den = [1, w0]
lowPass = signal.TransferFunction(num, den)  #連續時間轉移函數
print(lowPass)
dt = 1/1000   # 採樣時間 1/1000Hz
dlowPass = lowPass.to_discrete(dt, method='gbt', alpha=0.5) #將連續時間轉移函數數位化，使用雙線性轉換
print(dlowPass) 
b = dlowPass.num  #分母係數
a = dlowPass.den #分子係數
print('filter coefficient b_i: ' + str(b))
print('filter coefficient a_i: ' + str(a[1:]))
w, mag, phase = signal.bode(lowPass) #畫出波德圖
plt.figure()
plt.subplot(2,1,1)
plt.semilogx(w, mag)
for sf in signalFreq:
    plt.semilogx([sf*2*np.pi, sf*2*np.pi], [min(mag), max(mag)], 'k:')
    plt.semilogx([w0, w0], [min(mag), max(mag)], 'r:')
plt.xlabel('$\omega$ (rad/s)')
plt.ylabel('Magnitude ($dB$)')
plt.subplot(2,1,2)
plt.semilogx(w, phase)
for sf in signalFreq:
    plt.semilogx([w0, w0], [min(phase), max(phase)], 'r:')
plt.xlabel('$\omega$ (rad/s)')
plt.ylabel('Phase ($^\circ$)')
plt.show()