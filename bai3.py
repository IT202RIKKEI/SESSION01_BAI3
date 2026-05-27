print("--- HỆ THỐNG TIẾP NHẬN BỆNH ÁN ---")

# Nhập họ tên bệnh nhân
while True:
    patient_name = input("Mời bạn nhập họ và tên bệnh nhân: ")

    if not patient_name.strip():
        print("LỖI: Họ tên bệnh nhân không được để trống!")
        continue

    break


# Nhập mã bệnh án
while True:
    medical_record_id = input("Nhập mã bệnh án VD(BN1024, BA9901): ")

    if not medical_record_id.strip():
        print("LỖI: Mã bệnh án không được để trống!")
        continue

    break


# Nhập khoa/phòng khám
while True:
    department = input("Nhập khoa/phòng khám chỉ định: ")

    if not department.strip():
        print("LỖI: Khoa/phòng khám không được để trống!")
        continue

    break


# Chuẩn hóa dữ liệu
patient_name = patient_name.strip().title()
medical_record_id = medical_record_id.strip().upper()
department = department.strip().title()


# Tạo phiếu khám bệnh điện tử
system_message = (
    f"Bệnh nhân: [{patient_name}] - "
    f"Mã BA: [{medical_record_id}] - "
    f"Chuyển tới: [{department}]"
)


# In kết quả
print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(system_message)

print("\nThông báo: Tiếp nhận bệnh án thành công!")