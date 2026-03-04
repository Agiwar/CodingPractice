from typing import List

class Solution:
    """
    [wrong: the main idea is group the strings from strs, each string from strs has its unique groupings,
        so need to define class-level attributes to store some data,
        one is from encode method call, which is a single encoded string from list of string strs,
        the other is storing each string's length from strs,
        after first class calling, class-level attributes are kept there to be shared across all instance
        and then call decode method to convert decoded string to be original strs]

    [correct: this question is asking how the message transferred through machines,
        it's serialization, but using eval is not allowed, and it's not asking design an optimal pipeline,
        so can't use external or tempt status shared across all machines,
        e.g., registry mechanism like schema registry,
        so can only use the encoded single string itself for decode method, anything else is not allowed
        in order to store each string's length, define a separator to record each string and its length,
        this separator may be any non-integer char such as #, !, ? or even $$, @@@, etc]

    time = O(n), n total number of chars in strs plus 
    space = O(1)
    """

    _sep = "!"

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(string)}{Solution._sep}{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        idx = 0
        
        while idx < len(s):
            pt = idx
            length = 0
            
            while s[pt] != Solution._sep:
                length = length * 10 + int(s[pt])
                pt += 1
            
            pt += len(Solution._sep)
            decoded_strs.append(s[pt:(pt + length)])
            
            idx = pt + length
        
        return decoded_strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

codec = Solution()


def test_encode_decode():
    # LeetCode examples
    assert codec.decode(codec.encode(["lint","code","love","you"])) == ["lint","code","love","you"]
    assert codec.decode(codec.encode(["we","say",":","yes"])) == ["we","say",":","yes"]

    # Edge cases
    codec.decode(codec.encode(["Hello","World"])) == ["Hello","World"]
    codec.decode(codec.encode([""])) == [""]

    print("All tests passed")


if __name__ == "__main__":
    test_encode_decode()
