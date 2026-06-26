# new_list = [biểu thức for biến in vòng lặp if điều kiện]
"""
Đẹp và Gọn = Dùng.
Dài và Rối (khiến code khó đọc hơn) = Bỏ, quay về dùng vòng lặp thường.
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if i + j + k != n]
    print(result)