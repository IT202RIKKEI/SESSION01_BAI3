print("--- HỆ THỐNG NHẬP PHÒNG KHÁM ---")

patient_name = input("Mời bạn nhập tên bệnh nhân: ")
portfolio_id = input("Nhập số bệnh án: ")
department = input("nhập vào phòng khám: ")

system_message = f"[{patient_name}] - Mã BA: [{portfolio_id}] - chuyển tới: [{department}]"

print(system_message)


# em xác định kiểu dữ liệu của các biến trước khi cho nhập vào
# em cho nhập dữ liệu vào 3 trường patient_id, patient_temperature, patient_heart_rate
# sau khi nhập vào thì e sử dụng f string, nhúng các biến chứa dữ liệu vào chuỗi để in ra 
# in ra thôi