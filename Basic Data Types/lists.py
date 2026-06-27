if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range (N):
        # Tách tên lệnh và các tham số đi kèm (nếu có)
        command, *args = input().split()
        # Chuyển các tham số trong args từ chữ (string) thành số nguyên (int)
        args = list(map(int, args))
        if command == "insert":
            my_list.insert(args[0], args[1]) # args[0] là index i, args[1] là số e
        elif command == "print":
            print(my_list)
        elif command == "remove":
            my_list.remove(args[0])
        elif command == "append":
            my_list.append(args[0])
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
#  args = list(map(int, args)) -> Dùng map() như một băng chuyền để ép kiểu toàn bộ phần tử trong mảng sang số nguyên cùng lúc.
#  my_list.pop() -> Xóa và trả về phần tử cuối cùng của mảng (giống như bốc cái đĩa trên cùng ra khỏi chồng đĩa).
#  Phân biệt pop(index) và remove(value) -> pop() xóa theo vị trí (chỉ số), còn remove() xóa theo giá trị chính xác.