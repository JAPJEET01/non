import socket
import pyaudio

# Server configuration
SERVER_IP = '192.168.29.157'  # Replace with the actual IP address of the server
SERVER_PORT = 12345
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize PyAudio
audio = pyaudio.PyAudio()
input_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
output_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)
print(f"Listening for incoming connections on {SERVER_IP}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

try:
    while True:
        data = client_socket.recv(CHUNK)
        output_stream.write(data)

        # Capture audio from the server and send it to the client
        input_data = input_stream.read(CHUNK)
        client_socket.send(input_data)
except KeyboardInterrupt:
    pass

# Clean up
server_socket.close()
audio.terminate()
