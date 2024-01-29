
##################################################### USED LIBRARIES ###########################################################
import customtkinter as ck 
import mysql.connector
import uuid 
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import datetime
from PIL import Image,ImageTk
############################################### SOME GLOBAL VARIABLES #####################################################
global e1
global e2
global e3
global e4
global uid
global cur
global tv
global date1
global c_date


##################################################################################### Database connectivity#####################################################################
con=mysql.connector.connect(host="localhost",user="root",password="honey@2003#")
cur=con.cursor(buffered=True)
try:
    cur.execute("use tenant")
except:
    cur.execute("create database tenant")
    cur.execute("use tenant")
#################################################################################### CREATED DATABASE TABLE ####################################################################
try:
    cur.execute("describe tenants")
except:
    cur.execute("create table tenants(id varchar(4) primary key not null unique,NAME VARCHAR(100), MobileNumber varchar(10),MothlyRent int(50),RentStatus  varchar(30),ShiftingDate date,dues int(50),PreDues int(50))")

#cur.execute("drop table tenants")




############################################################################### Main Window creation #############################################################################
ck.set_appearance_mode("system")
ck.set_default_color_theme("blue")
win=ck.CTk()
win.geometry("1300x750")
win.title("Tenant Managment System")
win.iconbitmap("logo.ico")
se=Image.open("abc.png")
ri1=se.resize((1298,748))
v=ImageTk.PhotoImage(ri1)
sd=Image.open("win3.png")
ri2=sd.resize((1298,748))
x=ImageTk.PhotoImage(ri2)
sg=Image.open("win4.jpg")
ri3=sg.resize((1298,748))
y=ImageTk.PhotoImage(ri3)


