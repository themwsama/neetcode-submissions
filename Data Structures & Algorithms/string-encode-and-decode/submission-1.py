
class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s

        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        liststr = []
        while i < len(s):
            # 1. Find the delimiter '#' starting from index i
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract and convert the entire length prefix to an integer
            length = int(s[i:j])
            
            # 3. Use the length to accurately slice the original string
            liststr.append(s[j + 1 : j + 1 + length])
            
            # 4. Move the pointer past the processed string segment
            i = j + 1 + length

        return liststr


