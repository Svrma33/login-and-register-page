from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk, ImageFilter
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1230x750+130+18")
        self.root.resizable(False,False)

        # ==================variables====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        #====================background image====================
        img1 = Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/hotel_img.png")
        img1 = img1.resize((1230,750), Image.LANCZOS)
        img1_blur = img1.filter(ImageFilter.GaussianBlur)
        self.photoimg1 = ImageTk.PhotoImage(img1_blur)

        lbl_bg= Label(self.root, image=self.photoimg1)
        lbl_bg.place(x=0, y=0, width=1230, height=750)

        #====================main frame====================
        frame=Frame(self.root,bg="white")
        frame.place(x=215,y=102,width=800,height=550)

        register_lbl=Label(frame,text="New User Register",font=("Times new roman",20,"bold"),fg="Red",bg="white")
        register_lbl.place(x=285,y=20)

        #====================label and entry====================
        #row-1
        fname=Label(frame,text="First Name",font=("Times new roman",15,"bold"),bg="white")
        fname.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times new roman",15))
        fname_entry.place(x=100,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("Times new roman",15,"bold"),bg="white")
        lname.place(x=450,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Times new roman",15))
        lname_entry.place(x=450,y=130,width=250)

        #row-2
        contact=Label(frame,text="Contact Number",font=("Times new roman",15,"bold"),bg="white")
        contact.place(x=100,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("Times new roman",12))
        contact_entry.place(x=100,y=200,width=250)
        
        email=Label(frame,text="Email",font=("Times new roman",15,"bold"),bg="white")
        email.place(x=450,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Times new roman",12))
        email_entry.place(x=450,y=200,width=250)

        #row-3
        security_Q=Label(frame,text="Select Security Questions",font=("Times new roman",15,"bold"),bg="white")
        security_Q.place(x=100,y=250)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name","Your Pet's Name")
        self.combo_security_Q.place(x=100,y=280,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("Times new roman",15,"bold"),bg="white")
        security_A.place(x=450,y=250)

        security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times new roman",15))
        security_A_entry.place(x=450,y=280,width=250)

        #row-4
        pswd=Label(frame,text="Password",font=("Times new roman",15,"bold"),bg="white")
        pswd.place(x=100,y=320)

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("Times new roman",15))
        pswd_entry.place(x=100,y=350,width=250)
        
        cpswd=Label(frame,text="Confirm Password",font=("Times new roman",15,"bold"),bg="white")
        cpswd.place(x=450,y=320)

        cpswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times new roman",15))
        cpswd_entry.place(x=450,y=350,width=250)

        # ==================checkbutton====================
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("Times new roman",12),onvalue=1,offvalue=0)
        checkbtn.place(x=100,y=390)

        # ==================button====================
        img=Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/register now.png")
        img=img.resize((150,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=150,y=440,width=150)

        img0=Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/login now.png")
        img0=img0.resize((150,50),Image.LANCZOS)
        self.photoimage0=ImageTk.PhotoImage(img0)
        b1=Button(frame,image=self.photoimage0,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=480,y=440,width=150)

        # ==================Function declaration====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User aleady exist,please try another email")
            else:
                my_cursor.execute("insert into registernow values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_fname.get(),
                                                                    self.var_lname.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_email.get(),
                                                                    self.var_securityQ.get(),
                                                                    self.var_securityA.get(),
                                                                    self.var_pass.get()
                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")







if __name__ =="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()