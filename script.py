import os

def write_file_info(output_file, directory):
    try:
        with open(output_file, 'w', encoding='utf-8') as extract_file:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    extract_file.write(f"File: {file_path}\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            extract_file.write("Content:\n")
                            extract_file.write(content + "\n\n")
                    except Exception as e:
                        extract_file.write(f"Could not read file. Error: {e}\n\n")
        print(f"File information written to {output_file}")
    except Exception as e:
        print(f"Failed to write to {output_file}. Error: {e}")

if __name__ == "__main__":
    output_file = "extract.txt"
    directory = input("Enter the directory to scan: ") or os.getcwd()
    write_file_info(output_file, directory)
