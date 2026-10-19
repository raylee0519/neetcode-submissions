class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        # 0 = 아직 안 봄
        # 1 = 현재 DFS 경로에서 방문 중
        # 2 = 방문 완료

        def dfs(course):
            if state[course] == 1:
                return False   # cycle

            if state[course] == 2:
                return True    # 이미 확인 완료

            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True