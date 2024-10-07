import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps

def load_image():
	global img, tk_img, original_img
	file_path = filedialog.askopenfilename()
	if file_path:
		img = Image.open(file_path)
		original_img = img.copy()
		img.thumbnail((500, 500))
		tk_img = ImageTk.PhotoImage(img)
		canvas.itemconfig(image_container, image=tk_img)

def rotate_image():
	global img, tk_img
	angle = float(rotate_entry.get())
	img = img.rotate(angle, expand=True)
	tk_img = ImageTk.PhotoImage(img)
	canvas.itemconfig(image_container, image=tk_img)

def scale_image():
	global img, tk_img
	scale = float(scale_entry.get())
	img = original_img.resize((int(original_img.width * scale),
	int(original_img.height * scale)))
	tk_img = ImageTk.PhotoImage(img)
	canvas.itemconfig(image_container, image=tk_img)

def move_image(dx, dy):
	canvas.move(image_container, dx, dy)	

def reset_image():
	global img, tk_img
	img = original_img.copy()
	img.thumbnail((500, 500))
	tk_img = ImageTk.PhotoImage(img)
	canvas.itemconfig(image_container, image=tk_img)

app = tk.Tk()
app.title('Image Manipulation App')
app.geometry('900x700')
app.configure(bg='#282c34')

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 10), padding=10)
style.configure('TLabel', font=('Helvetica', 10), background='#282c34', foreground='white')
style.configure('TEntry', font=('Helvetica', 10))

control_frame = ttk.Frame(app, padding=(10, 10))
control_frame.pack(side=tk.TOP, fill=tk.X)

canvas = tk.Canvas(app, width=800, height=600, bg='lightgray', highlightthickness=0)
canvas.pack(pady=20)

img = None
original_img = None
tk_img = None
image_container = canvas.create_image(400, 300, image=tk_img)

load_button = ttk.Button(control_frame, text='Load Image', command=load_image)
load_button.grid(row=0, column=0, padx=5, pady=5)

rotate_label = ttk.Label(control_frame, text='Rotate Angle:')
rotate_label.grid(row=0, column=1, padx=5)

rotate_entry = ttk.Entry(control_frame, width=10)
rotate_entry.grid(row=0, column=2, padx=5)

rotate_button = ttk.Button(control_frame, text='Rotate', command=rotate_image)
rotate_button.grid(row=0, column=3, padx=5)

scale_label = ttk.Label(control_frame, text='Scale Factor:')
scale_label.grid(row=1, column=1, padx=5)

scale_entry = ttk.Entry(control_frame, width=10)
scale_entry.grid(row=1, column=2, padx=5)

scale_button = ttk.Button(control_frame, text='Scale', command=scale_image)
scale_button.grid(row=1, column=3, padx=5)

move_left_button = ttk.Button(control_frame, text='←', command=lambda: move_image(-10, 0))
move_left_button.grid(row=2, column=1, padx=5, pady=5)

move_right_button = ttk.Button(control_frame, text='→', command=lambda: move_image(10, 0))
move_right_button.grid(row=2, column=2, padx=5, pady=5)

move_up_button = ttk.Button(control_frame, text='↑', command=lambda: move_image(0, -10))
move_up_button.grid(row=2, column=3, padx=5, pady=5)

move_down_button = ttk.Button(control_frame, text='↓', command=lambda: move_image(0, 10))
move_down_button.grid(row=2, column=4, padx=5, pady=5)

reset_button = ttk.Button(control_frame, text='Reset', command=reset_image)
reset_button.grid(row=2, column=5, padx=5, pady=5)

app.mainloop()
