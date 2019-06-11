import serial, struct
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

se = serial.Serial('com3', 9600, timeout=1)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
c = 0
mute = False
while True:
	currentVolume = volume.GetMasterVolumeLevel()
	line = se.readline().strip()
	if len(line)>0:
		c = c + 1
		values = line.decode('ascii').split(',')
		x = int(values[0])
		print(x)
		if x>0 and not mute:
			newVolume = round(x*60/1023)
			if abs(newVolume-currentVolume)> 10:
				if c>5:
					volume.SetMasterVolumeLevel(-newVolume, None)
					c=0
		elif x==-1:
			volume.SetMute(not mute, None)
			mute = not mute
			
		
		
