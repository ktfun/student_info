# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import tkFileDialog
import pickle

### 定义一个身份信息的类
class MyId:
    def __init__(self, tname="", tsex="", tage="18", tblood="", tstar="", theight="175", tweight="75"):
        self.name = tname ### 姓名
        self.sex = tsex  ### 性别
        self.age = tage  ### 年纪
        self.blood = tblood  ### 血型
        self.star = tstar  ### 星座
        self.height = theight ### 身高
        self.weight = tweight ### 体重
        self.str = ""

    def __str__(self):
        self.str = ""
        self.str += "姓名: " + str(self.name) + "\n"
        self.str += "性别: " + str(self.sex) + "\n"
        self.str += "年纪: " + str(self.age) + "\n"
        self.str += "血型: " + str(self.blood) + "\n"
        self.str += "星座: " + str(self.star) + "\n"
        self.str += "身高: " + str(self.height) + "\n"
        self.str += "体重: " + str(self.weight) + "\n"
        return str(self.str)

    def show(self):
        print self

    def tolist(self):
        mylist = [self.name, self.sex, self.age, self.blood, self.star, self.height, self.weight]
        return mylist


### 点击确认后调用的函数
def on_button_enter_clicked():
    print "on_button_enter_clicked"
    ### 检查输入，如果有空的，就弹出提示框
    if text_name.get() == "" or text_star.get() == "" or text_height.get() == "" or text_weight.get() == "":
        tkMessageBox.showerror("错误", "请输入完整的信息")
        return
    ### 都是有输入的
    else:
        new_info = MyId(str(text_name.get().encode("utf-8")), str(var_sex.get().encode("utf-8")),
                        str(spinbox_age.get().encode("utf-8")), str(var_blood.get().encode("utf-8")),
                        str(text_star.get().encode("utf-8")), str(text_height.get().encode("utf-8")),
                        str(text_weight.get().encode("utf-8"))) ### 注意这里要转码，否则中文会乱码
        print new_info.tolist()  ### 调整的打印
        for index in range(len(InfoStore)):
            ### 在仓库里面找一下，如果有一个同名的，就先把同名的删掉
            if InfoStore[index].name == new_info.name:
                print "del %d" % (index)
                del InfoStore[index]
        ### 把新的对象加到仓库中
        InfoStore.append(new_info)
        ### 弹框提示成功
        tkMessageBox.showinfo("成功", "成功添加 %s"%(new_info.name))

### 点击搜索后调用的函数
def on_button_search_clicked():
    print "on_button_search_clicked"
    new_info = MyId(str(text_name.get().encode("utf-8")), str(var_sex.get().encode("utf-8")),
                    str(spinbox_age.get().encode("utf-8")), str(var_blood.get().encode("utf-8")),
                    str(text_star.get().encode("utf-8")), str(text_height.get().encode("utf-8")),
                    str(text_weight.get().encode("utf-8")))
    ### 清理一下显示框
    text_detail.delete(0.0, END)
    text_detail.insert(END, "*****查找如下*****\n")
    data_index = 0
    ### 在仓库中查找数据
    for index in InfoStore:
        ### 姓名 - 如果输入框的数据长度为0，则跳过对比；否则，则要对比
        if len(new_info.name) != 0:
            if index.name != new_info.name:
                continue
        ### 性别 - 如果输入框的数据长度为0，或者性别设定为“未知”的话，或者仓库里面的性别为“未知”的话，就跳过对比
        if len(new_info.sex) != 0 and new_info.sex != "未知" and index.sex != "未知":
            if index.sex != new_info.sex:
                continue
        ### 年龄 - 如果输入框的数据长度为0，或者年龄为0的话，就跳过查找
        if len(new_info.age) != 0 and new_info.age != "0":
            if index.age != new_info.age:
                continue
        ### 血型 - 如果输入框的数据长度为0，或者血型设定为“未知”的话，或者仓库里面的血型为“未知”的话，就跳过对比
        if len(new_info.blood) != 0 and new_info.blood != "未知" and index.blood != "未知":
            if index.blood != new_info.blood:
                continue
        ### 星座 - 如果输入框的数据长度为0，则跳过对比；否则，则要对比
        if len(new_info.star) != 0:
            if index.star != new_info.star:
                continue
        ### 身高 -  如果输入框的数据长度为0，或者身高设置为“0”的话，就跳过对比
        if len(new_info.height) !=0 and new_info.height !="0":
            if index.height != new_info.height:
                continue
        ### 体重 - 如果输入框的数据长度为0，或者体重设置为“0”的话，就跳过对比
        if len(new_info.weight) !=0 and new_info.weight != "0":
            if index.weight != new_info.weight:
                continue
        ### 打印出来匹配的数据项目
        data_index += 1
        text_detail.insert(END, "=====%s=====\n" % (data_index))
        text_detail.insert(END, index)
    ### 没有匹配的数据项目
    if data_index == 0:
        text_detail.insert(END,"无记录")

