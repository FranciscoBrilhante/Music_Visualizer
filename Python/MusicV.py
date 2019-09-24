
 
import argparse
import logging

   
try:
    import sounddevice as sd
    import numpy as np  
    assert np  
    import matplotlib.pyplot as plt
    import serial
    import struct
    import sys
    from scipy import signal 
    import time
    
    ser1 = serial.Serial('COM5',9600) #modify accordingly
    time.sleep(0.5)
    

    def callback(indata, outdata, frames, time, status):
        if status:
            print(status)
            
        N = indata.shape[0]
        L = N/44100
        tuckey_window=signal.tukey(N,0.01,True) 
	#generate the Tuckey window, widely open, alpha=0.01
        ysc=indata[:,0]*tuckey_window                   
        yk = np.fft.rfft(ysc)
        
        
        k = np.arange(yk.shape[0])
        freqs = k/L
        
        amplitude=1000
        
	   #Unfolded for manual tuning
        final=[0,0,0,0,0]
        final[0]=int((sum(abs(yk[0:47]))/amplitude)*100)
        final[1]=int((sum(abs(yk[47:141]))/amplitude)*100)
        final[2]=int((sum(abs(yk[141:329]))/amplitude)*100)
        final[3]=int((sum(abs(yk[329:705]))/amplitude)*100)
        final[4]=int((sum(abs(yk[705:1470]))/amplitude)*100)
        
        
        for i in range(5):
            if (final[i]>100):
                final[i]=100
            final[i]=int((final[i]*14)/100)
            if(final[i]==0):
                final[i]=1        
        #print(final)
        ser1.write([15])
        ser1.write(final)
        
            
        
    #modify accordingly
    with sd.Stream(device=(2, 6), 
                   samplerate=44100, blocksize=2940,
                   latency="low",
                   channels=1,callback=callback):
        
        print('#' * 90)
        print('Start - Fs=44100//Blocksize=2940//Latency=Low//Channels=1')
        print('#' * 90)
        input()
        
except KeyboardInterrupt:
    parser.exit('\nInterrupted by user')




