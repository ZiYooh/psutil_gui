import psutil
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt

import bg_rc

def get_size_bytes(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
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
        MainWindow.setEnabled(True)
        # MainWindow.resize(1000, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../psutil_gui/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cpuUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.cpuUsageLabel.setGeometry(QtCore.QRect(330, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.cpuUsageLabel.setFont(font)
        self.cpuUsageLabel.setObjectName("cpuUsageLabel")
        self.memUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.memUsageLabel.setGeometry(QtCore.QRect(330, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.memUsageLabel.setFont(font)
        self.memUsageLabel.setObjectName("memUsageLabel")
        self.cpuPercent = QtWidgets.QProgressBar(self.centralwidget)
        self.cpuPercent.setGeometry(QtCore.QRect(590, 140, 361, 31))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(12)
        self.cpuPercent.setFont(font)
        self.cpuPercent.setProperty("value", 24)
        self.cpuPercent.setObjectName("cpuPercent")
        self.memPercent = QtWidgets.QProgressBar(self.centralwidget)
        self.memPercent.setGeometry(QtCore.QRect(590, 202, 361, 31))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(12)
        self.memPercent.setFont(font)
        self.memPercent.setProperty("value", 24)
        self.memPercent.setObjectName("memPercent")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(330, 260, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.networkUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkUsageLabel.setGeometry(QtCore.QRect(330, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkUsageLabel.setFont(font)
        self.networkUsageLabel.setObjectName("networkUsageLabel")
        self.networkSentLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkSentLabel.setGeometry(QtCore.QRect(420, 280, 51, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkSentLabel.setFont(font)
        self.networkSentLabel.setObjectName("networkSentLabel")
        self.networkRecvLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkRecvLabel.setGeometry(QtCore.QRect(420, 320, 41, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkRecvLabel.setFont(font)
        self.networkRecvLabel.setObjectName("networkRecvLabel")
        self.networkSentBps = QtWidgets.QLabel(self.centralwidget)
        self.networkSentBps.setGeometry(QtCore.QRect(490, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkSentBps.setFont(font)
        self.networkSentBps.setObjectName("networkSentBps")
        self.networkRecvBps = QtWidgets.QLabel(self.centralwidget)
        self.networkRecvBps.setGeometry(QtCore.QRect(490, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.networkRecvBps.setFont(font)
        self.networkRecvBps.setObjectName("networkRecvBps")
        self.aotCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.aotCheckBox.setGeometry(QtCore.QRect(330, 450, 101, 16))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(9)
        self.aotCheckBox.setFont(font)
        self.aotCheckBox.setObjectName("aotCheckBox")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setEnabled(True)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 1000, 550))
        self.backgroundLabel.setStyleSheet("background-image: url(:/newPrefix/background.jpg);\n"
                                           "background-repeat: no-repeat;\n"
                                           "background-position: center;")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.memUsage = QtWidgets.QLabel(self.centralwidget)
        self.memUsage.setGeometry(QtCore.QRect(460, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.memUsage.setFont(font)
        self.memUsage.setObjectName("memUsage")
        self.cpuFreq = QtWidgets.QLabel(self.centralwidget)
        self.cpuFreq.setGeometry(QtCore.QRect(460, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("경기천년제목 Medium")
        font.setPointSize(15)
        self.cpuFreq.setFont(font)
        self.cpuFreq.setObjectName("cpuFreq")
        self.backgroundLabel.raise_()
        self.cpuUsageLabel.raise_()
        self.memUsageLabel.raise_()
        self.cpuPercent.raise_()
        self.memPercent.raise_()
        self.line.raise_()
        self.networkUsageLabel.raise_()
        self.networkSentLabel.raise_()
        self.networkRecvLabel.raise_()
        self.networkSentBps.raise_()
        self.networkRecvBps.raise_()
        self.aotCheckBox.raise_()
        self.memUsage.raise_()
        self.cpuFreq.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        '''
            아래 부터 Qt Designer 통하지 않고 직접 추가한 코드
        '''
        # 창 크기 고정
        MainWindow.setFixedSize(1000, 550)

        # 창 항상 위에 표시 토글 (현재 작동 안함)
        self.aotCheckBox.stateChanged.connect(self.change_always_on_top)

        # 실시간 정보 업데이트 관련
        self.timer = QTimer()  # timer 변수에 QTimer 할당
        self.timer.start(1000)  # 1000msec(1sec) 마다 반복
        self.timer.timeout.connect(self.update_info)  # start time out시 연결할 함수

        # 창 항상 위에 유지 일단 영구적으로 임시 적용
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        '''
            직접 추가 코드 끝
        '''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PC Monitor with ARONA"))
        self.cpuUsageLabel.setText(_translate("MainWindow", "CPU 사용량"))
        self.memUsageLabel.setText(_translate("MainWindow", "메모리 사용량"))
        self.networkUsageLabel.setText(_translate("MainWindow", "네트워크"))
        self.networkSentLabel.setText(_translate("MainWindow", "보내기"))
        self.networkRecvLabel.setText(_translate("MainWindow", "받기"))
        self.networkSentBps.setText(_translate("MainWindow", "0"))
        self.networkRecvBps.setText(_translate("MainWindow", "0"))
        self.aotCheckBox.setText(_translate("MainWindow", "창 항상 위에"))
        self.memUsage.setText(_translate("MainWindow", "0"))
        self.cpuFreq.setText(_translate("MainWindow", "0"))

    def update_info(self):
        io = psutil.net_io_counters()
        bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
        # CPU
        cpu_ = psutil.cpu_percent()
        cpu_freq_ = round(psutil.cpu_freq().current / 1024, 4)

        # Memory
        memory_ = psutil.virtual_memory()

        # network
        io_2 = psutil.net_io_counters()
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

        dict_example = {
            'cpu': f"{cpu_}",
            'cpu_freq': f"{cpu_freq_}",
            'memory_percent': f"{memory_.percent}",
            'memory_used': f"{get_size_bytes(memory_.used)}",
            'memory_total': f"{get_size_bytes(memory_.total)}",
            'network_upload_speed': f"{get_size_bps(us)}",
            'network_download_speed': f"{get_size_bps(ds)}"
        }
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
        # print(int(float(dict_example['cpu'])))

        self.cpuPercent.setValue(int(float(dict_example['cpu'])))
        self.memPercent.setValue(int(float(dict_example['memory_percent'])))

        self.cpuFreq.setText(dict_example['cpu_freq'] + 'GHz')
        self.memUsage.setText(dict_example['memory_used'] + '/' + dict_example['memory_total'])

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
