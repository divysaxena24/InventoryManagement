import time


f = open("Inventory.txt", "r")
products = [line.strip().split(",") for line in f if line.strip()]
f.close()


print(f"{'ID':<5} {'Product Name':<25} {'Price (₹)':<10} {'Quantity':<10}")
print("-" * 55)
for prod in products:
    print(f"{prod[0]:<5} {prod[1]:<25} {prod[2]:<10} {prod[3]:<10}")


ui_prod_username = input("\n Enter Username: ")
ui_prod_number = input("Enter Mobile Number: ")
ui_prod_mail = input("Enter Mail: ")
ui_prod_id = input("Enter Product ID: ")
ui_prod_qn = int(input("Enter Product Quantity: "))

updated_product_lst = []


for prod_det in products:
    if prod_det[0] == ui_prod_id:
        if int(ui_prod_qn) <= int(prod_det[3]):
            
            print("----------------------------")
            print("Product Name     :", prod_det[1])
            print("Product Price    :", prod_det[2])
            print("Product Quantity :", prod_det[3])
            bill = int(ui_prod_qn) * int(prod_det[2])
            print("----------------------------")
            print("Bill Amount      :", bill)
            print("----------------------------")

            fd = open("Sale.txt", "a")
            sales_det = ",".join([
                ui_prod_username,
                ui_prod_number,
                ui_prod_mail,
                ui_prod_id,
                str(ui_prod_qn),
                str(bill),
                time.ctime()
            ]) + "\n"
            fd.write(sales_det)
            fd.close()

            prod_det[3] = str(int(prod_det[3]) - int(ui_prod_qn))

        else:
            
            print("Sorry we only have", prod_det[3], "in stock.")
            ch = input("Would you like to purchase the available quantity? (Y/y): ")
            if ch.lower() == 'y':
                bill = int(prod_det[3]) * int(prod_det[2])
                print("----------------------------")
                print("Product Name     :", prod_det[1])
                print("Product Price    :", prod_det[2])
                print("Product Quantity :", prod_det[3])
                print("----------------------------")
                print("Bill Amount      :", bill)
                print("----------------------------")

                fd = open("Sale.txt", "a")
                sales_det = ",".join([
                    ui_prod_username,
                    ui_prod_number,
                    ui_prod_mail,
                    ui_prod_id,
                    prod_det[3],
                    str(bill),
                    time.ctime()
                ]) + "\n"
                fd.write(sales_det)
                fd.close()

                prod_det[3] = '0'
            else:
                print("Purchase Cancelled.")

    updated_product_lst.append(prod_det)


lst = []
for i in updated_product_lst:
    if len(i) == 4:
        prod = ",".join(i) + "\n"
        lst.append(prod)

if lst:
    lst[-1] = lst[-1].rstrip("\n")

fd = open("Inventory.txt", "w")
fd.writelines(lst)
fd.close()
