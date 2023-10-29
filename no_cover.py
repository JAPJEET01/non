import socket
import pyaudio

# Client configuration
SERVER_IP = '192.168.29.157'  # Replace with the server's IP address
SERVER_PORT = 12345
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Create a socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

while True:
    data = client_socket.recv(CHUNK)
    stream.write(data)

# Clean up
client_socket.close()
audio.terminate()
