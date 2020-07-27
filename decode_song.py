import wave
end_char = '#$%'

song = wave.open('song_embedded.wav', 'rb')

frame_bytes = bytearray(list(song.readframes(song.getnframes())))

received = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]  
# print(type(received[0]))

decoded = ""
for i in range(0, len(received), 8):
	char = chr(int("".join(map(str, received[i:i+8])), 2))
	decoded += char
	if end_char in decoded[len(decoded) - len(end_char) - 1:-1]:
		decoded = decoded.split(end_char)[0]
		break

print(decoded)