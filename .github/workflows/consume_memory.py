# consume_memory.py
import numpy as np

def consume_ram():
    print("Attempting to allocate 8GB of RAM...")
    try:
        # Allocate an array of float64 numbers, each consuming 8 bytes.
        # 8GB = 8 * 1024^3 bytes, so the number of elements is (8 * 1024^3) / 8.
        arr = np.zeros((1024**3), dtype=np.float64)
        print("Successfully allocated approximately 8GB of RAM.")
    except MemoryError:
        print("Failed to allocate 8GB of RAM.")

if __name__ == "__main__":
    consume_ram()
