import tkinter as tk
from tkinter import ttk, messagebox
import tkinter
from tkinter import *

class theatre():#Theatre adıyla bir class oluşturduk.

    
    
        def _init_ (self,name,surname,phone_number,day,month,year,theatre,saloon,people,seat):#Constructorda nesneleri tanımladık.
            self.name=name
            self.surname=surname
            self.phone_number=phone_number
            self.day=day
            self.month=month
            self.year=year
            self.theatre=theatre
            self.saloon=saloon
            self.people=people
            self.seat=seat
    
        def theatres(self):#Girdi alıcağımız ekranı bu fonksiyona bağladık.
            theatres=tkinter.Tk()#Açılacak ekranı burada belirledik.
            theatres.geometry("5000x5000")#Ekran boyutunu burada ayarladık.
            theatres.title("EB theatre")#Açılan ekranın ismini belirledik.
            theatres.configure(background="bisque")#Arkaplan rengini ayarladıkç
            name_text=tk.Label(theatres,text="Name:",font="times 20 italic").place(x=100,y=50)#Ekrana Name yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            surname_text=tk.Label(theatres,text="Surname:",font="times 20 italic").place(x=100,y=100)#Ekrana Surname yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            Phone_text=tk.Label(theatres,text="Phone Number:",font="times 20 italic").place(x=100,y=150)#Ekrana Phone Number yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            name=tk.Entry(theatres)#Girdi almak için Entry fonksiyonunu kullandık.
            name.place(x=200,y=60)#Girdi kutusunun yeri ayarlandı.
            surname=tk.Entry(theatres)#Girdi almak için Entry fonksiyonunu kullandık.
            surname.place(x=220,y=110)#Girdi kutusunun yeri ayarlandı.
            phone_number=tk.Entry(theatres)#Girdi almak için Entry fonksiyonunu kullandık.
            phone_number.place(x=290,y=160)#Girdi kutusunun yeri ayarlandı.    
            #Day----------------------------------
            reservation_text=tk.Label(theatres,text="Reservation",font=20).place(x=100,y=10)#Ekrana Reservation yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            day_list = ["1","2","3","4","5","6","7","8","9","10"
            ,"11","12","13","14","15","16","17","18","19","20"
            ,"21","22","23","24","25","26","27","28","29","30"]#Günleri bir dizi haline getirdik.
            Day = ttk.Combobox(theatres, values = day_list)#Gün seçimi için değeri listeye atadık. 
            Day.set("Pick A Day")#Gün seçimi için kutuya Pick A Day yazdırıp set() fonksiyonu ile listeyi çağırdık.
            Day.place(x=100, y = 200)#Seçim ekranı için yeri ayarladık.
            #Month--------------------------------
            month_list = ["January", "February", "March",
            "April", "May","June","July","August","September"
            ,"October","November","December"]#Ayları bir dizi haline getirdik. 
            Month = ttk.Combobox(theatres, values = month_list)#Ay seçimi için değeri listeye atadık.
            Month.set("Pick A Month")#Ay seçimi için kutuya Pick A Month yazdırıp set() fonksiyonu ile listeyi çağırdık.
            Month.place(x=250, y = 200)#Seçim ekranı için yeri ayarladık.
            #Year---------------------------------
            year_list = ["2022", "2023", "2024",]#Yılları bir dizi haline getirdik.
            Year = ttk.Combobox(theatres, values = year_list)#Yıl seçimi için değeri listeye atadık.
            Year.set("Pick A Year")#Yıl seçimi için kutuya Pick A Yeat yazdırıp set() fonksiyonu ile listeyi çağırdık.
            Year.place(x=400, y = 200)#Seçim ekranı için yeri ayarladık.
            #Show--------------------------------
            theatre_list=["CMYLMZ","Arkadaşım Hoşgeldin","Konuşanlar"]#Gösterileri bir dizi haline getirdik.
            theatre= ttk.Combobox(theatres,values=theatre_list)#Gösteri seçimi için değeri listeye atadık.
            theatre.set("Pick a theatre")#Gösteri seçimi için kutuya Pick a theatre yazdırıp set() fonksiyonu ile listeyi çağırdık.
            theatre.place(x=100, y=250)#Seçim ekranı için yeri ayarladık.
            #Saloon-------------------------------
            saloon_list=["1.saloon","2.saloon","3.saloon"]#Salonları bir dizi haline getirdik.
            saloon=ttk.Combobox(theatres,values=saloon_list)#Salon seçimi için değeri listeye atadık.
            saloon.set("Pick a saloon")#Salon seçimi için kutuya Pick a Saloon yazdırıp set() fonksiyonu ile listeyi çağırdık.
            saloon.place(x=250,y=250)#Seçim ekranı için yeri ayarladık.
            #Number of people---------------------
            people_list=["1","2","3","4","5"]#Kişi sayısını bir dizi haline getirdik.
            people=ttk.Combobox(theatres,values=people_list)#Kişi sayısı seçimi için değeri listeye atadık.
            people.set("Chose number of people")#Kişi sayısı seçimi için kutuya Choose number of people yazdırıp set() fonksiyonu ile listeyi çağırdık.
            people.place(x=400,y=250)#Seçim ekranı için yeri ayarladık.
           
            def theatrelist():#Bu fonksiyonda yeni açılan pencerede get() fonksiyonu ile rezervasyon bilgilerini yeni ekrana yazdırdık.
                theatrelist=tkinter.Tk()
                a1=name.get()
                c1=tk.Label(theatrelist,text="name :"+a1,font="times 20 italic").pack()
                
                a2=surname.get()
                c2=tk.Label(theatrelist,text="surname :"+a2,font="times 20 italic").pack()
                
                
                a3=phone_number.get()
                c3=tk.Label(theatrelist,text="phone number :"+a3,font="times 20 italic").pack()
                
                a4=Day.get()
                c4=tk.Label(theatrelist,text="Day :"+a4,font="times 20 italic").pack()
                
                a5=Month.get()
                c5=tk.Label(theatrelist,text="Month :"+a5,font="times 20 italic").pack()
                
                
                a7=Year.get()
                c7=tk.Label(theatrelist,text="Year :"+a7,font="times 20 italic").pack()
                
                a8=theatre.get()
                c8=tk.Label(theatrelist,text="Theatre :"+a8,font="times 20 italic").pack()
                
                a9=saloon.get()
                c9=tk.Label(theatrelist,text="Saloon :"+a9,font="times 20 italic").pack()
                
                a10=people.get()
                c10=tk.Label(theatrelist,text="People :"+a10,font="times 20 italic").pack()

                c12=tk.Label(theatrelist,text="The reservation has been made successfully. You will pay the fee at the box office."
                ,font="times 20 italic").pack()
            reservation_button = Button(theatres, text = " Make a reservation " , width=15, command=theatrelist)#Butonu rezervasyon bilgilerini gösteren fonksiyonu butona bağladık.
            reservation_button.place(x=250, y=300)#Yerini ayarladık.


            #Günlük bilet Satımı
            ticket_text=tk.Label(theatres,text="Day ticket purchase",font=20).place(x=100,y=350)#Ekrana Day ticket purchase yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            ticket_name=tk.Label(theatres,text="Name:",font=20).place(x=100,y=400)#Ekrana Name yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            ticket_surname=tk.Label(theatres,text="Surname:",font=20).place(x=100,y=450)#Ekrana Surname yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            ticket_phone=tk.Label(theatres,text="Phone number:",font=20).place(x=100,y=500)#Ekrana Phone Number yazısını getirdik.(yazı tipi ve yeri ayarlandı)
            ticket_name=tk.Entry(theatres)#Girdi almak için Entry fonksiyonunu kullandık.
            ticket_name.place(x=180,y=405)#Yerini ayarladık.
            ticket_surname=tk.Entry(theatres)#Girdi almak için Entry fonksiyonunu kullandık.
            ticket_surname.place(x=200,y=455)#Seçim ekranı için yeri ayarladık.
            ticket_phone=tk.Entry(theatres)#Girdi almak için Entry fonksiyonunu kullandık.
            ticket_phone.place(x=250,y=505)#Seçim ekranı için yeri ayarladık.
            #Movie--------------------------------
            ticket_theatre_list=["CMYLMZ","Arkadaşım Hoşgeldin","Konuşanlar"]#Gösterileri bir dizi haline getirdik.
            ticket_theatre= ttk.Combobox(theatres,values=ticket_theatre_list)#Gösteri seçimi için değeri listeye atadık.
            ticket_theatre.set("Pick a theatre")#Gösteri seçimi için kutuya Pick a theatre yazdırıp set() fonksiyonu ile listeyi çağırdık.
            ticket_theatre.place(x=100, y=550)#Yerini ayarladık.
            #Saloon-------------------------------
            ticket_saloon_list=["1.saloon","2.saloon","3.saloon"]#Salonları bir dizi haline getirdik.
            ticket_saloon=ttk.Combobox(theatres,values=ticket_saloon_list)#Salon seçimi için değeri listeye atadık.
            ticket_saloon.set("Pick a saloon")#Salon seçimi için kutuya Pick a Saloon yazdırıp set() fonksiyonu ile listeyi çağırdık.
            ticket_saloon.place(x=250,y=550)#Seçim ekranı için yeri ayarladık.
            #Number of people---------------------
            ticket_people_list=["1","2","3","4","5"]#Kişi sayısını bir dizi haline getirdik.
            ticket_people=ttk.Combobox(theatres,values=ticket_people_list)#Kişi sayısı seçimi için değeri listeye atadık.
            ticket_people.set("Chose number of people")#Kişi sayısı seçimi için kutuya Choose number of people yazdırıp set() fonksiyonu ile listeyi çağırdık.
            ticket_people.place(x=400,y=550)#Seçim ekranı için yeri ayarladık.
            #Seat---------------------------------
            ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
            "14","15","16","17","18","19","20"]#Koltuk sayısını bir dizi haline getirdik
            ticket_seat=ttk.Combobox(theatres,values=ticket_seat_list)#Koltuk sayısı seçimi için değeri listeye atadık.
            ticket_seat.set("Chose a seat")#Koltuk sayısı seçimi için kutuya Choose number of people yazdırıp set() fonksiyonu ile listeyi çağırdık.
            ticket_seat.place(x=100,y=580)#Seçim ekranı için yeri ayarladık.
            
            def chooseseat():#Bu fonksiyonda if yapısı kullanarak diğer koltukları seçmemizi sağlayan bir yapı oluşturduk.Bilgileri get() fonksiyonu ile de ekrana yazdırdık.
                a15=ticket_people.get()
                if a15=="1":
                    pass
                    
                elif a15=="2":
                    ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                    "14","15","16","17","18","19","20"]
                    ticket_seat=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat.set("Choose a seat for the 2nd person")
                    ticket_seat.place(x=100,y=610) 
                    a1=ticket_seat.get()
                    tk.Label(buyticket,text="a"+a1).pack()
                    
                elif a15=="3":
                    ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                    "14","15","16","17","18","19","20"]
                    ticket_seat1=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat1.set("Choose a seat for the 2nd person")
                    ticket_seat1.place(x=100,y=610) 
                    
                    ticket_seat2=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat2.set("Choose a seat for the 3nd person")
                    ticket_seat2.place(x=100,y=640) 
                    
                    
                elif a15=="4":    
                    ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                    "14","15","16","17","18","19","20"]
                    ticket_seat1=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat1.set("Choose a seat for the 2nd person")
                    ticket_seat1.place(x=100,y=610) 
                    
                    ticket_seat2=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat2.set("Choose a seat for the 3nd person")
                    ticket_seat2.place(x=100,y=640) 
                    
                    ticket_seat3=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat3.set("Choose a seat for the 4nd person")
                    ticket_seat3.place(x=100,y=670) 
                    
                    
                    
                elif a15=="5":
                    ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                    "14","15","16","17","18","19","20"]
                    ticket_seat1=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat1.set("Choose a seat for the 2nd person")
                    ticket_seat1.place(x=100,y=610) 
                    
                    ticket_seat2=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat2.set("Choose a seat for the 3nd person")
                    ticket_seat2.place(x=100,y=640) 
                    
                    ticket_seat3=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat3.set("Choose a seat for the 4nd person")
                    ticket_seat3.place(x=100,y=670) 
            
                    ticket_seat3=ttk.Combobox(theatres,values=ticket_seat_list)
                    ticket_seat3.set("Choose a seat for the 5nd person")
                    ticket_seat3.place(x=250,y=580)
                
                else:
                    pass
    
            
            def buyticket():#Bilet bilgilerini get() fonksiyonu ile çağırıp ekrana yazdırdık.
                buyticket=tkinter.Tk()
                name1=ticket_name.get()
                c1=tk.Label(buyticket,text="name :"+name1,font="times 20 italic").pack()
                
                surname1=ticket_surname.get()
                c2=tk.Label(buyticket,text="surname :"+surname1,font="times 20 italic").pack()
                
                
                a3=ticket_phone.get()
                c3=tk.Label(buyticket,text="phone number :"+a3,font="times 20 italic").pack()
            
                a4=ticket_theatre.get()
                c8=tk.Label(buyticket,text="Theatre :"+a4,font="times 20 italic").pack()
                
                a5=ticket_seat.get()
                c9=tk.Label(buyticket,text="Saloon :"+a5,font="times 20 italic").pack()
                
                
                a6=ticket_people.get()
                c10=tk.Label(buyticket,text="People :"+a6,font="times 20 italic").pack()

                a7=ticket_seat.get()
                c11=tk.Label(buyticket,text="Seat Number :"+a7,font="times 20 italic").pack()
                
            
                #İf yapısı ile fiyatı belirledik.
                if a6=="1":
                    tk.Label(buyticket,text="Purchase succesful.The ticket has been purchased. Please go to the saloon.Total price=10$").pack()
                elif a6=="2":
                    tk.Label(buyticket,text="Purchase succesful.The ticket has been purchased. Please go to the saloon.Total price=20$").pack()
                elif a6=="3":
                    tk.Label(buyticket,text="Purchase succesful.The ticket has been purchased. Please go to the saloon.Total price=30$").pack()
                elif a6=="4":
                    tk.Label(buyticket,text="Purchase succesful.The ticket has been purchased. Please go to the saloon.Total price=40$").pack()
                elif a6=="5":
                    tk.Label(buyticket,text="Purchase succesful.The ticket has been purchased. Please go to the saloon.Total price=50$").pack() 
            
        
            daily_button = Button(theatres, text = "Choose other seat" , width=15, command=chooseseat)#Buton oluşturup koltuk seçimini sağlayan buton ayarladık.
            daily_button.place(x=100, y=700) 
                
                
                
                
            reservation_button = Button(theatres, text = " Make a reservation " , width=15, command=theatrelist)#Rezervasyon bilgilerini gösteren buton ayarladık. 
            reservation_button.place(x=250, y=300)
            
            
            buybutton=Button(theatres,text="Buy Ticket",width=15,command=buyticket)#Günlük bilet alım bilgilerini gösteren buton ayarladık.
            buybutton.place(x=220,y=700)
            
            


            

            def ex_but():#Programı kapatması için fonksiyon belirledik.
                exit(theatres)#exit()^fonksiyonunu kullandık.
            exit_buton=Button(theatres,text="Confirm and finish",command=ex_but)#Çıkış butonunu fonksiyona bağladık.
            exit_buton.place(x=450,y=700)#Yerini ayarladık.
       
       