import TrackFX
class RecordMode:
    def __init__(self):
        self.__Recording=False
        self.__Playing=False
        self.__RecordMode=False
        self.__PlayMode=True
        self.__LoopMode=False
        self.__FXMode=False
        self.KeyToTrack={}
        self.ChoosingTrackMode=False
        self.ChoosingFXMode=True
        self.ChoosingKeyMode=False
        self.ChosenTrack=[]
        self.ChosenFX=None
        self.NewTrack=None
        self.track=TrackFX.TrackFX()

    def getRecording(self):
        return self.__Recording
    
    def getKetToTrack(self):
        return self

    def getPlaying(self):
        return self.__Playing
    
    def setRecording(self,Recording):
        self.__Recording=Recording

    def __NoneAllMode(self):
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
            if self.getRecordMode():
                self.setPlayMode() #进入录音模式
            else:
                self.setRecordMode()
            return True
        elif keydata=="'q'":
            if self.getLoopMode():
                self.setPlayMode()
            else:
                self.setLoopMode()
            return True
        elif keydata=="'e'":
            if self.getFXMode():
                self.setPlayMode()
            else:
                self.setFXMode()
                self.ShowFX()
                print("Choose Your FXes")
            return True
        else:
            return False
    
    def ShowFX(self):
        self.track.ShowList()

    
    def ChooseFX(self,keydata): #选择效果
        #self.track.ChooseFX(keydata,self.ChosenTrack,self.NewTrack)
        return self.track.ChooseFX(keydata)
    
    def giveFXtoTrack(self,ChosenTrack,NewTrack):
        self.ChosenFX.FX(ChosenTrack,NewTrack)
        
if __name__=="__main__":
    print("This is RecordControl module")