import os

def read_bits(file_path):
    with open(file_path, 'rb') as f:
        while (byte := f.read(1)):
            for i in range(7, -1, -1):
                yield (byte[0] >> i) & 1

def write_bits(file_path, bits):
    with open(file_path, 'w') as f:
        for bit in bits:
            f.write(str(bit))

def main():
    file_path = input("Enter the file path: ")
    dir_path = os.path.dirname(file_path)
    output_path = os.path.join(dir_path, "output.txt")

    bits = read_bits(file_path)
    write_bits(output_path, bits)

    print(f"Bits written to {output_path}")

if __name__ == "__main__":
    main()
