from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPainter, QPoint, QPen, QSize
from PyQt5.QtCore import Qt


class PaintBoard(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.__size = QSize(350, 350)
        
        # 新建画板，尺寸为__size
        self.__board = QPixmap(self.__size)
        self.__board.fill(Qt.white)  # 用白色填充画板

        self.__painter = QPainter()  # 新建绘图工具
        self.eraser_mode = False  # 默认为禁用橡皮擦模式
        self.__thickness = 6        # 默认画笔粗细为10px
        
        self.__lastPos = QPoint(0, 0)  # 上一次鼠标位置
        self.__currentPos = QPoint(0, 0)  # 当前的鼠标位置
        self.__undo_num = 0
        self.__redo_num = 0
        self.__undo_list = []
        self.__redo_list = []
        self.__undo_list.append(self.__board.toImage())

        # 设置界面的尺寸为__size
        self.setFixedSize(self.__size)
        
    def clear(self):
        self.__board.fill(Qt.white)
        # 清空画板
        self.update()
        self.__undo_list.append(self.__board.toImage())
        self.__redo_list = []
        self.__undo_num += 1
        self.__redo_num = 0

    def up(self, image):
        self.__board = image
        # 清空画板
        self.update()
        self.__undo_list.append(self.__board.toImage())
        self.__redo_list = []
        self.__undo_num += 1
        self.__redo_num = 0

    def undo(self):
        if self.__undo_num > 0:
            image = self.__undo_list[self.__undo_num - 1]
            self.__board = QPixmap.fromImage(image)
            self.update()
            self.__redo_list.append(self.__undo_list.pop())
            self.__redo_num += 1
            self.__undo_num -= 1

    def redo(self):
        if self.__redo_num > 0:
            image = self.__redo_list[self.__redo_num - 1]
            self.__board = QPixmap(image)
            self.update()
            self.__undo_list.append(self.__redo_list.pop())
            self.__redo_num -= 1
            self.__undo_num += 1

    def change_pen_thickness(self, thickness=10):
        # 改变画笔粗细
        self.__thickness = thickness
    
    def get_content_as_image(self):
        # 获取画板内容（返回QImage）
        image = self.__board.toImage()
        return image
        
    def paintEvent(self, paint_event):
        # 绘图事件
        # 绘图时必须使用QPainter的实例，此处为__painter
        # 绘图在begin()函数与end()函数间进行
        # begin(param)的参数要指定绘图设备，即把图画在哪里
        self.__painter.begin(self)
        # 0,0为绘图的左上角起点的坐标，__board即要绘制的图
        self.__painter.drawPixmap(0, 0, self.__board)
        self.__painter.end()

    def mouse_press_event(self, mouse_event):
        # 鼠标按下时，获取鼠标的当前位置保存为上一次位置
        # self.__currentPos = mouse_event.pos()
        self.__currentPos.setX(mouse_event.pos().x() - 803)
        self.__currentPos.setY(mouse_event.pos().y() - 147)
        self.__lastPos = self.__currentPos

    def mouse_move_event(self, mouse_event):
        # self.__currentPos = mouse_event.pos()
        # 鼠标移动时，更新当前位置，并在上一个位置和当前位置间画线
        self.__currentPos.setX(mouse_event.pos().x() - 803)
        self.__currentPos.setY(mouse_event.pos().y() - 147)
        self.__painter.begin(self.__board)

        if not self.eraser_mode:
            # 非橡皮擦模式
            self.__painter.setPen(QPen(Qt.black, self.__thickness))  # 设置画笔颜色，粗细
        else:
            # 橡皮擦模式下画笔为纯白色，粗细为10
            self.__painter.setPen(QPen(Qt.white, self.__thickness))

        # 画线
        self.__painter.drawLine(self.__lastPos, self.__currentPos)
        self.__painter.end()
        self.__lastPos = self.__currentPos

        self.update()  # 更新显示

    def mouse_release_event(self, mouse_event):
        self.__undo_list.append(self.__board.toImage())
        self.__redo_list = []
        self.__undo_num += 1
        self.__redo_num = 0
