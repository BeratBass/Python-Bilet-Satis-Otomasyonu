import tkinter as tk
from tkinter import ttk, messagebox
import tkinter
from tkinter import *
from tkinter import messagebox as msgbox




class cinema():
    
    def _init_(self,name,surname,phone_number,day,month,year,movie,saloon,people,seat,price):
         
        self.name=name
        self.surname=surname
        self.phone_number=phone_number
        self.day=day
        self.month=month
        self.year=year
        self.movie=movie
        self.saloon=saloon
        self.people=people
        self.seat=seat

    def cinemas(self):

#RESERVATİON--------------------------
#İnformation--------------------------  
        cinemas=tkinter.Tk()
        cinemas.geometry("1800x800")
        cinemas.title("EB cinema")
        cinemas.configure(background="bisque")
        name_text=tk.Label(cinemas,text="Name:",font="times 20 italic").place(x=100,y=50)
        surname_text=tk.Label(cinemas,text="Surname:",font="times 20 italic").place(x=100,y=100)
        Phone_text=tk.Label(cinemas,text="Phone Number:",font="times 20 italic").place(x=100,y=150)
        name=tk.Entry(cinemas)
        name.place(x=200,y=60)
        surname=tk.Entry(cinemas)
        surname.place(x=220,y=110)
        phone_number=tk.Entry(cinemas)
        phone_number.place(x=290,y=160)    
        #Day----------------------------------
        reservation_text=tk.Label(cinemas,text="Reservation",font=20).place(x=100,y=10)
        day_list = ["1","2","3","4","5","6","7","8","9","10"
        ,"11","12","13","14","15","16","17","18","19","20"
        ,"21","22","23","24","25","26","27","28","29","30"]
        Day = ttk.Combobox(cinemas, values = day_list)
        Day.set("Pick a Day")
        Day.place(x=100, y = 200)
        #Month--------------------------------
        month_list = ["January", "February", "March",
          "April", "May","June","July","August","September"
          ,"October","November","December"] 
        Month = ttk.Combobox(cinemas, values = month_list)
        Month.set("Pick a Month")
        Month.place(x=250, y = 200)
        #Year---------------------------------
        year_list = ["2022", "2023", "2024",]
        Year = ttk.Combobox(cinemas, values = year_list)
        Year.set("Pick a Year")
        Year.place(x=400, y = 200)
        #Movie--------------------------------
        movie_list=["Recep İvedik 7","Maskeli Beşler Irak","Kolpaçino:Bomba","Avatar 2","Babam ve Oğlum","GORA"
        ,"AROG","Issız Adam","Kurtlar Vadisi Irak"]
        Movie= ttk.Combobox(cinemas,values=movie_list)
        Movie.set("Pick a movie")
        Movie.place(x=100, y=250)
        #Saloon-------------------------------
        saloon_list=["1.saloon","2.saloon","3.saloon"]
        saloon=ttk.Combobox(cinemas,values=saloon_list)
        saloon.set("Pick a saloon")
        saloon.place(x=250,y=250)
        #Number of people---------------------
        people_list=["1","2","3","4","5"]
        people=ttk.Combobox(cinemas,values=people_list)
        people.set("Chose number of people")
        people.place(x=400,y=250)
       
        def cinemalist():
            cinemalist=tkinter.Tk()
            a1=name.get()
            c1=tk.Label(cinemalist,text="name :"+a1,font="times 20 italic").pack()
            
            a2=surname.get()
            c2=tk.Label(cinemalist,text="surname :"+a2,font="times 20 italic").pack()
            
            
            a3=phone_number.get()
            c3=tk.Label(cinemalist,text="phone number :"+a3,font="times 20 italic").pack()
            
            a4=Day.get()
            c4=tk.Label(cinemalist,text="Day :"+a4,font="times 20 italic").pack()
            
            a5=Month.get()
            c5=tk.Label(cinemalist,text="Month :"+a5,font="times 20 italic").pack()
            
            
            a7=Year.get()
            c7=tk.Label(cinemalist,text="Year :"+a7,font="times 20 italic").pack()
            
            a8=Movie.get()
            c8=tk.Label(cinemalist,text="Movie :"+a8,font="times 20 italic").pack()
            
            a9=saloon.get()
            c9=tk.Label(cinemalist,text="Saloon :"+a9,font="times 20 italic").pack()
            
            a10=people.get()
            c10=tk.Label(cinemalist,text="People :"+a10,font="times 20 italic").pack()

          

            c12=tk.Label(cinemalist,text="The reservation has been made successfully. You will pay the fee at the box office."
            ,font="times 20 italic").pack()
            exit_button=Button(text="confirm and finish",width=15,command=exit)
            exit_button.place(x=10,y=10)

            
        reservation_button = Button(cinemas, text = " Make a reservation " , width=15, command=cinemalist) 
        reservation_button.place(x=250, y=300)
        
        
        

        
        #Buy Ticket-------------------------------------
        ticket_text=tk.Label(cinemas,text="Day ticket purchase",font=20).place(x=100,y=350)
        ticket_name=tk.Label(cinemas,text="Name:",font=20).place(x=100,y=400)
        ticket_surname=tk.Label(cinemas,text="Surname:",font=20).place(x=100,y=450)
        ticket_phone=tk.Label(cinemas,text="Phone number:",font=20).place(x=100,y=500)
        ticket_name=tk.Entry(cinemas)
        ticket_name.place(x=180,y=405)
        ticket_surname=tk.Entry(cinemas)
        ticket_surname.place(x=200,y=455)
        ticket_phone=tk.Entry(cinemas)
        ticket_phone.place(x=250,y=505)
        #Movie--------------------------------
        ticket_movie_list=["Recep İvedik 7","Maskeli Beşler Irak","Kolpaçino:Bomba","Avatar 2","Babam ve Oğlum","GORA"
        ,"AROG","Issız Adam","Kurtlar Vadisi Irak"]
        ticket_Movie= ttk.Combobox(cinemas,values=ticket_movie_list)
        ticket_Movie.set("Pick a movie")
        ticket_Movie.place(x=100, y=550)
        #Saloon-------------------------------
        ticket_saloon_list=["1.saloon","2.saloon","3.saloon"]
        ticket_saloon=ttk.Combobox(cinemas,values=ticket_saloon_list)
        ticket_saloon.set("Pick a saloon")
        ticket_saloon.place(x=250,y=550)
        #Number of people---------------------
        ticket_people_list=["1","2","3","4","5"]
        ticket_people=ttk.Combobox(cinemas,values=ticket_people_list)
        ticket_people.set("Chose number of people")
        ticket_people.place(x=400,y=550)
        #Seat---------------------------------
        ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
        "14","15","16","17","18","19","20"]
        ticket_seat=ttk.Combobox(cinemas,values=ticket_seat_list)
        ticket_seat.set("Chose a seat")
        ticket_seat.place(x=100,y=580)
        
        def chooseseat():
            a15=ticket_people.get()
            if a15=="1":
                pass
                
            elif a15=="2":
                ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                "14","15","16","17","18","19","20"]
                ticket_seat=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat.set("Choose a seat for the 2nd person")
                ticket_seat.place(x=100,y=610) 
                a1=ticket_seat.get()
                tk.Label(buyticket,text="a"+a1).pack()
                
                
            elif a15=="3":
                ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                "14","15","16","17","18","19","20"]
                ticket_seat1=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat1.set("Choose a seat for the 2nd person")
                ticket_seat1.place(x=100,y=610) 
                
                ticket_seat2=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat2.set("Choose a seat for the 3nd person")
                ticket_seat2.place(x=100,y=640) 
                
                 
            elif a15=="4":    
                ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                "14","15","16","17","18","19","20"]
                ticket_seat1=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat1.set("Choose a seat for the 2nd person")
                ticket_seat1.place(x=100,y=610) 
                
                ticket_seat2=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat2.set("Choose a seat for the 3nd person")
                ticket_seat2.place(x=100,y=640) 
                
                ticket_seat3=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat3.set("Choose a seat for the 4nd person")
                ticket_seat3.place(x=100,y=670) 
                
                
                
            elif a15=="5":
                ticket_seat_list=["1","2","3","4","5","6","7","8","9","10","11","12","13",
                "14","15","16","17","18","19","20"]
                ticket_seat1=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat1.set("Choose a seat for the 2nd person")
                ticket_seat1.place(x=100,y=610) 
                
                ticket_seat2=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat2.set("Choose a seat for the 3nd person")
                ticket_seat2.place(x=100,y=640) 
                
                ticket_seat3=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat3.set("Choose a seat for the 4nd person")
                ticket_seat3.place(x=100,y=670) 
        
                ticket_seat3=ttk.Combobox(cinemas,values=ticket_seat_list)
                ticket_seat3.set("Choose a seat for the 5nd person")
                ticket_seat3.place(x=250,y=580)
             
            else:
                pass
 
        
        def buyticket():
            buyticket=tkinter.Tk()
            name1=ticket_name.get()
            c1=tk.Label(buyticket,text="name :"+name1,font="times 20 italic").pack()
            
            surname1=ticket_surname.get()
            c2=tk.Label(buyticket,text="surname :"+surname1,font="times 20 italic").pack()
            
            
            a3=ticket_phone.get()
            c3=tk.Label(buyticket,text="phone number :"+a3,font="times 20 italic").pack()
        
            a4=ticket_Movie.get()
            c8=tk.Label(buyticket,text="Movie :"+a4,font="times 20 italic").pack()
            
            a5=ticket_seat.get()
            c9=tk.Label(buyticket,text="Saloon :"+a5,font="times 20 italic").pack()
            
            
            a6=ticket_people.get()
            c10=tk.Label(buyticket,text="People :"+a6,font="times 20 italic").pack()

            a7=ticket_seat.get()
            c11=tk.Label(buyticket,text="Seat Number :"+a7,font="times 20 italic").pack()
            
        
            
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
           
    
        daily_button = Button(cinemas, text = "Choose other seat" , width=15, command=chooseseat) 
        daily_button.place(x=100, y=700) 
            
            
            
            
        reservation_button = Button(cinemas, text = " Make a reservation " , width=15, command=cinemalist) 
        reservation_button.place(x=250, y=300)
        
        
        buybutton=Button(cinemas,text="Buy Ticket",width=15,command=buyticket)
        buybutton.place(x=220,y=700)

        def ex_but():
            exit(cinemas)
        exit_buton=Button(cinemas,text="Confirm and finish",command=ex_but)
        exit_buton.place(x=450,y=700)

        