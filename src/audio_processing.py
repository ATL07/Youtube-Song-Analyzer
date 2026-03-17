import librosa
import numpy as np
from langdetect import detect
from src.download import download_audio

def load_audio(path="data/song.wav"):
    # Only load first 60 seconds (faster for testing)
    y, sr = librosa.load(path, duration=60)
    return y, sr

def detect_bpm(y, sr):
    """
    Returns BPM as a float, safe for formatting.
    """
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    # Sometimes tempo comes as ndarray; force float
    if hasattr(tempo, "__len__"):
        tempo = float(tempo[0])
    else:
        tempo = float(tempo)
    
    return tempo


def detect_key(y, sr):
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_avg = np.mean(chroma, axis=1)

    notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
             'F#', 'G', 'G#', 'A', 'A#', 'B']

    return notes[np.argmax(chroma_avg)]


def detect_language(text):
    return detect(text)


def extract_features(y, sr):
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc.mean(axis=1)


def analyze_song(url):
    # Step 1: Download
    download_audio(url)

    # Step 2: Load audio
    y, sr = load_audio()

    # Step 3: Analyze
    results = {
        "BPM": detect_bpm(y, sr),
        "Key": detect_key(y, sr),
    }

    return results