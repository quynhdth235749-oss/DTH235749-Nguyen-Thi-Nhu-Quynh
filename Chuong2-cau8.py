'''
Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.

1. Các Loại Lỗi Khi Lập Trình
- Lỗi cú pháp (Syntax Error):
+ Mô tả: Là lỗi do viết sai quy tắc cấu trúc của ngôn ngữ lập trình Python, ví dụ như sai dấu ngoặc đơn, thiếu dấu hai chấm, sai chính tả từ khóa.
+ Biểu hiện: Chương trình không thể thông dịch được và sẽ dừng lại ngay lập tức, hiển thị thông báo lỗi Syntax Error. 

- Lỗi ngoại lệ (Exception/Runtime Error):
+ Mô tả: Lỗi xảy ra trong quá trình thực thi chương trình, tức là chương trình đã được thông dịch hoàn chỉnh nhưng gặp phải một lệnh không thực hiện được.
+ Biểu hiện: Chương trình sẽ dừng lại và báo một mã lỗi ngoại lệ cụ thể, ví dụ như lỗi chia cho 0, lỗi đọc tệp không tồn tại, lỗi kết nối mạng. 

- Lỗi logic (Logic Error):
+ Mô tả: Là lỗi nghiêm trọng nhất, xảy ra khi chương trình vẫn chạy bình thường và không gặp lỗi cú pháp hay ngoại lệ, nhưng kết quả trả về lại sai hoặc không chính xác so với yêu cầu.
+ Biểu hiện: Chương trình vẫn chạy trơn tru, nhưng kết quả không như mong đợi, và các lỗi này thường khó tìm, khó phát hiện và khó sửa chữa. 

2. Cách Bắt Lỗi Trong Python
- Bắt Lỗi Ngoại Lệ (Exceptions):
Sử dụng cấu trúc try-except để bắt và xử lý các lỗi ngoại lệ.
Cú pháp:
python
try:
    # Đoạn mã có khả năng gây ra lỗi ngoại lệ
    ket_qua = 10 / 0
except ZeroDivisionError:
    # Xử lý khi lỗi ZeroDivisionError xảy ra
    print("Không thể chia cho 0!")
except Exception as e:
    # Bắt các loại lỗi ngoại lệ khác
    print(f"Đã xảy ra lỗi: {e}")
 
- Kiểm Tra Lỗi Logic:
Thực hiện các bài kiểm tra (unit tests) để kiểm tra tính đúng đắn của các hàm và module.
Sử dụng các công cụ gỡ lỗi (debugger) để theo dõi từng bước thực thi của chương trình và xem xét giá trị các biến. 

- Xử lý Lỗi Cú Pháp:
Trình thông dịch Python sẽ tự động báo lỗi cú pháp khi phát hiện, vì vậy cách tốt nhất là kiểm tra kỹ cú pháp trong quá trình viết mã và sử dụng các trình soạn thảo có khả năng tô sáng cú pháp và báo lỗi sớm. 
Các loại lỗi trong Python

'''