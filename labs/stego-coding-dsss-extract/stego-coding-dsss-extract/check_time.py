import subprocess
import time

start = time.time()

proc = subprocess.run(
    ["python3", " "],
    input="text.txt\n",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True
)

elapsed = time.time() - start

assert elapsed < 3, f"Script chay qua cham: {elapsed:.2f} giây"
print(f"Script chay trong nguong het {elapsed:.2f} giây")
