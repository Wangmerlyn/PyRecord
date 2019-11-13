import Recorder
import wave
import threading
import pyaudio
class TrackFX:
    def __init__(self):
        self.__ChosenFX=None
        self.__FXDic={}
        self.__FXList={}
        self.__FXDic["'a'"]=AllFast()
        for key in self.__FXDic:
            self.__FXList[key]=self.__FXDic[key].Name
        
    def ShowList(self):
        print(self.__FXList)
    def ChooseFX(self,Keydata):
        #self.__ChosenFX=Keydata
        return self.__FXDic[Keydata]

    def Choose(self,keydata,track,ChosenTrack):
        self.__FXDic[keydata](track,ChosenTrack)
    
    def getDic(self):
        return self.__FXDic
        
class AllFast:
    def __init__(self):
        self.Name="AllFast"
        self.__Number=1
    def FX(self,track,new_track):

        wf_track=wave.open(track[0].getName(),'rb')
        i=0
        print("input a rate\n")
        j=2
        frames=[]
        data=wf_track.readframes(track[0].CHUNK)
        while data!=b'' :
            if i%j==0:
                data=wf_track.readframes(track[0].CHUNK)
                i%=2
                i+=1
            else :
                wf_track.readframes(track[0].CHUNK)
                i%=j
                i+=1
            frames.append(data)
        #new_track.RATE*=2
        new_track.save(frames)
        
    def getNumber(self):
        return self.__Number
        
if __name__=="__main__":
    print("This is FX Library")
        
    
