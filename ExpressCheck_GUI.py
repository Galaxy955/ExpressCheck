import tkinter
import ExpressCheck as ec

# Build the GUI.
class GUI():
    def __init__(self):
        window = tkinter.Tk()
        window.title("  快递状态查询小工具")
        window.geometry("406x528+500+100") # Set the size of the window.
        label0 = tkinter.Label(window, text="省份：")
        label1 = tkinter.Label(window, text="城市：")
        label2 = tkinter.Label(window, text="区县：")
        label3 = tkinter.Label(window, text="详细地址：")
        label4 = tkinter.Label(window, text="查询结果：")
        self.entry0 = tkinter.Entry(window)
        self.entry1 = tkinter.Entry(window)
        self.entry2 = tkinter.Entry(window)
        self.entry3 = tkinter.Entry(window)
        button0 = tkinter.Button(window, text="查询", width=30, command=self.GetParam)
        self.text0 = tkinter.Text(window, width=55, height=21, spacing1=3)
        label0.grid(row=0, column=0, sticky="w", padx="5px")
        self.entry0.grid(row=1, column=0, padx="5px")
        label1.grid(row=0, column=1, sticky="w", padx="5px")
        self.entry1.grid(row=1, column=1, padx="5px")
        label2.grid(row=2, column=0, sticky="w", padx="5px")
        self.entry2.grid(row=3, column=0, padx="5px")
        label3.grid(row=2, column=1, sticky="w", padx="5px")
        self.entry3.grid(row=3, column=1, padx="5px")
        button0.grid(row=4, column=0, columnspan=2, pady="10px")
        label4.grid(row=5, column=0, columnspan=2, sticky="w", padx="5px")
        self.text0.grid(row=6, column=0, columnspan=2, padx="5px", pady="5px")
        window.mainloop()

    def GetParam(self):
        old_text = self.text0.get("1.0", "14.0")
        # print(old_text)
        try:
            if old_text != "":
                self.text0.delete("1.0", "14.0")
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
            if len(result) == 35:
                self.text0.insert("2.0", "查询过于频繁，请稍后再试！")
            else:

                if province != city:
                    self.text0.insert("1.0", "{}{}{}{}的快递情况：\n".format(province, city, area, address))
                    self.text0.insert(2.0,"------------------------------\n")
                else:
                    self.text0.insert("1.0", "{}{}{}的快递情况：\n".format(province, area, address))
                    self.text0.insert(2.0, "------------------------------\n")
                self.text0.insert("4.0", result+"\n")
                self.text0.insert("end", "------------------------------")
        except:
            self.text0.insert(4.0,"网络错误，请重试")

GUI()