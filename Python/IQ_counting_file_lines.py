# Let’s say you’re given a huge 100 GB log file. You want to be able to count how many lines are in the file. 

# How would you count the total number of lines in the file in Python?


CHUNK_SIZE = 8192 * 1024


def count_file_lines(file_path: str) -> int:
    line_ct = 0
    with open(file_path, "r") as f:
        while True:
            if buffer := f.read(size=CHUNK_SIZE):
                line_ct += buffer.count("\n")
            else:
                break
    
    return line_ct
