import numpy as np
from pprint import pprint
from scipy.io.wavfile import write

samplerate = 44100  # Frequecy in Hz


def get_wave(freq, duration=0.5):
    '''
    Function takes the "frequecy" and "time_duration" for a wave 
    as the input and returns a "numpy array" of values at all points 
    in time
    '''
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave


def get_piano_notes():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 261.63  # Frequency of Note C4

    note_freqs = {octave[i]: base_freq * pow(2, (i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0  # silent note

    return note_freqs


def get_song_data(music_notes):
    '''
    Function to concatenate all the waves (notes)
    '''
    note_freqs = get_piano_notes()  # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

# To get a 1 second long wave of frequency 440Hz
a_wave = get_wave(440, 1)
note_freqs = get_piano_notes()

pprint(note_freqs)
#wave features
print(len(a_wave))  # 44100
print(np.max(a_wave))  # 4096
print(np.min(a_wave))  # -4096

music_notes = 'C-C-G-G-A-A-G-F-F-E-E-D-D-C-G-G-F-F-E-E-D-G-G-F-F-E-E-D-C-C-G-G-A-A-G-F-F-E-E-D-D-C'
# music_notes = 'D-f-D-A-A-D-F-D-A-A-D-F-D--A-A'
data = get_song_data(music_notes)

data = data * (16300/np.max(data))  # Adjusting the Amplitude (Optional)
write('twinkle-twinkle.wav', samplerate, data.astype(np.int16))
