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
    if Mode.ChooseMode(keydata):
        return
    elif Mode.getRecordMode():  #如果处于录音模式
        if not Mode.getRecording():
                Mode.setRecording(True)
                a=recorder.Recorder(keydata)
                Mode.setKeySet(keydata,a) #没有开始录音
                a.start()   #录音开始
        elif Mode.getRecording() :
            print("Recording mode On\nrecording stopped")
            Mode.setRecording(False)
            Mode.KeyToTrack[keydata].stop()
            Mode.setPlayMode()  #退出录音模式
    elif Mode.getPlayMode():    #如果处于播放模式
        if Mode.getLoopMode():
            if keydata in Mode.KeyToTrack:
                if Mode.KeyToTrack[keydata].getLooping():
                    Mode.KeyToTrack[keydata].stoploop()
                else :
                    Mode.KeyToTrack[keydata].loop()
            else:
                return 
        else :
            if keydata in Mode.KeyToTrack:
                print(Mode.KeyToTrack[keydata].getLength())
                Mode.KeyToTrack[keydata].play()
    elif Mode.getSyncMode():
        if Mode.ChoosingSyncMode:
            Mode.ChosenTrackTime=Mode.KeyToTrack[keydata].getLength()
            Mode.ChoosingSyncMode=False
            print("Choose A Track To Record\n")
        else:
            if not Mode.getRecording():
                    Mode.setRecording(True)
                    a=recorder.Recorder(keydata)
                    Mode.setKeySet(keydata,a) #没有开始录音
                    a.startSync(Mode.ChosenTrackTime)   #录音开始
                    print("Recording Start\n")
            elif Mode.getRecording() :
                print("recording stopped\n")
                Mode.setRecording(False)
                Mode.KeyToTrack[keydata].stop()
                Mode.ChoosingSyncMode=True
                Mode.setPlayMode()  #退出录音模式
        
            
    elif Mode.getFXMode():
        if Mode.ChoosingFXMode:
            Mode.ChosenFX=Mode.ChooseFX(keydata)    #选择完效果
            Mode.ChoosingFXMode=False   #选择完效果
            Mode.ChoosingTrackMode=True #选择完效果
            print("Choose Your Tracks")
        elif Mode.ChoosingTrackMode:
            Mode.ChosenTrack.append(Mode.KeyToTrack[keydata])
            if len(Mode.ChosenTrack)>=Mode.ChosenFX.getNumber():
                Mode.ChoosingTrackMode=False
                Mode.ChoosingKeyMode=True
                print("Choose A Key For The New Track\n")
        elif Mode.ChoosingKeyMode:
            Mode.NewTrack=recorder.Recorder(keydata)
            Mode.KeyToTrack[keydata]=Mode.NewTrack
            Mode.giveFXtoTrack(Mode.ChosenTrack,Mode.NewTrack)
            Mode.ChoosingKeyMode=False
            Mode.ChoosingFXMode=True
            Mode.ChosenTrack=[]
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