__author__ = 'Aether'
# -*- coding: UTF8 -*-
from PyQt4 import QtCore, QtGui,uic
import sys, os,math ,time
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#预设值######################
Image_Width = 100
Image_Height = 100
Image_Min = 0
Image_Max = 256
FILE_TYPE = ['jpg', 'jpeg', 'tif', 'bmp', 'gif','exr']
#################################################

qtCreatorFile = "HDRI studio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.closebutton.clicked.connect(quit)
        self.closebutton.setIcon(QIcon("close.png"))
        #self.setWindowFlags(Qt.FramelessWindowHint) ################隐藏窗口
        self.imagepath = "D:\VFX"    #####################默认文件夹
        self.imagesize.valueChanged.connect(self.changeValue)  ############滑块
        self.action.clicked.connect(self.openFile)
        self.action.setShortcut('Ctrl+R')
        self.imagesize.setMinimum(Image_Min)
        self.imagesize.setMaximum(Image_Max)
        self.List.clicked.connect(self.display)#############
        #self.List.clicked.connect(self.myListWidgetContext)
        self.List.customContextMenuRequested[QtCore.QPoint].connect(self.myListWidgetContext)
        self.setStyleSheet("background-color:#2B2B2B;")
        #self.List.setViewMode(QListView.IconMode)   #显示模式：图标模式
        self.List.setIconSize(QSize(Image_Width,Image_Height*0.9))   #图标大小
        self.List.setGridSize(QSize(Image_Width,Image_Height))   #格子大小
        self.List.setStyleSheet("background-color:#2B2B2B;"
                                "color: rgb(255, 255, 255);")
        #self.List.setMaximumWidth(800)  # 最大宽度
        #self.List.setSelectionMode(0)   #选择模式：0无法选择
        self.List.setMovement(QtGui.QListView.Static)#设置图片不可移动
        self.List.setSpacing(10)#设置图片间距为10
        #self.List.setCurrentRow(10)
        #self.List.setSortingEnabled(0)
        #self.List.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)#单选
        ###################################################################################################默认加载GIF图
        # self.movie = QMovie(r"D:\参考图\乌鸦\14-4-39-11-11-27137.gif", QByteArray(), self)
        # self.movie.setCacheMode(QMovie.CacheAll)
        # self.movie.setSpeed(100)
        # self.pics.setMovie(self.movie)
        # self.movie.start()
        """特效种类列表###################################################################################################"""
        self.fxtype.setIconSize(QSize(Image_Width,Image_Height*0.9))
        self.fxtype.setGridSize(QSize(Image_Width*0.5,Image_Height*0.6))
        fxitem = os.listdir(self.imagepath)
        os.chdir(self.imagepath)
        for root in fxitem:
            if(os.path.isdir(root)):
                #listItem.append(QListWidgetItem(QIcon(self.imagepath+"\\"+lst),lst,))
                configButton = QtGui.QListWidgetItem(self.fxtype)
                configButton.setIcon(QtGui.QIcon(self.imagepath+"\\"+root+"\\"+"image.ico"))
                configButton.setText(root)
        self.fxtype.clicked.connect(self.selectfx)
        self.fxtype.clicked.connect(self.opentypefile)
        """#################################################################################################"""
        item = os.listdir(self.imagepath)
        listItem = []
        for lst in item:
            item = os.listdir(self.imagepath+"\\"+lst)
            for dizhi in item:
                if not dizhi.split('.')[-1] in "ico":
                    #listItem.append(QListWidgetItem(QIcon(self.imagepath+"\\"+lst),lst,))
                    configButton = QtGui.QListWidgetItem(self.List)
                    configButton.setIcon(QtGui.QIcon(self.imagepath+"\\"+lst+"\\"+dizhi+"\image.gif"))
                    configButton.setText(dizhi)
                    #configButton.setSizeHint(QtCore.QSize(200,200))
        for i in range(len(listItem)):
            self.List.insertItem(i+1,listItem[i])


    def myListWidgetContext(self, point):
        popMenu = QtGui.QMenu()
        popMenu.addAction(QtGui.QAction(u'添加', self))
        popMenu.addAction(QtGui.QAction(u'删除', self))
        popMenu.addAction(QtGui.QAction(u'修改', self))
        popMenu.exec_(QtGui.QCursor.pos())


    def openFile(self):
        self.imagepath = QFileDialog.getExistingDirectory(self,"choose directory","D:\\")
        self.List.clear()
        item = os.listdir(self.imagepath)
        listItem = []
        for lst in item:
            if lst.split('.')[-1] in FILE_TYPE:
                listItem.append(QListWidgetItem(QIcon(self.imagepath+"\\"+lst),lst,))

        for i in range(len(listItem)):
            self.List.insertItem(i+1,listItem[i])


