class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoded string pattern: length of string, delimiter (#), string
        if len(strs) == 0:
            return ""
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_string.append(s[j+1:j+1+length])
            i = j+1+length
        return decoded_string
