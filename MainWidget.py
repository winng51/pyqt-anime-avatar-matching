from PyQt5.Qt import QColor, QPixmap, QIcon, QCursor
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PaintBoard import PaintBoard
import random
from getline import do_image
from compare import compare_image
import data


class MainWidget(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("./UI/icons/icon.png"))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 初始化界面
        self.__see = 1
        self.setWindowOpacity(self.__see)  # 设置透明度
        self.setFixedSize(1200, 740)  # 设置窗口大小
        self.setWindowTitle("动漫头像搜索工具")  # 设置窗口标题
        self.m_flag = False  # 是否拖动
        self.m_Position = self.pos()  # 自身（全局）位置

        # 添加内部窗口
        self.widget = QWidget(self)
        self.widget.resize(1197, 736)
        self.widget.setStyleSheet("border-image: url(./UI/background.png) 0 0 0 0 stretch stretch;")
        self.widget.move(0, 0)

        # 初始化成员变量
        self.__paintBoard = PaintBoard(self)
        self.__paintBoard.move(800, 145)
        # 获取颜色列表(字符串类型)
        self.__colorList = QColor.colorNames()
        self.__color = "null"  # 当前颜色
        self.__is_searched = False
        self.__search_files = []
        self.__now_files = []
        self.__pic_files = data.pic_files
        self.__files = data.pic_files
        self.__number = 0  # 当前页码
        self.__select = [False, False, False, False, False, False, False, False, False, False, False, False]

        # 图像
        self.__pic_1 = QPixmap("./pictures/bbxy 1.jpg")
        self.__pic_2 = QPixmap("./pictures/bbxy 12.jpg")
        self.__pic_3 = QPixmap("./pictures/bbxy 13.jpg")
        self.__pic_4 = QPixmap("./pictures/bbxy 14.jpg")
        self.__pic_5 = QPixmap("./pictures/bbxy 15.jpg")
        self.__pic_6 = QPixmap("./pictures/bbxy 16.jpg")
        self.__pic_7 = QPixmap("./pictures/bbxy 17.jpg")
        self.__pic_8 = QPixmap("./pictures/bbxy 18.jpg")
        self.__pic_9 = QPixmap("./pictures/bbxy 19.jpg")
        self.__pic_10 = QPixmap("./pictures/bbxy 2.jpg")
        self.__pic_11 = QPixmap("./pictures/bbxy 20.jpg")
        self.__pic_12 = QPixmap("./pictures/bbxy 21.jpg")

        # 图片
        self.__label_1 = QLabel(self)
        self.__label_1.resize(150, 150)
        self.__label_1.move(65, 150)
        self.__label_1.setPixmap(self.__pic_1)
        self.__label_1.setScaledContents(True)

        self.__btn_1 = QPushButton()
        self.__btn_1.setParent(self)
        self.__btn_1.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_1.clicked.connect(self.on_btn_1_clicked)
        self.__btn_1.resize(150, 150)
        self.__btn_1.move(65, 150)

        self.__label_2 = QLabel(self)
        self.__label_2.resize(150, 150)
        self.__label_2.move(231, 150)
        self.__label_2.setPixmap(self.__pic_2)
        self.__label_2.setScaledContents(True)

        self.__btn_2 = QPushButton()
        self.__btn_2.setParent(self)
        self.__btn_2.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_2.clicked.connect(self.on_btn_2_clicked)
        self.__btn_2.resize(150, 150)
        self.__btn_2.move(231, 150)

        self.__label_3 = QLabel(self)
        self.__label_3.resize(150, 150)
        self.__label_3.move(397, 150)
        self.__label_3.setPixmap(self.__pic_3)
        self.__label_3.setScaledContents(True)

        self.__btn_3 = QPushButton()
        self.__btn_3.setParent(self)
        self.__btn_3.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_3.clicked.connect(self.on_btn_3_clicked)
        self.__btn_3.resize(150, 150)
        self.__btn_3.move(397, 150)

        self.__label_4 = QLabel(self)
        self.__label_4.resize(150, 150)
        self.__label_4.move(563, 150)
        self.__label_4.setPixmap(self.__pic_4)
        self.__label_4.setScaledContents(True)

        self.__btn_4 = QPushButton()
        self.__btn_4.setParent(self)
        self.__btn_4.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_4.clicked.connect(self.on_btn_4_clicked)
        self.__btn_4.resize(150, 150)
        self.__btn_4.move(563, 150)

        self.__label_5 = QLabel(self)
        self.__label_5.resize(150, 150)
        self.__label_5.move(65, 316)
        self.__label_5.setPixmap(self.__pic_5)
        self.__label_5.setScaledContents(True)

        self.__btn_5 = QPushButton()
        self.__btn_5.setParent(self)
        self.__btn_5.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_5.clicked.connect(self.on_btn_5_clicked)
        self.__btn_5.resize(150, 150)
        self.__btn_5.move(65, 316)

        self.__label_6 = QLabel(self)
        self.__label_6.resize(150, 150)
        self.__label_6.move(231, 316)
        self.__label_6.setPixmap(self.__pic_6)
        self.__label_6.setScaledContents(True)

        self.__btn_6 = QPushButton()
        self.__btn_6.setParent(self)
        self.__btn_6.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_6.clicked.connect(self.on_btn_6_clicked)
        self.__btn_6.resize(150, 150)
        self.__btn_6.move(231, 316)

        self.__label_7 = QLabel(self)
        self.__label_7.resize(150, 150)
        self.__label_7.move(397, 316)
        self.__label_7.setPixmap(self.__pic_7)
        self.__label_7.setScaledContents(True)

        self.__btn_7 = QPushButton()
        self.__btn_7.setParent(self)
        self.__btn_7.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_7.clicked.connect(self.on_btn_7_clicked)
        self.__btn_7.resize(150, 150)
        self.__btn_7.move(397, 316)

        self.__label_8 = QLabel(self)
        self.__label_8.resize(150, 150)
        self.__label_8.move(563, 316)
        self.__label_8.setPixmap(self.__pic_8)
        self.__label_8.setScaledContents(True)

        self.__btn_8 = QPushButton()
        self.__btn_8.setParent(self)
        self.__btn_8.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_8.clicked.connect(self.on_btn_8_clicked)
        self.__btn_8.resize(150, 150)
        self.__btn_8.move(563, 316)

        self.__label_9 = QLabel(self)
        self.__label_9.resize(150, 150)
        self.__label_9.move(65, 482)
        self.__label_9.setPixmap(self.__pic_9)
        self.__label_9.setScaledContents(True)

        self.__btn_9 = QPushButton()
        self.__btn_9.setParent(self)
        self.__btn_9.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_9.clicked.connect(self.on_btn_9_clicked)
        self.__btn_9.resize(150, 150)
        self.__btn_9.move(65, 482)

        self.__label_10 = QLabel(self)
        self.__label_10.resize(150, 150)
        self.__label_10.move(231, 482)
        self.__label_10.setPixmap(self.__pic_10)
        self.__label_10.setScaledContents(True)

        self.__btn_10 = QPushButton()
        self.__btn_10.setParent(self)
        self.__btn_10.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_10.clicked.connect(self.on_btn_10_clicked)
        self.__btn_10.resize(150, 150)
        self.__btn_10.move(231, 482)

        self.__label_11 = QLabel(self)
        self.__label_11.resize(150, 150)
        self.__label_11.move(397, 482)
        self.__label_11.setPixmap(self.__pic_11)
        self.__label_11.setScaledContents(True)

        self.__btn_11 = QPushButton()
        self.__btn_11.setParent(self)
        self.__btn_11.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_11.clicked.connect(self.on_btn_11_clicked)
        self.__btn_11.resize(150, 150)
        self.__btn_11.move(397, 482)

        self.__label_12 = QLabel(self)
        self.__label_12.resize(150, 150)
        self.__label_12.move(563, 482)
        self.__label_12.setPixmap(self.__pic_12)
        self.__label_12.setScaledContents(True)

        self.__btn_12 = QPushButton()
        self.__btn_12.setParent(self)
        self.__btn_12.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_12.clicked.connect(self.on_btn_12_clicked)
        self.__btn_12.resize(150, 150)
        self.__btn_12.move(563, 482)

        # 按钮
        self.__btn_see = QPushButton()
        self.__btn_see.setParent(self)  # 设置父对象为本界面
        self.__btn_see.clicked.connect(self.on_btn_see_clicked)
        self.__btn_see.setStyleSheet("QPushButton{border-image: url(./UI/icons/see.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/see_hover.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/see_pressed.png)}")
        self.__btn_see.move(27, 58)
        self.__btn_see.resize(89, 70)
        self.__btn_see.setToolTip('透明度')

        self.__btn_refresh = QPushButton()
        self.__btn_refresh.setParent(self)  # 设置父对象为本界面
        self.__btn_refresh.clicked.connect(self.refresh)
        self.__btn_refresh.setStyleSheet("QPushButton{border-image: url(./UI/icons/refresh.png)}"
                                         "QPushButton:hover{border-image: url(./UI/icons/refresh_hover.png)}"
                                         "QPushButton:pressed{border-image: url(./UI/icons/refresh_pressed.png)}")
        self.__btn_refresh.move(485, 50)
        self.__btn_refresh.resize(35, 35)
        self.__btn_refresh.setToolTip('随便看看')

        self.__btn_min = QPushButton()
        self.__btn_min.setParent(self)  # 设置父对象为本界面
        self.__btn_min.clicked.connect(self.showMinimized)
        self.__btn_min.setStyleSheet("QPushButton{border-image: url(./UI/icons/min.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/min_hover.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/min_pressed.png)}")
        self.__btn_min.move(1085, 57)
        self.__btn_min.resize(45, 45)
        self.__btn_min.setToolTip('最小化')

        self.__btn_Quit = QPushButton()
        self.__btn_Quit.setParent(self)  # 设置父对象为本界面
        self.__btn_Quit.clicked.connect(self.close)
        self.__btn_Quit.setStyleSheet("QPushButton{border-image: url(./UI/icons/close.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/close_hover.png)}"
                                      "QPushButton:pressed{border-image: url(./UI/icons/close_pressed.png)}")
        self.__btn_Quit.move(1135, 57)
        self.__btn_Quit.resize(45, 45)
        self.__btn_Quit.setToolTip('关闭')

        self.__btn_eraser = QPushButton()
        self.__btn_eraser.setParent(self)
        self.__btn_eraser.clicked.connect(self.on_btn_eraser_clicked)
        self.__btn_eraser.move(913, 522)
        self.__btn_eraser.resize(39, 39)
        self.__btn_eraser.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_pen.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/button_pen_hover.png)}"
                                        "QPushButton:pressed{border-image: url(./UI/icons/button_eraser_pressed.png)}")
        self.__btn_eraser.setToolTip('切换橡皮')

        self.__btn_undo = QPushButton()
        self.__btn_undo.setParent(self)  # 设置父对象为本界面
        self.__btn_undo.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_undo.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/button_undo_hover.png)}"
                                      "QPushButton:pressed{border-image: url(./UI/icons/button_undo_pressed.png)}")
        self.__btn_undo.clicked.connect(self.__paintBoard.undo)
        self.__btn_undo.move(955, 522)
        self.__btn_undo.resize(39, 39)
        self.__btn_undo.setToolTip('撤销')

        self.__btn_redo = QPushButton()
        self.__btn_redo.setParent(self)  # 设置父对象为本界面
        self.__btn_redo.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_redo.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/button_redo_hover.png)}"
                                      "QPushButton:pressed{border-image: url(./UI/icons/button_redo_pressed.png)}")
        self.__btn_redo.clicked.connect(self.__paintBoard.redo)
        self.__btn_redo.move(997, 522)
        self.__btn_redo.resize(39, 39)
        self.__btn_redo.setToolTip('重做')

        self.__btn_up = QPushButton()
        self.__btn_up.setParent(self)  # 设置父对象为本界面
        self.__btn_up.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_up.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/button_up_hover.png)}"
                                    "QPushButton:pressed{border-image: url(./UI/icons/button_up_pressed.png)}")
        self.__btn_up.clicked.connect(self.on_btn_up_clicked)
        self.__btn_up.move(1039, 522)
        self.__btn_up.resize(39, 39)
        self.__btn_up.setToolTip('上传文件')

        self.__btn_Clear = QPushButton()
        self.__btn_Clear.setParent(self)  # 设置父对象为本界面
        self.__btn_Clear.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_clear.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/button_clear_hover.png)}"
                                       "QPushButton:pressed{border-image: url(./UI/icons/button_clear_pressed.png)}")
        self.__btn_Clear.clicked.connect(self.__paintBoard.clear)
        self.__btn_Clear.move(1081, 522)
        self.__btn_Clear.resize(39, 39)
        self.__btn_Clear.setToolTip('清空画板')

        self.__btn_Save = QPushButton()
        self.__btn_Save.setParent(self)
        self.__btn_Save.clicked.connect(self.on_btn_save_clicked)
        self.__btn_Save.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_save.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/button_save_hover.png)}"
                                      "QPushButton:pressed{border-image: url(./UI/icons/button_save_pressed.png)}")
        self.__btn_Save.move(1123, 522)
        self.__btn_Save.resize(39, 39)
        self.__btn_Save.setToolTip('保存画板')

        self.__btn_save_all = QPushButton()
        self.__btn_save_all.setParent(self)
        self.__btn_save_all.clicked.connect(self.on_btn_save_all_clicked)
        self.__btn_save_all.setStyleSheet("QPushButton{border-image: url(./UI/icons/download.png)}"
                                          "QPushButton:hover{border-image: url(./UI/icons/download_hover.png)}")
        self.__btn_save_all.move(80, 670)
        self.__btn_save_all.resize(42, 38)
        self.__btn_save_all.setToolTip('保存选中图片')

        self.__btn_eye = QPushButton()
        self.__btn_eye.setParent(self)  # 设置父对象为本界面
        self.__btn_eye.setStyleSheet("QPushButton{border-image: url(./UI/icons/eye.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/eye_hover.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/eye_pressed.png)}")
        self.__btn_eye.clicked.connect(self.on_btn_line_clicked)
        self.__btn_eye.move(1125, 568)
        self.__btn_eye.resize(35, 35)
        self.__btn_eye.setToolTip('线条化图片')

        self.__btn_search = QPushButton()
        self.__btn_search.setParent(self)  # 设置父对象为本界面
        self.__btn_search.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_search.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/button_search_hover.png)}"
                                        "QPushButton:pressed{border-image: url(./UI/icons/button_search_pressed.png)}")
        self.__btn_search.clicked.connect(self.on_btn_search_clicked)
        self.__btn_search.move(1123, 607)
        self.__btn_search.resize(39, 39)
        self.__btn_search.setToolTip('查找图片')

        # 画笔
        self.__btn_small = QPushButton()
        self.__btn_small.setParent(self)
        self.__btn_small.clicked.connect(self.on_btn_small_clicked)
        self.__btn_small.move(787, 528)
        self.__btn_small.resize(30, 30)
        self.__btn_small.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_small.png)}"
                                       "QPushButton:pressed{border-image: url(./UI/icons/button_small_pressed.png)}")
        self.__btn_small.setToolTip('画笔粗细 - 细')

        self.__btn_mid = QPushButton()
        self.__btn_mid.setParent(self)
        self.__btn_mid.clicked.connect(self.on_btn_mid_clicked)
        self.__btn_mid.move(817, 528)
        self.__btn_mid.resize(30, 30)
        self.__btn_mid.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_mid_selected.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_mid_pressed.png)}")
        self.__btn_mid.setToolTip('画笔粗细 - 中')

        self.__btn_big = QPushButton()
        self.__btn_big.setParent(self)
        self.__btn_big.clicked.connect(self.on_btn_big_clicked)
        self.__btn_big.move(852, 528)
        self.__btn_big.resize(30, 30)
        self.__btn_big.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_big.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_big_pressed.png)}")
        self.__btn_big.setToolTip('画笔粗细 - 粗')

        # 颜色框
        self.__btn_black = QPushButton()
        self.__btn_black.setParent(self)
        self.__btn_black.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_black.clicked.connect(self.on_btn_black_clicked)
        self.__btn_black.move(809, 565)
        self.__btn_black.resize(41, 41)

        self.__btn_gray = QPushButton()
        self.__btn_gray.setParent(self)
        self.__btn_gray.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_gray.clicked.connect(self.on_btn_gray_clicked)
        self.__btn_gray.move(850, 565)
        self.__btn_gray.resize(41, 41)

        self.__btn_brown = QPushButton()
        self.__btn_brown.setParent(self)
        self.__btn_brown.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_brown.clicked.connect(self.on_btn_brown_clicked)
        self.__btn_brown.move(892, 565)
        self.__btn_brown.resize(41, 41)

        self.__btn_khaki = QPushButton()
        self.__btn_khaki.setParent(self)
        self.__btn_khaki.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_khaki.clicked.connect(self.on_btn_khaki_clicked)
        self.__btn_khaki.move(932, 565)
        self.__btn_khaki.resize(41, 41)

        self.__btn_wheat = QPushButton()
        self.__btn_wheat.setParent(self)
        self.__btn_wheat.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_wheat.clicked.connect(self.on_btn_wheat_clicked)
        self.__btn_wheat.move(974, 565)
        self.__btn_wheat.resize(41, 41)

        self.__btn_yellow = QPushButton()
        self.__btn_yellow.setParent(self)
        self.__btn_yellow.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_yellow.clicked.connect(self.on_btn_yellow_clicked)
        self.__btn_yellow.move(1015, 565)
        self.__btn_yellow.resize(41, 41)

        self.__btn_pink = QPushButton()
        self.__btn_pink.setParent(self)
        self.__btn_pink.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_pink.clicked.connect(self.on_btn_pink_clicked)
        self.__btn_pink.move(1056, 565)
        self.__btn_pink.resize(41, 41)

        self.__btn_white = QPushButton()
        self.__btn_white.setParent(self)
        self.__btn_white.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_white.clicked.connect(self.on_btn_white_clicked)
        self.__btn_white.move(809, 606)
        self.__btn_white.resize(41, 41)

        self.__btn_red = QPushButton()
        self.__btn_red.setParent(self)
        self.__btn_red.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_red.clicked.connect(self.on_btn_red_clicked)
        self.__btn_red.move(850, 606)
        self.__btn_red.resize(41, 41)

        self.__btn_purple = QPushButton()
        self.__btn_purple.setParent(self)
        self.__btn_purple.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_purple.clicked.connect(self.on_btn_purple_clicked)
        self.__btn_purple.move(892, 606)
        self.__btn_purple.resize(41, 41)

        self.__btn_sapphire = QPushButton()
        self.__btn_sapphire.setParent(self)
        self.__btn_sapphire.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                          "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_sapphire.clicked.connect(self.on_btn_sapphire_clicked)
        self.__btn_sapphire.move(932, 606)
        self.__btn_sapphire.resize(41, 41)

        self.__btn_blue = QPushButton()
        self.__btn_blue.setParent(self)
        self.__btn_blue.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_blue.clicked.connect(self.on_btn_blue_clicked)
        self.__btn_blue.move(974, 606)
        self.__btn_blue.resize(41, 41)

        self.__btn_sky = QPushButton()
        self.__btn_sky.setParent(self)
        self.__btn_sky.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_sky.clicked.connect(self.on_btn_sky_clicked)
        self.__btn_sky.move(1015, 606)
        self.__btn_sky.resize(41, 41)

        self.__btn_green = QPushButton()
        self.__btn_green.setParent(self)
        self.__btn_green.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_green.clicked.connect(self.on_btn_green_clicked)
        self.__btn_green.move(1056, 606)
        self.__btn_green.resize(41, 41)

        self.__btn_left = QPushButton()
        self.__btn_left.setParent(self)
        self.__btn_left.setStyleSheet("QPushButton{border-image: url(./UI/icons/left.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/left_hover.png)}"
                                      "QPushButton:pressed{border-image: url(./UI/icons/left_pressed.png)}")
        self.__btn_left.clicked.connect(self.on_btn_left_clicked)
        self.__btn_left.move(185, 655)
        self.__btn_left.resize(65, 65)
        self.__btn_left.setToolTip('上一页')

        self.__more_1 = QLabel(self)
        self.__more_1.setStyleSheet("QLabel{border-image: url(./UI/numbers/more.png)}")
        self.__more_1.move(285, 685)
        self.__more_1.resize(25, 4)
        self.__more_1.setVisible(False)

        self.__btn_one = QPushButton()
        self.__btn_one.setParent(self)
        self.__btn_one.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}")
        self.__btn_one.clicked.connect(self.on_btn_left_clicked)
        self.__btn_one.move(334, 678)
        self.__btn_one.resize(18, 17)

        self.__dot = QLabel(self)
        self.__dot.setStyleSheet("QLabel{border-image: url(./UI/numbers/down.png)}")
        self.__dot.move(379, 678)
        self.__dot.resize(18, 17)

        self.__btn_two = QPushButton()
        self.__btn_two.setParent(self)
        self.__btn_two.setStyleSheet("QPushButton{border-image: url(./UI/numbers/1.png)}")
        self.__btn_two.move(379, 678)
        self.__btn_two.resize(18, 18)

        self.__btn_three = QPushButton()
        self.__btn_three.setParent(self)
        self.__btn_three.setStyleSheet("QPushButton{border-image: url(./UI/numbers/2.png)}")
        self.__btn_three.clicked.connect(self.on_btn_right_clicked)
        self.__btn_three.move(424, 678)
        self.__btn_three.resize(18, 17)

        self.__more_2 = QLabel(self)
        self.__more_2.setStyleSheet("QLabel{border-image: url(./UI/numbers/more.png)}")
        self.__more_2.move(465, 685)
        self.__more_2.resize(25, 4)
        self.__more_2.setVisible(True)

        self.__btn_right = QPushButton()
        self.__btn_right.setParent(self)
        self.__btn_right.setStyleSheet("QPushButton{border-image: url(./UI/icons/right.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/right_hover.png)}"
                                       "QPushButton:pressed{border-image: url(./UI/icons/right_pressed.png)}")
        self.__btn_right.clicked.connect(self.on_btn_right_clicked)
        self.__btn_right.move(525, 655)
        self.__btn_right.resize(65, 65)
        self.__btn_right.setToolTip('下一页')

        self.refresh()

    def on_btn_left_clicked(self):
        if self.__number > 0:
            self.__number -= 1
            file_list = self.__files[0 + self.__number * 12: 12 + self.__number * 12]
            self.load(file_list)

    def on_btn_right_clicked(self):
        length = len(self.__files)
        if (self.__number + 2) * 12 < length:
            self.__number += 1
            file_list = self.__files[0 + self.__number * 12: 12 + self.__number * 12]
            self.load(file_list)
        elif (self.__number + 1) * 12 < length:
            self.__number += 1
            file_list = []
            for i in range(length - self.__number * 12):
                file_list.append(self.__files[self.__number * 12 + i])
            self.load(file_list)

    def refresh(self):
        self.reset_select()
        self.__files = self.__pic_files
        self.__number = 0
        self.__is_searched = False
        random.shuffle(self.__files)
        file_list = self.__files[0 + self.__number * 12: 12 + self.__number * 12]
        self.load(file_list)

    def load(self, file_list):
        self.reset_select()
        if self.__number == 0:
            self.__btn_one.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}")
        elif self.__number > 0:
            self.__btn_one.setStyleSheet("QPushButton{border-image: url(./UI/numbers/" + str(self.__number) + ".png)}")
        self.__btn_two.setStyleSheet("QPushButton{border-image: url(./UI/numbers/" + str(self.__number + 1) + ".png)}")
        if self.__number <= 1:
            self.__more_1.setVisible(False)
        else:
            self.__more_1.setVisible(True)
        if (self.__number + 2) * 12 >= len(self.__files):
            self.__more_2.setVisible(False)
        else:
            self.__more_2.setVisible(True)
        if (self.__number + 1) * 12 < len(self.__files):
            self.__btn_three.setStyleSheet("QPushButton"
                                           "{border-image: url(./UI/numbers/" + str(self.__number + 2) + ".png)}")
        elif self.__number * 12 < len(self.__files):
            self.__btn_three.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}")

        length = len(file_list)
        self.__now_files = file_list
        if length >= 12:
            self.__pic_12.load("./pictures/" + file_list[11])
            self.__label_12.setPixmap(self.__pic_12)
            length = 11
        else:
            self.__pic_12.load("./UI/icons/nothing.png")
            self.__label_12.setPixmap(self.__pic_12)
        if length == 11:
            self.__pic_11.load("./pictures/" + file_list[10])
            self.__label_11.setPixmap(self.__pic_11)
            length = 10
        else:
            self.__label_11.setPixmap(self.__pic_12)
        if length == 10:
            self.__pic_10.load("./pictures/" + file_list[9])
            self.__label_10.setPixmap(self.__pic_10)
            length = 9
        else:
            self.__label_10.setPixmap(self.__pic_12)
        if length == 9:
            self.__pic_9.load("./pictures/" + file_list[8])
            self.__label_9.setPixmap(self.__pic_9)
            length = 8
        else:
            self.__label_9.setPixmap(self.__pic_12)
        if length == 8:
            self.__pic_8.load("./pictures/" + file_list[7])
            self.__label_8.setPixmap(self.__pic_8)
            length = 7
        else:
            self.__label_8.setPixmap(self.__pic_12)
        if length == 7:
            self.__pic_7.load("./pictures/" + file_list[6])
            self.__label_7.setPixmap(self.__pic_7)
            length = 6
        else:
            self.__label_7.setPixmap(self.__pic_12)
        if length == 6:
            self.__pic_6.load("./pictures/" + file_list[5])
            self.__label_6.setPixmap(self.__pic_6)
            length = 5
        else:
            self.__label_6.setPixmap(self.__pic_12)
        if length == 5:
            self.__pic_5.load("./pictures/" + file_list[4])
            self.__label_5.setPixmap(self.__pic_5)
            length = 4
        else:
            self.__label_5.setPixmap(self.__pic_12)
        if length == 4:
            self.__pic_4.load("./pictures/" + file_list[3])
            self.__label_4.setPixmap(self.__pic_4)
            length = 3
        else:
            self.__label_4.setPixmap(self.__pic_12)
        if length == 3:
            self.__pic_3.load("./pictures/" + file_list[2])
            self.__label_3.setPixmap(self.__pic_3)
            length = 2
        else:
            self.__label_3.setPixmap(self.__pic_12)
        if length == 2:
            self.__pic_2.load("./pictures/" + file_list[1])
            self.__label_2.setPixmap(self.__pic_2)
            length = 1
        else:
            self.__label_2.setPixmap(self.__pic_12)
        if length == 1:
            self.__pic_1.load("./pictures/" + file_list[0])
            self.__label_1.setPixmap(self.__pic_1)
        else:
            self.__label_1.setPixmap(self.__pic_12)

    def on_btn_see_clicked(self):
        if self.__see == 1:
            self.__see = 0.85
            self.setWindowOpacity(self.__see)
        elif self.__see == 0.85:
            self.__see = 0.70
            self.setWindowOpacity(self.__see)
        elif self.__see == 0.70:
            self.__see = 0.55
            self.setWindowOpacity(self.__see)
        elif self.__see == 0.55:
            self.__see = 1
            self.setWindowOpacity(self.__see)

    def on_btn_small_clicked(self):
        self.__btn_small.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_small_selected.png)}"
                                       "QPushButton:pressed{border-image: url(./UI/icons/button_small_pressed.png)}")
        self.__btn_mid.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_mid.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_mid_pressed.png)}")
        self.__btn_big.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_big.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_big_pressed.png)}")
        pen_thickness = 3
        self.__paintBoard.change_pen_thickness(pen_thickness)

    def on_btn_mid_clicked(self):
        self.__btn_small.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_small.png)}"
                                       "QPushButton:pressed{border-image: url(./UI/icons/button_small_pressed.png)}")
        self.__btn_mid.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_mid_selected.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_mid_pressed.png)}")
        self.__btn_big.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_big.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_big_pressed.png)}")
        pen_thickness = 6
        self.__paintBoard.change_pen_thickness(pen_thickness)

    def on_btn_big_clicked(self):
        self.__btn_small.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_small.png)}"
                                       "QPushButton:pressed{border-image: url(./UI/icons/button_small_pressed.png)}")
        self.__btn_mid.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_mid.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_mid_pressed.png)}")
        self.__btn_big.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_big_selected.png)}"
                                     "QPushButton:pressed{border-image: url(./UI/icons/button_big_pressed.png)}")
        pen_thickness = 9
        self.__paintBoard.change_pen_thickness(pen_thickness)

    def on_btn_up_clicked(self):
        open_path = QFileDialog.getOpenFileName(self, 'Choose Your Paint', '.\\', 'picture files(*.jpg;*.png)')
        # print(open_path)
        if open_path[0] == "":
            print("Save cancel")
            return
        image = QPixmap(open_path[0]).scaled(350, 350)
        self.__paintBoard.up(image)

    def on_btn_save_clicked(self):
        save_path = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\', 'picture files(*.jpg;*.png)')
        # print(save_path)
        if save_path[0] == "":
            print("Save cancel")
            return
        image = self.__paintBoard.get_content_as_image()
        image.save(save_path[0])

    def on_btn_line_clicked(self):
        self.__paintBoard.get_content_as_image().save("./temp/tmp.png")
        do_image()
        self.__paintBoard.up(QPixmap("./temp/line.png").scaled(350, 350))

    def on_btn_search_clicked(self):
        self.__color = "null"
        self.reset_color_btn()
        self.reset_select()
        self.__paintBoard.get_content_as_image().save("./temp/tmp.png")
        do_image()
        self.__number = 0
        self.__is_searched = True
        self.__search_files = compare_image()
        self.__files = self.__search_files
        self.load(self.__files)

    def on_btn_eraser_clicked(self):
        if self.__paintBoard.eraser_mode:
            self.__paintBoard.eraser_mode = False  # 退出橡皮擦模式
            self.__btn_eraser.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_pen.png)}"
                                            "QPushButton:hover{border-image: url(./UI/icons/button_pen_hover.png)}"
                                            "QPushButton:pressed"
                                            "{border-image: url(./UI/icons /button_eraser_pressed.png)}")
            self.__btn_eraser.setToolTip('切换橡皮')
        else:
            self.__paintBoard.eraser_mode = True  # 进入橡皮擦模式
            self.__btn_eraser.setStyleSheet("QPushButton{border-image: url(./UI/icons/button_eraser_pressed.png)}"
                                            "QPushButton:hover{border-image: url(./UI/icons/button_eraser_hover.png)}"
                                            "QPushButton:pressed{border-image: url(./UI/icons/button_pen_pressed.png)}")
            self.__btn_eraser.setToolTip('切换画笔')

    def reset_select(self):
        self.__select = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.__btn_1.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_2.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_3.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_4.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_5.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_6.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_7.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_8.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_9.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                   "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_10.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_11.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
        self.__btn_12.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                    "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")

    def reset_color_btn(self):
        self.__btn_black.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_gray.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_brown.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_khaki.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_wheat.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_yellow.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_pink.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_white.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_red.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_purple.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_sapphire.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                          "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_blue.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                      "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_sky.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                     "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
        self.__btn_green.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/border.png)}")

    def on_btn_black_clicked(self):
        self.__number = 0
        if self.__color == "black":
            self.__btn_black.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "black"
            self.reset_color_btn()
            self.__btn_black.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.black_files)))
                self.load(self.__files)
            else:
                self.__files = data.black_files
                self.load(self.__files)

    def on_btn_gray_clicked(self):
        self.__number = 0
        if self.__color == "gray":
            self.__btn_gray.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "gray"
            self.reset_color_btn()
            self.__btn_gray.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.gray_files)))
                self.load(self.__files)
            else:
                self.__files = data.gray_files
                self.load(self.__files)

    def on_btn_brown_clicked(self):
        self.__number = 0
        if self.__color == "brown":
            self.__btn_brown.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "brown"
            self.reset_color_btn()
            self.__btn_brown.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.brown_files)))
                self.load(self.__files)
            else:
                self.__files = data.brown_files
                self.load(self.__files)

    def on_btn_khaki_clicked(self):
        self.__number = 0
        if self.__color == "khaki":
            self.__btn_khaki.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "khaki"
            self.reset_color_btn()
            self.__btn_khaki.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.khaki_files)))
                self.load(self.__files)
            else:
                self.__files = data.khaki_files
                self.load(self.__files)

    def on_btn_wheat_clicked(self):
        self.__number = 0
        if self.__color == "wheat":
            self.__btn_wheat.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "wheat"
            self.reset_color_btn()
            self.__btn_wheat.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_dark.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.wheat_files)))
                self.load(self.__files)
            else:
                self.__files = data.wheat_files
                self.load(self.__files)

    def on_btn_yellow_clicked(self):
        self.__number = 0
        if self.__color == "yellow":
            self.__btn_yellow.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                            "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "yellow"
            self.reset_color_btn()
            self.__btn_yellow.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_dark.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.yellow_files)))
                self.load(self.__files)
            else:
                self.__files = data.yellow_files
                self.load(self.__files)

    def on_btn_pink_clicked(self):
        self.__number = 0
        if self.__color == "pink":
            self.__btn_pink.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                          "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "pink"
            self.reset_color_btn()
            self.__btn_pink.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.pink_files)))
                self.load(self.__files)
            else:
                self.__files = data.pink_files
                self.load(self.__files)

    def on_btn_white_clicked(self):
        self.__number = 0
        if self.__color == "white":
            self.__btn_white.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "white"
            self.reset_color_btn()
            self.__btn_white.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_dark.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.white_files)))
                self.load(self.__files)
            else:
                self.__files = data.white_files
                self.load(self.__files)

    def on_btn_red_clicked(self):
        self.__number = 0
        if self.__color == "red":
            self.__btn_red.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                         "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "red"
            self.reset_color_btn()
            self.__btn_red.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.red_files)))
                self.load(self.__files)
            else:
                self.__files = data.red_files
                self.load(self.__files)

    def on_btn_purple_clicked(self):
        self.__number = 0
        if self.__color == "purple":
            self.__btn_purple.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                            "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "purple"
            self.reset_color_btn()
            self.__btn_purple.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.purple_files)))
                self.load(self.__files)
            else:
                self.__files = data.purple_files
                self.load(self.__files)

    def on_btn_sapphire_clicked(self):
        self.__number = 0
        if self.__color == "sapphire":
            self.__btn_sapphire.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                              "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "sapphire"
            self.reset_color_btn()
            self.__btn_sapphire.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.sapphire_files)))
                self.load(self.__files)
            else:
                self.__files = data.sapphire_files
                self.load(self.__files)

    def on_btn_blue_clicked(self):
        self.__number = 0
        if self.__color == "blue":
            self.__btn_blue.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                          "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "blue"
            self.reset_color_btn()
            self.__btn_blue.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.blue_files)))
                self.load(self.__files)
            else:
                self.__files = data.blue_files
                self.load(self.__files)

    def on_btn_sky_clicked(self):
        self.__number = 0
        if self.__color == "sky":
            self.__btn_sky.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                         "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "sky"
            self.reset_color_btn()
            self.__btn_sky.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.sky_files)))
                self.load(self.__files)
            else:
                self.__files = data.sky_files
                self.load(self.__files)

    def on_btn_green_clicked(self):
        self.__number = 0
        if self.__color == "green":
            self.__btn_green.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                           "QPushButton:hover{border-image: url(./UI/icons/border.png)}")
            self.__color = "null"
            if self.__is_searched:
                self.__files = self.__search_files
                self.load(self.__files)
            else:
                self.refresh()
        else:
            self.__color = "green"
            self.reset_color_btn()
            self.__btn_green.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick_light.png)}")
            if self.__is_searched:
                self.__files = list(set(self.__search_files).intersection(set(data.green_files)))
                self.load(self.__files)
            else:
                self.__files = data.green_files
                self.load(self.__files)

    def on_btn_1_clicked(self):
        if self.__select[0]:
            self.__btn_1.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[0] = False
        else:
            self.__btn_1.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_1.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[0] = True

    def on_btn_2_clicked(self):
        if self.__select[1]:
            self.__btn_2.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[1] = False
        else:
            self.__btn_2.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_2.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[1] = True

    def on_btn_3_clicked(self):
        if self.__select[2]:
            self.__btn_3.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[2] = False
        else:
            self.__btn_3.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_3.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[2] = True

    def on_btn_4_clicked(self):
        if self.__select[3]:
            self.__btn_4.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[3] = False
        else:
            self.__btn_4.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_4.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[3] = True

    def on_btn_5_clicked(self):
        if self.__select[4]:
            self.__btn_5.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[4] = False
        else:
            self.__btn_5.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_5.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[4] = True

    def on_btn_6_clicked(self):
        if self.__select[5]:
            self.__btn_6.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[5] = False
        else:
            self.__btn_6.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_6.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[5] = True

    def on_btn_7_clicked(self):
        if self.__select[6]:
            self.__btn_7.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[6] = False
        else:
            self.__btn_7.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_7.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[6] = True

    def on_btn_8_clicked(self):
        if self.__select[7]:
            self.__btn_8.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[7] = False
        else:
            self.__btn_8.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_8.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[7] = True

    def on_btn_9_clicked(self):
        if self.__select[8]:
            self.__btn_9.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                       "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[8] = False
        else:
            self.__btn_9.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_9.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[8] = True

    def on_btn_10_clicked(self):
        if self.__select[9]:
            self.__btn_10.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[9] = False
        else:
            self.__btn_10.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_10.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[9] = True

    def on_btn_11_clicked(self):
        if self.__select[10]:
            self.__btn_11.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[10] = False
        else:
            self.__btn_11.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_11.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[10] = True

    def on_btn_12_clicked(self):
        if self.__select[11]:
            self.__btn_12.setStyleSheet("QPushButton{border-image: url(./UI/icons/nothing.png)}"
                                        "QPushButton:hover{border-image: url(./UI/icons/tick_hover.png)}")
            self.__select[11] = False
        else:
            self.__btn_12.setStyleSheet("QPushButton{border-image: url(./UI/icons/tick.png)}")
            image = self.__label_12.pixmap().scaled(350, 350)
            self.__paintBoard.up(image)
            self.__select[11] = True

    def on_btn_save_all_clicked(self):
        save_path = QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
        print(save_path)
        if save_path == "":
            print("Save cancel")
            return
        for i in range(len(self.__now_files)):
            if self.__select[i]:
                image = QPixmap("./pictures/" + self.__now_files[i])
                image.save(save_path + "/" + self.__now_files[i])
        self.reset_select()

    def mousePressEvent(self, event):
        self.m_Position = event.globalPos() - self.pos()
        if event.button() == Qt.LeftButton and self.m_Position.x() < 575 and self.m_Position.y() < 90:
            self.m_flag = True  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        else:
            self.__paintBoard.mouse_press_event(event)

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)  # 更改窗口位置
            event.accept()
        else:
            self.__paintBoard.mouse_move_event(event)

    def mouseReleaseEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.m_flag = False
            self.setCursor(QCursor(Qt.ArrowCursor))
        else:
            self.__paintBoard.mouse_release_event(event)
