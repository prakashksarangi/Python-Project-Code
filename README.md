from tkinter import*
import math
import random
import os
from tkinter import messagebox


<!-- Suman Sourabh  12007886
Saurav Singh   12006233 -->

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Greed Villa")
        title=Label(self.root,text="Greed Villa",bd=12,relief=GROOVE,bg="#07266C",fg="White",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        
        #----------------------------------------  Variable    -------------------------------------------------------------------------------
        
        #----- Costomer Detail-------
        self.c_name=StringVar()
        self.c_number=StringVar()
        self.bill_number=StringVar()
        self.b_no=random.randint(100000,999999)
        self.bill_number.set(str(self.b_no))
        self.search_bill=StringVar()
        
        
        #---- cosmetic  ---------
        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.shampoo=IntVar()
        self.hair_oil=IntVar()
        self.body_lotion=IntVar()
        
        #----- Grocery -----------
        self.food_oil=IntVar()
        self.rice=IntVar()
        self.sugar=IntVar()
        self.salt=IntVar()
        self.flour=IntVar()
        self.spices=IntVar()
        
        #------- snacks ----------
        self.cold_drink=IntVar()
        self.pizza=IntVar()
        self.burger=IntVar()
        self.sweet=IntVar()
        self.boos=IntVar()
        self.samosa=IntVar()
        
        
        #---- Total and Tax Price-----
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.snacks_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.snacks_tax=StringVar()
        
                   
        
        
        #========================================== Customer Detail ====================================================
               
        f1=LabelFrame(self.root,text="Customer Detail",font=("times new roman",15,"bold"),fg="gold",bg="#07266C")
        f1.place(x=0,y=80,relwidth=1)
        
        cname=Label(f1,text="Customer Name",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=30,pady=6)
        cname_txt=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(f1,text=" Phone No.",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=30,pady=6)
        cphn_txt=Entry(f1,width=15,textvariable=self.c_number,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(f1,text=" Bill Number",bg="#07266C",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=30,pady=6)
        c_bill_txt=Entry(f1,width=15,textvariable=self.bill_number,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(f1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold"). grid(row=0,column=6,padx=10, pady=10)
        
        
        
        #==========================================      Cosmetics Frame===============================================================================================================
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Cosmetics",font=("times new roman",15,"bold"),fg="gold")
        F2.place(x=5,y=180,width=325,height=380)
        
        bath_soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_lbl=Entry(F2,width=10,textvariable=self.bath_soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_lbl=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        face_Wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_lbl=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        shampoo_lbl=Label(F2,text="Shampoo",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        shampoo_lbl=Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        hair_Oil_lbl=Label(F2,text="Hair Oil",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_Oil_lbl=Entry(F2,width=10,textvariable=self.hair_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lotion_lbl=Entry(F2,width=10,textvariable=self.body_lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        
        #===========================================     Grocery Frame    ================================================================================================
              
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Grocery",font=("times new roman",15,"bold"),fg="gold")
        F3.place(x=335,y=180,width=325,height=380)
        
        food_oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        food_oil_lbl=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        rice_lbl=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sugar_lbl=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        salt_lbl=Label(F3,text="Salt",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        salt_lbl=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        flour_lbl=Label(F3,text="Flour",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        flour_lbl=Entry(F3,width=10,textvariable=self.flour,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        spices_lbl=Label(F3,text="Spices",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        spices_lbl=Entry(F3,width=10,textvariable=self.spices,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        
        
        #==========================================      Snacks Frame     ==============================================================================
        
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Snacks",font=("times new roman",15,"bold"),fg="gold")
        F4.place(x=670,y=180,width=325,height=380)
        
        cold_drink_lbl=Label(F4,text="Cold Drink",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cold_drink_lbl=Entry(F4,width=10,textvariable=self.cold_drink,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        Pizza_lbl=Label(F4,text="Pizza",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        pizza_lbl=Entry(F4,width=10,textvariable=self.pizza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        burger_lbl=Label(F4,text="Burger",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        burger_lbl=Entry(F4,width=10,textvariable=self.burger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        sweets_lbl=Label(F4,text="Sweets",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sweets_lbl=Entry(F4,width=10,textvariable=self.sweet,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        boos_lbl=Label(F4,text="Boos",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        boos_lbl=Entry(F4,width=10,textvariable=self.boos,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        samosa_lbl=Label(F4,text="Samosa",font=("times new roman",16,"bold"),bg="#07266C",fg="green").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        samosa_lbl=Entry(F4,width=10,textvariable=self.samosa,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        
        
        #==========================================  Bill Printing Area    ==============================================================================
        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=345,height=380)
        bill_label=Label(F5,text="Bill area", font=("arial",18,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        
        #==========================================   Snacks Frame    ==============================================================================
        
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,bg="#07266C",text="Bill Menu",font=("times new roman",15,"bold"),fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F6,text="Total Grocery Price",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3=Label(F6,text="Total Snacks Price",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.snacks_price,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        m4=Label(F6,text="Cosmetic Tax",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        m4_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        m5=Label(F6,text="Grocery Tax",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        m5_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        m6=Label(F6,text="Snacks Tax",font=("times new roman",14,"bold"),bg="#07266C",fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        m6_txt=Entry(F6,width=18,textvariable=self.snacks_tax,font="arial 10 bold", bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        
        
        #======================================== Button Frame ============================================
        
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=730,width=595,height=105)
        
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)

        gbill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)

        clear_btn=Button(btn_f,text="Clear bill",command=self.clear_data,bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,bd=5,width=12,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        
        
        self.welcome_bill()
        
        
    def total(self):
        
        #--------------- Cosmetic Price----------------
          self.c_bath_soap=self.bath_soap.get()*40
          self.c_face_cream=self.face_cream.get()*40
          self.c_face_wash=self.face_wash.get()*40
          self.c_shampoo=self.shampoo.get()*40
          self.c_hair_oil=self.hair_oil.get()*40
          self.c_body_lotion=self.body_lotion.get()*40
          
          
          self.cosmetic_pri=(float(
                                    (self.c_bath_soap)+
                                    (self.c_face_cream)+
                                    (self.c_face_wash)+
                                    (self.c_shampoo)+
                                    (self.c_hair_oil)+
                                    (self.c_body_lotion)
                                )
                            )
          self.cosmetic_price.set("Rs."+str(self.cosmetic_pri))
        
        #-------------- Grocery Price ------------------------  
        
          self.c_food_oil=self.food_oil.get()*40
          self.c_rice=self.rice.get()*40
          self.c_sugar=self.sugar.get()*40
          self.c_salt=self.salt.get()*40
          self.c_flour=self.flour.get()*40
          self.c_spices=self.spices.get()*40
          
          
          self.grocery_pri=(float(
                                    (self.c_food_oil)+
                                    (self.c_rice)+
                                    (self.c_sugar)+
                                    (self.c_salt)+
                                    (self.c_flour)+
                                    (self.c_spices)
                                )
                            )
          self.grocery_price.set("Rs."+str(self.grocery_pri))
        
        #-------------- Snacks Price -------------------------
          self.c_cold_drink=self.cold_drink.get()*40
          self.c_pizza=self.pizza.get()*40
          self.c_burger=self.burger.get()*40
          self.c_sweet=self.sweet.get()*40
          self.c_boos=self.boos.get()*40
          self.c_samosa=self.samosa.get()*40
          
          
          self.snacks_pri=(float(
                                    (self.c_cold_drink)+
                                    (self.c_pizza)+
                                    (self.c_burger)+
                                    (self.c_sweet)+
                                    (self.c_boos)+
                                    (self.c_samosa)
                                )
                            )
          self.snacks_price.set("Rs."+str(self.snacks_pri))
          
        #------------- Calculating Tax---------------    
          self.c_tax=self.cosmetic_pri*0.05
          self.cosmetic_tax.set("Rs."+str(self.c_tax))
          self.c_grocery=self.grocery_pri*0.05
          self.grocery_tax.set("Rs."+str(self.c_grocery))
          self.c_snacks=self.snacks_pri*0.05
          self.snacks_tax.set("Rs."+str(self.c_snacks))
          
          
          
          self.total_price=float(
                                 self.cosmetic_pri+
                                 self.grocery_pri+
                                 self.snacks_pri+
                                 self.c_tax+
                                 self.c_grocery+
                                 self.c_snacks
                                )
          
          
          
        #===============================   Bill Area==========================================================
    
    def welcome_bill(self):
        
          self.txtarea.delete('1.0',END)
          self.txtarea.insert(END,"\t      Greed Villa")
          self.txtarea.insert(END,f"\nBill Number:{self.b_no}")
          self.txtarea.insert(END,f"\nCustomer Name:{self.c_name.get()}")
          self.txtarea.insert(END,f"\nCostomer Number:{self.c_number.get()}")
          self.txtarea.insert(END,"\n======================================")
          self.txtarea.insert(END,"\n Product\t\tQTY\t\tPrice")
          self.txtarea.insert(END,"\n======================================")
          
          
    def bill_area(self):
        # if self.c_name.get()=="" or self.c_phon.get()=="":
        #     messagebox.showerror("Error","customer details are must")
            
        # elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.snacks_price.get()=="Rs. 0.0":
        #     messagebox.showerror("Error","No product purchased")
            
        # else:
            self.welcome_bill()
        #-------cosmetics=======
    
            if self.bath_soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.bath_soap.get()}\t\t{self.c_bath_soap}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n face cream\t\t{self.face_cream.get()}\t\t{self.c_face_cream}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n face wash\t\t{self.face_wash.get()}\t\t{self.c_face_wash}")

            if self.shampoo.get()!=0:
                self.txtarea.insert(END,f"\n shampoo\t\t{self.shampoo.get()}\t\t{self.c_shampoo}")

            if self.hair_oil.get()!=0:
                self.txtarea.insert(END,f"\n hair oil\t\t{self.hair_oil.get()}\t\t{self.c_hair_oil}")

            if self.body_lotion.get()!=0:
                self.txtarea.insert(END,f"\n body lotion\t\t{self.body_lotion.get()}\t\t{self.c_body_lotion}")


            #=======Grocery============
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n rice\t\t{self.rice.get()}\t\t{self.c_rice}")

            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n food oil\t\t{self.food_oil.get()}\t\t{self.c_food_oil}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n sugar\t\t{self.sugar.get()}\t\t{self.c_sugar}")

            if self.salt.get()!=0:
                self.txtarea.insert(END,f"\n salt\t\t{self.salt.get()}\t\t{self.c_salt}")
                
            if self.flour.get()!=0:
                self.txtarea.insert(END,f"\n flour\t\t{self.flour.get()}\t\t{self.c_flour}")
                
            if self.spices.get()!=0:
                self.txtarea.insert(END,f"\n spices\t\t{self.spices.get()}\t\t{self.c_spices}")


            #===============snacks price====================
            if self.cold_drink.get()!=0:
                self.txtarea.insert(END,f"\n cold drink\t\t{self.cold_drink.get()}\t\t{self.c_cold_drink}")
                
            if self.pizza.get()!=0:
                self.txtarea.insert(END,f"\n pizza\t\t{self.pizza.get()}\t\t{self.c_pizza}")

            if self.burger.get()!=0:
                self.txtarea.insert(END,f"\n burger\t\t{self.burger.get()}\t\t{self.c_burger}")

            if self.sweet.get()!=0:
                self.txtarea.insert(END,f"\n sweet\t\t{self.sweet.get()}\t\t{self.c_sweet}")

            if self.boos.get()!=0:
                self.txtarea.insert(END,f"\n boo\t\t{self.boos.get()}\t\t{self.c_boos}")

            if self.samosa.get()!=0:
                self.txtarea.insert(END,f"\n samosa\t\t{self.samosa.get()}\t\t{self.c_samosa}")   
            
            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.cosmetic_tax.get!="0.0":
                self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t      {self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get!="0.0":
                self.txtarea.insert(END,f"\nGrocery Tax\t\t\t      {self.grocery_tax.get()}")
            
            if self.snacks_tax.get!="0.0":
                self.txtarea.insert(END,f"\nSnacks Tax\t\t\t      {self.snacks_tax.get()}")
            
            self.txtarea.insert(END,f"\n--------------------------------------")   
            self.txtarea.insert(END,f"\nTotal Price\t\t\t      Rs.{self.total_price}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            
            
            
            # if self.cosmetic_tax.get()!="RS. 0.0":
            #     self.txtarea.insert(END,f"\n Cosmetics Tax\t\t\t{self.cosmetic_tax.get()}")
            
            
            # if self.grocery_tax.get()!="RS. 0.0":
            #     self.txtarea.insert(END,f"\n grocery Tax\t\t\t{self.grocery_tax.get()}")

            # if self.snacks_price_tax.get()!="RS. 0.0":
            #     self.txtarea.insert(END,f"\n snacks price Tax\t\t\t{self.snacks_price_tax.get()}")
            #     self.txtarea.insert(END,f"\n Total bill\t\t\t  Rs.  {self.Total_bill}")

            #     self.txtarea.insert(END,f"\n--------------------------------")     

            self.save_bill()
        
    def save_bill(self):
          op=messagebox.askyesno("save Bill","Do you want to save the Bill?")
          if op>0:
              self.bill_data=self.txtarea.get('1.0',END)
              f1=open("bills/"+str(self.bill_number.get())+".txt","w")
              f1.write(self.bill_data)
              f1.close()
              messagebox.showinfo("saved",f"Bill no. :{self.bill_number.get()}saved Successfully")
          else:
              return
          
    def find_bill(self):
          present="no"
          for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in f1:
                            self.txtarea.insert(END,d)
                    f1.close()
                    present="yes"
          if present=="no":
                messagebox.showerror("Error","Invalid Bill No.")
        
    def clear_data(self):
                op=messagebox.askyesno("Exit","Do you really want tot clear?")
                if op>0:
                    #---- cosmetic  ---------
                    self.bath_soap=set(0)
                    self.face_cream=set(0) 
                    self.face_wash=set(0)
                    self.shampoo=set(0)
                    self.hair_oil=set(0)
                    self.body_lotion=set(0)
                    
                    #----- Grocery -----------
                    self.food_oil=set(0)
                    self.rice=set(0)
                    self.sugar=set(0)
                    self.salt=set(0)
                    self.flour=set(0)
                    self.spices=set(0)
                    
                    #------- snacks ----------
                    self.cold_drink=set(0)
                    self.pizza=set(0)
                    self.burger=set(0)
                    self.sweet=set(0)
                    self.boos=set(0)
                    self.samosa=set(0)
                    
                    
                    #---- Total and Tax Price-----
                    self.cosmetic_price.set("")
                    self.grocery_price.set("")
                    self.snacks_price.set("")
                    
                    self.cosmetic_tax.set("")
                    self.grocery_tax.set("")
                    self.snacks_tax.set("")
                    
                    #===============Customer============
                    self.bill_no.set("")
                    X=random.randiant(1000,9999)
                    self.bill_no.set(str(X))

                    self.search_bill.set("")
                    self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want tot exit?")
        if op>0:
            self.root.destroy()                      
    
        
                                

root=Tk() 
obj = Bill_App(root)
root.mainloop()
