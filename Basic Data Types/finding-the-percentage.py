if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    percentage = sum(query_scores) / len(query_scores)
    print(f"{percentage:.2f}")

# 1. name, *line = input().split() -> Dấu * giúp bốc từ đầu cho name, gom hết đống từ còn lại vào List 'line'.
# 2. Dictionary {Key: Value} -> Tìm kiếm trực tiếp bằng student_marks[query_name], KHÔNG dùng vòng lặp for.
# 3. Hàm đo độ dài List trong Python là len(), không phải length().
# 4. print(f"{percentage:.2f}") -> Mẹo F-string luôn in đúng 2 chữ số thập phân (vừa đẹp vừa đúng testcase).