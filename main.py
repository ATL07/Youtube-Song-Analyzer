from src.audio_processing import analyze_song

def main():
    print("🚀 YouTube Song Analyzer")

    url = input("Enter YouTube URL: ")

    results = analyze_song(url)

    print(f"🥁 BPM: {results['BPM']:.2f}")
    print(f"🎼 Key: {results['Key']}")
    print("✅ Done!")

if __name__ == "__main__":
    main()