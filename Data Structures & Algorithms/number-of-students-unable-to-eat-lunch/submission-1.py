class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        res = n
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                break
            
        return res