import wave
def decode(path):

    end_char = '#$%'

    # song = wave.open('song_embedded.wav', 'rb')
    song = wave.open(path, 'rb')

    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    received = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]  
    # print(type(received[0]))

    decoded = ""
    for i in range(0, len(received), 8):
        '''
            map(str, [int list]): will convert all ints to string: [1,0,1]: ['1','0','1']
            .join(): convert list to string
            int(string, 2): convert given string to integer and the given base is 2(binary)
            chr: convert the given integer to it's corresponding character
        '''
        char = chr(int("".join(map(str, received[i:i+8])), 2))
        decoded += char
        if end_char in decoded[len(decoded) - len(end_char) - 1:-1]:
            decoded = decoded.split(end_char)[0]
            break

    return decoded