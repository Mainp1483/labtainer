import numpy as np
from scipy.io import wavfile

def get_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def dsss_embed(audio_path, text_path, alpha=0.03):
    fs, signal = wavfile.read(audio_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float32) / np.max(np.abs(signal))

    print(f"Audio loaded: {len(signal)} samples, {fs} Hz")

    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
    bits = get_bits(text)
    print(f"Text loaded: {len(text)} characters, {len(bits)} bits")

    s_len = len(signal)
    bit_len = len(bits)

    L = s_len // bit_len
    if L < 8:
        raise ValueError(f"Frame too small (L={L}). Need longer audio or shorter text.")
    
    N = bit_len
    total_len = N * L
    print(f"Calculated L = {L}, total length = {total_len} samples")

    # Chuẩn bị chuỗi DSSS trải phổ
    np.random.seed(42)
    PN = np.random.choice([-1, 1], size=L)
    spread_signal = []

    for b in bits:
        bit_val = 1 if b == '1' else -1
        spread = bit_val * PN  # XOR thực chất là nhân ±1 với PN
        spread_signal.append(spread)

    spread_signal = np.concatenate(spread_signal)

    # Nhúng vào tín hiệu
    stego = signal.copy()
    stego[:total_len] += alpha * spread_signal
    stego = stego / np.max(np.abs(stego))

    wavfile.write("output_dsss.wav", fs, np.int16(stego * 32767))
    print("Stego audio saved to output_dsss.wav")

if __name__ == "__main__":
    audio_path = input("Enter path to input audio WAV file: ").strip()
    text_path = input("Enter path to text file: ").strip()
    dsss_embed(audio_path, text_path)
