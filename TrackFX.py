import Recorder
import wave
import threading
import pyaudio
class TrackFX:
    def __init__(self):
        self.__FXDic={}
        self.__FXList={}
        self.__FXDic["'a'"]=self.AllFast
        self.__FXList["'A'"]="'AllFast'"

    def ShowList(self):
        print(self.__FXList)

    def Choose(self,keydata,track,ChosenTrack):
        self.__FXDic[keydata](track,ChosenTrack)
        
    #def AllFast(self,track,ChosenTrack):
    #    threading._start_new_thread(self.__AllFast,(track,ChosenTrack))

    def AllFast(self,track,new_track):

        #p=pyaudio.PyAudio()
        #stream=p.open(format=track.FORMAT,channels=track.CHANNELS,rate=track.RATE,output=True)
        wf_track=wave.open(track.getName(),'rb')
        i=0
        print("input a rate\n")
        #input(i)
        frames=[]
        data=wf_track.readframes(track.CHUNK)
        while data!=b'' :
            if i%2==0:
                data=wf_track.readframes(track.CHUNK)
                i%=2
                i+=1
            else :
                wf_track.readframes(track.CHUNK)
                i%=2
                i+=1
            frames.append(data)
        #new_track.RATE*=2
        new_track.save(frames)

        
        
        
    
