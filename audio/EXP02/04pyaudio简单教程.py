import pyaudio
p = pyaudio.PyAudio()

devices = p.get_device_count()    # Return the number of PortAudio Host APIS
print(devices)