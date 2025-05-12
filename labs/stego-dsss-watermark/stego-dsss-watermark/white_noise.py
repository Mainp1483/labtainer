import numpy as np
from scipy.io import wavfile

def add_white_noise(input_file='', output_file='attacked_noisy.wav', noise_level=0.005):
    fs, signal = wavfile.read(input_file)
    
    if signal.ndim > 1:
        signal = signal[:, 0] 

    signal = signal.astype(np.float32)
    signal /= np.max(np.abs(signal))  

   
    noise = np.random.normal(0, 1, len(signal))
    noise /= np.max(np.abs(noise))  
    noisy_signal = signal + noise_level * noise

   
    noisy_signal /= np.max(np.abs(noisy_signal))

   
    wavfile.write(output_file, fs, np.int16(noisy_signal * 32767))
    print(f"White noise added. Output saved to: {output_file}")

if __name__ == "__main__":
    add_white_noise()