### 点击清除后调用的函数
def on_button_clear_clicked():
    print "on_button_clear_clicked"
    #### 删除或者清零输入框的数据
    text_name.delete(0, END)
    spinbox_age.config(value="0")
    radiobutton_unknown.select()
    radiobutton_ABO.select()
    text_star.delete(0, END)
    text_height.config(value="0")
    text_weight.config(value="0")


### 点击显示所有的信息
def on_button_show_clicked():
    print "on_button_show_clicked"
    ### 清理显示区
    text_detail.delete(0.0, END)
    text_detail.insert(END, "*****查看如下*****\n")
    if len(InfoStore) == 0:
        text_detail.insert(END, "无记录")
    index = 0
    ### 便利仓库里面的数据，全部打印出来
    for info in InfoStore:
        info.show
        index = index + 1
        text_detail.insert(END, "=====%s=====\n"%(index))
        text_detail.insert(END, info)


### 导入数据后调用的数据
def on_button_in_clicked():
    print "on_button_in_clicked"
    ### 弹出一个文件对话框，选择一个存在的数据文件
    fp = tkFileDialog.askopenfile(mode='r', defaultextension="txt", filetypes=[("文件", "*")])
    ### 判断一下有没有"close"这个属性（函数），如果没有的话，就说明文件打开失败
    if not hasattr(fp, "close"):
        return
    else:
        ### 这里如果有异常，说明文件格式有问题
        try:
            ###这里用到的是pickle模块的反序列化
            NewInfoStore = pickle.load(fp)
        except:
            tkMessageBox.showerror("错误","文件格式异常")
            return
        ### 便利导入的仓库
        for new_info in NewInfoStore:
            ### 便利旧的仓库，如果存在导入的数据（对比姓名），则先删掉，再添加
            for old_info in InfoStore:
                if old_info.name == new_info.name:
                    InfoStore.remove(old_info)
            InfoStore.append(new_info)
    ### 关闭文件
    fp.close()


### 导出数据
def on_button_out_clicked():
    print "on_button_out_clicked"
    ### 仓库中没有数据
    if len(InfoStore) == 0:
        tkMessageBox.showinfo("信息","无记录")
        return
    ### 弹出文件框，选择一个导出文件（必须存在）
    fp = tkFileDialog.asksaveasfile(mode='w+', defaultextension="txt", filetypes=[("文件", "*")])
    ### 判断下是否有close属性，如果没有的话，说明没有打开文件
    if not hasattr(fp, "close"):
        return
    for info in InfoStore:
        ### 这里用到pickle的序列化
        pickle.dump(InfoStore, fp)
    ### 关闭文件
    fp.close()
    ### 弹框提示-导出成功
    tkMessageBox.showinfo("成功", "导出成功")

