from tkinter import *
from PIL import Image, ImageTk
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.configure(bg="#f0f0f0")

        # ===== TITLE =====
        title = Label(
            self.root,
            text="DEVELOPER",
            font=("Helvetica", 32, "bold"),
            bg="#0d47a1",
            fg="white"
        )
        title.pack(fill=X)

        # ===== MAIN FRAME =====
        main_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)

        base_dir = os.path.dirname(__file__)

        # ===== LEFT SIDE : TECH IMAGE =====
        tech_img_path = os.path.join(
            base_dir,
            "college_images",
            "KPIs-and-Agile-software-development-metrics-for-teams-1.jpg"
        )
        tech_img = Image.open(tech_img_path)
        tech_img = tech_img.resize((1100, 800), Image.LANCZOS)
        self.tech_photo = ImageTk.PhotoImage(tech_img)

        left_label = Label(main_frame, image=self.tech_photo, bd=0)
        left_label.pack(side=LEFT, padx=10, pady=10)

        # ===== RIGHT SIDE PANEL (WIDTH INCREASED) =====
        info_frame = Frame(main_frame, bg="white", width=500)
        info_frame.pack(side=RIGHT, fill=Y, padx=20, pady=10)

        # ===== INFO CARD (FIXED TEXT CUT ISSUE) =====
        card = Frame(info_frame, bg="#ffc107", bd=3, relief=RIDGE)
        card.pack(fill=X, pady=(0,20), padx=10)

        Label(
            card,
            text="AUTHOR : SONU YADAV",
            font=("Helvetica", 18, "bold"),
            bg="#ffc107",
            fg="#0d47a1"
        ).pack(pady=(10,5), padx=10)

        Label(
            card,
            text="Data Science Mentor\nat Physics Wallah",
            font=("Helvetica", 14, "bold"),
            bg="#ffc107",
            fg="#0d47a1",
            justify=CENTER
        ).pack(pady=5, padx=10)

        Label(
            card,
            text="📞 9142022872",
            font=("Helvetica", 14, "bold"),
            bg="#ffc107",
            fg="#0d47a1"
        ).pack(pady=(5,12), padx=10)

        # ===== BIG VERTICAL PHOTO (RIGHT SIDE FULL) =====
        profile_path = os.path.join(
            base_dir,
            "D:\Face Recognition, Student Attendance System\college_images\WhatsApp Image 2026-01-03 at 10.45.19 AM.jpeg"
        )
        profile_img = Image.open(profile_path)
        profile_img = profile_img.resize((380, 540), Image.LANCZOS)
        self.profile_photo = ImageTk.PhotoImage(profile_img)

        photo_frame = Frame(info_frame, bg="#0d47a1", bd=4, relief=RIDGE)
        photo_frame.pack(pady=10)

        photo_label = Label(photo_frame, image=self.profile_photo, bg="white")
        photo_label.pack()

        # ===== OPTIONAL TEAM IMAGE =====
        team_img_path = os.path.join(base_dir, "college_images", "dev.jpg")
        team_img = Image.open(team_img_path)
        team_img = team_img.resize((420, 200), Image.LANCZOS)
        self.team_photo = ImageTk.PhotoImage(team_img)

        team_label = Label(info_frame, image=self.team_photo, bd=3, relief=RIDGE)
        team_label.pack(pady=15)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
