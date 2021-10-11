import os, sys, glob, cv2
import pandas as pd
from typing import List, Dict, Tuple, Callable
from PySide2.QtWidgets import QApplication, QFileDialog, QInputDialog, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QShortcut
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QImage, QKeySequence, QPixmap
from Ui_Form import Ui_Form

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Form(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.label_count: int = 0
        self.img_folder: str = ''
        self.output_file: str = ''
        self.img_list: List[str] = []
        self.active_img_list: List[str] = []
        self.current_index: int = 0
        self.img_labels: Dict[str, int] = {}

        self.setupUi(self)
        self.setupSignalSlots()
        self.setupKeyboardShortcuts()

        self.key_label_widget_mapping: Dict[str, Tuple[int, QPushButton]] = {
            'A': (0, self.btn_label_A),
            'S': (1, self.btn_label_S),
            'D': (2, self.btn_label_D),
        }
        self.label_widget_mapping: Dict[str, QPushButton] = {
            str(label): btn for key, (label, btn) in self.key_label_widget_mapping.items()
        }
        # testing
        # self.open_img_folder()

    def keyPressEvent(self, event):
        super(Form, self).keyPressEvent(event)
        self.on_key(event.key())

    def setupSignalSlots(self):
        self.btn_img_folder.clicked.connect(self.open_img_folder)
        self.btn_output_file.clicked.connect(self.set_output_file)
        self.tbl_browser.cellClicked.connect(self.go_to_image)
        self.btn_label_A.clicked.connect(self.label_btn_clicked)
        self.btn_label_S.clicked.connect(self.label_btn_clicked)
        self.btn_label_D.clicked.connect(self.label_btn_clicked)
        self.btn_edit_classA.clicked.connect(self.set_class_nameA)
        self.btn_edit_classS.clicked.connect(self.set_class_nameS)
        self.cmb_browser_filter.currentIndexChanged.connect(self.populate_table)

    def setupKeyboardShortcuts(self):
        self.shortcut_save = QShortcut(QKeySequence('Ctrl+S'), self)
        self.shortcut_save.activated.connect(self.save_labels)
        self.shortcut_next_img = QShortcut(QKeySequence('right'), self)
        self.shortcut_next_img.activated.connect(self.next_img)
        self.shortcut_prev_img = QShortcut(QKeySequence('left'), self)
        self.shortcut_prev_img.activated.connect(self.prev_img)

    def set_class_nameA(self):
        text, ok = QInputDialog.getText(self, 'Set Class Name', 'Class Name:', QLineEdit.Normal)
        if ok:
            self.btn_label_A.setText(text)

    def set_class_nameS(self):
        text, ok = QInputDialog.getText(self, 'Set Class Name', 'Class Name:', QLineEdit.Normal)
        if ok:
            self.btn_label_S.setText(text)

    def set_output_file(self):
        fn, _ = QFileDialog.getOpenFileName(self, 'Open labels', "", "CSV (*.csv)")
        if fn != '':
            self.read_output_file(fn)

    def read_output_file(self, file_path):
        df = pd.read_csv(file_path, index_col='File path')
        self.output_file = file_path
        self.img_labels = df.to_dict('index')
        self.img_labels = {key: column_label_dict['0'] for key, column_label_dict in self.img_labels.items()}
        self.lbl_output_file.setText(file_path)

    def open_img_folder(self):
        folder = QFileDialog.getExistingDirectory()
        if folder != '' :
            self.img_folder = folder   
            img_path_list = sorted(
                glob.glob(os.path.join(folder, "*.png")),
                key=lambda x: int(x[:-4].split("-")[-1]),
            )
            self.img_list = [img_path.split(os.sep)[-1] for img_path in img_path_list]
            self.active_img_list = self.img_list
            self.display_img(0)

            try:
                label_file = os.path.join(folder, 'labels.csv')
                self.read_output_file(label_file)
            except:
                pass

            self.populate_table(3)
            self.lbl_image_folder.setText(folder)

    def populate_table(self, filter:int =3):
        self.tbl_browser.clear()
        self.tbl_browser.setHorizontalHeaderLabels(['Image', 'Label'])
        self.current_index = 0

        if filter == 3:
            self.active_img_list = self.img_list
        elif filter == 4:
            self.active_img_list = [img_name for img_name in self.img_list if self.img_labels.get(img_name) == None]
        else:
            self.active_img_list = [img_name for img_name in self.img_list if self.img_labels.get(img_name) == filter]

        self.tbl_browser.setRowCount(len( self.active_img_list))
        for i, img_name in enumerate( self.active_img_list):
            label = self.img_labels.get(img_name)
            if label is None:
                label = ''
            path_item = QTableWidgetItem()
            label_item = QTableWidgetItem()
            path_item.setText(img_name)
            label_item.setText(str(label))
            self.tbl_browser.setItem(i,0,path_item)
            self.tbl_browser.setItem(i,1,label_item)
    
    def go_to_image(self, row: int, col: int):
        self.current_index = row
        self.display_img(row)
        self.setFocus()

    def display_img(self, index):
        img_path = os.path.join(self.img_folder, self.active_img_list[index])
        frame = cv2.imread(img_path)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h,w,ch = frame.shape
        qimage = QImage(frame.data, w, h, ch*w, QImage.Format_RGB888)
        img = QPixmap.fromImage(qimage)
        img = img.scaled(self.lbl_img.size(), Qt.KeepAspectRatio)
        self.lbl_img.setPixmap(img)
        self.lbl_img_name.setText(self.active_img_list[index])

        # highlight button if labeled
        label = self.img_labels.get(self.active_img_list[index])
        for lbl, btn in self.label_widget_mapping.items():
            if label == int(lbl):
                btn.setCheckable(True)
                btn.setChecked(True)
            else:
                btn.setChecked(False)
                btn.setCheckable(False)

        # highlight row in table
        self.tbl_browser.selectRow(index)

    def save_labels(self):
        df = pd.DataFrame.from_dict(self.img_labels, orient='index')
        if self.output_file == '':
            fn = os.path.join(self.img_folder, 'labels.csv')
        else:
            fn = self.output_file
        df.to_csv(fn, index_label='File path')
        self.lbl_output_file.setText(fn)
        self.lbl_status_msg.setText('Save successful!')

    def on_key(self, key:Qt.Key):
        if key == Qt.Key.Key_A or key == Qt.Key.Key_S or key == Qt.Key.Key_D:
            key_string = chr(int(key.__str__()))
            btn = self.key_label_widget_mapping[key_string][1]
            btn.animateClick(100)

    def label_btn_clicked(self):
        btn = self.sender()
        for key, (label, btn_widget) in self.key_label_widget_mapping.items():
            if btn is btn_widget:
                self.label_img(label)
                return
        
    def label_img(self, label):
        if len(self.img_list) > 0:
            self.img_labels[self.active_img_list[self.current_index]] = label
            
            # update table
            label_item = self.tbl_browser.item(self.current_index, 1)
            label_item.setText(str(self.img_labels[self.active_img_list[self.current_index]]))
            self.next_img()

            # perform autosave
            self.label_count += 1
            if self.label_count == 10:
                self.save_labels()
                self.label_count = 0
    
    def next_img(self):
        self.current_index += 1
        self.update_img()

    def prev_img(self):
        self.current_index -= 1
        self.update_img()

    def update_img(self):
        self.current_index = self.current_index % len(self.active_img_list)
        self.display_img(self.current_index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec_())