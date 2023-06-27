from tkinter import *
import os
from PIL import ImageTk,Image 

#main screen 
master = Tk()
master.title('TN Pay')
master.configure(bg="white")
master.geometry('410x450+700+200')
#var
#Function
def num_account_user():
    try:
        with open('num_acc_user.txt', 'r') as file:
            num_acc_user = int(file.read())
    except FileNotFoundError:
        num_acc_user = 1
    
    account = str(num_acc_user).zfill(8)
    
    with open('num_acc_user.txt', 'w') as file:
        file.write(str(num_acc_user + 1))
    return account
def finish_reg():
    global check_ac_reg
    check_ac_reg = 0
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    account = temp_account.get()
    password = temp_password.get()
    num_account = temp_num_account
    all_account = os.listdir()
    if name == "" or age == "" or gender == "" or account == "" or password == "" or num_account=="":
        notif.config(fg="red", text = "Vui lòng điền đầy đủ thông tin ")
        return
    for name_check in all_account:
        if account == name_check:
            notif.config(fg="red", text= " Tên tài khoản đã tồn tại")
            return
    new_file = open(account,"w")
    new_file.write(account+'\n')
    new_file.write(password+'\n')
    new_file.write(name+'\n')
    new_file.write(age+'\n')
    new_file.write(gender+'\n')
    new_file.write(num_account+'\n')
    new_file.write('0')
    new_file.close()
    notif.config(fg="green", text ="Tài khoản được tạo thành công")
    check_ac_reg = 1
    delay_time = 200
    register_screen.after(delay_time, register_screen.destroy)

def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_account
    global temp_password
    global notif
    global register_screen
    global temp_num_account
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_account = StringVar()
    temp_password = StringVar()
    temp_num_account = num_account_user()
    #screen
    register_screen = Toplevel(master,width=40)
    register_screen.geometry('410x350+700+200')
    register_screen.title("Đăng kí")
    register_screen.configure(bg="white")
    #label
    Label(register_screen, text = "Nhập thông tin của bạn", font = ('Calibri, 15'),bg="white").grid(row = 0,column=0, sticky = N, pady = 6)
    Label(register_screen, text = "Họ và Tên", font = ('Calibri, 12'),bg="white").grid(row = 1, sticky = W)
    Label(register_screen, text = "Tuổi", font = ('Calibri, 12'),bg="white").grid(row = 2, sticky = W)
    Label(register_screen, text = "Giới tính", font = ('Calibri, 12'),bg="white").grid(row = 3, sticky = W)
    Label(register_screen, text = "Tên tài khoản", font = ('Calibri, 12'),bg="white").grid(row = 4, sticky = W)
    Label(register_screen, text = "Mật khẩu", font = ('Calibri, 12'),bg="white").grid(row = 5, sticky = W)
    notif = Label(register_screen,font = ('Calibri, 12'),bg="white")
    notif.grid(row = 7, sticky = N, pady = 10)
    #entries
    Entry(register_screen,textvariable=temp_name).grid(row = 1, column=1)
    Entry(register_screen,textvariable=temp_age).grid(row = 2, column=1)
    Entry(register_screen,textvariable=temp_gender).grid(row = 3, column=1)
    Entry(register_screen,textvariable=temp_account).grid(row = 4, column=1)
    Entry(register_screen,textvariable=temp_password,show='*').grid(row = 5, column=1)
    Button(register_screen, text ="Đăng kí", command= finish_reg , font = ('Calibri', 12),bg="grey").grid(row = 8, stick = N, pady = 10)
    #buttons

def infor():
    file = open(login_account , "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_account = user_details[0]
    details_name = user_details[2]
    details_age = user_details[3]
    details_gender = user_details[4]
    details_num_account = user_details[5]
    details_balance = user_details[-1]


    infor_screen = Toplevel(master)
    infor_screen.geometry('410x400+700+200')
    infor_screen.title("Thông tin cá nhân")
    infor_screen.configure(bg="white")
    #labels
    Label(infor_screen , text = "Thông tin cá nhân "+ details_name , font = ('Calibri', 12),bg="white").grid(row = 0, stick = N, pady = 10)
    Label(infor_screen , text = "\tSố tài khoản: "+ details_num_account , font = ('Calibri', 12),bg="white").grid(row = 1, stick = W)
    Label(infor_screen , text = "\tTên tài khoản: "+ details_account , font = ('Calibri', 12),bg="white").grid(row = 2, stick = W)
    Label(infor_screen , text = "\tTên: "+ details_name , font = ('Calibri', 12),bg="white").grid(row = 3, stick = W)
    Label(infor_screen , text = "\tTuổi: "+ details_age , font = ('Calibri', 12),bg="white").grid(row = 4, stick = W)
    Label(infor_screen , text = "\tGiới Tính "+ details_gender , font = ('Calibri', 12),bg="white").grid(row = 5, stick = W)
    Label(infor_screen , text = "\tSố dư: "+ details_balance , font = ('Calibri', 12),bg="white").grid(row = 6, stick = W)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text = "Vui lòng nhập số tiền ", fg = "red")
        return
    if float(amount.get()) <= 0 :
        deposit_notif.config(text = "Giao dịch không thành công !", fg ="red")
        return
    file = open(login_account, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]
    update_balance = current_balance
    update_balance = float(update_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text= "Số dư : $ "+ str(update_balance), fg="green")
    deposit_notif.config(text = "Nạp tiền thành công", fg = "green")
