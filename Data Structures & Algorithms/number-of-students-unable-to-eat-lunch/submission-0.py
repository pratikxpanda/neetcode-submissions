class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        students_queue = deque(students)
        res = n

        for sandwich in sandwiches:
            cnt = 0
            
            while cnt < n and students_queue[0] != sandwich:
                students_queue.append(students_queue.popleft())
                cnt += 1
            
            if students_queue[0] == sandwich:
                students_queue.popleft()
                res -= 1
            else:
                break
            
        return res