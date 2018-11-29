from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMenu, QMenuBar, QDockWidget
from PyQt5.QtGui import QIcon
from os import walk

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowIcon(QIcon('totalcmd.png'))
        self.setWindowTitle("Total Commander")
        mainMenu = self.menuBar() 
        filesMenu = mainMenu.addMenu('Files')
        marksMenu = mainMenu.addMenu('Mark')
        commandsMenu = mainMenu.addMenu('Commands')
        netMenu = mainMenu.addMenu('Net')
        showMenu = mainMenu.addMenu('Show')
        configurationMenu = mainMenu.addMenu('Configuration')
        startMenu = mainMenu.addMenu('Start')

        exitAct = QtWidgets.QAction(QIcon('refresh.png'), 'Exit', self)
        gridAct = QtWidgets.QAction(QIcon('grid.png'), 'Grid', self)
        listAct = QtWidgets.QAction(QIcon('list.png'), 'List', self)
        self.toolbar = self.addToolBar('ToolBar')
        self.toolbar.addAction(exitAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(gridAct)
        self.toolbar.addAction(listAct)

        mid = Mid()
        self.setCentralWidget(mid)
        
        self.show()

class Mid(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Mid, self).__init__(parent)
        mainLayout = QtWidgets.QVBoxLayout()
        bottom = Bottom()
        listsOfFiles = ListsOfFiles()
        mainLayout.addWidget(listsOfFiles)
        mainLayout.addWidget(bottom)
        self.setLayout(mainLayout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored,
                           QtWidgets.QSizePolicy.Preferred)
        

class ListsOfFiles(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ListsOfFiles, self).__init__(parent)
        mainLayout = QtWidgets.QHBoxLayout()
        list1 = QtWidgets.QListWidget()
        list2 = QtWidgets.QListWidget()
        f = []
        myfilenames = []
        preparedfilenames = []
        mydirnames = []
        prepareddirnames = []
        for (dirpath, dirnames, filenames) in walk("C:/"):
            myfilenames = filenames
            mydirnames = dirnames
            break
        for filename in myfilenames:
            filename = 'f ' + filename
            preparedfilenames.append(filename)
        print(myfilenames)
        for dirname in mydirnames:
            dirname = 'd ' + dirname
            prepareddirnames.append(dirname)
        f.extend(prepareddirnames)
        f.extend(preparedfilenames)
        
        list1.addItems(f)
        list2.addItems(f)
        mainLayout.addWidget(list1)
        mainLayout.addWidget(list2)
        self.setLayout(mainLayout)

class Bottom(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Bottom, self).__init__(parent)
        mainLayout = QtWidgets.QHBoxLayout()
        viewButton = Button('F3 View')
        editButton = Button('F4 Edit')
        copyButton = Button('F5 Copy')
        moveButton = Button('F6 Move')
        newFolderButton = Button('F7 NewFolder')
        deleteButton = Button('F8 Delete')
        exitButton = Button('Alt+F4 Exit')
        mainLayout.addWidget(viewButton)
        mainLayout.addWidget(editButton)
        mainLayout.addWidget(copyButton)
        mainLayout.addWidget(moveButton)
        mainLayout.addWidget(newFolderButton)
        mainLayout.addWidget(deleteButton)
        mainLayout.addWidget(exitButton)
        self.setLayout(mainLayout)

class Button(QtWidgets.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Fixed)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
