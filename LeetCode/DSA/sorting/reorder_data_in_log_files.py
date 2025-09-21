import re
from typing import List


def is_alpha_only_with_space(string: str) -> bool:
    return re.fullmatch(r'[a-zA-Z]+(\s[a-zA-Z]+)*', string)


def is_digit_only_with_space(string: str) -> bool:
    return re.fullmatch(r'\d+(\s\d+)*', string)


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []
        
        letter_logs = []
        
        idx = 0
        while idx < len(logs):
            log_details = logs[idx].split()
            identifier, content = log_details[0], " ".join(log_details[1:])
            
            if is_digit_only_with_space(content):
                idx += 1
                continue
            
            letter_logs.append((identifier, content))
            logs.pop(idx)
        
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        logs_parsed = [f"{identifier} {content}" for identifier, content in letter_logs]
        logs_parsed.extend(logs)
        
        return logs_parsed
