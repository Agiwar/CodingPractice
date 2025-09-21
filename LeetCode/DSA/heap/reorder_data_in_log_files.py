import re
import heapq
from collections import defaultdict
from typing import List


def is_alpha_only_with_space(string: str) -> bool:
    return re.fullmatch(r'[a-zA-Z]+(\s[a-zA-Z]+)*', string)


def is_digit_only_with_space(string: str) -> bool:
    return re.fullmatch(r'\d+(\s\d+)*', string)


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []

        letter_logs_heap = []
        letter_logs_dict = defaultdict(list)

        idx = 0
        while idx < len(logs):
            log_details = logs[idx].split()
            identifier, content = log_details[0], " ".join(log_details[1:])

            if is_alpha_only_with_space(content):
                letter_logs_heap.append(content)
                letter_logs_dict[content].append(identifier)

                logs.pop(idx)
                continue

            idx += 1

        heapq.heapify(letter_logs_heap)
        
        for identifier_list in letter_logs_dict.values():
            if len(identifier_list) > 1:
                heapq.heapify(identifier_list)
        
        letter_logs_length = len(letter_logs_heap)
        logs_parsed = []
        
        for _ in range(letter_logs_length):
            content = heapq.heappop(letter_logs_heap)
            identifier = letter_logs_dict[content][0] if len(letter_logs_dict[content]) == 1 else heapq.heappop(letter_logs_dict[content])
            
            logs_parsed.append(f"{identifier} {content}")

        logs_parsed.extend(logs)

        return logs_parsed
