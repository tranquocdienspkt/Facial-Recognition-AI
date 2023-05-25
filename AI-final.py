from keras.models import load_model
from keras.utils import load_img, img_to_array

from numpy import asarray
from numpy import save
import numpy as np

model = load_model('FaceAttendance.h5')


from tkinter import *
from cv2 import *
from PIL import Image, ImageTk

vid = cv2.VideoCapture(0)
width, height = 300, 300
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

name_nv = ['LE QUOC CUONG', 'TRAN VAN DANH', 'TRAN QUOC DIEN']
birthday_nv = ['16/6/2002', '7/7/2002', '03/10/2002']
post_nv = ['NHÂN VIÊN THỬ VIỆC', 'THỰC TẬP', 'NHÂN VIÊN CHÍNH THỨC']
office_nv = ['VỆ SINH', 'BASIC SOFTWAVE', 'BASIC SOFTWAVE']

def open_camera():

	# Capture the video frame by frame
	_, frame = vid.read()

	# Convert image from one color space to other
	opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	# Capture the latest frame and transform to image
	captured_image = Image.fromarray(opencv_image)

	# Convert captured image to photoimage
	photo_image = ImageTk.PhotoImage(image=captured_image)

	# Displaying photoimage in the label
	label_widget.photo_image = photo_image

	# Configure image in the label
	label_widget.configure(image=photo_image)

	label_widget.after(1, open_camera)

def cap_image():
	label1_1.configure(text = "")
	# reading the input using the camera
	result, image = vid.read()
	  
	# If image will detected without any error, 
	# show result
	if result:
	    # saving image in local storage
	    imwrite("Dien.png", image)
	    # If keyboard interrupt occurs, destroy image 
	    # window
	    waitKey(0)
	    destroyWindow("GeeksForGeeks")
	# If captured image is corrupted, moving to else part
	else:
	    print("No image detected. Please! try again")

	img_url = 'Dien.png'
	x_test = []
	img_test = load_img(img_url, target_size=(200,200))
	img_test = img_to_array(img_test)
	x_test.append(img_test)
	x_test = asarray(x_test)
	x_test = x_test.reshape(1,200,200,3)
	x_test = x_test.astype('float32')/255
	y = np.argmax(model.predict(x_test), axis = -1)
	print(y)
	
	label1_1.configure(text = name_nv[y[0]-1])
	label2_1.configure(text = birthday_nv[y[0]-1])
	label3_1.configure(text = post_nv[y[0]-1])
	label4_1.configure(text = office_nv[y[0]-1])
	


app = Tk()
app.title('CHECK ATTENDANCE')
app.geometry("750x400")
app.bind('<Escape>', lambda e: app.quit())
label_widget = Label(app)
label_widget.pack()


bg1 = PhotoImage(file = "Untitled.png")
background1 = Label(app, image = bg1)

bg2 = PhotoImage(file = "backgroundwhite1.png")
background2 = Label(app, image = bg2)

bg3 = PhotoImage(file = "backgroundwhite2.png")
background3 = Label(app, image = bg3)

click_btn1= PhotoImage(file='OPENCAM.PNG')
img_label1= Label(image = click_btn1)
button1 = Button(app, image = click_btn1, command = open_camera, borderwidth = 0)

click_btn2= PhotoImage(file='ATTENDANCE.png')
img_label2= Label(image=click_btn2)
button2 = Button(app, image = click_btn2, command = cap_image, borderwidth = 0)

label_bg = '#9ad7fc'

label1 = Label(text="Tên: ", 		font = ('Verdana', 12), bg = label_bg)
label1_1 = Label(text="", 			font = ('Verdana', 12), bg = label_bg)

label2 = Label(text="Ngày sinh: ", 	font = ('Verdana', 12), bg = label_bg)
label2_1 = Label(text="", 			font = ('Verdana', 12), bg = label_bg)

label3 = Label(text="Chức vụ: ", 	font = ('Verdana', 12), bg = label_bg)
label3_1 = Label(text="", 			font = ('Verdana', 12), bg = label_bg)

label4 = Label(text="Phòng ban: ", 	font = ('Verdana', 12), bg = label_bg)
label4_1 = Label(text="", 			font = ('Verdana', 12), bg = label_bg)

button1.place(x = 5, y = 50)
button2.place(x = 10, y = 150)

label1.place(x = 5, y = 300)
label1_1.place(x = 100, y = 300)
label2.place(x = 330, y = 300)
label2_1.place(x = 430, y = 300)

label3.place(x = 5 , y = 340)
label3_1.place(x = 100, y = 340)
label4.place(x = 330, y = 340)
label4_1.place(x = 430, y = 340)
background1.place(x = 0, y = 290)
background2.place(x = 0, y = 0)
background3.place(x = 550, y = 0)

app.mainloop()