################################################# MAIN WINDOW ###########################################################
def tab2():
    ############################################# Edit button event ####################################################
    def edit():
        ########################################## go back button4 event ###########################################
        def back():
            mainfr4.destroy()
            tab2()
        ######################################### save button event #####################################################
        def save():
            
            
            e1a=ent_tenant_name1.get()
            e2a=ent_mobile_no1.get()
            e3a=ent__monthly_rent1.get()
            len_m_noa=len(e2a)

            if not e1a:
                messagebox.showerror("Error","Name field cant't be empty!")
            elif not e2a:
                messagebox.showerror("Error","Please enter Mobile number!")
            elif not e3a:
                messagebox.showerror("Error","Please enter Monthly rent!")
            else:
                if len_m_noa != 10:
                    messagebox.showerror("error","Mobile number not valid!")
                else:
                    update_querry="update tenants set NAME = %s , MobileNumber = %s , MothlyRent = %s where id = %s"
                    cur.execute(update_querry,(e1a,e2a,e3a,ii))
                    ent_tenant_name1.delete(0,tkinter.END)
                    ent_mobile_no1.delete(0,tkinter.END)
                    ent__monthly_rent1.delete(0,tkinter.END)
                    messagebox.showinfo("success","details saved successfully")

                    

        
        selc_items=tv.focus()
        global values
        values=tv.item(selc_items,'values')
        ii=values[0]
        nam=values[1]
        PN=values[2]
        MR=values[3]
        RS=values[4]
        mainfr1.destroy()
        global mainfr4
        mainfr4=ck.CTkFrame(master=win, border_width=5,border_color="sky blue",fg_color="ivory",height=750,width=1300)
        mainfr4.place(relx=0,rely=0)
        lbl_image3=tkinter.Label(mainfr4,image=x,border=1)
        lbl_image3.place(relx=0,rely=0)
        lblfr1=ck.CTkFrame(mainfr4,width=500,height=70,corner_radius=0,border_width=1,fg_color="black",border_color="ivory")
        lblfr1.place(relx=0.3,rely=0.08)
       
        
        lbl_add_tenant1=ck.CTkLabel(master=lblfr1,text="Edit Tenant",width=200,height=20,font=("arial",35,'bold'), text_color="ivory",corner_radius=20)
        lbl_add_tenant1.place(relx=0.3,rely=0.2)
        
        
 
        ent_tenant_name1=ck.CTkEntry(master=mainfr4,placeholder_text="Tenant name",width=900,height=50,text_color="white",border_width=1,border_color="ivory",corner_radius=0,font=("arial",15))
        ent_tenant_name1.insert(0,nam)
        ent_tenant_name1.place(relx=0.05,rely=0.35)

        
        ent_mobile_no1=ck.CTkEntry(master=mainfr4,placeholder_text="Tenant Mobile Number",width=900 ,font=("arial",15),height=50,border_width=1,text_color="white",border_color="ivory",corner_radius=0)
        ent_mobile_no1.insert(0,PN)
        ent_mobile_no1.place(relx=0.05,rely=0.5)


        
        ent__monthly_rent1=ck.CTkEntry(master=mainfr4,placeholder_text="Monthly Rent",width=900,height=50,corner_radius=0,border_width=1,text_color="white",border_color="ivory",font=("arial",15))
        ent__monthly_rent1.insert(0,MR)
        ent__monthly_rent1.place(relx=0.05,rely=0.65)

        ######################################################################## save Button for windowv "edit details" ###########################################################################
        btn_save=ck.CTkButton(master=mainfr4,text="SAVE",command=save,text_color="ivory",corner_radius=0,border_width=1)
        btn_save.place(relx=0.85,rely=0.9 )

        ########################################################################## go back button for window "edi details" #######################################################################
        btn_go_back4=ck.CTkButton(master=mainfr4,text="Go Back",command=back,text_color="ivory",corner_radius=0,border_width=1)
        btn_go_back4.place(relx=0.73,rely=0.9)
    def delt():
        conf=messagebox.askyesno("confirmation","Do You Want To Delete Selected Row ?")
        if conf:
            selc_items=tv.focus()
            global values
            values=tv.item(selc_items,'values')
            btn_delete.configure(state=DISABLED)
            btn_edit.destroy()
            id=values[0]
            qw="delete from tenants where id = %s"
            cur.execute(qw,(id,))
            tv.delete(id)
            con.commit()
    ########################################### EXIT button event #########################################################
    def Exit():
        conf=messagebox.askyesno("confirmation","Do You Want To Exit ?")
        if conf:
            win.destroy()

    ################################################ window "further details" #####################################################
    def get_more_details():
        selc_items=tv.focus()
        global values
        values=tv.item(selc_items,'values')
        #################################################### Paid button event ##########################################################
        def paid():
            qury="select * from tenants where id = %s"
            cur.execute(qury,(ii,))
            result=cur.fetchone() 
            dues=result[6]
            pre_dues=result[7]
            dues_int=int(dues)
            pre_dues_int=int(pre_dues)
            e_1_a=ent_1_a.get()
            ea=int(e_1_a)
            u=resul3-ea
            e=resul2-ea
            if u >= 0:
                lbl_5_e.configure(text=u,text_color="red")
                lbl_5_c.configure(text=e,text_color="red")
                up_que2="update tenants set dues=%s,PreDues=%s where id=%s"
                cur.execute(up_que2,(e,u,ii))
                con.commit()
            else:
                if e < 0:
                    messagebox.showerror("Error","Enetered amount should be less than Dues!")
                else:
                    u=0
                    up_que2="update tenants set PreDues=%s where id=%s"
                    cur.execute(up_que2,(u,ii))
                    con.commit()
                    ury="select * from tenants where id = %s"
                    cur.execute(qury,(ii,))
                    resul=cur.fetchone() 
                    resul21=resul[6]
                    resul31=resul[7]
                    resul2=int(resul21)
                    resul3=int(resul31)
                    lbl_5_e.configure(text=resul3,text_color="green")
                    if e==0:
                        lbl_5_c.configure(text=e,text_color="green")
                        up_que2="update tenants set dues=%s where id=%s"
                        cur.execute(up_que2,(e,ii))
                        con.commit()
                        lbl_5_a.configure(text="Rent Clear",text_color="green")
                    else:
                        lbl_5_c.configure(text=e,text_color="red")
                        up_que2="update tenants set dues=%s where id=%s"
                        cur.execute(up_que2,(e,ii))
                        con.commit()
                    ent_1_a.delete(0,tkinter.END)
            
        print(values)
        ii=values[0]
        nam=values[1]
        PN=values[2]
        MR=values[3]
        RS=values[4]
        qury="select * from tenants where id = %s"
        cur.execute(qury,(ii,))
        resul=cur.fetchone() 
        resul21=resul[6]
        resul31=resul[7]
        resul2=int(resul21)
        resul3=int(resul31)
        con.commit()
        print(resul2,resul3)
        mainfr3=ck.CTkFrame(master=win, border_width=5,height=750,width=1300)
        mainfr3.place(relx=0,rely=0)
        lblb=tkinter.Label(mainfr3,image=y,border=1)
        lblb.place(relx=0,rely=0)
        fr_1=ck.CTkFrame(mainfr3,height=400,width=1200,border_width=1,border_color="ivory",fg_color="black",corner_radius=10)
        fr_1.place(relx=0.04,rely=0.05)
        fr_2=ck.CTkFrame(mainfr3,height=180,width=1200,border_width=1,border_color="ivory",fg_color="black",corner_radius=10)
        fr_2.place(relx=0.04,rely=0.61)
        lbl_1=ck.CTkLabel(fr_1,text="Tenant Details",font=('arial',40),text_color="ivory")
        lbl_1.place(relx=0.4,rely=0.1)
        lbl_2=ck.CTkLabel(fr_1,text="NAME :",font=('arial',25,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="ivory")
        lbl_2.place(relx=0.04,rely=0.4)
        lbl_3=ck.CTkLabel(fr_1,text="PHONE NUMBER :",font=('arial',25,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="ivory")
        lbl_3.place(relx=0.25,rely=0.4)
        lbl_4=ck.CTkLabel(fr_1,text="MONTHLY RENT :",font=('arial',25,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="ivory")
        lbl_4.place(relx=0.54,rely=0.4)
        lbl_5=ck.CTkLabel(fr_1,text="RENT STATUS :",font=('arial',25,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="ivory")
        lbl_5.place(relx=0.80,rely=0.4)
        lbl_2_a=ck.CTkLabel(fr_1,text=(nam),font=('arial',20,),corner_radius=20,bg_color="black",fg_color="black",text_color="green")
        lbl_2_a.place(relx=0.04,rely=0.6)
        lbl_3_a=ck.CTkLabel(fr_1,text=PN,font=('arial',20,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="green")
        lbl_3_a.place(relx=0.25,rely=0.6)
        lbl_4_a=ck.CTkLabel(fr_1,text=MR,font=('arial',20,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="green")
        lbl_4_a.place(relx=0.54,rely=0.6)
        lbl_5=ck.CTkLabel(fr_2,text="Rent Clearense Portal",font=('arial',30),text_color="ivory")
        lbl_5.place(relx=0.4,rely=0.1)
        lbl_5_b=ck.CTkLabel(fr_2,text="Previous Dues:",font=('arial',15,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="ivory")
        lbl_5_b.place(relx=0.8,rely=0.4)
        if resul3 == 0:
            lbl_5_e=ck.CTkLabel(fr_2,text="",font=('arial',15),corner_radius=20,bg_color="black",fg_color="black",text_color="green")
            lbl_5_e.place(relx=0.9,rely=0.4)
        else:
            lbl_5_e=ck.CTkLabel(fr_2,text="",font=('arial',15),corner_radius=20,bg_color="black",fg_color="black",text_color="red")
            lbl_5_e.place(relx=0.9,rely=0.4)
        lbl_5_d=ck.CTkLabel(fr_2,text="Total Dues:",font=('arial',15,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="ivory")
        lbl_5_d.place(relx=0.8,rely=0.6)
        if resul2==0:
            lbl_5_c=ck.CTkLabel(fr_2,text="",font=('arial',15),corner_radius=15,bg_color="black",fg_color="black",text_color="green")
            lbl_5_c.place(relx=0.9,rely=0.6)
        else:
            lbl_5_c=ck.CTkLabel(fr_2,text="",font=('arial',15),corner_radius=15,bg_color="black",fg_color="black",text_color="red")
            lbl_5_c.place(relx=0.9,rely=0.6)
        if RS=='Rent Clear':
            ent_1_a=ck.CTkEntry(fr_2,placeholder_text="amount to be payed",width=700,corner_radius=50,border_width=1,border_color="ivory",text_color="ivory",state=DISABLED)
            ent_1_a.place(relx=0.05,rely=0.6)
            prev=resul3
            td=resul2
            lbl_5_e.configure(text=prev)
            lbl_5_c.configure(text=td)
            lbl_5_a=ck.CTkLabel(fr_1,text=RS,font=('arial',20,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="green")
            lbl_5_a.place(relx=0.80,rely=0.6)
        else: 
            ent_1_a=ck.CTkEntry(fr_2,placeholder_text="amount to be payed",width=700,corner_radius=50,border_width=1,border_color="ivory",text_color="ivory",state=NORMAL)
            ent_1_a.place(relx=0.05,rely=0.6)
            prev=resul3
            td=resul2
            lbl_5_e.configure(text=prev)
            lbl_5_c.configure(text=td)
            lbl_5_a=ck.CTkLabel(fr_1,text=RS,font=('arial',20,'bold'),corner_radius=20,bg_color="black",fg_color="black",text_color="red")
            lbl_5_a.place(relx=0.80,rely=0.6)           
        ############################################ Go back button event in window "further details"#######################################           
        def tab5():
            mainfr3.destroy()
            tab2()

        ############################################go back button for window"fuether details ##############################################
        global btn_2
        g_btn_2=ck.CTkButton(master=mainfr3,text="Go Back",command=tab5,text_color="ivory",corner_radius=0,border_width=1)
        g_btn_2.place(relx=0.73,rely=0.9)

        #####################################################paid button for window "further details"######################################
        btn_1_a=ck.CTkButton(master=mainfr3,text="Paid",command=paid,text_color="ivory",corner_radius=0,border_width=1)
        btn_1_a.place(relx=0.85,rely=0.9 )
        mainfr1.destroy()
    
    ############################################ Go back button event for window "add tenant" ##########################################
    def tab4():
        
        mainfr2.destroy()
        tab2()


    ############################################## Window "add tenant" #############################################################    
    def tab3():
        global mainfr2
        mainfr2=ck.CTkFrame(master=win, border_width=5,border_color="sky blue",fg_color="ivory",height=750,width=1300)
        mainfr2.place(relx=0,rely=0)
        lbl_image2=tkinter.Label(mainfr2,image=x,border=1)
        lbl_image2.place(relx=0,rely=0)
        lblfr=ck.CTkFrame(mainfr2,width=500,height=70,corner_radius=0,border_width=1,fg_color="black",border_color="ivory")
        lblfr.place(relx=0.3,rely=0.08)
       
        
        lbl_add_tenant=ck.CTkLabel(master=lblfr,text="ADD TENANT",width=200,height=20,font=("arial",35,'bold'), text_color="ivory",corner_radius=0)
        lbl_add_tenant.place(relx=0.3,rely=0.2)
        
        
 
        ent_tenant_name=ck.CTkEntry(master=mainfr2,placeholder_text="Tenant name",width=900,height=50,text_color="white",border_width=1,border_color="ivory",corner_radius=0,font=("arial",15))
        ent_tenant_name.place(relx=0.05,rely=0.35)

        
        ent_mobile_no=ck.CTkEntry(master=mainfr2,placeholder_text="Tenant Mobile Number",width=900 ,font=("arial",15),height=50,border_width=1,text_color="white",border_color="ivory",corner_radius=0)
        ent_mobile_no.place(relx=0.05,rely=0.5)


        
        ent__monthly_rent=ck.CTkEntry(master=mainfr2,placeholder_text="Monthly Rent",width=900,height=50,corner_radius=0,border_width=1,text_color="white",border_color="ivory",font=("arial",15))
        ent__monthly_rent.place(relx=0.05,rely=0.65)
        

        
        ################################# "CLICK TO ADD BUTTON" EVENT for window"add tenant" #################################################################
        def Ad_btn():
            print(values)
            e1=ent_tenant_name.get()
            e2=ent_mobile_no.get()
            e3=ent__monthly_rent.get()
            initial_pre_dues=0
            e4=0
            uid=(str(uuid.uuid4())[0:4])
            len_m_no=len(e2)

            if not e1:
                messagebox.showerror("Error","Name field cant't be empty!")
            elif not e2:
                messagebox.showerror("Error","Please enter Mobile number!")
            elif not e3:
                messagebox.showerror("Error","Please enter Monthly rent!")
            else:
                if len_m_no != 10:
                    messagebox.showerror("error","Mobile number not valid!")
                else:
                    date1=date.today()
                    #f_date=date.strftime('%Y-%B-%d')
                    rt="Rent Due"
                    cur.execute("insert into tenants(id,NAME,MobileNumber,MothlyRent,RentStatus,ShiftingDate,dues,PreDues) values(%s,%s,%s,%s,%s,%s,%s,%s)",(uid,e1,e2,e3,rt,date1,e4,initial_pre_dues))
                    ent_tenant_name.delete(0,tkinter.END)
                    ent_mobile_no.delete(0,tkinter.END)
                    ent__monthly_rent.delete(0,tkinter.END)
                    con.commit()
                     
                    print(date)
                    messagebox.showinfo("success","Tenant added successfuly")
                    
                    
        ######################################## "CLICK TO ADD" Button for window"add tenant" #############################################
        btn_click_to_add=ck.CTkButton(master=mainfr2,text="Click to Add",command=Ad_btn,text_color="ivory",corner_radius=0,border_width=1)
        btn_click_to_add.place(relx=0.85,rely=0.9 )
        mainfr1.destroy()

        ############################################# "GO BACK"BUTTON for window "add tenant" ############################################
        
        btn_go_back1=ck.CTkButton(master=mainfr2,text="Go Back",command=tab4,text_color="ivory",corner_radius=0,border_width=1)
        btn_go_back1.place(relx=0.73,rely=0.9)
        
    
    ########################################################### current date stored ########################################################
    c_date=date.today()

    ############################################################## main window #############################################################
    mainfr1=ck.CTkFrame(master=win, border_width=5,height=750,width=1300)
    mainfr1.place(relx=0,rely=0)
    lbl_mainfr1=tkinter.Label(mainfr1,image=v,border=1)
    lbl_mainfr1.place(relx=0,rely=0)
    
    ######################################################### main window all buttons ########################################################
    btn_add_new=ck.CTkButton(master=mainfr1,text="Add New Tenant",command=tab3,text_color="ivory",corner_radius=0,border_width=1)
    btn_add_new.place(relx=0.85,rely=0.09)
    btn_get_more=ck.CTkButton(master=mainfr1,text="Get More Details",command=get_more_details,text_color="ivory",corner_radius=0,border_width=1,state=DISABLED)
    btn_get_more.place(relx=0.85,rely=0.15)
    btn_exit=ck.CTkButton(master=mainfr1,text="EXIT",text_color="ivory",command=Exit,corner_radius=0,border_width=1)
    btn_exit.place(relx=0.85,rely=0.9)
    btn_delete=ck.CTkButton(master=mainfr1,text="DELETE",command=delt,text_color="ivory",corner_radius=0,border_width=1,state=DISABLED)
    btn_delete.place(relx=0.85,rely=0.84)
    
    
    
    ############################################################ CREATED TREEVIEW to show added tenant #########################################
    tree_frame=ck.CTkFrame(master=mainfr1,height=695,width=1000 ,border_width=10,border_color="grey",fg_color="black")
    tree_frame.place(relx=0.03,rely=0.03)
    title_lbl=ck.CTkLabel(tree_frame,text="Your Tenants",width=100,height=20,font=("arial",35,'bold','underline'), text_color="ivory",corner_radius=20)
    title_lbl.place(relx=0.4,rely=0.05)
    column=('uid','name','ph.no','monthly rent','rent status')
    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",font=('arial',15),background="black",headingheight=40,foreground="ivory",fieldbackground="black",rowheight=50)
    tv=ttk.Treeview(tree_frame,columns=column,show="headings",height=11,style="Treeview",selectmode="browse")
    tv.column('# 1',anchor=CENTER,width=176)
    tv.column('# 2',anchor=CENTER)
    tv.column('# 3',anchor=CENTER)
    tv.column('# 4',anchor=CENTER)
    tv.column('# 5',anchor=CENTER)
    tv.heading('uid',text='UID')
    tv.heading('name',text='NAME')
    tv.heading('ph.no',text='PHONE NUMBER')
    tv.heading('monthly rent',text='MONTHLY RENT')
    tv.heading('rent status',text='RENT STATUS')
    tv.place(relx=0.01,rely=0.15)
    sb=ck.CTkScrollbar(tv,command=tv.yview)
    sb.place(relx=0.98,rely=0.1)
    tv.configure(yscrollcommand=sb.set)
    

    
    ################################################################## Enabling/Disabling buttons on selction ####################################
    def btn_enabling_desabling(event): 
        selection=tv.selection()
        if selection:
            btn_get_more.configure(state=tkinter.NORMAL)
            btn_delete.configure(state=tkinter.NORMAL)
            global btn_edit
            btn_edit=ck.CTkButton(master=tree_frame,text="EDIT",command=edit,text_color="black",corner_radius=0,border_width=1,width=50,fg_color="light grey")
            btn_edit.place(relx=0.92,rely=0.03)
        else:   
        
            btn_get_more.configure(state=tkinter.DISABLED)
            btn_delete.configure(state=tkinter.DISABLED)
    tv.bind("<<TreeviewSelect>>",btn_enabling_desabling)       
    ######################################################################## INSERTING & UPDATING DATA IN TREEVIEW ##################################
    cur.execute("select * from tenants")
    rows=cur.fetchall()
    for i in rows:
        uid=i[0]
        monthly_rent=i[3]
        s_date=i[5]
        t_dues=i[6]
        p_dues=i[7]
        u_date=s_date+datetime.timedelta(days=30)
        if u_date < c_date or t_dues != 0 :
            if u_date < c_date:
                new_val='Rent Due!'
                new_p_dues=p_dues+t_dues
                new_t_dues=t_dues+monthly_rent
                up_que="update tenants set RentStatus= %s,dues=%s,ShiftingDate=%s,PreDues=%s where id= %s"
                cur.execute(up_que,(new_val,new_t_dues,c_date,new_p_dues,uid))
                con.commit()
            else:
                
                new_val='Rent Due!'
                up_que="update tenants set RentStatus= %s  where id= %s"
                cur.execute(up_que,(new_val,uid))
                con.commit()
        else:
            new_val='Rent Clear'
            up_que="update tenants set RentStatus= %s  where id= %s"
            cur.execute(up_que,(new_val,uid))
            con.commit()
    
    cur.execute("select * from tenants")
    rows_1=cur.fetchall()
    for d in rows_1:
        tv.insert('','end',iid=d[0] ,values=(d[0],d[1],d[2],d[3],d[4]))
    values=None
    del_btn=ck.CTkButton(mainfr1,)
    
        
######################################################################################### calling main function #############################################  
tab2()
########################################################## windows execution #################################################
win.mainloop()