########################################################################################################################
    def opentypefile(self):
        self.newimagepath =self.imagepath+ "\\"+self.openfxfloder
        self.List.clear()
        item = os.listdir(self.newimagepath)
        listItem = []
        for lst in item:
            #if lst.split('.')[-1] in FILE_TYPE:
                if not lst.split('.')[-1] in "ico":
                    #listItem.append(QListWidgetItem(QIcon(self.imagepath+"\\"+lst),lst,))
                    configButton = QtGui.QListWidgetItem(self.List)
                    configButton.setIcon(QtGui.QIcon(self.newimagepath+"\\"+lst+"\preview\preview.jpg"))
                    configButton.setText(lst)
                    #configButton.setSizeHint(QtCore.QSize(200,200))
                    #label1.setAlignment(QtCore.Qt.AlignCenter)
        # for i in range(len(listItem)):
        #     self.List.insertItem(i+1,listItem[i])

########################################################################################################################
    def display(self):
        ###################################################################第一种方法
        self.List.setSelectionMode(QAbstractItemView.ExtendedSelection)
        for it in self.List.selectedItems():
            item = os.listdir(self.newimagepath)
            for dizhi in item:
                #print(self.newimagepath+"\\"+dizhi+"\preview\preview.gif")
                self.movie = QMovie(self.newimagepath+"\\"+dizhi+"\preview\preview.gif", QByteArray(), self)
                self.movie.setCacheMode(QMovie.CacheAll)
                self.movie.setSpeed(100)
                self.pics.setMovie(self.movie)
                self.movie.start()
        ###################################################################第二种方法
        # tempDict = {}
        # for item in self.List.selectedItems():
        #     tempDict[self.List.row(item)] = item
        # tempIndexes = sorted(tempDict)
        # resultItems = []
        #
        # for index in tempIndexes:
        #     resultItems.append(tempDict[index])
        #
        # for it in resultItems:
        #     print(it.text())
        #     self.movie = QMovie(self.imagepath+"\\"+it.text(), QByteArray(), self)
        #     self.movie.setCacheMode(QMovie.CacheAll)
        #     self.movie.setSpeed(100)
        #     self.pics.setMovie(self.movie)
        #     self.movie.start()
        ###################################################################
    def changeValue(self):
        pos = self.imagesize.value()+Image_Width
        self.List.setGridSize(QSize(pos,pos*0.7))
        self.List.setIconSize(QSize(pos,pos))
        self.layout()

    def selectfx(self):
        for it in self.fxtype.selectedItems():
            self.openfxfloder = it.text()

    """下面这两个才是重点，是动得关键"""
    def mousePressEvent(self,event):
       #鼠标点击事件
       if event.button() == QtCore.Qt.LeftButton:
           self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
           event.accept()

    def mouseMoveEvent(self,event):
       #鼠标移动事件
        if event.buttons() ==QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
if __name__ == "__main__":

    app=QApplication(sys.argv)
    splash=QSplashScreen(QPixmap("D:/qqw.png"))
    splash.show()
    QThread.sleep(1)
    app.processEvents()

    window = MyApp()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())