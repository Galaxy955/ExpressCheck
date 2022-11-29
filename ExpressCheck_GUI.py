import tkinter
import ExpressCheck as ec

# Build the GUI.
class GUI():
    def __init__(self):
        window = tkinter.Tk()
        window.title("快递状态查询小工具")
        window.geometry("384x528+500+100") # Set the size of the window.
        label0 = tkinter.Label(window, text="省份：")
        label1 = tkinter.Label(window, text="城市：")
        label2 = tkinter.Label(window, text="区县：")
        label3 = tkinter.Label(window, text="详细地址：")
        label_blank = tkinter.Label(window)
        label4 = tkinter.Label(window, text="查询结果：")
        self.entry0 = tkinter.Entry(window)
        self.entry1 = tkinter.Entry(window)
        self.entry2 = tkinter.Entry(window)
        self.entry3 = tkinter.Entry(window)
        button0 = tkinter.Button(window, text="查询", width=30, command=self.GetParam)
        self.text0 = tkinter.Text(window, width=52, height=26)
        label0.grid(row=0, column=0)
        self.entry0.grid(row=1, column=0)
        label1.grid(row=0, column=1)
        self.entry1.grid(row=1, column=1)
        label2.grid(row=2, column=0)
        self.entry2.grid(row=3, column=0)
        label3.grid(row=2, column=1)
        self.entry3.grid(row=3, column=1)
        label_blank.grid(row=4, column=0, columnspan=2)
        label_blank.grid(row=5, column=0, columnspan=2)
        button0.grid(row=6, column=0, columnspan=2)
        label4.grid(row=7, column=0, columnspan=2)
        self.text0.grid(row=8, column=0, columnspan=2)
        window.mainloop()

    def GetParam(self):
        province = self.entry0.get()
        if province == "":
            province = "重庆市"
        city = self.entry1.get()
        if city == "":
            city = "重庆市"
        area = self.entry2.get()
        if area == "":
            area = "南岸区"
        address = self.entry3.get()
        if address == "":
            address = "重庆邮电大学"
        result = ec.main(province, city, area, address, command=1)
        # print(result)
        self.text0.insert("1.0", "\n"+result)

GUI()