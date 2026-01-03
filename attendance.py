from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import csv
import os

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # ================= VARIABLES =================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ================= TOP IMAGES =================
        img = Image.open("college_images/smart-attendance.jpg")
        img = img.resize((760,200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=760, height=200)

        img1 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((760,200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=760, y=0, width=760, height=200)

        # ================= BACKGROUND IMAGE =================
        bg_img = Image.open("college_images/university.jpg")
        bg_img = bg_img.resize((1530,710), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=200, width=1530, height=710)

        # ================= TITLE =================
        title_lbl = Label(
            bg_label,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================= MAIN FRAME =================
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # ================= LEFT FRAME =================
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold")
        )
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("college_images/face-recognition.png")
        img_left = img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=135, width=715, height=350)

        # ================= FORM =================
        Label(left_inside_frame, text="Attendance ID:", bg="white",
              font=("arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=22).grid(row=0, column=1)

        Label(left_inside_frame, text="Roll:", bg="white",
              font=("arial", 11, "bold")).grid(row=0, column=2, padx=10, pady=5)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=22).grid(row=0, column=3)

        Label(left_inside_frame, text="Name:", bg="white",
              font=("arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=22).grid(row=1, column=1)

        Label(left_inside_frame, text="Department:", bg="white",
              font=("arial", 11, "bold")).grid(row=1, column=2, padx=10, pady=5)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=22).grid(row=1, column=3)

        Label(left_inside_frame, text="Time:", bg="white",
              font=("arial", 11, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=22).grid(row=2, column=1)

        Label(left_inside_frame, text="Date:", bg="white",
              font=("arial", 11, "bold")).grid(row=2, column=2, padx=10, pady=5)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=22).grid(row=2, column=3)

        Label(left_inside_frame, text="Attendance Status:", bg="white",
              font=("arial", 11, "bold")).grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.atten_status = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_atten_attendance,
            state="readonly",
            width=20
        )
        self.atten_status["values"] = ("present", "absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1)

        # ================= BUTTONS =================
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=710, height=40)

        Button(btn_frame, text="Import CSV", command=self.importCsv,
               width=17, bg="blue", fg="white",
               font=("times new roman", 12, "bold")).grid(row=0, column=0)

        Button(btn_frame, text="Export CSV", command=self.exportCsv,
               width=17, bg="blue", fg="white",
               font=("times new roman", 12, "bold")).grid(row=0, column=1)

        Button(btn_frame, text="Reset", command=self.reset_data,
               width=17, bg="blue", fg="white",
               font=("times new roman", 12, "bold")).grid(row=0, column=2)

        # ================= RIGHT FRAME =================
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 12, "bold")
        )
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=("id","roll","name","department","time","date","attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col in ("id","roll","name","department","time","date","attendance"):
            self.AttendanceReportTable.heading(col, text=col.upper())
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ================= FUNCTIONS =================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(filetypes=[("CSV File", "*.csv")])
        with open(fln) as f:
            csvread = csv.reader(f)
            for row in csvread:
                mydata.append(row)
        self.fetchData(mydata)

    def exportCsv(self):
        if len(mydata) < 1:
            messagebox.showerror("Error", "No Data Found")
            return
        fln = filedialog.asksaveasfilename(defaultextension=".csv")
        with open(fln, mode="w", newline="") as f:
            writer = csv.writer(f)
            for row in mydata:
                writer.writerow(row)
        messagebox.showinfo("Success", "CSV Exported Successfully")

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

if __name__ == "__main__":
    root = Tk()
    Attendance(root)
    root.mainloop()
