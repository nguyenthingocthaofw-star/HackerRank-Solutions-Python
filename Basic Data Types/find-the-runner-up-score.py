if __name__ == '__main__':
    n = int(input())
    #Đọc dữ liệu và chuyển thành một list các số nguyên để có thể 
    arr = list(map(int, input().split()))
    #Loại bỏ các số trùng nhau bằng set() rồi sắp xếp tăng dần bằng sorted()
    unique_scores = sorted(list(set(arr)))
    #In ra phần tử áp chót
    print(unique_scores[-2])
    
'''
mục đích của việc bọc list(...) bên ngoài chính là: 
Ép Python phải đổ toàn bộ các số đó vào một mảng bộ nhớ cố định
Từ đó mới có thể dùng index [0], [1], [i] để truy cập thoải mái.
'''