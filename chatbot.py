from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        
        
        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()
        
        img_chat=Image.open('chat.jpg')
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        
        Title_label=Label(main_frame,bd=3,relief=RIDGE,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='gold',bg='white')
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()
        
        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        
        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)
        
        
        
        
        
        
    # function
    
    
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
    
    
    
    
    
    
    
    
    
    
    
    
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        
        
        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')
        
        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
            
        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')
            
        elif (self.entry.get()=='How Are You'):
            self.text.insert(END,'\n\n'+'Bot: Fine and you')
            
        elif (self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice To Hear')
            
        elif (self.entry.get()=='Who created you'):
            self.text.insert(END,'\n\n'+'Bot: Sonu Yadav did using python')
            
        elif (self.entry.get()=='What is your name'):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr. Hacker')
            
        
            
        elif (self.entry.get()=='Can you speak marathi'):
            self.text.insert(END,'\n\n'+'Bot: I am  still learning it...')
            
        elif (self.entry.get()=='what is machine learning'):
            self.text.insert(END,'\n\n'+'Bot: Machine Learning is the science of making computers learn from data and improve their performance over time without being explicitly programmed.')
            
        elif (self.entry.get()=='How does face recognition work'):
            self.text.insert(END,'\n\n'+'Bot: Face recognition works by first detecting a face using techniques like Haar Cascade or deep learning, then extracting unique facial features (like distance between eyes, nose shape, etc.), and finally comparing these features with a stored database using algorithms like LBPH, EigenFaces, or FaceNet to identify or verify the person.')
            
            
        elif (self.entry.get()=='How does facial recognition work step by step?'):
            self.text.insert(END,'\n\n'+'Bot: Facial recognition works step by step by detecting a face, extracting facial features, comparing them with a stored database, and identifying the person based on the best match.')   
            
         
        elif (self.entry.get()=='How many countries use facial recognition'):
            self.text.insert(END,'\n\n'+'Bot:As of now, over 100 countries use facial recognition technology in some form, including for surveillance, security, law enforcement, airport screening, and mobile authentication.')
            
            
        elif (self.entry.get()=='What is python programming'):
            self.text.insert(END,'\n\n'+'Bot: Python programming is the process of writing code using the Python language, a high-level, easy-to-read, and versatile programming language used for web development, data analysis, automation, machine learning, AI, software development, and more.')    
            
            
        elif (self.entry.get()=='What is chatbot'):
            self.text.insert(END,'\n\n'+'Bot: A chatbot is a computer program that can simulate human conversation using text or voice, and is designed to interact with users automatically — often used in websites, apps, or customer service.')   
            
         
            
        elif (self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')
            
        else:
            self.text.insert(END,'\n\n'+"Bot: sorry I did not get it")       
        
if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
    

