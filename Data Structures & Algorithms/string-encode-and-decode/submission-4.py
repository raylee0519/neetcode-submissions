class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs :
            result += f"{len(i)}#{i}"
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s) :
            j = i
            while j < len(s) and s[j] != "#" :
                j += 1
            length = int(s[i:j])
            result.append(s[j+1 : j+length+1])
            i = j + length + 1 # 다음 걸로 이동
        return result