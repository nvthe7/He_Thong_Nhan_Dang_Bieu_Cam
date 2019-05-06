
from tkinter import filedialog
from tkinter import *
import PIL
from PIL import Image,ImageTk
import image_test as it
win = Tk()
win.title("Face Emotion Recognition")
win.geometry("990x600+70+10")
win.config(bg='#00CFC9')
win.resizable(0,0)
label =Label(win, text="ỨNG DỤNG NHẬN DẠNG BIỂU CẢM KHUÔN MẶT",fg='white',bg='#00CFC9')
label.config(font=("Arial", 18,'bold'))
label.place(x=200,y=18)
img = ImageTk.PhotoImage(Image.open("bg-img.jpg"))
canvas = Canvas(win,width=890,height=500) 
canvas.create_image(0,0,anchor = NW, image=img)
canvas.place(x=50, y= 60)

def callback():
    filename =  filedialog.askopenfilename(parent=win,initialdir = "/",title = "Select file",filetypes = (("Tệp hình ảnh","*.jpg"),("all files","*.*")))
    it.test_image(filename)
b = Button(win, text="START UPLOADING",fg='white',bg ='#25A55B',width = 18,height=2, command=callback)
b.config(font=("Arial", 13,'bold'))
b.place(x = 400,y = 480)
win.mainloop()
