from tkinter import *
from PIL import ImageTk
import os




def detection():
    os.system("python C:\\Users\\User\\Desktop\\Face-Mask-Detection-master\\detect_mask_video.py")



root = Tk()
root.geometry("640x320")
root.title("Face Mask Detection")
root.resizable(FALSE,0)
root.iconbitmap('C:\\Users\\User\\Desktop\\Face-Mask-Detection-master\\mask icon.ico')

bg_image= ImageTk.PhotoImage(file='C:\\Users\\User\\Desktop\\Face-Mask-Detection-master\\face mask pic.jpg', master=root)
bg_canvas = Canvas(root, width=640, height=318)
bg_canvas.pack(fill='both', expand=True)

bg_canvas.create_image(0,0, image=bg_image, anchor='nw')

bg_button = Button(bg_canvas, height=2, width=14,command=detection,bg="#2feb00", fg="white",activebackground="White", relief=RAISED, bd=4, text="Start Detecting",
                         font=("Arial", 12, "bold"), cursor="hand2")
bg_button_window = bg_canvas.create_window(233, 250, anchor="nw", window=bg_button)






root.mainloop()
