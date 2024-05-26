import librosa
import os

def getSampleRate(input_file):

    audio, sr = librosa.load(input_file, sr=None)

    return sr

def pitchShift(input_file, semitone_shift):

    audio, sr = librosa.load(input_file, sr=None)

    audio_shifted = librosa.effects.pitch_shift(audio, sr=sr, n_steps=semitone_shift)

    return audio_shifted

def trimAudio(input_file, top_db):

    audio, sr = librosa.load(input_file)
    audio_trimmed = librosa.effects.trim(audio, top_db= top_db)

    return audio_trimmed

def changeSampleRate(input_file, target_sample_rate):

    audio, sr = librosa.load(input_file, sr=None)

    audio_resampled = librosa.resample(audio, 
                                orig_sr=sr,
                                target_sr=target_sample_rate)
    
    return audio_resampled

def getAudioDuration(input_file):
    
    audio, sr = librosa.load(input_file, sr=None)

    duration = librosa.get_duration(y=audio)

    return duration
