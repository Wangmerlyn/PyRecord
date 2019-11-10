import TrackFX
class RecordMode:
    def __init__(self):
        self.__Recording=False
        self.__Playing=False
        self.__RecordMode=False
        self.__PlayMode=True
        #self.__NoneMode=True
        self.__LoopMode=False
        self.__FXMode=False
        self.KeyToTrack={}
        self.ChoosingTrackMode=True
        self.ChoosingFXMode=False
        self.ChosenTrack=None
        self.track=TrackFX.TrackFX()

    def getRecording(self):
        return self.__Recording
    
    def getKetToTrack(self):
        return self

    def getPlaying(self):
        return self.__Playing
    
    def setRecording(self,Recording):
        self.__Recording=Recording
        return None

    def __NoneAllMode(self):
        #self.__NoneMode=False
        self.__PlayMode=False
        self.__RecordMode=False
        self.__LoopMode=False
        self.__FXMode=False

    def setRecordMode(self):
        print("Recording mode ON\n")
        self.__NoneAllMode()
        self.__RecordMode=True

    def getRecordMode(self):
        return self.__RecordMode

    def setPlayMode(self):
        print("Play Mode On\n")
        self.__NoneAllMode()
        self.__PlayMode= True

    def getPlayMode(self):
        return self.__PlayMode
    
    #def setNoneMode(self):
    #    print("None Mode ON\n")
    #    self.__NoneAllMode()
    #    self.__NoneMode=True

   # def getNoneMode(self):
   #     return self.__NoneMode
    
    def setLoopMode(self):
        print("Loop Mode On\n")
        self.__NoneAllMode()
        self.__PlayMode=True
        self.__LoopMode=True
    
    def getLoopMode(self):
        return self.__LoopMode
    
    def setFXMode(self):
        print("FX Mode On\n")
        self.__NoneAllMode()
        self.__FXMode=True
    
    def getFXMode(self):
        return self.__FXMode
    
    def setKeySet(self,keydata,track):
        self.KeyToTrack[keydata]=track
    
    def ChooseMode(self,keydata):
        if keydata=="'r'":
            self.setRecordMode() #进入录音模式
        elif keydata=="'w'":
            self.setPlayMode()
        elif keydata=="'e'":
            self.setFXMode()
    
    def ShowFX(self):
        self.track.ShowList()
        pass
    
    def ChooseFX(self,keydata):
        self.track.Choose(keydata,self.ChosenTrack)
        pass
        
    
if __name__=="__main__":
    print("This is RecordControl module")