# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex.ui'
#
# Created: Fri Jun 10 08:46:58 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 517)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.feature_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.feature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.feature_label.setObjectName(_fromUtf8("feature_label"))
        self.horizontalLayout_4.addWidget(self.feature_label)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.take_shot_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.take_shot_btn.setObjectName(_fromUtf8("take_shot_btn"))
        self.verticalLayout_10.addWidget(self.take_shot_btn)
        self.take_video_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.take_video_btn.setObjectName(_fromUtf8("take_video_btn"))
        self.verticalLayout_10.addWidget(self.take_video_btn)
        self.show_camera_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.show_camera_btn.setObjectName(_fromUtf8("show_camera_btn"))
        self.verticalLayout_10.addWidget(self.show_camera_btn)
        self.feature_check_stop_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.feature_check_stop_btn.setObjectName(_fromUtf8("feature_check_stop_btn"))
        self.verticalLayout_10.addWidget(self.feature_check_stop_btn)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_9 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout.addWidget(self.line_9)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.align_label_01 = QtGui.QLabel(self.verticalLayoutWidget)
        self.align_label_01.setAlignment(QtCore.Qt.AlignCenter)
        self.align_label_01.setObjectName(_fromUtf8("align_label_01"))
        self.verticalLayout_6.addWidget(self.align_label_01)
        self.align_btn_01 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_btn_01.setObjectName(_fromUtf8("align_btn_01"))
        self.verticalLayout_6.addWidget(self.align_btn_01)
        self.align_stop_btn_01 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_stop_btn_01.setObjectName(_fromUtf8("align_stop_btn_01"))
        self.verticalLayout_6.addWidget(self.align_stop_btn_01)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.align_label_12 = QtGui.QLabel(self.verticalLayoutWidget)
        self.align_label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.align_label_12.setObjectName(_fromUtf8("align_label_12"))
        self.verticalLayout_5.addWidget(self.align_label_12)
        self.align_btn_12 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_btn_12.setObjectName(_fromUtf8("align_btn_12"))
        self.verticalLayout_5.addWidget(self.align_btn_12)
        self.align_stop_btn_12 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_stop_btn_12.setObjectName(_fromUtf8("align_stop_btn_12"))
        self.verticalLayout_5.addWidget(self.align_stop_btn_12)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.align_label_23 = QtGui.QLabel(self.verticalLayoutWidget)
        self.align_label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.align_label_23.setObjectName(_fromUtf8("align_label_23"))
        self.verticalLayout_4.addWidget(self.align_label_23)
        self.align_btn_23 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_btn_23.setObjectName(_fromUtf8("align_btn_23"))
        self.verticalLayout_4.addWidget(self.align_btn_23)
        self.align_stop_btn_23 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_stop_btn_23.setObjectName(_fromUtf8("align_stop_btn_23"))
        self.verticalLayout_4.addWidget(self.align_stop_btn_23)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line_4 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.align_label_34 = QtGui.QLabel(self.verticalLayoutWidget)
        self.align_label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.align_label_34.setObjectName(_fromUtf8("align_label_34"))
        self.verticalLayout_3.addWidget(self.align_label_34)
        self.align_btn_34 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_btn_34.setObjectName(_fromUtf8("align_btn_34"))
        self.verticalLayout_3.addWidget(self.align_btn_34)
        self.align_stop_btn_34 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_stop_btn_34.setObjectName(_fromUtf8("align_stop_btn_34"))
        self.verticalLayout_3.addWidget(self.align_stop_btn_34)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.line_5 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.align_label_45 = QtGui.QLabel(self.verticalLayoutWidget)
        self.align_label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.align_label_45.setObjectName(_fromUtf8("align_label_45"))
        self.verticalLayout_2.addWidget(self.align_label_45)
        self.align_btn_45 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_btn_45.setObjectName(_fromUtf8("align_btn_45"))
        self.verticalLayout_2.addWidget(self.align_btn_45)
        self.align_stop_btn_45 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.align_stop_btn_45.setObjectName(_fromUtf8("align_stop_btn_45"))
        self.verticalLayout_2.addWidget(self.align_stop_btn_45)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.img_stitch_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.img_stitch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_stitch_label.setObjectName(_fromUtf8("img_stitch_label"))
        self.verticalLayout_7.addWidget(self.img_stitch_label)
        self.img_stitch_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.img_stitch_btn.setObjectName(_fromUtf8("img_stitch_btn"))
        self.verticalLayout_7.addWidget(self.img_stitch_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.line_7 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_2.addWidget(self.line_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.save_params_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.save_params_btn.setObjectName(_fromUtf8("save_params_btn"))
        self.verticalLayout_8.addWidget(self.save_params_btn)
        self.load_params_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.load_params_btn.setObjectName(_fromUtf8("load_params_btn"))
        self.verticalLayout_8.addWidget(self.load_params_btn)
        self.save_final_matrix_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.save_final_matrix_btn.setObjectName(_fromUtf8("save_final_matrix_btn"))
        self.verticalLayout_8.addWidget(self.save_final_matrix_btn)
        self.load_final_matrix_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.load_final_matrix_btn.setObjectName(_fromUtf8("load_final_matrix_btn"))
        self.verticalLayout_8.addWidget(self.load_final_matrix_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.line_8 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout_2.addWidget(self.line_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.create_mask_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.create_mask_btn.setObjectName(_fromUtf8("create_mask_btn"))
        self.verticalLayout_9.addWidget(self.create_mask_btn)
        self.img_stitch_without_seam_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.img_stitch_without_seam_btn.setObjectName(_fromUtf8("img_stitch_without_seam_btn"))
        self.verticalLayout_9.addWidget(self.img_stitch_without_seam_btn)
        self.img_stitch_with_seam_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.img_stitch_with_seam_btn.setObjectName(_fromUtf8("img_stitch_with_seam_btn"))
        self.verticalLayout_9.addWidget(self.img_stitch_with_seam_btn)
        self.video_stitch_without_seam_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.video_stitch_without_seam_btn.setObjectName(_fromUtf8("video_stitch_without_seam_btn"))
        self.verticalLayout_9.addWidget(self.video_stitch_without_seam_btn)
        self.video_stitch_with_seam_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.video_stitch_with_seam_btn.setObjectName(_fromUtf8("video_stitch_with_seam_btn"))
        self.verticalLayout_9.addWidget(self.video_stitch_with_seam_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.line_6 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_2.addWidget(self.line_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.feature_label.setText(_translate("MainWindow", "TextLabel", None))
        self.take_shot_btn.setText(_translate("MainWindow", "Take a Shot", None))
        self.take_video_btn.setText(_translate("MainWindow", "Take Video", None))
        self.show_camera_btn.setText(_translate("MainWindow", "Show Camera", None))
        self.feature_check_stop_btn.setText(_translate("MainWindow", "Stop Camera", None))
        self.align_label_01.setText(_translate("MainWindow", "Camera 0,1", None))
        self.align_btn_01.setText(_translate("MainWindow", "Alignment", None))
        self.align_stop_btn_01.setText(_translate("MainWindow", "Stop", None))
        self.align_label_12.setText(_translate("MainWindow", "Camera 1,2", None))
        self.align_btn_12.setText(_translate("MainWindow", "Alignment", None))
        self.align_stop_btn_12.setText(_translate("MainWindow", "Stop", None))
        self.align_label_23.setText(_translate("MainWindow", "Camera 2,3", None))
        self.align_btn_23.setText(_translate("MainWindow", "Alignment", None))
        self.align_stop_btn_23.setText(_translate("MainWindow", "Stop", None))
        self.align_label_34.setText(_translate("MainWindow", "Camera 3,4", None))
        self.align_btn_34.setText(_translate("MainWindow", "Alignment", None))
        self.align_stop_btn_34.setText(_translate("MainWindow", "Stop", None))
        self.align_label_45.setText(_translate("MainWindow", "Camera 4,5", None))
        self.align_btn_45.setText(_translate("MainWindow", "Alignment", None))
        self.align_stop_btn_45.setText(_translate("MainWindow", "Stop", None))
        self.img_stitch_label.setText(_translate("MainWindow", "TextLabel", None))
        self.img_stitch_btn.setText(_translate("MainWindow", "Image Stitch", None))
        self.save_params_btn.setText(_translate("MainWindow", "Save Parameters", None))
        self.load_params_btn.setText(_translate("MainWindow", "Load Parameters", None))
        self.save_final_matrix_btn.setText(_translate("MainWindow", "PushButton", None))
        self.load_final_matrix_btn.setText(_translate("MainWindow", "PushButton", None))
        self.create_mask_btn.setText(_translate("MainWindow", "Create Mask", None))
        self.img_stitch_without_seam_btn.setText(_translate("MainWindow", "Image Stitch without Seam", None))
        self.img_stitch_with_seam_btn.setText(_translate("MainWindow", "Image Stitch wit Seam", None))
        self.video_stitch_without_seam_btn.setText(_translate("MainWindow", "Video Stitch without Seam", None))
        self.video_stitch_with_seam_btn.setText(_translate("MainWindow", "Video Stitch with Seam", None))

