from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


class ImageConverter:
    def __init__(self, master):
        self.master = master
        master.title("이미지 변환기")

        # 이미지 선택 버튼
        self.select_btn = Button(self.master, text="이미지 선택", command=self.load_image)
        self.select_btn.pack()
        
        # 흑백모드 버튼
        self.grayscale_btn = Button(self.master, text="흑백 모드", command=self.grayscale_mode)
        self.grayscale_btn.pack()

        # 좌우반전 버튼
        self.flip_left_right_btn = Button(self.master, text="좌우반전", command=self.flip_left_right)
        self.flip_left_right_btn.pack()

        # 상하반전 버튼
        self.flip_top_bottom_btn = Button(self.master, text="상하반전", command=self.flip_top_bottom)
        self.flip_top_bottom_btn.pack()

        # 이미지 화면
        self.img = None
        self.panel = Label(self.master)
        self.panel.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            self.img = Image.open(file_path)
            self.panel.config(text="")
            self.update_image()

    def update_image(self):
        if self.img.mode != "RGB":
            self.img = self.img.convert("RGB")

        img = self.img.resize((400, 400))
        img_tk = ImageTk.PhotoImage(img)

        self.panel.config(image=img_tk)
        self.panel.image = img_tk

    def grayscale_mode(self):
        if self.img:
            self.img = self.img.convert("L")
            self.update_image()

    def flip_left_right(self):
        if self.img:
            self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
            self.update_image()

    def flip_top_bottom(self):
        if self.img:
            self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
            self.update_image()

root = Tk()
app = ImageConverter(root)
root.mainloop()