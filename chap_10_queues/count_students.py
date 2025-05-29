from collections import deque
def count_students(students, sandwiches) -> int:
    student_queue = deque(students)
    sandwiches.reverse()

    attempts = 0
    while student_queue and sandwiches:
        student = student_queue.popleft()
        if student == sandwiches[-1]:
            sandwiches.pop()
            attempts = 0
        else:
            student_queue.append(student)
            attempts += 1
            if attempts == len(student_queue):
                break
        return len(student_queue)