def finish_transfer():
    if transfer_amount.get() == "":
        transfer_notif.config(text="Vui lòng nhập số tiền", fg="red")
        return
    if float(transfer_amount.get()) <= 0:
        transfer_notif.config(text="Giao dịch không thành công!", fg="red")
        return

    global name_account
    global login_account

    # guest
    file = open(login_account, "r+")
    file_data = file.readlines()
    file.seek(0)

    current_balance = float(file_data[6].strip())
    updated_balance = current_balance - float(transfer_amount.get())
    file_data[6] = str(updated_balance) + "\n"

    file.writelines(file_data)
    file.truncate()
    file.close()

    # user
    name_account_guest = name_account.get()
    file_guest = open(name_account_guest, "r+")
    file_data_guest = file_guest.readlines()
    file_guest.seek(0)

    current_balance_guest = float(file_data_guest[6].strip())
    updated_balance_guest = current_balance_guest + float(transfer_amount.get())
    file_data_guest[6] = str(updated_balance_guest) + "\n"

    file_guest.writelines(file_data_guest)
    file_guest.truncate()
    file_guest.close()

    transfer_current_balance_label.config(text="Số dư: $ " + str(updated_balance), fg="green")
    transfer_notif.config(text="Chuyển tiền thành công", fg="green")
def transfer():
    global name_account
    global transfer_amount 
    global transfer_notif
    global  details_account
    global transfer_current_balance_label
    name_account = StringVar()
    transfer_amount = StringVar()
    file = open(login_account,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[6]
    #stk
    details_account = StringVar()
    #deposit screen
    transfer_screen = Toplevel(master)
    transfer_screen.geometry('410x300+700+200')
    transfer_screen.title("Chuyển tiền")
    transfer_screen.configure(bg="lightgrey")
    #label
    Label(transfer_screen, text ="Chuyển tiền", font = ('calibri', 12)).grid(row = 0, sticky=N, pady = 10)
    Label(transfer_screen, text ="Số tiền : ", font = ('Calibri', 12)).grid(row = 2 ,sticky=W)
    Label(transfer_screen, text ="Số tài khoản : ", font = ('Calibri', 12)).grid(row = 4 ,sticky=W)
    Label(transfer_screen, text ="Ten tài khoản : ", font = ('Calibri', 12)).grid(row = 3 ,sticky=W)
    transfer_current_balance_label = Label(transfer_screen, text ="Số dư : $ " + details_balance, font=(('Calibri'), 12))
    transfer_current_balance_label.grid(row = 1, sticky=W)
    transfer_notif = Label(transfer_screen , font =('Calibri', 12))
    transfer_notif.grid(row = 5, sticky=N , pady = 5)
    #entry
    Entry(transfer_screen, textvariable=transfer_amount).grid(row = 2, column=1)
    Entry(transfer_screen, textvariable=name_account).grid(row = 3, column=1)
    Entry(transfer_screen, textvariable=details_account).grid(row = 4, column=1)
    #buttons
    Button(transfer_screen, text = "Đồng ý", font =('Calibri', 12), command=finish_transfer,bg="grey").grid(row = 6, sticky=W, pady = 5)

def deposit():
    global amount 
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_account,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[-1]
    #deposit screen
    deposit_screen = Toplevel(master)
    deposit_screen.geometry('410x300+700+200')
    deposit_screen.title("Nạp tiền")
    deposit_screen.configure(bg="lightgrey")
    #label
    Label(deposit_screen, text ="Nạp tiền", font = ('calibri', 12)).grid(row = 0, sticky=N, pady = 10)
    current_balance_label = Label(deposit_screen, text ="Số dư : $ " + details_balance, font=(('Calibri'), 12))
    current_balance_label.grid(row = 1, sticky=W)
    Label(deposit_screen, text ="Số tiền : ", font = ('Calibri', 12)).grid(row = 2 ,sticky=W)
    deposit_notif = Label(deposit_screen , font =('Calibri', 12))
    deposit_notif.grid(row = 5, sticky=N , pady = 5)
    #entry
    Entry(deposit_screen, textvariable=amount).grid(row = 2, column=1)
    #buttons
    Button(deposit_screen, text = "Kết thúc", font =('Calibri', 12), command=finish_deposit,bg="grey").grid(row = 3, sticky=W, pady = 5)

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text = "Vui lòng nhập số tiền ", fg = "red")
        return
    if float( withdraw_amount.get()) <= 0 :
        withdraw_notif.config(text = "Giao dịch không thành công !", fg ="red")
        return
    file = open(login_account, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text ="Số dư không đủ", fg="red")
        return
    update_balance = current_balance
    update_balance = float(update_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text= "Số dư : $ "+str(update_balance), fg="green")
    withdraw_notif.config(text = "Rút tiền thành công", fg = "green")

