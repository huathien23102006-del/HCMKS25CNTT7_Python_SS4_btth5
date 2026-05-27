total_bill = 0
total_rev = 0
big_bill = 0
i = 1
while True:
    bill = int(input(f"Khách hàng {i} - Nhập giá trị hóa đơn: "))
    total_rev += bill
    total_bill += 1

    if (bill >= 1000000):
        big_bill += 1

    choose = input("Có muốn tiếp tục nhập không? (C/K): ")
    if(choose.lower() == "k"):
        break
    
    i += 1

print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print("Tổng hóa đơn đã xử lý: ",total_bill)
print("Tống doanh thu ngày hôm nay: ",total_rev)
print("Số hóa đơn lớn (>= 1,000,000): ", big_bill)
print("Tỷ lệ hóa đơn lớn đạt: ", (big_bill / total_bill) * 100,"%"," trên tổng số đơn hàng.")
