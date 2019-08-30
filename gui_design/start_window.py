import tkinter as tk 
import tkinter.messagebox as msg
from . import main_window
# import tkMessageBox

window = tk.Tk()
window.configure(background="#313131")
window.geometry("600x500")

Username =tk.StringVar(window)
Password = tk.StringVar(window)

# window.wm_attributes('-alpha', 0.7)
#313131
# root_canvas = tk.Canvas(master=window, bg="blue", height="500", width="600") 
main_frame = tk.Frame(master=window, bg="#313131").pack()

main_label_frame = tk.Frame(master=main_frame,bg="#313131")
main_label_frame.pack(padx=50,pady=60)

# root_canvas.create_window(0,0,anchor='nw',height=300,width=300,window=label_frame)
label = tk.Label(main_label_frame, text = "Login", font='Helvetica 18 ', bg="#313131", fg="#c4e9ef").pack()

label_username_frame = tk.Frame(master=main_frame, bg="#313131")
label_username_frame.pack(ipadx=10)

login_label = tk.Label(label_username_frame, text = "Username", bg="#313131", fg="#c4e9ef",font='Helvetica 12').pack(side=tk.LEFT)
login_text = tk.Entry(label_username_frame, width=40, textvariable=Username, borderwidth=5, relief=tk.FLAT, fg="black", font='Helvetica 10 bold').pack(side=tk.RIGHT,ipady=3, ipadx=10)

label_password_frame = tk.Frame(master=main_frame, bg="#313131")
label_password_frame.pack(ipadx=10,pady=10)

bullet = "\u2022"
password_label = tk.Label(label_password_frame, text = "Password", font='Helvetica 12', bg="#313131", fg="#c4e9ef").pack(side=tk.LEFT)
password_text = tk.Entry(label_password_frame, textvariable=Password, width=40, borderwidth=5, relief=tk.FLAT, fg="black", show=bullet).pack(side=tk.RIGHT,ipady=3, ipadx=10)

button_submit_frame = tk.Frame(master=main_frame, bg="#313131")
button_submit_frame.pack(ipadx=10,pady=10, padx=0)


def on_closing():
	print("window close")
	window.destroy()

def login_button_clicked():
	global login_text
	print("clicked",login_text)
	
	if Username.get() == "p" and Password.get() == "1":
		print("sucessssss")
		main_window_obj = tk.Toplevel()
		child_window = main_window.main_window_init(main_window_obj,window)
		child_window.protocol("WM_DELETE_WINDOW", on_closing)


button_submit = tk.Button(button_submit_frame, text="Login", relief=tk.FLAT, bg="#313131", fg="#c4e9ef", bd=1, width=15,height="2", command=login_button_clicked).pack(side=tk.LEFT)

# button_submit = tk.CustomButton(button_submit_frame, text="Login", relief=tk.FLAT, bg="#ffffff").pack(side=tk.LEFT)
window.mainloop()

