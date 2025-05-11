import subprocess

r1 = subprocess.run(
    ["python3", "dsss_extract.py"],
    input="text.txt\n",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True
)
r2 = subprocess.run(
    ["python3", "dsss_extract.py"],
    input="text.txt\n",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True
)
r3 = subprocess.run(
    ["python3", "dsss_extract.py"],
    input="text.txt\n",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True
)

assert r1.stdout != r2.stdout != r3.stdout, "Ket qua khong on dinh"
print("Ket qua on dinh sau nhieu lan trich")
