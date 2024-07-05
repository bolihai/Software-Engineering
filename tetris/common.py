from tkinter import (Button, Radiobutton, Label)

# 画布的宽度
CANVAS_WIDTH = 600

# 画布的高度
CANVAS_HEIGHT = 900

# 滑块大小
BLOCK_SIZE = 30

# 方块的形状及其旋转形态
SHAPES = [
    [[1, 1, 1, 1]],            
    [[1, 1, 1], [0, 1, 0]],    
    [[1, 1, 1], [1, 0, 0]],    
    [[1, 1, 1], [0, 0, 1]],      
    [[1, 1], [1, 1]],         
    [[0, 1, 1], [1, 1, 0]],    
    [[1, 1, 0], [0, 1, 1]]       
]

# 滑块的颜色
SHAPES_COLORS = ["cyan", "purple", "orange", "blue", "yellow", "green", "red"]

# 按钮之间的间隔
BUTTON_PADDING = 100

# 按钮的宽度
BUTTON_WIDTH = 150

# 按钮的高度
BUTTON_HEIGHT = 50

# 设置每多少秒刷新一次
DELAY = 200

# 设置实际没多少秒刷新一次
TRUE_DELAY = 200

def button(root, text, command, borderWidth=2):
  """返回一个按钮的控件"""
  return Button(root, text=text, command=command, borderwidth=borderWidth)

def radiobox(root, text, variable, value):
  """返回一个单选框的控件"""
  return Radiobutton(root, text=text, variable=variable, value=value)

def label(root, text, font=(3, 40)):
  return Label(root, text=text, font=font)

def settingDelay(self, var):
  """设置实际屏幕没多久刷新一次"""
  global TRUE_DELAY
  TRUE_DELAY = var.get()
  self.menu()