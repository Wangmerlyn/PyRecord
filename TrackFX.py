class TrackFX:
    def __init__(self):
        self.__FXDic={}
        self.__FXDic["'a'"]=self.AllFast
        self.__FXList={}
        self.__FXList["'a'"]="'AllFast'"
        pass
    def ShowList(self):
        print(self.__FXList)
    def Choose(self,keydata,track):
        self.__FXList[keydata](track)
    def AllFast(self,track):
        track
    
