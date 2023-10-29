import socket
import pyaudio

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SERVER_IP = 'LAPTOP_2_IP'
SERVER_PORT = 12345

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create an audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

while True:
    data = stream.read(CHUNK)
    sock.sendto(data, (SERVER_IP, SERVER_PORT))

# Clean up
stream.stop_stream()
stream.close()
audio.terminate()
sock.close()