### 程序的主入口
if __name__== "__main__":
    root = Tk()
    root.title('信息录入与查找系统')
    InfoStore = []  ### 存储所有的录入信息 - 仓库

    ### 整体frame划分 - 划分为上中下三层。上层都是输入框，中层都是功能按钮，下层是显示框
    frame_top = Frame(root, width = 400, height = 200)  ### 上层 - 根据输入的项目再分成几个小的框体
    frame_top_0 = Frame(frame_top) ### 上层0
    frame_top_1 = Frame(frame_top) ### 上层1
    frame_top_2 = Frame(frame_top) ### 上层2
    frame_top_3 = Frame(frame_top) ### 上层3
    frame_top_4 = Frame(frame_top) ### 上层4
    frame_top_5 = Frame(frame_top) ### 上层5
    frame_top_6 = Frame(frame_top) ### 上层6
    frame_mid = Frame(root, width = 400, height = 40) ### 中层
    frame_bot = Frame(root, width = 400, height = 200) ### 下层
    ###### 这下面的grid是布局管理器，按照表格划分区域
    frame_top.grid(row=0)
    frame_mid.grid(row=1)
    frame_bot.grid(row=2)
    frame_top_0.grid(row=0, sticky=W) ### sticky=W指的是按照WEST（左对齐）的方式排放
    frame_top_1.grid(row=1, sticky=W)
    frame_top_2.grid(row=2, sticky=W)
    frame_top_3.grid(row=3, sticky=W)
    frame_top_4.grid(row=4, sticky=W)
    frame_top_5.grid(row=5, sticky=W)
    frame_top_6.grid(row=6, sticky=W)

    #####################################################
    ### frame_top - 这一层主要是信息的输入
    #####################################################
    ## 姓名
    label_name = Label(frame_top_0, text="姓名")
    text_name = Entry(frame_top_0)
    label_name.grid(row=0, column=0)
    text_name.grid(row=0, column=1)

    ## 性别
    var_sex = StringVar()  ### 表明性别的变量，用于和后面的radiobutton绑定
    label_sex = Label(frame_top_1, text="性别")
    radiobutton_male = Radiobutton(frame_top_1, text="男", value="男", variable=var_sex)
    radiobutton_female = Radiobutton(frame_top_1, text="女", value="女", variable=var_sex)
    radiobutton_unknown = Radiobutton(frame_top_1, text="未知", value="未知", variable=var_sex)
    label_sex.grid(row=0, column=0)
    radiobutton_male.grid(row=0, column=1)
    radiobutton_female.grid(row=0, column=2)
    radiobutton_unknown.grid(row=0, column=3)
    radiobutton_unknown.select() ### 默认“未知”

    ## 年龄
    label_age = Label(frame_top_2, text="年龄")
    spinbox_age = Spinbox(frame_top_2, from_=0, to=150)
    label_age.grid(row=0, column=0)
    spinbox_age.grid(row=0, column=1)

    ## 血型
    haha = ["A","B","AB","O"]
    var_blood = StringVar() ### 表明血型的变量，用于和后面的radiobutton绑定
    label_blood = Label(frame_top_3, text="血型")
    radiobutton_A = Radiobutton(frame_top_3, text="A", value="A", variable=var_blood)
    radiobutton_B = Radiobutton(frame_top_3, text="B", value="B", variable=var_blood)
    radiobutton_AB = Radiobutton(frame_top_3, text="AB", value="AB", variable=var_blood)
    radiobutton_O = Radiobutton(frame_top_3, text="O", value="O", variable=var_blood)
    radiobutton_ABO = Radiobutton(frame_top_3, text="未知", value="未知", variable=var_blood)
    label_blood.grid(row=0, column=0)
    radiobutton_A.grid(row=0, column=1)
    radiobutton_B.grid(row=0, column=2)
    radiobutton_AB.grid(row=0, column=3)
    radiobutton_O.grid(row=0, column=4)
    radiobutton_ABO.grid(row=0, column=5)
    radiobutton_ABO.select()  ## 默认“未知”

    ## 星座
    label_star  = Label(frame_top_4, text="星座")
    text_star = Entry(frame_top_4)
    label_star.grid(row=4, column=0)
    text_star.grid(row=4, column=1)

    ## 身高
    label_height = Label(frame_top_5, text="身高")
    text_height = Spinbox(frame_top_5, from_=0, to=250)
    label_height_cm = Label(frame_top_5, text="cm")
    label_height.grid(row=5, column=0)
    text_height.grid(row=5, column=1)
    label_height_cm.grid(row=5, column=2)

    ## 体重
    label_weight = Label(frame_top_6, text="体重")
    text_weight = Spinbox(frame_top_6, from_=0, to=250)
    label_weight_kg = Label(frame_top_6, text="kg")
    label_weight.grid(row=6, column=0)
    text_weight.grid(row=6, column=1)
    label_weight_kg.grid(row=6, column=2)

    #####################################################
    ### frame_mid - 这一层主要是功能按键
    #####################################################
    ## 确认 查找 清除 backspace
    button_enter = Button(frame_mid, text="确认", command=on_button_enter_clicked)  ### 确认按键
    button_search = Button(frame_mid, text="查找", command=on_button_search_clicked)  ### 查找按键
    button_clear = Button(frame_mid, text="清除", command=on_button_clear_clicked)  ### 清除按键
    button_show = Button(frame_mid, text="查看", command=on_button_show_clicked)  ### 查看按键
    button_in = Button(frame_mid, text="导入", command=on_button_in_clicked)  ### 导入按键
    button_out = Button(frame_mid, text="导出", command=on_button_out_clicked)  ### 导出按键
    button_enter.grid(row=0, column=0)
    button_search.grid(row=0, column=1)
    button_clear.grid(row=0, column=2)
    button_show.grid(row=0, column=3)
    button_in.grid(row=1, column=1)
    button_out.grid(row=1, column=2)

    #####################################################
    ### frame_bot - 这一层主要是显示区域
    #####################################################
    bar_text_detail = Scrollbar(frame_bot)  ### 滚动条
    bar_text_detail.pack(side = RIGHT, fill=Y)  ### 滚动条放到右边
    text_detail = Text(frame_bot, width = 100, height = 20, yscrollcommand=bar_text_detail.set) ### 显示框，将垂直的滚动条绑定起来
    text_detail.pack(side = LEFT, fill = BOTH) ### 显示狂放到左边
    bar_text_detail.config(command = text_detail.yview) ### 将滚动条的显示和显示框绑定

    root.mainloop() ### 事件主循环

