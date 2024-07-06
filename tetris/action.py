from common import *
import random

def generatingSlider(self):
  """生成一个颜色随机且形状随机的滑块"""
  shapeIndex = random.randint(0, len(SHAPES) - 1)
  colorIndex = random.randint(0, len(SHAPES_COLORS) - 1)

  self.currentShape = SHAPES[shapeIndex]
  self.currentColor = SHAPES_COLORS[colorIndex]

  # 计算滑块的起始位置
  startX = CANVAS_WIDTH // 2 - BLOCK_SIZE * len(self.currentShape[0]) // 2
  startY = 0

  # 创建滑块
  self.currentSlider = createSlider(self, startX, startY, self.currentShape, self.currentColor)

def createSlider(self, startX, startY, shape, color):
  """在画布上创建一个滑块"""
  slider = []
  for i in range(len(shape)):
    for j in range(len(shape[i])):
      if shape[i][j] == 1:
        x1 = startX + j * BLOCK_SIZE
        y1 = startY + i * BLOCK_SIZE
        x2 = x1 + BLOCK_SIZE
        y2 = y1 + BLOCK_SIZE
        block = self.gameCanvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        slider.append(block)
  return slider

def getSliderPosition(self):
  """获取当前滑块的位置信息"""
  if self.currentSlider:
    coords = [self.gameCanvas.coords(block) for block in self.currentSlider]
    xCoords = [coord[0] for coord in coords]
    yCoords = [coord[1] for coord in coords]
    minX = min(xCoords)
    maxX = max(xCoords)
    minY = min(yCoords)
    maxY = max(yCoords)
    return minX, maxX, minY, maxY
  else:
    return None

def convert(self):
  """控制滑块的变形"""
  pass

def moveLeft(self):
  """控制滑块向左移动一个单位"""
  if self.currentSlider:
    minX, _, _, _ = getSliderPosition(self)
    if minX > 0: 
      for block in self.currentSlider:
        self.gameCanvas.move(block, -BLOCK_SIZE, 0)


def moveRight(self):
  """控制滑块向右移动一个单位"""
  if self.currentSlider:
    _, maxX, _, _ = getSliderPosition(self)
    if maxX < CANVAS_WIDTH:
      for block in self.currentSlider:
        self.gameCanvas.move(block, BLOCK_SIZE, 0)


def moveDown(self):
  """控制滑块向下移动一个单位"""
  if self.currentSlider:
    _, _, maxY, _ = getSliderPosition(self)
    if maxY < CANVAS_HEIGHT:
      for block in self.currentSlider:
        self.gameCanvas.move(block, 0, BLOCK_SIZE)


def snapDown(self):
  """控制滑块快速向下移动到最底部"""
  if self.currentSlider:
    while self.check_collision(self.currentSlider):
      for block in self.currentSlider:
        self.gameCanvas.move(block, 0, BLOCK_SIZE)



