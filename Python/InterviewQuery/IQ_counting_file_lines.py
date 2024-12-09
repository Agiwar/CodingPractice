# Let’s say you’re given a huge 100 GB log file. You want to be able to count how many lines are in the file. 

# How would you count the total number of lines in the file in Python?


def count_file_lines(file_path: str, chunk_size: int = 8192 * 1024) -> int:
    # 8192 * 1024 = 8MB
    line_ct = 0
    with open(file_path, "r") as f:
        while True:
            if buffer := f.read(size=chunk_size):
                line_ct += buffer.count("\n")
            else:
                break
    
    return line_ct
