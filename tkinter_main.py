from tkinter import * 
import tkinter as tk
from cinema import cinema
from concert import concert
from theatre import theatre
import webbrowser


class automationn (Frame,concert,theatre,cinema): #class oluşturulup cinema,concert ve theatre sayfalarından bilgileri çektik.

    def __init__(self,automation=None):
        Frame.__init__(self,automation)
        self.automation=automation



        F1 = Frame(self.automation)#main pencereyi oluşturduk.
        F1.pack(pady=15, padx=25)

        self.automation=automation
        self.automation.title("Ticket Automation")
        self.automation.geometry("1800x800") #main pencerenin boyutunu ayarladık.

        bgimg= tk.PhotoImage(file = "--image--\\cinemaphoto\\backs.png") #main pencerenin arkaplanını ayarladık
        limg= Label(windows, i=bgimg)
        limg.image=bgimg
        limg.place(x=0,y=0)

    
        

        B1=tk.Button(automation,text="CINEMAS",fg="white",font=20,command=self.cinemas,width=30,height=10,bg="black").place(x=200,y=30)
        B2=tk.Button(automation,text="THEATRE",fg="white",font=20,command=self.theatres,width=30,height=10,bg="black").place(x=600,y=30)
        B3=tk.Button(automation,text="CONCERT",fg="white",font=20,command=self.concerts,width=30,height=10,bg="black").place(x=1000,y=30)
        #3 tane buton oluşturup çektiğimiz verileri butonlara atadık.
    
    
    
    
    
        #CİNEMA
        #cinema fragmanlarına ait url ekledik.
        new=1
        url1 = "https://www.youtube.com/watch?v=KCKWmyVUvF8"
        url2= "https://www.beyazperde.com/filmler/film-178014/fragman-19562741/"
        url3="https://www.beyazperde.com/filmler/film-111471/fragman-19262000/"
        url4="https://www.youtube.com/watch?v=UTUiQ9NWZcM"
        url5="https://www.youtube.com/watch?v=b4eRD9iK2Zg"
        url6="https://www.beyazperde.com/filmler/film-190818/fragman-19201997/"
        url7="https://www.beyazperde.com/filmler/film-110721/fragman-19519528/"
        url8="https://www.beyazperde.com/filmler/film-186880/fragman-19520546/"
        url9="https://www.beyazperde.com/filmler/film-305459/fragman-19565539/"

        def openweb():
            webbrowser.open(url1,new=new)
        def openweb1():
            webbrowser.open(url2,new=new) 
        def openweb2():
            webbrowser.open(url3,new=new) 
        def openweb3():
            webbrowser.open(url4,new=new) 
        def openweb4():
            webbrowser.open(url5,new=new) 
        def openweb5():
            webbrowser.open(url6,new=new) 
        def openweb6():
            webbrowser.open(url7,new=new) 
        def openweb7():
            webbrowser.open(url8,new=new) 
        def openweb8():
            webbrowser.open(url9,new=new) 
        
        
        film_text=Label(text="Films:",font=20,bg="lavenderblush").place(x=200,y=280)
        trailer_text=Label(text="   Click on the movie buttons for the trailer    ",font=1,bg="lavenderblush").place(x=200,y=750)
        

        #cinemaya ait pngleri ekledik. 
        filmimg=PhotoImage(file="--image--\\cinemaphoto\\arog.png")
        filmbutton=tk.Button(windows,image=filmimg,command=openweb)
        filmbutton.image=filmimg
        filmbutton.place(x=200,y=325,width=125,height=125)

        filmimg2=PhotoImage(file="--image--\\cinemaphoto\\avatar_2.png")
        filmbutton2=tk.Button(windows,image=filmimg2,command=openweb1)
        filmbutton2.image=filmimg2
        filmbutton2.place(x=320,y=325,width=125,height=125)

        filmimg3=PhotoImage(file="--image--\\cinemaphoto\\Babam_Ve_Oğlum.png")
        filmbutton3=tk.Button(windows,image=filmimg3,command=openweb2)
        filmbutton3.image=filmimg3
        filmbutton3.place(x=440,y=325,width=125,height=125)

        filmimg4=PhotoImage(file="--image--\\cinemaphoto\\Gora.png")
        filmbutton4=tk.Button(windows,image=filmimg4,command=openweb3)
        filmbutton4.image=filmimg4
        filmbutton4.place(x=200,y=475,width=125,height=125)

        filmimg5=PhotoImage(file="--image--\\cinemaphoto\\Issız_Adam.png")
        filmbutton5=tk.Button(windows,image=filmimg5,command=openweb4)
        filmbutton5.image=filmimg5
        filmbutton5.place(x=320,y=475,width=125,height=125)

        filmimg6=PhotoImage(file="--image--\\cinemaphoto\\kolpacino.png")
        filmbutton6=tk.Button(windows,image=filmimg6,command=openweb5)
        filmbutton6.image=filmimg6
        filmbutton6.place(x=440,y=475,width=125,height=125)

        filmimg7=PhotoImage(file="--image--\\cinemaphoto\\Kurtlar_Vadisi_Irak.png")
        filmbutton7=tk.Button(windows,image=filmimg7,command=openweb6)
        filmbutton7.image=filmimg7
        filmbutton7.place(x=200,y=625,width=125,height=125)

        filmimg8=PhotoImage(file="--image--\\cinemaphoto\\Maskeli_Besler_Irak.png")
        filmbutton8=tk.Button(windows,image=filmimg8,command=openweb7)
        filmbutton8.image=filmimg8
        filmbutton8.place(x=320,y=625,width=125,height=125)

        filmimg9=PhotoImage(file="--image--\\cinemaphoto\\Recepİvedik_7.png")
        filmbutton9=tk.Button(windows,image=filmimg9,command=openweb8)
        filmbutton9.image=filmimg9
        filmbutton9.place(x=440,y=625,width=125,height=125)       
        
        #THEATRE
        #thatre ait gösterim linklerini ekledik.
        url1_1="https://www.youtube.com/watch?v=wtb4z9IUY88&ab_channel=CemY%C4%B1lmaz"
        url2_1="https://www.youtube.com/watch?v=tEz45puL2MA&ab_channel=Konu%C5%9Fanlar"
        url3_1="https://www.youtube.com/watch?v=48DjAw-TLhU&ab_channel=Arkada%C5%9F%C4%B1mHo%C5%9Fgeldin"
        def theatreopenweb():
            webbrowser.open(url1_1,new=new)
        def theatreweb1():
            webbrowser.open(url2_1,new=new) 
        def theatreweb2():
            webbrowser.open(url3_1,new=new)
        example_show_text=Label(text="Click the buttons for sample shows",font=1,bg="lavenderblush").place(x=640,y=750)
        show_text=Label(text="Shows:",font=20,bg="lavenderblush").place(x=600,y=280)

        #theatre ait pngleri ekledik.
        theatreimg=PhotoImage(file="--image--\\theatrephoto\\cmylmz.png")
        theatrebutton=tk.Button(windows,image=theatreimg,command=theatreopenweb)
        theatrebutton.image=theatreimg
        theatrebutton.place(x=700,y=325,width=125,height=175)

        theatreimg2=PhotoImage(file="--image--\\theatrephoto\\konusanlar.png")
        theatrebutton2=tk.Button(windows,image=theatreimg2,command=theatreweb1)
        theatrebutton2.image=theatreimg2
        theatrebutton2.place(x=700,y=490,width=125,height=125)
        
        theatreimg3=PhotoImage(file="--image--\\theatrephoto\\tolga.png")
        theatrebutton3=tk.Button(windows,image=theatreimg3,command=theatreweb2)
        theatrebutton3.image=theatreimg3
        theatrebutton3.place(x=700,y=625,width=125,height=125)

        #CONCERTİMAGE
        #concert ait videoları ekledik
        url1_2="https://www.youtube.com/watch?v=05aMeIQCiUc"
        url2_2="https://www.youtube.com/watch?v=XWzEcIj1xk8&ab_channel=maNga"
        url3_2="https://www.youtube.com/watch?v=GGnNh91k9TI&ab_channel=SD"
        url4_2="https://www.youtube.com/watch?v=AnAr-ol3YTA&ab_channel=Kaan"
        url5_2="https://www.youtube.com/watch?v=b6S-QNWK7pY&ab_channel=CenkAlma"
        url6_2="https://www.youtube.com/watch?v=R-igUeDzvVk&ab_channel=PollProduction"

        def concertopenweb():
            webbrowser.open(url1_2,new=new)
        def concertopenweb1():
            webbrowser.open(url2_2,new=new) 
        def concertopenweb2():
            webbrowser.open(url3_2,new=new)
        def concertopenweb3():
            webbrowser.open(url4_2,new=new)
        def concertopenweb4():
            webbrowser.open(url5_2,new=new)
        def concertopenweb5():
            webbrowser.open(url6_2,new=new)                    
        sing_text=Label(text="Click the buttons for sample concert",font=1,bg="lavenderblush").place(x=1100,y=750)

        singer_text=Label(text="Singers:",font=20,bg="lavenderblush").place(x=1000,y=280)
        
        #concert ait pngleri ekledik
        concertimg=PhotoImage(file="--image--\\concertphoto\\duman.png")
        concertbutton=tk.Button(windows,image=concertimg,command=concertopenweb)
        concertbutton.image=concertimg
        concertbutton.place(x=1000,y=325,width=150,height=150)

        concertimg2=PhotoImage(file="--image--\\concertphoto\\manga.png")
        concertbutton2=tk.Button(windows,image=concertimg2,command=concertopenweb1)
        concertbutton2.image=concertimg2
        concertbutton2.place(x=1160,y=325,width=150,height=150)

        concertimg3=PhotoImage(file="--image--\\concertphoto\\şanışer.png")
        concertbutton3=tk.Button(windows,image=concertimg3,command=concertopenweb2)
        concertbutton3.image=concertimg3
        concertbutton3.place(x=1320,y=325,width=150,height=150)

        concertimg4=PhotoImage(file="--image--\\concertphoto\\sezenaksu.png")
        concertbutton4=tk.Button(windows,image=concertimg4,command=concertopenweb3)
        concertbutton4.image=concertimg4
        concertbutton4.place(x=1160,y=525,width=150,height=150)

        concertimg5=PhotoImage(file="--image--\\concertphoto\\yalın.png")
        concertbutton5=tk.Button(windows,image=concertimg5,command=concertopenweb4)
        concertbutton5.image=concertimg5
        concertbutton5.place(x=1000,y=525,width=150,height=150)

        concertimg6=PhotoImage(file="--image--\\concertphoto\\yıldız tilbe.png")
        concertbutton6=tk.Button(windows,image=concertimg6,command=concertopenweb5)
        concertbutton6.image=concertimg6
        concertbutton6.place(x=1320,y=525,width=150,height=150)
        
        
       




        
        
windows=Tk()#windows adında pencere oluşturduk.       
windows.configure()

automationn(windows)#classı pencereye bağladık.
windows.mainloop()

  