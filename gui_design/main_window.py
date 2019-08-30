import tkinter as tk
from PIL import Image

def main_window_init(window,root):
	print("window")
	root.withdraw()
	window.configure(background="#313131")
	window.geometry("600x500")

	label_text_frame = tk.Frame(master=window, bg="#313131")
	label_text_frame.pack()

	label_text = tk.Label(label_text_frame, text="Task", font="Helvetica 12 bold", bg="#313131", fg="#c4e9ef").pack(pady=20)
	
	# canvas_circle = tk.Canvas(window, bg="white")
	# canvas_circle.create_oval(100, 100, 200, 200)
	# # canvas_circle.pack()
	file_in = 'play_small.png'
	button_image_raw = tk.PhotoImage(file='play_small.png')
	# button_image = button_image_raw.resize((50, 50), Image.ANTIALIAS)
	# img = tk.PhotoImage(button_image)
	# file_out = 'play_small.png'
	# button_image.save(file_out)
	# button_image = tk.PhotoImage(file="play.png") 
	play_button = tk.Button(label_text_frame, height="48", width="48",bd=0,fg="#313131",bg="#313131", image=button_image_raw)
	play_button.image = button_image_raw
	play_button.pack(side=tk.TOP)
	play_button.configure(highlightthickness=0)
	# canvas_circle.pack()

	task_list_frame = tk.Frame(master=window, bg="#313131").pack()

	

	return window

	


	
