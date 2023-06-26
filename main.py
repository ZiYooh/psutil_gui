import psutil
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt


def get_size_bytes(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


def get_size_bps(bytes):
    bytes *= 8
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}bps"
        bytes /= 1024


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(380, 270)
        MainWindow.setFixedSize(380, 250)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cpuUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.cpuUsageLabel.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.cpuUsageLabel.setFont(font)
        self.cpuUsageLabel.setObjectName("cpuUsageLabel")
        self.memUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.memUsageLabel.setGeometry(QtCore.QRect(10, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.memUsageLabel.setFont(font)
        self.memUsageLabel.setObjectName("memUsageLabel")
        self.cpuPercent = QtWidgets.QProgressBar(self.centralwidget)
        self.cpuPercent.setGeometry(QtCore.QRect(150, 20, 221, 23))
        self.cpuPercent.setProperty("value", 24)
        self.cpuPercent.setObjectName("cpuPercent")
        self.memPercent = QtWidgets.QProgressBar(self.centralwidget)
        self.memPercent.setGeometry(QtCore.QRect(150, 60, 221, 23))
        self.memPercent.setProperty("value", 24)
        self.memPercent.setObjectName("memPercent")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.networkUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkUsageLabel.setGeometry(QtCore.QRect(150, 100, 71, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkUsageLabel.setFont(font)
        self.networkUsageLabel.setObjectName("networkUsageLabel")
        self.networkSentLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkSentLabel.setGeometry(QtCore.QRect(60, 130, 51, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkSentLabel.setFont(font)
        self.networkSentLabel.setObjectName("networkSentLabel")
        self.networkRecvLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkRecvLabel.setGeometry(QtCore.QRect(270, 130, 41, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkRecvLabel.setFont(font)
        self.networkRecvLabel.setObjectName("networkRecvLabel")
        self.networkSentBps = QtWidgets.QLabel(self.centralwidget)
        self.networkSentBps.setGeometry(QtCore.QRect(55, 170, 120, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkSentBps.setFont(font)
        self.networkSentBps.setObjectName("networkSentBps")
        self.networkRecvBps = QtWidgets.QLabel(self.centralwidget)
        self.networkRecvBps.setGeometry(QtCore.QRect(255, 170, 120, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkRecvBps.setFont(font)
        self.networkRecvBps.setObjectName("networkRecvBps")

        self.aotCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.aotCheckBox.setGeometry(QtCore.QRect(10, 210, 101, 16))
        self.aotCheckBox.setObjectName("aotCheckBox")
        self.aotCheckBox.stateChanged.connect(self.change_always_on_top)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.timer = QTimer()  # timer 변수에 QTimer 할당
        self.timer.start(1000)  # 1000msec(1sec) 마다 반복
        self.timer.timeout.connect(self.update_info)  # start time out시 연결할 함수

        # 창 항상 위에 유지 일단 영구적으로 임시 적용
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cpuUsageLabel.setText(_translate("MainWindow", "CPU 사용량"))
        self.memUsageLabel.setText(_translate("MainWindow", "메모리 사용량"))
        self.networkUsageLabel.setText(_translate("MainWindow", "네트워크"))
        self.networkSentLabel.setText(_translate("MainWindow", "보내기"))
        self.networkRecvLabel.setText(_translate("MainWindow", "받기"))
        self.networkSentBps.setText(_translate("MainWindow", "0"))
        self.networkRecvBps.setText(_translate("MainWindow", "0"))
        self.aotCheckBox.setText(_translate("MainWindow", "창 항상 위에"))

    def update_info(self):
        io = psutil.net_io_counters()
        bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
        # CPU
        cpu_ = psutil.cpu_percent()

        # Memory
        memory_ = psutil.virtual_memory()

        # network
        io_2 = psutil.net_io_counters()
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

        dict_example = {
            'cpu': f"{cpu_}",
            'memory_percent': f"{memory_.percent}",
            'network_upload_speed': f"{get_size_bps(us)}",
            'network_download_speed': f"{get_size_bps(ds)}"
        }
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
        # print(int(float(dict_example['cpu'])))

        self.cpuPercent.setValue(int(float(dict_example['cpu'])))
        self.memPercent.setValue(int(float(dict_example['memory_percent'])))

        self.networkSentBps.setText(dict_example['network_upload_speed'])
        self.networkRecvBps.setText(dict_example['network_download_speed'])
        # self.cpuPercent.repaint()

    def change_always_on_top(self, state):
        if state == Qt.Checked:
            # MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            print('test1')
        else:
            # MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            print('test2')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
