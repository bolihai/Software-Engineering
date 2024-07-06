from tkinter import *
from common import *
from action import *

class Menu:
    def __init__(self, master):
      """初始化画布"""
      self.master = master

      # 获取屏幕的大小
      screenWidth = self.master.winfo_screenwidth()
      screenHeight = self.master.winfo_screenheight()

      # 获取屏幕中间的位置
      xPosition = (screenWidth - CANVAS_WIDTH) // 2  
      yPosition = (screenHeight - CANVAS_HEIGHT) // 2

      # 将窗口生成在正中间
      self.master.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}+{xPosition}+{yPosition}")
      
      # 设置无法改变窗口大小
      self.master.resizable(width=False, height=False)

      # 设置画布的标题以及大小
      self.master.title("俄罗斯方块")
      self.master.resizable(False, False)

      # 创建不同的页面
      self.menuFrame = Frame(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
      self.gameFrame = Frame(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
      self.settingFrame = Frame(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

      self.menu()

    def menu(self):
      """设置菜单栏，包括开始游戏，设置，退出"""
       # 清除其他页面
      self.gameFrame.pack_forget()
      self.settingFrame.pack_forget()

      # 显示菜单页面
      self.menuFrame.pack()

      # 生成欢迎语
      welcome = label(self.menuFrame, "俄罗斯方块")

      # 生成按钮
      gameButton = button(self.menuFrame, "开始游戏", self.game)
      settingButton = button(self.menuFrame, "设置", self.setting)
      exitButton = button(self.menuFrame, "退出游戏", self.exit)

      # 安装按钮
      welcome.place(x=150, y=150)
      gameButton.place(x=(CANVAS_WIDTH-BUTTON_WIDTH)/2, y=BUTTON_PADDING*4, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
      settingButton.place(x=(CANVAS_WIDTH-BUTTON_WIDTH)/2, y=BUTTON_PADDING*5, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
      exitButton.place(x=(CANVAS_WIDTH-BUTTON_WIDTH)/2, y=BUTTON_PADDING*6, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

    def game(self):
      """开始游戏"""
      # 清除其他页面
      self.menuFrame.pack_forget()
      self.settingFrame.pack_forget()

      # 显示游戏界面
      self.gameFrame.pack()
      self.master.title("俄罗斯方块")

      # 初始化游戏状态
      self.gameCanvas = Canvas(self.gameFrame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
      self.gameCanvas.pack()

      # 生成滑块
      generatingSlider(self)

      # 绑定键盘事件
      self.master.bind("<Left>", lambda event: moveLeft(self))
      self.master.bind("<Right>", lambda event: moveRight(self))
      self.master.bind("<Down>", lambda event: moveDown(self))
      self.master.bind("<space>", lambda event: snapDown(self))


    def setting(self):
      """设置游戏难度"""
      # 清除其他页面
      self.gameFrame.pack_forget()
      self.menuFrame.pack_forget()

      # 显示设置页面
      self.settingFrame.pack()
      self.master.title("设置")

      # 设置时延
      var = IntVar()

      # 设置语言
      settingsLabel = Label(self.settingFrame, text="难度", font=("Helvetica", 20))

      # 生成返回和确定按钮
      exitButton = Button(self.settingFrame, text="返回", command=self.menu)
      confirmButton = Button(self.settingFrame, text="确定", command=lambda: settingDelay(self, var))

      # 生成难度等级：简单，中等，困难
      easyRadioButton = Radiobutton(self.settingFrame, text="简单", variable=var, value=DELAY)
      mediumRadioButton = Radiobutton(self.settingFrame, text="中等", variable=var, value=DELAY*2)
      difficultRadioButton = Radiobutton(self.settingFrame, text="困难", variable=var, value=DELAY*3)

      # 设置默认选中项
      easyRadioButton.select()  # 设置简单为默认选中项

      # 安装控件
      settingsLabel.place(x=(CANVAS_WIDTH - settingsLabel.winfo_reqwidth()) // 2, y=130)
      easyRadioButton.place(x=(CANVAS_WIDTH - BUTTON_WIDTH) // 2, y=200, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
      mediumRadioButton.place(x=(CANVAS_WIDTH - BUTTON_WIDTH) // 2, y=230, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
      difficultRadioButton.place(x=(CANVAS_WIDTH - BUTTON_WIDTH) // 2, y=260, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
      exitButton.place(x=120, y=330, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
      confirmButton.place(x=320, y=330, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


    def exit(self):
      """设置退出"""
      self.master.destroy()

def main():
    # 创建tk
    root = Tk()

    # 开始菜单
    app = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
