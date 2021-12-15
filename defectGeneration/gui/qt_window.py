# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1920, 1081)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
		self.centralwidget.setSizePolicy(sizePolicy)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
		self.horizontalLayout.setSpacing(2)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setObjectName("label_3")
		self.verticalLayout_2.addWidget(self.label_3)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.filename_input = QtWidgets.QTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.filename_input.sizePolicy().hasHeightForWidth())
		self.filename_input.setSizePolicy(sizePolicy)
		self.filename_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.filename_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.filename_input.setTabChangesFocus(True)
		self.filename_input.setReadOnly(True)
		self.filename_input.setObjectName("filename_input")
		self.horizontalLayout_3.addWidget(self.filename_input)
		self.filename_browse = QtWidgets.QPushButton(self.centralwidget)
		self.filename_browse.setEnabled(True)
		self.filename_browse.setObjectName("filename_browse")
		self.horizontalLayout_3.addWidget(self.filename_browse)
		self.horizontalLayout_3.setStretch(0, 7)
		self.horizontalLayout_3.setStretch(1, 3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem)
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_14 = QtWidgets.QLabel(self.centralwidget)
		self.label_14.setObjectName("label_14")
		self.verticalLayout_3.addWidget(self.label_14)
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.label_15 = QtWidgets.QLabel(self.centralwidget)
		self.label_15.setMinimumSize(QtCore.QSize(0, 31))
		self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_15.setObjectName("label_15")
		self.horizontalLayout_8.addWidget(self.label_15)
		self.layer_dropdown = QtWidgets.QComboBox(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.layer_dropdown.sizePolicy().hasHeightForWidth())
		self.layer_dropdown.setSizePolicy(sizePolicy)
		self.layer_dropdown.setObjectName("layer_dropdown")
		self.horizontalLayout_8.addWidget(self.layer_dropdown)
		self.horizontalLayout_8.setStretch(0, 1)
		self.horizontalLayout_8.setStretch(1, 6)
		self.verticalLayout_3.addLayout(self.horizontalLayout_8)
		self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_9.setObjectName("horizontalLayout_9")
		self.label_13 = QtWidgets.QLabel(self.centralwidget)
		self.label_13.setMinimumSize(QtCore.QSize(0, 31))
		self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_13.setObjectName("label_13")
		self.horizontalLayout_9.addWidget(self.label_13)
		self.density_mean_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.density_mean_input.sizePolicy().hasHeightForWidth())
		self.density_mean_input.setSizePolicy(sizePolicy)
		self.density_mean_input.setMinimumSize(QtCore.QSize(0, 31))
		self.density_mean_input.setTabChangesFocus(True)
		self.density_mean_input.setObjectName("density_mean_input")
		self.horizontalLayout_9.addWidget(self.density_mean_input)
		self.density_stddev_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.density_stddev_input.sizePolicy().hasHeightForWidth())
		self.density_stddev_input.setSizePolicy(sizePolicy)
		self.density_stddev_input.setMinimumSize(QtCore.QSize(0, 31))
		self.density_stddev_input.setTabChangesFocus(True)
		self.density_stddev_input.setObjectName("density_stddev_input")
		self.horizontalLayout_9.addWidget(self.density_stddev_input)
		self.horizontalLayout_9.setStretch(0, 1)
		self.horizontalLayout_9.setStretch(1, 3)
		self.horizontalLayout_9.setStretch(2, 3)
		self.verticalLayout_3.addLayout(self.horizontalLayout_9)
		self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_13.setObjectName("horizontalLayout_13")
		self.label_16 = QtWidgets.QLabel(self.centralwidget)
		self.label_16.setMinimumSize(QtCore.QSize(0, 31))
		self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_16.setObjectName("label_16")
		self.horizontalLayout_13.addWidget(self.label_16)
		self.size_mean_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.size_mean_input.sizePolicy().hasHeightForWidth())
		self.size_mean_input.setSizePolicy(sizePolicy)
		self.size_mean_input.setMinimumSize(QtCore.QSize(0, 31))
		self.size_mean_input.setTabChangesFocus(True)
		self.size_mean_input.setObjectName("size_mean_input")
		self.horizontalLayout_13.addWidget(self.size_mean_input)
		self.size_stddev_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.size_stddev_input.sizePolicy().hasHeightForWidth())
		self.size_stddev_input.setSizePolicy(sizePolicy)
		self.size_stddev_input.setMinimumSize(QtCore.QSize(0, 31))
		self.size_stddev_input.setTabChangesFocus(True)
		self.size_stddev_input.setObjectName("size_stddev_input")
		self.horizontalLayout_13.addWidget(self.size_stddev_input)
		self.horizontalLayout_13.setStretch(0, 1)
		self.horizontalLayout_13.setStretch(1, 3)
		self.horizontalLayout_13.setStretch(2, 3)
		self.verticalLayout_3.addLayout(self.horizontalLayout_13)
		self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_14.setObjectName("horizontalLayout_14")
		self.label_17 = QtWidgets.QLabel(self.centralwidget)
		self.label_17.setMinimumSize(QtCore.QSize(0, 31))
		self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_17.setObjectName("label_17")
		self.horizontalLayout_14.addWidget(self.label_17)
		self.vertices_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.vertices_input.sizePolicy().hasHeightForWidth())
		self.vertices_input.setSizePolicy(sizePolicy)
		self.vertices_input.setMinimumSize(QtCore.QSize(0, 31))
		self.vertices_input.setTabChangesFocus(True)
		self.vertices_input.setObjectName("vertices_input")
		self.horizontalLayout_14.addWidget(self.vertices_input)
		self.horizontalLayout_14.setStretch(0, 1)
		self.horizontalLayout_14.setStretch(1, 6)
		self.verticalLayout_3.addLayout(self.horizontalLayout_14)
		self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_10.setObjectName("horizontalLayout_10")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setMinimumSize(QtCore.QSize(0, 31))
		self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label.setObjectName("label")
		self.horizontalLayout_10.addWidget(self.label)
		self.angle_variance_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.angle_variance_input.sizePolicy().hasHeightForWidth())
		self.angle_variance_input.setSizePolicy(sizePolicy)
		self.angle_variance_input.setMinimumSize(QtCore.QSize(0, 31))
		self.angle_variance_input.setTabChangesFocus(True)
		self.angle_variance_input.setObjectName("angle_variance_input")
		self.horizontalLayout_10.addWidget(self.angle_variance_input)
		self.horizontalLayout_10.setStretch(0, 1)
		self.horizontalLayout_10.setStretch(1, 6)
		self.verticalLayout_3.addLayout(self.horizontalLayout_10)
		self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_15.setObjectName("horizontalLayout_15")
		self.label_18 = QtWidgets.QLabel(self.centralwidget)
		self.label_18.setMinimumSize(QtCore.QSize(0, 31))
		self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_18.setObjectName("label_18")
		self.horizontalLayout_15.addWidget(self.label_18)
		self.curviness_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.curviness_input.sizePolicy().hasHeightForWidth())
		self.curviness_input.setSizePolicy(sizePolicy)
		self.curviness_input.setMinimumSize(QtCore.QSize(0, 31))
		self.curviness_input.setTabChangesFocus(True)
		self.curviness_input.setObjectName("curviness_input")
		self.horizontalLayout_15.addWidget(self.curviness_input)
		self.horizontalLayout_15.setStretch(0, 1)
		self.horizontalLayout_15.setStretch(1, 6)
		self.verticalLayout_3.addLayout(self.horizontalLayout_15)
		self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_16.setObjectName("horizontalLayout_16")
		self.label_19 = QtWidgets.QLabel(self.centralwidget)
		self.label_19.setMinimumSize(QtCore.QSize(0, 31))
		self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_19.setObjectName("label_19")
		self.horizontalLayout_16.addWidget(self.label_19)
		self.blur_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.blur_input.sizePolicy().hasHeightForWidth())
		self.blur_input.setSizePolicy(sizePolicy)
		self.blur_input.setMinimumSize(QtCore.QSize(0, 31))
		self.blur_input.setTabChangesFocus(True)
		self.blur_input.setObjectName("blur_input")
		self.horizontalLayout_16.addWidget(self.blur_input)
		self.horizontalLayout_16.setStretch(0, 1)
		self.horizontalLayout_16.setStretch(1, 6)
		self.verticalLayout_3.addLayout(self.horizontalLayout_16)
		self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_11.setObjectName("horizontalLayout_11")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_11.addWidget(self.label_2)
		self.color_input = QtWidgets.QPushButton(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.color_input.sizePolicy().hasHeightForWidth())
		self.color_input.setSizePolicy(sizePolicy)
		self.color_input.setStyleSheet("background-color: black")
		self.color_input.setText("")
		self.color_input.setObjectName("color_input")
		self.horizontalLayout_11.addWidget(self.color_input)
		self.horizontalLayout_11.setStretch(0, 1)
		self.horizontalLayout_11.setStretch(1, 6)
		self.verticalLayout_3.addLayout(self.horizontalLayout_11)
		self.verticalLayout_2.addLayout(self.verticalLayout_3)
		spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem1)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setObjectName("label_6")
		self.horizontalLayout_4.addWidget(self.label_6)
		self.invalid_parameters_error = QtWidgets.QLabel(self.centralwidget)
		self.invalid_parameters_error.setEnabled(True)
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.invalid_parameters_error.setFont(font)
		self.invalid_parameters_error.setStyleSheet("QLabel { color : red; }")
		self.invalid_parameters_error.setText("")
		self.invalid_parameters_error.setScaledContents(False)
		self.invalid_parameters_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.invalid_parameters_error.setObjectName("invalid_parameters_error")
		self.horizontalLayout_4.addWidget(self.invalid_parameters_error)
		self.preview_button = QtWidgets.QPushButton(self.centralwidget)
		self.preview_button.setEnabled(False)
		self.preview_button.setObjectName("preview_button")
		self.horizontalLayout_4.addWidget(self.preview_button)
		self.clear_preview_button = QtWidgets.QPushButton(self.centralwidget)
		self.clear_preview_button.setEnabled(False)
		self.clear_preview_button.setObjectName("clear_preview_button")
		self.horizontalLayout_4.addWidget(self.clear_preview_button)
		self.toggle_accuracy_button = QtWidgets.QPushButton(self.centralwidget)
		self.toggle_accuracy_button.setObjectName("toggle_accuracy_button")
		self.horizontalLayout_4.addWidget(self.toggle_accuracy_button)
		self.toggle_bbox_button = QtWidgets.QPushButton(self.centralwidget)
		self.toggle_bbox_button.setCheckable(True)
		self.toggle_bbox_button.setObjectName("toggle_bbox_button")
		self.horizontalLayout_4.addWidget(self.toggle_bbox_button)
		self.horizontalLayout_4.setStretch(0, 1)
		self.horizontalLayout_4.setStretch(1, 4)
		self.horizontalLayout_4.setStretch(2, 4)
		self.horizontalLayout_4.setStretch(3, 4)
		self.horizontalLayout_4.setStretch(4, 1)
		self.horizontalLayout_4.setStretch(5, 1)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem2)
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setObjectName("label_7")
		self.verticalLayout_2.addWidget(self.label_7)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.gen_1_button = QtWidgets.QPushButton(self.centralwidget)
		self.gen_1_button.setObjectName("gen_1_button")
		self.horizontalLayout_2.addWidget(self.gen_1_button)
		self.gen_5_button = QtWidgets.QPushButton(self.centralwidget)
		self.gen_5_button.setObjectName("gen_5_button")
		self.horizontalLayout_2.addWidget(self.gen_5_button)
		self.gen_10_button = QtWidgets.QPushButton(self.centralwidget)
		self.gen_10_button.setObjectName("gen_10_button")
		self.horizontalLayout_2.addWidget(self.gen_10_button)
		self.gen_100_button = QtWidgets.QPushButton(self.centralwidget)
		self.gen_100_button.setObjectName("gen_100_button")
		self.horizontalLayout_2.addWidget(self.gen_100_button)
		self.gen_1000_button = QtWidgets.QPushButton(self.centralwidget)
		self.gen_1000_button.setObjectName("gen_1000_button")
		self.horizontalLayout_2.addWidget(self.gen_1000_button)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.gen_manual_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.gen_manual_input.sizePolicy().hasHeightForWidth())
		self.gen_manual_input.setSizePolicy(sizePolicy)
		self.gen_manual_input.setObjectName("gen_manual_input")
		self.horizontalLayout_5.addWidget(self.gen_manual_input)
		self.generate_button = QtWidgets.QPushButton(self.centralwidget)
		self.generate_button.setEnabled(False)
		self.generate_button.setObjectName("generate_button")
		self.horizontalLayout_5.addWidget(self.generate_button)
		self.horizontalLayout_5.setStretch(0, 7)
		self.horizontalLayout_5.setStretch(1, 3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_5)
		self.invalid_images_amount_error = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.invalid_images_amount_error.setFont(font)
		self.invalid_images_amount_error.setStyleSheet("QLabel { color : red; }")
		self.invalid_images_amount_error.setText("")
		self.invalid_images_amount_error.setObjectName("invalid_images_amount_error")
		self.verticalLayout_2.addWidget(self.invalid_images_amount_error)
		spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem3)
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setObjectName("label_8")
		self.verticalLayout_2.addWidget(self.label_8)
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.image_path_input = QtWidgets.QPlainTextEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.image_path_input.sizePolicy().hasHeightForWidth())
		self.image_path_input.setSizePolicy(sizePolicy)
		self.image_path_input.setReadOnly(True)
		self.image_path_input.setObjectName("image_path_input")
		self.horizontalLayout_6.addWidget(self.image_path_input)
		self.image_output_browse = QtWidgets.QPushButton(self.centralwidget)
		self.image_output_browse.setObjectName("image_output_browse")
		self.horizontalLayout_6.addWidget(self.image_output_browse)
		self.horizontalLayout_6.setStretch(0, 7)
		self.horizontalLayout_6.setStretch(1, 3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_6)
		self.invalid_output_dir_error = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.invalid_output_dir_error.setFont(font)
		self.invalid_output_dir_error.setStyleSheet("QLabel { color : red; }")
		self.invalid_output_dir_error.setText("")
		self.invalid_output_dir_error.setObjectName("invalid_output_dir_error")
		self.verticalLayout_2.addWidget(self.invalid_output_dir_error)
		spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem4)
		self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_12.setObjectName("horizontalLayout_12")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_12.addWidget(self.label_4)
		self.file_progress = QtWidgets.QLabel(self.centralwidget)
		self.file_progress.setAlignment(QtCore.Qt.AlignCenter)
		self.file_progress.setObjectName("file_progress")
		self.horizontalLayout_12.addWidget(self.file_progress)
		self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
		self.progressBar.setProperty("value", 0)
		self.progressBar.setObjectName("progressBar")
		self.horizontalLayout_12.addWidget(self.progressBar)
		self.horizontalLayout_12.setStretch(0, 2)
		self.horizontalLayout_12.setStretch(1, 1)
		self.horizontalLayout_12.setStretch(2, 9)
		self.verticalLayout_2.addLayout(self.horizontalLayout_12)
		spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem5)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.shown_image = QtWidgets.QLabel(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.shown_image.sizePolicy().hasHeightForWidth())
		self.shown_image.setSizePolicy(sizePolicy)
		self.shown_image.setText("")
		self.shown_image.setScaledContents(True)
		self.shown_image.setAlignment(QtCore.Qt.AlignCenter)
		self.shown_image.setObjectName("shown_image")
		self.verticalLayout.addWidget(self.shown_image)
		self.horizontalLayout.addLayout(self.verticalLayout)
		self.horizontalLayout.setStretch(0, 5)
		self.horizontalLayout.setStretch(1, 5)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.setTabOrder(self.filename_input, self.filename_browse)
		MainWindow.setTabOrder(self.filename_browse, self.layer_dropdown)
		MainWindow.setTabOrder(self.layer_dropdown, self.density_mean_input)
		MainWindow.setTabOrder(self.density_mean_input, self.density_stddev_input)
		MainWindow.setTabOrder(self.density_stddev_input, self.size_mean_input)
		MainWindow.setTabOrder(self.size_mean_input, self.size_stddev_input)
		MainWindow.setTabOrder(self.size_stddev_input, self.vertices_input)
		MainWindow.setTabOrder(self.vertices_input, self.angle_variance_input)
		MainWindow.setTabOrder(self.angle_variance_input, self.curviness_input)
		MainWindow.setTabOrder(self.curviness_input, self.blur_input)
		MainWindow.setTabOrder(self.blur_input, self.preview_button)
		MainWindow.setTabOrder(self.preview_button, self.clear_preview_button)
		MainWindow.setTabOrder(self.clear_preview_button, self.toggle_accuracy_button)
		MainWindow.setTabOrder(self.toggle_accuracy_button, self.toggle_bbox_button)
		MainWindow.setTabOrder(self.toggle_bbox_button, self.gen_1_button)
		MainWindow.setTabOrder(self.gen_1_button, self.gen_5_button)
		MainWindow.setTabOrder(self.gen_5_button, self.gen_10_button)
		MainWindow.setTabOrder(self.gen_10_button, self.gen_100_button)
		MainWindow.setTabOrder(self.gen_100_button, self.gen_1000_button)
		MainWindow.setTabOrder(self.gen_1000_button, self.gen_manual_input)
		MainWindow.setTabOrder(self.gen_manual_input, self.generate_button)
		MainWindow.setTabOrder(self.generate_button, self.image_path_input)
		MainWindow.setTabOrder(self.image_path_input, self.image_output_browse)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label_3.setText(_translate("MainWindow", "Select input file"))
		self.filename_input.setPlaceholderText(_translate("MainWindow", "Path to source image"))
		self.filename_browse.setText(_translate("MainWindow", "Browse"))
		self.label_14.setText(_translate("MainWindow", "Input parameters"))
		self.label_15.setText(_translate("MainWindow", "Layer"))
		self.label_13.setText(_translate("MainWindow", "Density"))
		self.density_mean_input.setPlaceholderText(_translate("MainWindow", "standard mean"))
		self.density_stddev_input.setPlaceholderText(_translate("MainWindow", "standard deviation"))
		self.label_16.setText(_translate("MainWindow", "Size"))
		self.size_mean_input.setPlaceholderText(_translate("MainWindow", "standard mean"))
		self.size_stddev_input.setPlaceholderText(_translate("MainWindow", "standard deviation"))
		self.label_17.setText(_translate("MainWindow", "Vertices"))
		self.vertices_input.setPlaceholderText(_translate("MainWindow", "amount of vertices"))
		self.label.setText(_translate("MainWindow", "Angle variance"))
		self.angle_variance_input.setPlaceholderText(_translate("MainWindow", "percentage between 0.0 and 100.0"))
		self.label_18.setText(_translate("MainWindow", "Curviness"))
		self.curviness_input.setPlaceholderText(_translate("MainWindow", "percentage between 0.0 and 100.0"))
		self.label_19.setText(_translate("MainWindow", "Blur"))
		self.blur_input.setPlaceholderText(_translate("MainWindow", "percentage between 0.0 and 100.0"))
		self.label_2.setText(_translate("MainWindow", "Color"))
		self.label_6.setText(_translate("MainWindow", "Preview"))
		self.preview_button.setText(_translate("MainWindow", "Preview"))
		self.clear_preview_button.setText(_translate("MainWindow", "Clear"))
		self.toggle_accuracy_button.setText(_translate("MainWindow", "Accurate"))
		self.toggle_bbox_button.setText(_translate("MainWindow", "Bbox"))
		self.label_7.setText(_translate("MainWindow", "Image Generation"))
		self.gen_1_button.setText(_translate("MainWindow", "1"))
		self.gen_5_button.setText(_translate("MainWindow", "5"))
		self.gen_10_button.setText(_translate("MainWindow", "10"))
		self.gen_100_button.setText(_translate("MainWindow", "100"))
		self.gen_1000_button.setText(_translate("MainWindow", "1000"))
		self.gen_manual_input.setPlaceholderText(_translate("MainWindow", "Enter custom amount to generate"))
		self.generate_button.setText(_translate("MainWindow", "Generate"))
		self.label_8.setText(_translate("MainWindow", "Output image file directory"))
		self.image_path_input.setPlaceholderText(_translate("MainWindow", "Path to image output directory"))
		self.image_output_browse.setText(_translate("MainWindow", "Browse"))
		self.label_4.setText(_translate("MainWindow", "Image generation progress"))
		self.file_progress.setText(_translate("MainWindow", "0 / 0"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
