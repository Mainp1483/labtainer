def parse_result(file_path):
    ber, nc = None, None
    with open(file_path) as f:
        for line in f:
            if "BER" in line:
                ber = float(line.strip().split(":")[1].replace("%", ""))
            elif "NC" in line:
                nc = float(line.strip().split(":")[1])
    return ber, nc

def main():
    ref_ber = 0.00
    ref_nc = 1.0000

    ber, nc = parse_result("result.txt")
    print(f"Extracted BER: {ber:.2f}%, NC: {nc:.4f}")
    print(f"Reference BER: {ref_ber:.2f}%, NC: {ref_nc:.4f}")

    if ber <= 10 and nc >= 0.90:
        print("Extraction SUCCESSFUL – watermark integrity maintained.")
    else:
        print("Extraction FAILED – watermark is degraded.")

if __name__ == "__main__":
    main()