def withdraw():
    global withdraw_amount 
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_account,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[-1]
    #deposit screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.geometry('410x300+700+200')
    withdraw_screen.title("Rút tiền")
    #label
    Label(withdraw_screen, text ="Rút tiền", font = ('calibri', 12)).grid(row = 0, sticky=N, pady = 10)
    current_balance_label = Label(withdraw_screen, text ="Số dư : $ " + details_balance, font=(('Calibri'), 12))
    current_balance_label.grid(row = 1, sticky=W)
    Label(withdraw_screen, text ="Số tiền : ", font = ('Calibri', 12)).grid(row = 2 ,sticky=W)
    withdraw_notif = Label(withdraw_screen , font =('Calibri', 12))
    withdraw_notif.grid(row = 5, sticky=N , pady = 5)
    #entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row = 2, column=1)
    #buttons
    Button(withdraw_screen, text = "Kết thúc", font =('Calibri', 12), command=finish_withdraw, bg="grey").grid(row = 3, sticky=W, pady = 5)

def login_session():
    global login_account
    all_account = os.listdir()
    login_account = temp_login_account.get()
    login_password = temp_login_password.get()
    for acc in all_account:
        if acc == login_account:
            file = open(acc, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            # account dashboard
            if login_password == password:
                login_screeen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.geometry('410x450+700+200')
                account_dashboard.title('TN banking')
                
                #labels
                Label(account_dashboard, text = "Trang chủ" , font = ('Calibri', 12)).grid(row = 0, stick = N, pady = 10)
                Label(account_dashboard, text = "Xin chào"+ acc , font = ('Calibri', 12)).grid(row = 1, stick = N, pady = 10)
                #buttons
                Button(account_dashboard, text = "Thông tin cá nhân",font = ('Calibri', 12), width = 25, command = infor, bg="grey" ).grid(row = 2, stick = N, padx = 5)
                Button(account_dashboard, text = "Nạp tiền",font = ('Calibri', 12), width = 25, command=deposit, bg="grey").grid(row = 3, stick = N, padx = 5)
                Button(account_dashboard, text = "Rút tiền",font = ('Calibri', 12), width = 25, command=withdraw, bg="grey").grid(row = 4, stick = N, padx = 5)
                Button(account_dashboard, text = "Chuyển tiền",font = ('Calibri', 12), width = 25, command= transfer, bg="grey").grid(row = 5, stick = N, padx = 5)
                return 
            else:
                login_notif.config(fg="red", text = "Sai tên tài khoản hoặc mật khẩu")
                return 
    login_notif.config(fg="red", text= " Tài khoản không tồn tại")

def login():
    # login screen
    global temp_login_account
    global temp_login_password
    global login_notif
    global login_screeen
    temp_login_account = StringVar()
    temp_login_password = StringVar()
    login_screeen = Toplevel(master)
    login_screeen.geometry('410x250+700+200')
    login_screeen.title("Đăng nhập")
    login_screeen.configure(bg="white")
    # label
    Label(login_screeen, text = "Đăng nhập bằng tài khoản của bạn", font = ('Calibri', 12), bg="white").grid(row = 0, sticky= N,pady = 6)
    Label(login_screeen, text = "Tên tài khoản", font = ('Calibri', 12),bg="white").grid(row = 1, sticky= W)
    Label(login_screeen, text = "Mật khẩu", font = ('Calibri', 12),bg="white").grid(row = 2, sticky= W)
    login_notif = Label(login_screeen, font =('Calibri', 12))
    login_notif.grid(row = 4,sticky=N)
    # entried
    Entry(login_screeen, textvariable= temp_login_account).grid(row = 1, column=1 ,sticky=W, padx= 5)
    Entry(login_screeen, textvariable=temp_login_password,show = '*').grid(row = 2,column=1, sticky=W, padx= 5)
    # buttons
    Button(login_screeen, text ="Đăng nhập", command= login_session, width= 15 , font = ('Calibri', 12), bg="grey").grid(row = 4, stick = N, pady = 5, padx= 5)
#image
img = Image.open('D:/python/face_id/face/project_python/image.jpg')
img = img.resize((250,250))
img =  ImageTk.PhotoImage(img)
#lable
Label(master, text="TN Pay", font =('Calibri',14), width = 40).grid(row=0, sticky=NSEW, pady=10)
Label(master, image= img).grid(row = 2, sticky = NSEW, pady =  15)

# butoons
Button(master, text ='Đăng kí', font = ('Calibri', 12), width=20 , command=register, bg="grey").grid(row = 3, sticky=N)
Button(master, text ='Đăng nhập', font = ('Calibri', 12), width=20, command=login, bg="grey").grid(row = 4, sticky=N, pady = 6)

master.mainloop()       