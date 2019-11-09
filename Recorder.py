import pyaudio
import threading
import wave


class Recorder():
    def __init__(self,Name,chunk=1024,channels=1,rate=64000):
        self.CHUNK=chunk
        self.CHANNELS=channels
        self.FORMAT=pyaudio.paInt16
        self.RATE=rate
        self.__name=Name
        self.__running =True
        self.__FRAMES=[]

    def start(self):
        print("recording")
        threading._start_new_thread(self.__recording,())

    def __recording(self):
        self._running=True
        self._FRAMES=[]
        p=pyaudio.PyAudio()
        stream=p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)
        while(self._running):
            data=stream.read(self.CHUNK)
            self._FRAMES.append(data)
        stream.stop_stream()
        stream.close
        p.terminate
    
        

    def stop(self):
        print("stop")
        self._running=False
    
    def save(self):
        p =pyaudio.PyAudio()
        if not self.__name.endswith(".wav"):
            self.__name+=".wav"
        wf=wave.open(self.__name,'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._FRAMES))
        wf.close()
        print("saved "+self.__name)
    
    def isRecording(self):
        return self._running
    
    def __play(self):
        print("Start Playing "+self.__name)
        p =pyaudio.PyAudio()
        stream=p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,output=True)
        wf=wave.open(self.__name,'rb')
        data=wf.readframes(self.CHUNK)
        while data!=b'':
            stream.write(data)
            data=wf.readframes(self.CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Complete Playing "+self.__name)

    def play(self):
        threading._start_new_thread(self.__play,())

        


if __name__=="__main__":
    print("This is Recorder Module")