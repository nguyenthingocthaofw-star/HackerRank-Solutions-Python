if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

#Chạy python2
# 1. Tuple t = tuple(...) -> Giống List nhưng bọc trong ngoặc () và KHÔNG THỂ thay đổi phần tử sau khi tạo (Immutable).
# 2. Hàm hash(t) -> Biến một Tuple thành một số nguyên duy nhất (như dấu vân tay dữ liệu). Chỉ hash được vật bất biến.