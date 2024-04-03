#đọc 1 file văn bản gồm nhiều dòng
#ghi ra màn hình theo thứ tự ngược lại của các dòng
#VD
#Nam quốc sơn hà
#Nam đế cư
#sang
#Nam đế cư
#Nam quốc sơn hà

# Mở tệp văn bản để đọc
with open('vanban.txt', 'r') as file:
    # Đọc tất cả các dòng vào một danh sách
    lines = file.readlines()

    # In các dòng ra màn hình theo thứ tự ngược lại
    for line in reversed(lines):
        print(line.strip())