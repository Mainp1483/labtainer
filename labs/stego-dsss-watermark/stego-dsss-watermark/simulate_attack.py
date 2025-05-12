import subprocess

def run_ffmpeg_convert():
    try:
        subprocess.run([
            "ffmpeg", "-y",
            "-i", " ",
            "-codec:a", "libmp3lame",
            "temp.mp3"
        ], check=True)

        subprocess.run([
            "ffmpeg", "-y",
            "-i", "temp.mp3",
            "attacked.wav"
        ], check=True)

        print("Convert success: output_dsss.wav to attacked.wav")

    except subprocess.CalledProcessError as e:
        print("Error run ffmpeg:", e)

if __name__ == "__main__":
    run_ffmpeg_convert()
