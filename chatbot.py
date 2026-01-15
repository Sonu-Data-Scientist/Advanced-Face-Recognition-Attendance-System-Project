from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from google import genai  # Nayi library import

# ======================== API CONFIG ========================
# Gemini Client Setup
#
client = genai.Client(api_key="AIzaSyALfRCWiiqXICiOFijy7DJRw1eSHgQ6Pp0")

def ask_gemini(question):
    try:
        # Naya model 'gemini-3-flash-preview' ya 'gemini-2.5-flash' use karein
        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=question
        )
        return response.text
    except Exception as e:
        return f"Sorry, AI error: {str(e)}"

# ======================== CHATBOT CLASS ========================
class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot - Sonu Yadav")
        self.root.geometry("830x620+0+0")
        self.root.bind('<Return>', self.enter_func)
        
        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()
        
        try:
            img_chat = Image.open('chat.jpg')
            img_chat = img_chat.resize((150, 70), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img_chat)
        except:
            self.photoimg = None

        Title_label = Label(
            main_frame, bd=3, relief=RIDGE, anchor='nw', width=830, compound=LEFT, 
            image=self.photoimg, 
            text='CHAT WITH MR SONU YADAV DATA SCIENTIST', 
            font=('arial', 20, 'bold'), 
            fg='gold', bg='white'
        )
        Title_label.pack(side=TOP)
        
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=75, height=20, bd=3, relief=RAISED, font=('arial', 14), 
                         yscrollcommand=self.scroll_y.set, wrap=WORD)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()
        
        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()
        
        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)
        
        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=45, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)
        
        self.send_btn = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 15, 'bold'), width=8, bg='green', fg='white')
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)
        
        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=('arial', 15, 'bold'), width=10, bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)
        
        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    def enter_func(self, event):
        self.send()
        
    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        user_val = self.entry.get().lower().strip()
        if user_val == '':
            self.label_11.config(text='Please enter some input', fg='red')
            return
        
        send_msg = '\t\t\t' + 'You: ' + self.entry.get()
        self.text.insert(END, '\n' + send_msg)
        self.text.yview(END)
        self.entry.set('') 
        self.label_11.config(text='', fg='red')

        if user_val in ['hello', 'hi']:
            self.text.insert(END, '\n\n' + 'Bot: Hello! How can I help you today?')
        elif user_val == 'who created you':
            self.text.insert(END, '\n\n' + 'Bot: Mr. Sonu Yadav (Data Scientist) created me using Python.')
        elif user_val == 'bye':
            self.text.insert(END, '\n\n' + 'Bot: Goodbye! Have a great day.')
        else:
            reply = ask_gemini(user_val)
            self.text.insert(END, '\n\n' + 'Bot: ' + reply)
        
        self.text.yview(END)

if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()