from pynput.keyboard import Listener
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import threading
import pyaudio 
import wave

import RecordControl as rc  #记录按键，控制状态
import Recorder as recorder #录音器


def writetofile(key):
    keydata =str(key)
    print(keydata)
    if keydata=="Key.enter":
        Listener.stop()
    #elif Mode.getNoneMode():
        #Mode.ChooseMode(keydata) #选择模式
    elif Mode.getRecordMode():  #如果处于录音模式
        if not Mode.getRecording():
            if keydata=="'q'":
                Mode.setPlayMode()
            else:
                Mode.setRecording(True)
                a=recorder.Recorder(keydata)
                Mode.setKeySet(keydata,a) #没有开始录音
                a.start()   #录音开始
        elif Mode.getRecording() :
            print("Recording mode On\nrecording stopped")
            Mode.setRecording(False)
            Mode.KeyToTrack[keydata].stop()
            Mode.KeyToTrack[keydata].save()
            Mode.setPlayMode()  #退出录音模式
    elif Mode.getPlayMode():    #如果处于播放模式
        if keydata=="'r'":
            Mode.setRecordMode()
        elif keydata=="'e'":
            Mode.setFXMode()
        elif Mode.getLoopMode():
            if keydata=="'q'":
                Mode.setPlayMode()
            elif Mode.KeyToTrack[keydata].getLooping():
                Mode.KeyToTrack[keydata].stoploop()
            else :
                Mode.KeyToTrack[keydata].loop()
        else :
            if keydata=="'q'":
                Mode.setLoopMode()
            else:
                Mode.KeyToTrack[keydata].play()
    elif Mode.getFXMode():
        if keydata=="'q'":
            Mode.setPlayMode()
        elif Mode.ChoosingTrackMode:
            Mode.ChosenTrack=Mode.KeyToTrack[keydata]
            Mode.ChoosingTrackMode=False
            Mode.ShowFX()
        elif Mode.ChoosingFXMode:
            Mode.ChooseFX(keydata)
            Mode.ChoosingFXMode=False
        else:
            Mode.KeyToTrack[keydata]=Mode.ChosenTrack
            Mode.ChoosingTrackMode=True
        
    with open("log.txt",'a') as f:
        f.write(str(time.clock())+":"+keydata+'\n')


if __name__=="__main__":
    plt.close('')
    print (sd.query_devices())
    with Listener(on_press=writetofile) as Listener:
        print('a')
        Mode=rc.RecordMode()
        Listener.join()
    print("End")