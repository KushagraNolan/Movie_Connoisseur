from Tkinter import * 
from tkMessageBox import *
from PIL import ImageTk, Image
import sqlite3
import webbrowser
con=sqlite3.Connection("movie database")
cur=con.cursor()
def go():
    root=Tk() 
    root.title("Python Project")
    root.geometry("800x650")
    background_image=PhotoImage(file="C://Users/Acer/Desktop/project work/AVENGERS.gif")
    background_label =Label(root,image=background_image).grid(row=0,column=0,rowspan=15,columnspan=10)
    Label(root,text="        Movie Database choice System:",font="Aerial 15 bold italic").grid(row=0,column=1,columnspan=10)
    Label(root,text="    WELCOME TO PLETHORA OF GLOBAL CINEMATIC EXPERIENCE.......!!!!!!",font="Chiller 20 bold italic").grid(row=1,column=1,columnspan=10)
    Label(root,text="       SUBMITTED TO:                        DR. MAHESH KUMAR    ").grid(row=2,column=1,columnspan=10)
    Label(root,text="       SUBMITTED BY:                      KUSHAGRA SRIVASTAVA  ").grid(row=3,column=1,columnspan=10)
    def fun():
        
        
        webbrowser.open('http://www.imdb.com/chart/top')
        Button(root,text='top 250 movies of IMDB',command=fun).grid(row=5,column=5)
        def fun1():
            webbrowser.open('https://www.rottentomatoes.com/browse/in-theaters/')
            Button(root,text='Top boxoffice collection this weekend',command=fun1).grid(row=6,column=1,columnspan=10)
        def fun2():
            webbrowser.open('http://www.imdb.com/movies-in-theaters/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2495768482&pf_rd_r=10KV9BXT5SXG3AQSZ2RG&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_hd')
            Button(root,text='  Check out the trending movies and T.V. series this week',command=fun2).grid(row=7,column=1,columnspan=10)
        def fun3():
            webbrowser.open('https://www.youtube.com/results?search_query=latest+movie+and+tv+series+trailers++of+hollywood+2016')
            Button(root,text=' latest movie and tv series trailers!!!!! ',command=fun3).grid(row=8,column=1,columnspan=10)
    
    
    def fun4():
        root.destroy()
        root2=Tk()
        root2.title("   Genres you might be interested in  ")
        Label(root2,text=' WHAT SORTS OF MOVIES YOU PREFER WATCHING..????',font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
        def fun5():
            root2.destroy()
            root3=Tk()
            root3.title("Action MANIA")
            Label(root3,text=  "Best Action movies of the 21st century....!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=1,column=1,sticky=N+W+E+S)
            def fun5_1():
                root3.destroy()
                root5_1=Tk()
                root5_1.title("MISSION IMPOSSIBLE FRANCHISE - 5 MOVIES")
                Label(root5_1,text="  TOM CRUISE AT HIS BEST.......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,columnspan=10)
                def fun5_1_1():
                    root5_1.destroy()
                    webbrowser.open("https://en.wikipedia.org/wiki/Mission:_Impossible_(film_series)")
                Button(root5_1,text="  All About MISSION IMPOSSIBLE ",font="Chiller 15 bold italic",command=fun5_1_1).grid(row=1,column=1,sticky=N+W+E+S)
                def fun5_1_2():
                    root5_1.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0117060/?ref_=fn_al_tt_2")
                Button(root5_1,text="  imdb-MISSION IMPOSSIBLE - I ",font="timesnewroman 15 bold italic",command=fun5_1_2).grid(row=2,column=1,sticky=N+W+E+S)
                def fun5_1_3():
                    root5_1.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0120755/?ref_=nv_sr_3")
                Button(root5_1,text=" imdb-MISSION IMPOSSIBLE - II ",font="timesnewroman 15 bold italic",command=fun5_1_3).grid(row=3,column=1,sticky=N+W+E+S)
                def fun5_1_4():
                    root5_1.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0317919/?ref_=nv_sr_4")
                Button(root5_1,text= " imdb-MISSION IMPOSSIBLE - III ",font="timesnewroman 15 bold italic",command=fun5_1_4).grid(row=4,column=1,sticky=N+W+E+S)
                def fun5_1_5():
                    root5_1.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt1229238/?ref_=nv_sr_8")
                Button(root5_1,text= " Watch imdb and Trailer for-MISSION IMPOSSIBLE - ghost Protocol ",font="timesnewroman 15 bold italic",command=fun5_1_5).grid(row=5,column=1,sticky=N+W+E+S)
                def fun5_1_6():
                    root5_1.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt2381249/?ref_=nv_sr_6")
                Button(root5_1,text= " Watch imdb and Trailer for-MISSION IMPOSSIBLE - Rogue Nation ",font="timesnewroman 15 bold italic",command=fun5_1_6).grid(row=6,column=1,sticky=N+W+E+S)    
                root5_1.mainloop()
            def fun5_2():
                root3.destroy()
                root5_2=Tk()
                root5_2.title("Suicide Squad-2016")
                Label(root5_2,text="  JOKER RETURNS IN HIS GRUESOME FORMS .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
                def fun5_2_1():
                    root5_2.destroy()
                    webbrowser.open("https://en.wikipedia.org/wiki/Suicide_Squad_(film)")
                Button(root5_2,text=" ABOUT THE MOVIE-cast,Plot,Crew etc ",font="timesnewroman 15 bold italic",command=fun5_2_1).grid(row=2,column=1,sticky=N+W+E+S)   
                def fun5_2_2():
                    root5_2.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt1386697/?ref_=nv_sr_1")
                Button(root5_2,text=" Watch IMDB and Trailer -Click Here",font="timesnewroman 15 bold italic",command=fun5_2_2).grid(row=3,column=1,sticky=N+W+E+S)
                root5_2.mainloop()   
            def fun5_3():
                root3.destroy()
                root5_3=Tk()
                root5_3.title("STAR WARS FRANCHISE - 7 MOVIES")
                Label(root5_3,text="  DIVE INTO THE FICTIONAL GALAXICAL ENTERTAINMENT .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
                def fun5_3_1():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0120915/?ref_=nv_sr_1")
                def fun5_3_2():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0121765/?ref_=nv_sr_1")
                def fun5_3_3():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0121766/?ref_=nv_sr_1")
                def fun5_3_4():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0076759/?ref_=nv_sr_4")
                def fun5_3_5():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0080684/?ref_=nv_sr_1")
                def fun5_3_6():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0086190/?ref_=fn_al_tt_1")
                def fun5_3_7():
                    root5_3.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt2488496/?ref_=nv_sr_1")
                Button(root5_3,text='Watch IMDB and Trailer for - SW I- The Phantom Menace  ',command=fun5_3_1).grid(row=1,column=1,sticky=N+W+E+S)
                Button(root5_3,text='  Watch IMDB and Trailer for - SW II- Attack of The Clones ',command=fun5_3_2).grid(row=2,column=1,sticky=N+W+E+S)
                Button(root5_3,text=' Watch IMDB  for - SW III- Revenge OF The Sith  ',command=fun5_3_3).grid(row=3,column=1,sticky=N+W+E+S)
                Button(root5_3,text='  Watch IMDB and Trailer for - SW IV- A New Hope ',command=fun5_3_4).grid(row=4,column=1,sticky=N+W+E+S)    
                Button(root5_3,text='   Watch IMDB and Trailer for - SW V- The Empire  Strikes Back',command=fun5_3_5).grid(row=5,column=1,sticky=N+W+E+S)
                Button(root5_3,text='  Watch IMDB and Trailer for - SW VI- Return Of The Jedi  ',command=fun5_3_6).grid(row=6,column=1,sticky=N+W+E+S)
                Button(root5_3,text=' Watch IMDB and Trailer for - SW VII- The Force AWAKENS  ',command=fun5_3_7).grid(row=7,column=1,sticky=N+W+E+S)                
                root5_3.mainloop()
            def fun5_4():
                root3.destroy()
                root5_4=Tk()
                root5_4.title("HARRY POTTER OCTOLOGY - 8 MOVIES")
                Label(root5_4,text="ENJOY THE SEVEN SERIES OF TALES OF TRUE ACTION,ADVENTURE AND MAGIC",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
                def fun5_4_1():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0241527/?ref_=nv_sr_1")
                def fun5_4_2():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0295297/?ref_=tt_rec_tt")
                def fun5_4_3():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0304141/?ref_=tt_rec_tt")
                def fun5_4_4():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0330373/?ref_=nv_sr_4")
                def fun5_4_5():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0373889/?ref_=tt_rec_tt")
                def fun5_4_6():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0417741/?ref_=tt_rec_tt")
                def fun5_4_7():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0926084/?ref_=tt_rec_tt")
                def fun5_4_8():
                    root5_4.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt1201607/?ref_=nv_sr_1")    
                Button(root5_4,text="Watch IMDB and Trailer for - HP I- The Socerror's Stone  ",command=fun5_4_1).grid(row=1,column=1,sticky=N+W+E+S)
                Button(root5_4,text='  Watch IMDB and Trailer for - HP II- The Chambers Of Secret ',command=fun5_4_2).grid(row=2,column=1,sticky=N+W+E+S)
                Button(root5_4,text=' Watch IMDB  for - HP III- The Prisonor Of Askaban ',command=fun5_4_3).grid(row=3,column=1,sticky=N+W+E+S)
                Button(root5_4,text='  Watch IMDB and Trailer for - HP IV- The Goblet Of Fire ',command=fun5_4_4).grid(row=4,column=1,sticky=N+W+E+S)    
                Button(root5_4,text='   Watch IMDB and Trailer for - HP V- The Order Of Phoenix',command=fun5_4_5).grid(row=5,column=1,sticky=N+W+E+S)
                Button(root5_4,text='  Watch IMDB and Trailer for - HP VI- The Half-Blood Prince  ',command=fun5_4_6).grid(row=6,column=1,sticky=N+W+E+S)
                Button(root5_4,text=' Watch IMDB and Trailer for - HP VII-The Deathly Hollows(I)   ',command=fun5_4_7).grid(row=7,column=1,sticky=N+W+E+S)
                Button(root5_4,text=' Watch IMDB and Trailer for - HP VII- The Deathly Hollows(II) ',command=fun5_4_8).grid(row=8,column=1,sticky=N+W+E+S)  
                root5_4.mainloop() 
            def fun5_5():
                root3.destroy()
                root5_5=Tk()
                root5_5.title("BORN TO CHASE THE BOURNE - 3 MOVIES")
                Label(root5_5,text="  MATT DAMON AT HIS BEST .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
                def fun5_5_1():
                    root5_5.destroy()
                    webbrowser.open("https://en.wikipedia.org/wiki/Bourne_(film_series)")
                Button(root5_5,text='About the Series ',font="Chiller 15 bold italic",command=fun5_5_1).grid(row=1,column=1,sticky=N+W+E+S)
                def fun5_5_2():
                    root5_5.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0258463/?ref_=nv_sr_2")
                Button(root5_5,text='IMDB ratings for - The Bourne Identity   ',command=fun5_5_2).grid(row=2,column=1,sticky=N+W+E+S)
                def fun5_5_3():
                    root5_5.destroy()
                    webbrowser.open("https://www.youtube.com/watch?v=FpKaB5dvQ4g")
                Button(root5_5,text="     WATCH TRAILER ----here---!!!!!",command=fun5_5_3).grid(row=3,column=1,sticky=N+W+E+S)
                def fun5_5_4():
                    root5_5.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0372183/?ref_=nv_sr_4")
                Button(root5_5,text=" IMDB ratings for - The Bourne Supremacy    ",command=fun5_5_4).grid(row=4,column=1,sticky=N+W+E+S)
                def fun5_5_5():
                    root5_5.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0440963/?ref_=nv_sr_1")
                Button(root5_5,text="IMDB ratings for - The Bourne Ultimatum ",command=fun5_5_5).grid(row=5,column=1,sticky=N+W+E+S)
                def fun5_5_6():
                    root5_5.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt1194173/?ref_=nv_sr_1")
                Button(root5_5,text=" Watch IMDB and trailer for --The Bourne Legacy ",command=fun5_5_6).grid(row=6,column=1,sticky=N+W+E+S)
                def fun5_5_7():
                    root5_5.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt4196776/?ref_=nv_sr_1")
                Button(root5_5,text=" Watch IMDB and trailer for --Jason Bourne ",command=fun5_5_7).grid(row=7,column=1,sticky=N+W+E+S)                 
                root5_5.mainloop()
            def fun5_6():
                root3.destroy()
                root5_6=Tk()
                root5_6.title("THE LORD OF THE RINGS TRILOGY - 3 MOVIES")
                Label(root5_6,text="  SALUTE TO PETER JACKSON'S BRILLIANCE",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
                def fun5_6_1(): 
                    root5_6.destroy()
                    webbrowser.open("https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)")
                Button(root5_6,text='About the Series ',font="Chiller 15 bold italic",command=fun5_6_1).grid(row=1,column=1,sticky=N+W+E+S)
                def fun5_6_2():
                    root5_6.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0120737/?ref_=nv_sr_1")
                Button(root5_6,text='IMDB ratings for -The Fellowship of The ring   ',command=fun5_6_2).grid(row=2,column=1,sticky=N+W+E+S)
                def fun5_6_3():
                    root5_6.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0167261/?ref_=nv_sr_3")
                Button(root5_6,text="     WATCH IMDB RATINGS HERE FOR- The Two Towers",command=fun5_6_3).grid(row=3,column=1,sticky=N+W+E+S)
                def fun5_6_4():
                    root5_6.destroy()
                    webbrowser.open("http://www.imdb.com/title/tt0167260/?ref_=nv_sr_2")
                Button(root5_6,text="     WATCH IMDB RATINGS HERE FOR- The Return Of King",command=fun5_6_4).grid(row=4,column=1,sticky=N+W+E+S)
                root5_6.mainloop()
            def fun5_7():
                root3.destroy()
                root5_7=Tk()
                root5_7.title("THE MATRIX TRILOGY")
                Label(root5_7,text="KEANU REAVES AND ANNE-MOSS TAKE THE SHOW HERE",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
                
             
             def fun5_7_1():
                 
                 root5_7.destroy()
                 webbrowser.open("https://en.wikipedia.org/wiki/The_Matrix_(franchise)")
             Button(root5_7,text='About the Series ',font="Chiller 15 bold italic",command=fun5_7_1).grid(row=1,column=1,sticky=N+W+E+S)
             def fun5_7_2():
                 root5_7.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0133093/?ref_=nv_sr_1")
             Button(root5_7,text='IMDB ratings for - The Matrix   ',command=fun5_7_2).grid(row=2,column=1,sticky=N+W+E+S)
             def fun5_7_3():
                 root5_7.destroy()         
                 webbrowser.open("http://www.imdb.com/title/tt0234215/?ref_=nv_sr_2")
             Button(root5_7,text="     WATCH IMDB - The Matrix Reloaded ----here---!!!!!",command=fun5_7_3).grid(row=3,column=1,sticky=N+W+E+S)
             def fun5_7_4():
                 root5_7.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0242653/?ref_=nv_sr_2")
             Button(root5_7,text=" IMDB ratings for -The Matrix Revolution     ",command=fun5_7_4).grid(row=4,column=1,sticky=N+W+E+S)
             root5_7.mainloop()
         def fun5_8():
             root3.destroy()
             root5_8=Tk()
             root5_8.title("PIRATES OF THE CARRIBBEAN - 5 MOVIES")
             Label(root5_8,text=" JOHNNY DEPP WILL BE REMEMBERED FOR THE PIRATES",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
             def destroy():
                 root5_8.destroy()      
             def fun5_8_1():
                 destroy()
                 webbrowser.open("https://en.wikipedia.org/wiki/Pirates_of_the_Caribbean_(film_series)")
             Button(root5_8,text="ALL About THE PIRATES OF THE CARREBEAN",command=fun5_8_1).grid(row=1,column=1,sticky=N+W+E+S)
             def fun5_8_2():
                 destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0325980/?ref_=nv_sr_1")
             Button(root5_8,text=" THE CURSE OF THE BLACK PEARL-2003",command=fun5_8_1).grid(row=2,column=1,sticky=N+W+E+S)
             def fun5_8_3():
                 destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0383574/?ref_=nv_sr_1")
             Button(root5_8,text=" THE DEAD MAN'S CHEST-2006",command=fun5_8_3).grid(row=3,column=1,sticky=N+W+E+S)
             def fun5_8_4():
                 webbrowser.open("http://www.imdb.com/title/tt0449088/?ref_=nv_sr_1")
             Button(root5_8,text=" AT WORLD'S END-2007",command=fun5_8_4).grid(row=4,column=1,sticky=N+W+E+S)
             def fun5_8_5():
                 webbrowser.open("http://www.imdb.com/title/tt1298650/?ref_=fn_al_tt_1")
             Button(root5_8,text=" ON STRANGER'S TIDES-2011",command=fun5_8_5).grid(row=5,column=1,sticky=N+W+E+S)
             def fun5_8_6():
                 webbrowser.open("http://www.imdb.com/title/tt1790809/?ref_=nv_sr_1")
             Button(root5_8,text=" DEAD AMN NO TALES-2017",command=fun5_8_6).grid(row=6,column=1,sticky=N+W+E+S)
             root5_8.mainloop()
         def fun5_9():
             root3.destroy()
             root5_9=Tk()
             root5_9.title("THE DARK KNIGHT TRILOGY - 3 MOVIES")
             Label(root5_9,text="  CHRISTOPHER NOLAN BRINGS BACK THE LOST BATMAN .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
             def fun5_9_1():
                 root5_9.destroy()
                 webbrowser.open("https://en.wikipedia.org/wiki/The_Dark_Knight_Trilogy")
             Button(root5_9,text=" ALL ABOUT THE  BATMAN TRILOGY ",command=fun5_9_1).grid(row=1,column=1,sticky=N+W+E+S)
             def fun5_9_2():
                 root5_9.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0372784/?ref_=nv_sr_4")
             Button(root5_9,text="BATMAN BEGINS - 2005 ",command=fun5_9_2).grid(row=2,column=1,sticky=N+W+E+S)
             def fun5_9_3():
                 root5_9.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0468569/?ref_=nv_sr_1")
             Button(root5_9,text=" The Dark Knight- Best Superhero Of The Decade ",command=fun5_9_3).grid(row=3,column=1,sticky=N+W+E+S)
             def fun5_9_4():
                 root5_9.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1345836/?ref_=nv_sr_2")
             Button(root5_9,text=" The Dark Knight Rises - Watch TrAiler And IMDB ",command=fun5_9_4).grid(row=4,column=1,sticky=N+W+E+S)
             root5_9.mainloop()
         def fun5_10():
             root3.destroy()
             root5_10=Tk()
             root5_10.title("TRANSFORMERS ULTIMATUM - 4 MOVIES")
             Label(root5_10,text="  ITS MACHINES VS HUMANS - WW-III",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
             def fun5_10_1():
                 root5_10.destroy()
                 webbrowser.open("https://en.wikipedia.org/wiki/Transformers_(film_series)")
             Button(root5_10,text=" ALL ABOUT THE  TRANSFORMERS  ",command=fun5_10_1).grid(row=1,column=1,sticky=N+W+E+S)
             def fun5_10_2():
                 root5_10.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0418279/?ref_=fn_al_tt_1")
             Button(root5_10,text="TRANSFORMERS - 2007 ",command=fun5_10_2).grid(row=2,column=1,sticky=N+W+E+S)
             def fun5_10_3():
                 root5_10.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1055369/?ref_=nv_sr_4")
             Button(root5_10,text=" TRANSFORMERS-II-REVENGE OF THE FALLEN-2009 ",command=fun5_10_3).grid(row=3,column=1,sticky=N+W+E+S)
             def fun5_10_4():
                 root5_10.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1399103/?ref_=nv_sr_1")
             Button(root5_10,text=" TRANSFORMERS-III-DARK OF THE MOON-2011 ",command=fun5_10_4).grid(row=4,column=1,sticky=N+W+E+S)
             def fun5_10_5():
                 root5_10.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt2109248/?ref_=nv_sr_3")
             Button(root5_10,text=" TRANSFORMERS-IV-AGE OF THE EXTINCTION-2014 ",command=fun5_10_5).grid(row=5,column=1,sticky=N+W+E+S)
             root5_10.mainloop()
         Button(root3,text='MISSION IMPOSSIBLE   ',command=fun5_1).grid(row=1,column=1,sticky=N+W+E+S)
         Button(root3,text=' SUICIDE SQUAD-2016  ',command=fun5_2).grid(row=2,column=1,sticky=N+W+E+S)
         Button(root3,text='STAR WARS FRANCHISE  ',command=fun5_3).grid(row=3,column=1,sticky=N+W+E+S)
         Button(root3,text=' HARRY POTTER OCTOLOGY  ',command=fun5_4).grid(row=4,column=1,sticky=N+W+E+S)    
         Button(root3,text='  BORN TO CHASE THE BOURNE ',command=fun5_5).grid(row=5,column=1,sticky=N+W+E+S)
         Button(root3,text=' THE LORD OF THE RINGS TRILOGY  ',command=fun5_6).grid(row=6,column=1,sticky=N+W+E+S)
         Button(root3,text=' THE MATRIX TRILOGY ',command=fun5_7).grid(row=7,column=1,sticky=N+W+E+S)
         Button(root3,text=' PIRATES OF THE CARRIBBEAN   ',command=fun5_8).grid(row=8,column=1,sticky=N+W+E+S)
         Button(root3,text=' THE DARK KNIGHT TRILOGY  ',command=fun5_9).grid(row=9,column=1,sticky=N+W+E+S)
         Button(root3,text=' TRANSFORMERS ULTIMATUM  ',command=fun5_10).grid(row=11,column=1,sticky=N+W+E+S)
         root3.mainloop()        

     def fun6():
         root2.destroy()
         root4=Tk()
         root4.title("Romantic comedies")
         Label(root4,text=  "dive into  the philosophy of love and attraction...!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
         def fun6_1():
             webbrowser.open('http://www.imdb.com/title/tt1041829/')             
         Button(root4,text='Watch IMDB ratings and Trailer for -The Proposal ',command=fun6_1).grid(row=1,column=1,sticky=N+W+E+S)
         def fun6_2():
             webbrowser.open('https://www.youtube.com/watch?v=KhKXjJQ-ixQ')
         Button(root4,text='Watch  Trailer for -The Holiday ',command=fun6_2).grid(row=2,column=1,sticky=N+W+E+S)
         def fun6_3():
             webbrowser.open("https://www.youtube.com/watch?v=FzYVvwwNwUM")
         Button(root4,text='Watch  Trailer for -About a Boy ',command=fun6_3).grid(row=3,column=1,sticky=N+W+E+S)
         def fun6_4():
             webbrowser.open("https://www.youtube.com/watch?v=6P4dXJ_Tvns")
         Button(root4,text='Watch  Trailer for -High Fidelity ',command=fun6_4).grid(row=4,column=1,sticky=N+W+E+S)
         def fun6_5():
             webbrowser.open("https://www.youtube.com/watch?v=rrRl2QQKkI8")
         Button(root4,text='Watch  Trailer for -As good As its gets ',command=fun6_5).grid(row=5,column=1,sticky=N+W+E+S)
         def fun6_6():
             webbrowser.open("https://www.youtube.com/watch?v=P27LBCgMjuU")
         Button(root4,text="Watch  Trailer for -Say Anything ",command=fun6_6).grid(row=6,column=1,sticky=N+W+E+S)
         root4.mainloop()
     def fun7():
         root2.destroy()
         root5=Tk()
         root5.title("SPECTACULAR THRILLERS ")
         Label(root5,text="  NJOY THE NAIL BITING SUSPENCE",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
         def fun7_1():
              webbrowser.open("http://www.imdb.com/title/tt0309698/?ref_=nv_sr_2")
         Button(root5,text="Watch IMDB Ratings For - Identity",command=fun7_1).grid(row=1,column=1,sticky=N+W+S+E)
         def fun7_2():
              webbrowser.open("http://www.imdb.com/title/tt1130884/?ref_=nv_sr_1")
         Button(root5,text="Watch IMDB Ratings and Trailer For - Shutter Island ",command=fun7_2).grid(row=2,column=1,sticky=N+W+S+E)            
         def fun7_3():
              webbrowser.open("http://www.imdb.com/title/tt1392214/?ref_=nv_sr_2")
         Button(root5,text="Watch IMDB Ratings and Trailer For - prisoners ",command=fun7_3).grid(row=3,column=1,sticky=N+W+S+E)              
         def fun7_4():
              webbrowser.open("http://www.imdb.com/title/tt2267998/?ref_=nv_sr_1")
         Button(root5,text="Watch IMDB Ratings and Trailer For - Gone Girl ",command=fun7_4).grid(row=4,column=1,sticky=N+W+S+E)             
         def fun7_5():
              webbrowser.open("http://www.imdb.com/title/tt1305806/?ref_=nv_sr_6")
         Button(root5,text="Watch IMDB Ratings and Trailer For - The Secret In Their Eyes ",command=fun7_5).grid(row=5,column=1,sticky=N+W+S+E)
         def fun7_6():
              webbrowser.open("http://www.imdb.com/title/tt0364569/?ref_=nv_sr_7")
         Button(root5,text="Watch IMDB Ratings  For - Oldboy ",command=fun7_6).grid(row=6,column=1,sticky=N+W+S+E)
         def fun7_7():
              webbrowser.open("http://www.imdb.com/title/tt0387898/?ref_=nv_sr_1")
         Button(root5,text="Watch IMDB Ratings For - Cache' ",command=fun7_7).grid(row=7,column=1,sticky=N+W+S+E)            
         def fun7_8():
              webbrowser.open("http://www.imdb.com/title/tt0443706/?ref_=nv_sr_1")
         Button(root5,text="Watch IMDB Ratings  For - Zodiac ",command=fun7_8).grid(row=8,column=1,sticky=N+W+S+E)
         def fun7_9():
              webbrowser.open("http://www.imdb.com/title/tt0209144/?ref_=nv_sr_2")
         Button(root5,text="Watch IMDB Ratings For - Memento ",command=fun7_9).grid(row=9,column=1,sticky=N+W+S+E)
         def fun7_10():
              webbrowser.open("http://www.imdb.com/title/tt0166924/?ref_=nv_sr_1")
         Button(root5,text="Watch IMDB Ratings For - Mulohand Dr.",command=fun7_10).grid(row=10,column=1,sticky=N+W+S+E)
         root5.mainloop()
     def fun8():
         root2.destroy()
         root6=Tk()
         root6.title(" nJOY tHE lAUGH rIDE ")
         Label(root6,text="  YOU WILL LAUGH UR HEART OUT!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
         def fun8_1():
             webbrowser.open("http://www.imdb.com/title/tt0109117/?ref_=nv_sr_1")
         Button(root6,text="IMDB-Andaz Apna Apna",command=fun8_1).grid(row=1,column=1,sticky=N+W+S+E)
         def fun8_2():
             webbrowser.open("http://www.imdb.com/title/tt1187043/?ref_=nv_sr_5")
         Button(root6,text="IMDB-3 Idiots",command=fun8_2).grid(row=2,column=1,sticky=N+W+S+E)
         def fun8_3():
             webbrowser.open("http://www.imdb.com/title/tt2096673/")
         Button(root6,text="Watch IMDB and Trailer For Inside Out",command=fun8_3).grid(row=3,column=1,sticky=N+W+S+E)
         def fun8_4():
             webbrowser.open("http://www.imdb.com/title/tt2293640/?ref_=nv_sr_1")
         Button(root6,text="Watch IMDB and Trailer For MINIONS",command=fun8_4).grid(row=4,column=1,sticky=N+W+S+E)
         def fun8_5():
             webbrowser.open("http://www.imdb.com/title/tt2582496/?ref_=nv_sr_7")
         Button(root6,text="Watch IMDB and Trailer For -Me And Earl And The Dying Girl",command=fun8_5).grid(row=5,column=1,sticky=N+W+S+E)
         def fun8_6():
             webbrowser.open("http://www.imdb.com/title/tt1638355/?ref_=nv_sr_2")
         Button(root6,text="Watch IMDB and Trailer For -The Man From U.N.C.L.E",command=fun8_5).grid(row=6,column=1,sticky=N+W+S+E)
         root6.mainloop()
     def fun9():
         root2.destroy()
         root7=Tk()
         root7.title(" Watch them at 3:00 A.M.")
         Label(root7,text=" GOOSEBUMPS ALERT .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
         def fun9_1():
             root7.destroy()
             root7_1=Tk()
             root7_1.title("  SAW FRANCHISE  ")
             def fun7_1_1():
                 root7_1.destroy()
                 webbrowser.open("https://en.wikipedia.org/wiki/Saw_(franchise)")
             Button(root7_1,text=" ALL ABOUT SAW SERIES  ",command=fun7_1_1).grid(row=1,column=1,sticky=N+W+S+E)
             def fun7_1_2():
                 root7_1.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0387564/?ref_=nv_sr_1")
             Button(root7_1,text=" SAW I - TRAILER AND IMDB  ",command=fun7_1_2).grid(row=2,column=1,sticky=N+W+S+E)
             def fun7_1_3():
                 root7_1.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0432348/?ref_=nv_sr_1")
             Button(root7_1,text=" SAW II - TRAILER AND IMDB  ",command=fun7_1_3).grid(row=3,column=1,sticky=N+W+S+E)
             def fun7_1_4():
                 root7_1.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0489270/?ref_=nv_sr_2")
             Button(root7_1,text=" SAW III - TRAILER AND IMDB ",command=fun7_1_4).grid(row=4,column=1,sticky=N+W+S+E)
             def fun7_1_5():
                 root7_1.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0890870/?ref_=nv_sr_1")
             Button(root7_1,text=" SAW IV - TRAILER AND IMDB  ",command=fun7_1_5).grid(row=5,column=1,sticky=N+W+S+E)
             def fun7_1_6():
                 root7_1.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1132626/?ref_=nv_sr_1")
             Button(root7_1,text=" SAW V - TRAILER AND IMDB  ",command=fun7_1_6).grid(row=6,column=1,sticky=N+W+S+E)
             def fun7_1_7():
                 root7_1.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1233227/?ref_=nv_sr_1")
             Button(root7_1,text=" SAW VI - TRAILER AND IMDB  ",command=fun7_1_7).grid(row=7,column=1,sticky=N+W+S+E)
             root7_1.destroy()
         def fun9_2():
              root7.destroy()
              root7_2=Tk()
              root7_2.title( "The Conjuring series ")
              Label(root7_2,text="  SHOULDN'T BE WATCHED ALONE .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
              def fun7_2_1():
                  root7_2.destroy()
                  webbrowser.open("http://www.imdb.com/title/tt1457767/?ref_=nv_sr_2")
              Button(root7_2,text="  WATCH TRAILER AND IMDB FOR THE CONJURING ",command=fun7_2_1).grid(row=1,column=1,sticky=N+W+E+S)
              def fun7_2_2():
                  root7_2.destroy()
                  webbrowser.open("http://www.imdb.com/title/tt3065204/?ref_=nv_sr_1")
              Button(root7_2,text="  WATCH TRAILER AND IMDB FOR THE CONJURING2 ",command=fun7_2_2).grid(row=2,column=1,sticky=N+W+E+S)
              root7_2.mainloop()
         def fun9_3():
             root7.destroy()
             root7_3=Tk()
             root7_3.title("The REC series ")
             Label(root7_3,text="  ALERT - VIOLENT AND GRUESOME CONTENT .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
             def fun7_3_1():
                 root7_3.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1038988/?ref_=nv_sr_1")
             def fun7_3_2():
                 root7_3.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1245112/?ref_=nv_sr_3")
             def fun7_3_3():
                 root7_3.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1649444/?ref_=nv_sr_4")
             def fun7_3_4():
                 root7_3.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt1649443/?ref_=nv_sr_1")                                
             Button(root7_3,text="  TRAILER AND IMDB FOR -REC IV- 2011 ",command=fun7_3_4).grid(row=4,column=1,sticky=N+W+E+S)
             Button(root7_3,text="  IMDB FOR REC-2007 ",command=fun7_3_1).grid(row=1,column=1,sticky=N+W+E+S)
             Button(root7_3,text="  TRAILER AND IMDB FOR -REC II- 2009 ",command=fun7_3_2).grid(row=2,column=1,sticky=N+W+E+S)
             Button(root7_3,text="  TRAILER AND IMDB FOR -REC III- 2012 ",command=fun7_3_3).grid(row=3,column=1,sticky=N+W+E+S)
             root7_3.mainloop()
         def fun9_4():
             root7.destroy()
             root7_4=Tk()
             root7_4.title("Ring Series")
             Label(root7_4,text="  THE WITCH  IS AFTER YOU-RUN FOR UR LIFE .......!!!!!!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
             def fun9_4_1():
                 root7_4.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0298130/?ref_=nv_sr_4")
             def fun9_4_2():
                 root7_4.destroy()
                 webbrowser.open("http://www.imdb.com/title/tt0377109/?ref_=nv_sr_3")
             Button(root7_4,text="  IMDB FOR RING-2002 ",command=fun9_4_1).grid(row=1,column=1,sticky=N+W+E+S)
             Button(root7_4,text="  IMDB FOR RING II -2005 ",command=fun9_4_2).grid(row=2,column=1,sticky=N+W+E+S)
             root7_4.mainloop()     
         Button(root7,text=" BEST FRANCHISE FOR FICTIONAL HORROR - SAW SERIES (1-6) ",command=fun9_1).grid(row=1,column=1,sticky=N+W+E+S)
         Button(root7,text="  WATCH TRAILER AND IMDB FOR THE CONJURING SERIES ",command=fun9_2).grid(row=2,column=1,sticky=N+W+E+S)
         Button(root7,text="  WATCH TRAILER AND IMDB  FOR REC SERIES ",command=fun9_3).grid(row=3,column=1,sticky=N+W+E+S)
         Button(root7,text="  WATCH TRAILER AND IMDB FOR RING SERIES ",command=fun9_4).grid(row=4,column=1,sticky=N+W+E+S)
         root7.mainloop()
     def fun10():
         root2.destroy()
         root8=Tk()
         root8.title(" Time to scratch ur head a li'll bit ")
         Label(root8,text="  ALERT : U MIGHT REQUIRE MULTIPLE VIEWINGS ....!",font="Chiller 20 bold italic",bg='green').grid(row=0,column=1,sticky=N+W+E+S)
         def fun10_1():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1")
         Button(root8,text="Watch the IMDB ratings and Trailer for - AVATAR",command=fun10_1).grid(row=1,column=1,sticky=N+W+S+E)
         def fun10_2():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt0816692/?ref_=nv_sr_1")
         Button(root8,text="Watch the IMDB ratings and Trailer for - INTERSTELLER",command=fun10_2).grid(row=2,column=1,sticky=N+W+S+E)
         def fun10_3():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt1454468/?ref_=nv_sr_3")
         Button(root8,text="Watch the IMDB ratings and Trailer for - GRAVITY",command=fun10_3).grid(row=3,column=1,sticky=N+W+S+E)
         def fun10_4():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt0246578/?ref_=nv_sr_1")
         Button(root8,text="Watch the IMDB ratings  - DONNIE DARKO",command=fun10_4).grid(row=4,column=1,sticky=N+W+S+E)
         def fun10_5():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt3659388/?ref_=nv_sr_4")
         Button(root8,text="Watch the IMDB ratings And Traler  - The Martian",command=fun10_5).grid(row=5,column=1,sticky=N+W+S+E)
         def fun10_6():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt1375666/?ref_=nv_sr_1")
         Button(root8,text="Watch the IMDB ratings And Traler  - INCEPTION",command=fun10_6).grid(row=6,column=1,sticky=N+W+S+E)
         def fun10_7():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt0338013/?ref_=nv_sr_1")
         Button(root8,text="Watch the IMDB ratings   - Eternal Sunshine of the Spotless Mind",command=fun10_7).grid(row=7,column=1,sticky=N+W+S+E)
         def fun10_8():
             root8.destroy()
             webbrowser.open("http://www.imdb.com/title/tt0910970/?ref_=nv_sr_5")
         Button(root8,text="Watch the IMDB ratings and Trailer for  -  WALL-E",command=fun10_8).grid(row=8,column=1,sticky=N+W+S+E)
         root8.mainloop()    
     Button(root2,text='  Action Packed Adventures...!!!! ',command=fun5).grid(row=1,column=1,sticky=N+W+E+S)
     Button(root2,text='  Romance or sort of rom-coms..... ',command=fun6).grid(row=3,column=1,sticky=N+W+E+S)
     Button(root2,text='  Psychological thrillers ',command=fun7).grid(row=5,column=1,sticky=N+W+E+S)
     Button(root2,text='  Hilarious comedies ',command=fun8).grid(row=07,column=1,sticky=N+W+E+S)
     Button(root2,text='  Fictional Horror AND  Paranormal Tales ',command=fun9).grid(row=9,column=1,sticky=N+W+E+S)
     Button(root2,text='  R U A Sci-Fi freak ?????? ',command=fun10).grid(row=11,column=1,sticky=N+W+E+S)              
     root2.mainloop()
Button(root,text='  What do you want ',command=fun4).grid(row=10,column=1,columnspan=10)
root.mainloop()
    

