if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score]) # Lưu cả cặp [tên, điểm] vào mảng students
        scores.append(score) # Chỉ lưu điểm vào mảng scores để tí nữa lọc
    # Tìm mức điểm thấp thứ hai 
    # Lọc trùng bằng set(), sắp xếp tăng dần bằng sorted()
    unique_scores = sorted(list(set(scores)))
    second_lowest_score = unique_scores[1]
    # Dùng List Comprehension để lọc ra tên các bạn có điểm bằng mức điểm này
    runner_up_names = [student[0] for student in students if student[1] == second_lowest_score]
    # Sắp xếp tên theo thứ tự chữ cái (A-Z) và in ra từng dòng
    runner_up_names.sort()
    for name in runner_up_names:
        print(name)