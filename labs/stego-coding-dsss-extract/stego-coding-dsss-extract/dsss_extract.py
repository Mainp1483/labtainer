import numpy as np
from scipy.io import wavfile

def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits) - 7, 8):
        byte = bits[i:i+8]
        try:
            chars.append(chr(int(byte, 2)))
        except:
            chars.append('?')
    return ''.join(chars)

def get_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def dsss_extract(audio_path='output_dsss.wav', text_path=None):
    if text_path is None:
        text_path = input("Enter path to original text file: ").strip()

    fs, signal = wavfile.read(audio_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float32) / np.max(np.abs(signal))

    print(f"Stego audio loaded: {len(signal)} samples, {fs} Hz")

    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
    bits = get_bits(text)
    bit_len = len(bits)

    L = len(signal) // bit_len
    if L < 8:
        raise ValueError(f"Frame too small (L={L})")

    N = bit_len
    total_len = N * L
    print(f"Calculated L = {L}, Total frames = {N}")

    np.random.seed(42)
    PN = np.random.choice([-1, 1], size=L)

    xsig = signal[:total_len].reshape(N, L)

    recovered_bits = []
    for frame in xsig:
        corr = np.dot(frame, PN)
        recovered_bits.append('1' if corr > 0 else '0')

    bitstring = ''.join(recovered_bits)
    recovered_text = bits_to_text(bitstring)

    original_bits = np.array(list(map(int, bits)))
    recovered_bits_arr = np.array(list(map(int, bitstring[:len(bits)])))
    ber = np.sum(original_bits != recovered_bits_arr) / len(original_bits) * 100
    nc = np.sum(original_bits * recovered_bits_arr) / (np.linalg.norm(original_bits) * np.linalg.norm(recovered_bits_arr))

    print(f"\nExtracted Text:\n{recovered_text}")
    print(f"BER (Bit Error Rate): {ber:.2f}%")
    print(f"NC (Normalized Correlation): {nc:.4f}")

if __name__ == "__main__":
    dsss_extract()
