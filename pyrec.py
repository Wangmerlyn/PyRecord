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
    if keydata=="Key.esc":
        Listener.stop()
    #elif Mode.getNoneMode():
        #Mode.ChooseMode(keydata) #选择模式
    if Mode.ChooseMode(keydata):
        return
    elif Mode.getRecordMode():  #如果处于录音模式
        if not Mode.getRecording():
            #if keydata=="'q'":
                #Mode.setPlayMode()
            #else:
                Mode.setRecording(True)
                a=recorder.Recorder(keydata)
                Mode.setKeySet(keydata,a) #没有开始录音
                a.start()   #录音开始
        elif Mode.getRecording() :
            print("Recording mode On\nrecording stopped")
            Mode.setRecording(False)
            Mode.KeyToTrack[keydata].stop()
            #Mode.KeyToTrack[keydata].save()
            Mode.setPlayMode()  #退出录音模式
    elif Mode.getPlayMode():    #如果处于播放模式
        #if keydata=="'r'":
            #Mode.setRecordMode()
        #elif keydata=="'e'":
            #Mode.setFXMode()
        if Mode.getLoopMode():
            #if keydata=="'q'":
                #Mode.setPlayMode()
            if keydata in Mode.KeyToTrack:
                if Mode.KeyToTrack[keydata].getLooping():
                    Mode.KeyToTrack[keydata].stoploop()
                else :
                    Mode.KeyToTrack[keydata]. loop()
            else:
                return 
        else :
            #if keydata=="'q'":
                #Mode.setLoopMode()
            #else:
            if keydata in Mode.KeyToTrack:
                Mode.KeyToTrack[keydata].play()
    elif Mode.getFXMode():
        if Mode.ChoosingTrackMode:
            if keydata=="'q'":
                Mode.setPlayMode()
            Mode.ChosenTrack=Mode.KeyToTrack[keydata]    #传入文件名
            Mode.ChoosingTrackMode=False
            Mode.ChoosingKeyMode=True
            print("Choose A Key For The New Track\n")
        elif Mode.ChoosingKeyMode:
            Mode.NewTrack=recorder.Recorder(keydata)
            Mode.ChoosingKeyMode=False
            Mode.ChoosingFXMode=True
            Mode.ShowFX()
            print("Choose Your Effect\n")
        elif Mode.ChoosingFXMode:
            Mode.ChooseFX(keydata)
            print(Mode.NewTrack.getName()[0:-4])
            Mode.KeyToTrack[Mode.NewTrack.getName()[0:-4]]=Mode.NewTrack
            Mode.ChoosingFXMode=False
            Mode.ChoosingTrackMode=True
            Mode.setPlayMode()
        
    #with open("log.txt",'a') as f:
    #    f.write(str(time.clock())+":"+keydata+'\n')


if __name__=="__main__":
    plt.close('')
    print (sd.query_devices())
    with Listener(on_press=writetofile) as Listener:
        print('a')
        Mode=rc.RecordMode()
        Listener.join()
    print("End")