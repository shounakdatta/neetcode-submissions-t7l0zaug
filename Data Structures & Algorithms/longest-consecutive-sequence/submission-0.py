class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {}
        res = 0
        for i in nums:
            visited[i] = 1

        def visit(i):
            if visited[i] == 1 and (i+1) in visited:
                visited[i] += visit(i+1)
            return visited[i]

        for i in visited.keys():
            visited[i] = visit(i)
            if res < visited[i]:
                res = visited[i]

        return res

            