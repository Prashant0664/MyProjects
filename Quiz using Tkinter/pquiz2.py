import tkinter
from tkinter import*
import random
import PIL
from PIL import ImageTk,Image
import os
ques=['WHAT IS THE FORMULA OF CHLORINE','WHAT IS THE FULL FORM OF ISRO','When is May Day observed?','When is Earth’s Day celebrated?',
      ' How many years make a millennium?','What is the name of the strongest and longest bone in the human body?',
      'Which planet in the Solar System has the largest number of moons?',
      'Who is the inventor of the Steam Engine?','What is the scientific name of Marsh gas?','Which is the hardest natural substance found on earth?']  #questions
anschoice=[['Cl','cl','CL','Chl'],
           ['Indian Space and Research Organisation','India Space and Research Organisation','India Space and Research Organisations','None of The above'],
           ['1 April','1 May','30 May','Wrong Question!'],
           ['22 April','23 April','24 April','1 January'],
           ['10000','100000','1000000','1000'],
           ['Feemur','Femuur','Femur','Femmur'],
           ['Mercury','Uranus','Saturn','Jupiter'],
           ['Thomas Edison','James Watt','Alber Einstein','Tesla'],
           ['Ethane','Methene','Methane','Ethyne'],
           ['Diamond','Dimond','Pearl','Steel']] #mcq choices
answers=[0,1,1,0,3,2,3,1,2,0]  #answer index value (for eg is option a is correct then index value is 0
indexes=[]
user_answer=[]
def gen():
    global indexes
    while (len(indexes)<10): # 10 QUESTIONS
        x=random.randint(0,9)
        user_answer.append(x)
        
        if x in indexes:
            continue
        else:
            indexes.append(x)
ques2=1
def showresult(score):
    lb3q.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    c=Label(root,text='CONGRATULATION \n YOUR TOTAL SCORE IS',font=('times',20),background='light green',foreground='RED',relief='flat',width=80)
    c.pack()
    c2=Label(root,text=score,font=('times',30),background='white',foreground='red',relief='flat')
    c2.pack()
    c3=Label(image=img4,background='white')
    c3.pack()
    c4=Label(text='© copyright 2020',background='white',foreground='#C2C2C2')
    c4.pack()
    
z3=[]
def calculated():
    global indexes,user_answer,answers,z3
    x=0
    score=0
    for i in range(10):
        a9=user_answer[-i-1]
        z3.append(a9)
        z3.reverse()
    user_answer=z3
    
    for i in indexes:
        if user_answer[x]==answers[i]:
            score=score+5  # 5 is score
        x+=1
    showresult(score)
        
def selected():
    global rv, user_answer
    global lb3q,r1,r2,r3,r4
    global ques2
    x=rv.get()
    user_answer.append(x)
    rv.set(-1)
    if ques2<10: # questions numbers ie 5
        lb3q.config(text=ques[indexes[ques2]])
        r1['text']=anschoice[indexes[ques2]][0]
        r2['text']=anschoice[indexes[ques2]][1]
        r3['text']=anschoice[indexes[ques2]][2]
        r4['text']=anschoice[indexes[ques2]][3]
        ques2+=1
        
    else:
        
        calculated()
       
def startquiz():
    global ques,lb3q
    global r1,r2,r3,r4
    lb3q=Label(root,text=ques[indexes[0]],font=('consolas',16),width=800,wraplength=400,image=img3,background='white',compound=CENTER)
    
    lb3q.pack(pady=(0,0))
    global rv
    rv=IntVar()
    rv.set(-1)
    r1=tkinter.Radiobutton(root,text=anschoice[indexes[0]][0],font=('times',12),value=0,variable=rv,justify='center',background='#B2FFFF',foreground='blue',activeforeground='orange',command=selected) 
    r1.pack()
    r2=tkinter.Radiobutton(root,text=anschoice[indexes[0]][1],font=('times',12),value=1,variable=rv,justify='center',background='#B2FFFF',foreground='blue',activeforeground='orange',command=selected)
    r2.pack()
    r3=tkinter.Radiobutton(root,text=anschoice[indexes[0]][2],font=('times',12),value=2,variable=rv,justify='center',foreground='blue',background='#B2FFFF',activeforeground='orange',command=selected)
    r3.pack()
    r4=tkinter.Radiobutton(root,text=anschoice[indexes[0]][3],font=('times',12),value=3,variable=rv,justify='center',foreground='blue',background='#B2FFFF',activeforeground='orange',command=selected)
    r4.pack()
    


def starpress():
    bstart.destroy()
    lb2.destroy()
    lbrules.destroy()
    lt.destroy()
    img11.destroy()
    gen()
    startquiz()
    
root=tkinter.Tk()
i1=Image.open('12.png')
i1=i1.resize((150,150),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(i1)
i3=Image.open('14.jpg')
i3=i3.resize((800,190),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(i3)
i4=Image.open('15.jpg')
i4=i4.resize((500,300),Image.ANTIALIAS)
img4=ImageTk.PhotoImage(i4)
i2=Image.open('13.jpg')
i2=i2.resize((200,110),Image.ANTIALIAS)
img2=ImageTk.PhotoImage(i2)
root.title('TULIpS INTERNATIONAL SCHOOL') #title not heading
root.geometry('1200x1000') #size
root.config(background='white')
root.resizable(0,0)
img11=Label(root,image=img1,background='white')
img11.pack()
lt=Label(root,text='TULIPS INTERNATIONAL SCHOOL',font=('ALGERIAN',33),background='white',foreground='#000080',relief='flat',width=100) # MAIN HEADING
lt.pack(pady=(0,0))
lt2=Label(root,text='comp name',font=('ravie',20),background='#ffe6ee',foreground='orange',relief='flat',width=100) # MAIN HEADING
lt2.pack()
bstart=Button(root,text='START',image=img2,relief='raised',font=('snap itc',15),justify='left',foreground='red',cursor='center_ptr',compound=CENTER,command=starpress) #start button
bstart.pack()

lb2=Label(root,text='\n \n \n \n RULES AND INSTRUCTIONS \n click start once you are ready \n THIS QUIZ CONTAIN 10 QUESTIONS \n EACH QUESTION HAVE 4 CHOICES ',background='white',font=('consolas',13),justify='center') #rules
lb2.pack()
lbrules=Label(root,text='THIS QUIZ CONTAIN 10 QUESRIONS AND WILL 10 SECOND TO SOLVE QUESTION \n OONCE ....',width=100,font=('times',14),background='black',foreground='light blue',justify='center')
lbrules.pack()  #belowinstruction


root.mainloop()

