class Solution:
    def encode(self, strs: List[str]) -> str:
        word = ""

        for s in strs:
            word += str(len(s)) + "#" + s

        return word

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # '#' 위치 찾기
            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j]) # 스트링 길이 가져오기 (숫자로 되어있는 것)

            # '#' 다음부터 length개만 가져오기
            result.append(s[j + 1 : j + 1 + length])

            # 다음 문자열의 길이 정보 위치로 이동
            i = j + 1 + length

        return result