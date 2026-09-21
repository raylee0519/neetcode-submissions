class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = dict()
        for i in strs :
            key = " ".join(sorted(i))
            if key not in answer:
                answer[key] = []
            answer[key].append(i)
        return list(answer.values())