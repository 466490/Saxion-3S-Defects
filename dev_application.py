from PyQt5 import QtCore, QtGui, QtWidgets
from multi_processor import MultiProcessor
import reader, time, os, json
import importlib, inspect


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
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout_7.addWidget(self.label_5)
		self.defect_dropdown = QtWidgets.QComboBox(self.centralwidget)
		self.defect_dropdown.setObjectName("defect_dropdown")
		self.horizontalLayout_7.addWidget(self.defect_dropdown)
		self.horizontalLayout_7.setStretch(0, 1)
		self.horizontalLayout_7.setStretch(1, 6)
		self.verticalLayout_2.addLayout(self.horizontalLayout_7)
		spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem1)
		self.input_parameters_vlayout = QtWidgets.QVBoxLayout()
		self.input_parameters_vlayout.setObjectName("input_parameters_vlayout")
		self.label_14 = QtWidgets.QLabel(self.centralwidget)
		self.label_14.setObjectName("label_14")
		self.input_parameters_vlayout.addWidget(self.label_14)
		self.verticalLayout_2.addLayout(self.input_parameters_vlayout)
		spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem2)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_2.addWidget(self.label_2)
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.preset_input = QtWidgets.QLineEdit(self.centralwidget)
		self.preset_input.setObjectName("preset_input")
		self.horizontalLayout_8.addWidget(self.preset_input)
		self.preset_save = QtWidgets.QPushButton(self.centralwidget)
		self.preset_save.setObjectName("preset_save")
		self.horizontalLayout_8.addWidget(self.preset_save)
		self.preset_delete = QtWidgets.QPushButton(self.centralwidget)
		self.preset_delete.setObjectName("preset_delete")
		self.horizontalLayout_8.addWidget(self.preset_delete)
		self.horizontalLayout_8.setStretch(0, 7)
		self.horizontalLayout_8.setStretch(1, 3)
		self.horizontalLayout_8.setStretch(2, 2)
		self.verticalLayout_2.addLayout(self.horizontalLayout_8)
		spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem3)
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
		spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem4)
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
		self.gen_manual_input = QtWidgets.QLineEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.gen_manual_input.sizePolicy().hasHeightForWidth())
		self.gen_manual_input.setSizePolicy(sizePolicy)
		self.gen_manual_input.setObjectName("gen_manual_input")
		# Custom code ---------------------------------------------------------------------------
		validator = QtGui.QIntValidator(0, int(10e6))
		self.gen_manual_input.setValidator(validator)
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
		spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem5)
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
		spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_2.addItem(spacerItem6)
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
		spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem7)
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

		self.defect_dropdown.currentTextChanged.connect(self.selected_defect_type)
		self.setup_function_connects()
		self.find_all_defect_types()

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.setTabOrder(self.filename_input, self.filename_browse)
		MainWindow.setTabOrder(self.filename_browse, self.preview_button)
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
		self.label_5.setText(_translate("MainWindow", "Select defect input"))
		self.label_14.setText(_translate("MainWindow", "Input parameters"))
		self.label_2.setText(_translate("MainWindow", "Save parameters as preset"))
		self.preset_save.setText(_translate("MainWindow", "Save"))
		self.preset_delete.setText(_translate("MainWindow", "Delete"))
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

	def setup_function_connects(self):
		# Connect filename browse button to function
		self.filename_browse.clicked.connect(self.browse_input_files)
		# Connect preview defect generation button to function
		self.preview_button.clicked.connect(self.generate_preview)
		# Connect clear preview to function
		self.clear_preview_button.clicked.connect(self.clear_preview)
		# Connect toggle accuarcy/speed to function
		self.toggle_accuracy_button.clicked.connect(self.toggle_accuracy)
		# Connect generate image button to function
		self.generate_button.clicked.connect(self.generate_images)

		self.preset_save.clicked.connect(self.save_preset)
		self.preset_delete.clicked.connect(self.delete_preset)
		
		self.gen_1_button.clicked.connect(lambda: self.input_amount_gen(1))
		self.gen_5_button.clicked.connect(lambda: self.input_amount_gen(5))
		self.gen_10_button.clicked.connect(lambda: self.input_amount_gen(10))
		self.gen_100_button.clicked.connect(lambda: self.input_amount_gen(100))
		self.gen_1000_button.clicked.connect(lambda: self.input_amount_gen(1000))

		self.image_output_browse.clicked.connect(self.browse_output_dir)
	
	def find_all_defect_types(self):
		files = [f[:-3] for f in os.listdir("defectTypes") if f.endswith('.py') and f != 'baseclass.py']
		self.defect_types = {}
		for file in files:
			module = importlib.import_module("defectTypes."+file, ".")
			for name, obj in inspect.getmembers(module):
				if inspect.isclass(obj) and name != "BaseClass":
					self.defect_types.update({obj.get_classname():obj})
					self.defect_dropdown.addItem(obj.get_classname())
		# Add presets
		preset_files = [f for f in os.listdir("defectPresets") if f.endswith(".txt")]
		for preset in  preset_files:
			with open("defectPresets/" + preset, "r") as f:
				file_contents = f.read()
			dic = json.loads(file_contents)
			self.defect_types.update({dic["inherits"] + " <- " + dic["classname"]: dic["inherits"]})
			self.defect_dropdown.addItem(dic["inherits"] + " <- " + dic["classname"])

	def clear_layout(self, layout):
		while layout.count():
			child = layout.takeAt(0)
			if child.widget() is not None:
				child.widget().deleteLater()
			elif child.layout() is not None:
				self.clear_layout(child.layout())

	def save_preset(self):
		preset = self.preset_input.text()
		if preset != "":
			parameters = self.get_parameters(withSrc=False)
			with open("defectPresets/" + preset + ".txt", "w") as file:
				file.write('{"classname":'+'"'+preset+'"')
				file.write(',"inherits":'+'"'+self.current_defect_class+'"')
				file.write(',"parameters":'+json.dumps(parameters)+'}')

	def delete_preset(self):
		pass

	def selected_defect_type(self, text):
		self.clear_layout(self.input_parameters_vlayout)
		if "<-" in text:
			filename = text.split(" <- ")
			with open("defectPresets/" + filename[-1] + ".txt", "r") as f:
				file_contents = f.read()
			dic = json.loads(file_contents)
			preset_parameters = dic["parameters"]
			self.current_defect_class = self.defect_types[filename[0]].get_classname()
			self.defect_parameters = self.defect_types[filename[0]].get_parameters()
			for key,value in preset_parameters.items():
				self.defect_parameters[key]["default"] = value
		else:
			self.defect_parameters = self.defect_types[text].get_parameters()
			self.current_defect_class = self.defect_types[text].get_classname()
		for key,value in self.defect_parameters.items():
			# Layout 
			layout = QtWidgets.QHBoxLayout()
			layout.setObjectName("hLayout_input_"+key)
			# Label
			label = QtWidgets.QLabel(self.centralwidget)
			label.setObjectName("label_"+key)
			label.setMinimumSize(QtCore.QSize(0, 31))
			label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
			label.setText(value["display_name"])
			# Input
			type = value["type"]
			if type == "int" or type == "float":
				input = QtWidgets.QLineEdit(self.centralwidget)
				sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(input.sizePolicy().hasHeightForWidth())
				input.setSizePolicy(sizePolicy)
				input.setMinimumSize(QtCore.QSize(0, 31))
				input.setObjectName("para_input_"+key)
				input.setText(str(value["default"]))
				if type == "float":
					validator = QtGui.QDoubleValidator(value["min"], value["max"], 1000)
				else:
					validator = QtGui.QIntValidator(int(value["min"]), int(value["max"]))
				input.setValidator(validator)
				layout.addWidget(label)
				layout.addWidget(input)
				layout.setStretch(0, 1)
				layout.setStretch(1, 6)
			elif type == "percentage":
				input = QtWidgets.QLineEdit(self.centralwidget)
				sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(input.sizePolicy().hasHeightForWidth())
				input.setSizePolicy(sizePolicy)
				input.setMinimumSize(QtCore.QSize(0, 31))
				input.setObjectName("para_input_"+key)
				input.setText(str(value["default"]))

				input_slider = QtWidgets.QSlider(self.centralwidget)
				input_slider.setOrientation(QtCore.Qt.Horizontal)
				input_slider.setMaximum(100)
				input_slider.setObjectName("slider_"+key)
				input_slider.setValue(int(value["default"]))
				
				input.textChanged.connect(lambda input_slider=input_slider, input_label=input: self.update_slider_from_input(input_slider, input_label.text()))
				input_slider.valueChanged.connect(lambda value, input_label=input: self.update_input_from_slider(input_label, value))
				
				layout.addWidget(label)
				layout.addWidget(input)
				layout.addWidget(input_slider)
				layout.setStretch(0, 1)
				layout.setStretch(1, 1)
				layout.setStretch(2, 5)
			elif type == "color":
				input = QtWidgets.QPushButton(self.centralwidget)
				sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(input.sizePolicy().hasHeightForWidth())
				input.setSizePolicy(sizePolicy)
				input.setStyleSheet("background-color: "+value["default"])
				input.setText("")
				input.setObjectName("para_button_"+key)

				input.clicked.connect(lambda flag, button=input: self.open_color_dialog(button))

				layout.addWidget(label)
				layout.addWidget(input)
				layout.setStretch(0, 1)
				layout.setStretch(1, 6)
			elif type == "layer":
				dropdown = QtWidgets.QComboBox(self.centralwidget)
				sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(dropdown.sizePolicy().hasHeightForWidth())
				dropdown.setSizePolicy(sizePolicy)
				dropdown.setObjectName("para_dropdown_"+key)
				if self.filename_input.toPlainText() != "":
					layers = reader.get_layers(self.filename_input.toPlainText())
					dropdown.clear()
					dropdown.insertItems(0, layers)

				layout.addWidget(label)
				layout.addWidget(dropdown)
				layout.setStretch(0, 1)
				layout.setStretch(1, 6)
			self.input_parameters_vlayout.addLayout(layout)
		defect_type = self.defect_dropdown.currentText()
		self.preset_input.setText(defect_type)

	def update_slider_from_input(self, input_slider, value):
		try:
			value = int(value)
			if 0 <= value <= 100:
				input_slider.setValue(value)
		except:
			pass

	def update_input_from_slider(self, input_label, value):
		input_label.setText(str(value))
	
	def open_color_dialog(self, color_button):
		color = QtWidgets.QColorDialog.getColor(initial=color_button.palette().button().color())
		if color.isValid():
			color_button.setStyleSheet("background-color:" + color.name() +";")

	def toggle_accuracy(self):
		if self.toggle_accuracy_button.text() == "Accurate":
			self.toggle_accuracy_button.setText("Fast")
		else:
			self.toggle_accuracy_button.setText("Accurate")


	def browse_input_files(self):
		filename = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Select Input Image", ".", "*.svg")[0]
		if filename != "":
			self.path_to_input_image = filename
			self.filename_input.setText(self.path_to_input_image)
			self.preview_button.setEnabled(True)
			try:
				self.shown_image.setPixmap(QtGui.QPixmap(self.path_to_input_image))
			except Exception:
				print("Unable to read or open the selected image")
				return
			
			if "layer" in self.defect_parameters:
				layers = reader.get_layers(self.path_to_input_image)
				self.layer_dropdown = self.centralwidget.findChild(QtWidgets.QComboBox, "para_dropdown_layer")
				self.layer_dropdown.clear()
				self.layer_dropdown.insertItems(0, layers)
	


	def generate_preview(self):
		defect_type = self.current_defect_class # TODO check for subclass with A <- n
		parameters = self.get_parameters()

		mp = MultiProcessor(self.defect_types[defect_type], parameters)
		if self.toggle_accuracy_button.text() == "Fast":
			svg_img = QtGui.QPixmap()
			svg_img.loadFromData(QtCore.QByteArray(mp.preview_defect("svg", self.toggle_bbox_button.isChecked())))
			self.shown_image.setPixmap(svg_img)
		else:
			png_img = QtGui.QPixmap()
			png_img.loadFromData(mp.preview_defect("png", self.toggle_bbox_button.isChecked()))
			self.shown_image.setPixmap(png_img)
		self.clear_preview_button.setEnabled(True)

	def generate_images(self):
		parameters = self.get_parameters()
		amount = int(self.gen_manual_input.text())
		if amount > 0 and self.image_out_dir != "":
			if not self.image_out_dir.endswith("/"):
				self.image_out_dir += "/"
			csv_out_file = reader.get_first_csv_file(self.image_out_dir)
			self.progressBar.setMaximum(amount)
			self.progressBar.setValue(0)
			self.file_progress.setText("0 / " + str(amount))

			defect_type = self.current_defect_class
			mp = MultiProcessor(self.defect_types[defect_type], parameters)
			start_time = time.perf_counter()
			mp.gen_defects(amount, 
						   self.image_out_dir, 
						   csv_out_file,
						   self.progressBar, 
						   self.file_progress)
			end_time = time.perf_counter()
			print(end_time - start_time)
			print("Generation done")

	def browse_output_dir(self):
		try:
			self.invalid_output_dir_error.setText("")
			directory = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Select Output directory", ".")
			if directory != "":
				self.image_out_dir = directory
				self.image_path_input.setPlainText(self.image_out_dir)
				self.generate_button.setEnabled(True)
		except Exception: 
			self.image_out_dir = ""
			self.invalid_output_dir_error.setText("Unable to select output directory")
			self.generate_button.setEnabled(False)

	def input_amount_gen(self, amount):
		self.gen_manual_input.setText(str(amount))

	def get_parameters(self, withSrc=True):
		parameters = {}
		if withSrc:
			# Always append srcImage
			parameters.update({"srcImg":self.path_to_input_image})
		# Find all input QLineEdit parameters
		for qlineEdit in self.centralwidget.findChildren(QtWidgets.QLineEdit):
			if "para_input_" in qlineEdit.objectName():
				parameter_name = qlineEdit.objectName().replace("para_input_","")
				type = self.defect_parameters[parameter_name]["type"]
				if qlineEdit.text() == "":
					qlineEdit.setText("0")
					# slider_
				if type == "int":
					parameters.update({parameter_name: int(qlineEdit.text())})
				else:
					parameters.update({parameter_name: float(qlineEdit.text())})
		# Find all color button input parameters
		for qbutton in self.centralwidget.findChildren(QtWidgets.QPushButton):
			if "para_button_" in qbutton.objectName():
				parameters.update({qbutton.objectName().replace("para_button_",""): qbutton.palette().button().color().name()})
		# Check the dropdowns (for examples layers)
		for qComboBox in self.centralwidget.findChildren(QtWidgets.QComboBox):
			if "para_dropdown_" in qComboBox.objectName():
				parameters.update({qComboBox.objectName().replace("para_dropdown_",""): qComboBox.currentText()})
		return parameters

	def clear_preview(self):
		try:
			self.shown_image.setPixmap(QtGui.QPixmap(self.path_to_input_image))
			self.clear_preview_button.setEnabled(False)
		except Exception:
			print("Unable to read or open the selected image")


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
