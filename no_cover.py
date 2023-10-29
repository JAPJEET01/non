import socket
import pyaudio

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 12345

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

# Create an audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

while True:
    data, addr = sock.recvfrom(CHUNK)
    stream.write(data)

# Clean up
stream.stop_stream()
stream.close()
audio.terminate()
sock.close()
