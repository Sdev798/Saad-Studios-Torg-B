import datetime
import os, random
import pandas as pd
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QMainWindow, QApplication, QCheckBox, QMessageBox, QFrame,
                               QPushButton, QGroupBox, QGridLayout, QScrollArea, QSpacerItem,
                               QHBoxLayout, QLabel, QSizePolicy, QToolButton, QWidget)
import app
import sys, time, threading, json

class POMODORO:
    def __init__(self, window, working_task=None):
        #Change Main Settings For complete our task

        #Gather Settings
        self.pomo_settings = None
        try:
            with open("tmsettings.json", "r+") as tm_settings_f:
                self.pomo_settings = json.loads(tm_settings_f.read())
        except FileNotFoundError:
            default_pomo_settings = {"pomo":30, "break":5, "long_break":15, "loop":4}
            with open('tmsettings.json', "w+") as tm_settings_f:
                json.dump(default_pomo_settings, tm_settings_f)
                tm_settings_f.close()
            self.pomo_settings = default_pomo_settings


        self.time_left = self.pomo_settings['pomo'] * 60
        hours = self.time_left // 3600
        min = self.time_left // 60
        window.ui.label.setText(f"{hours:02}:{min:02}:00")
        self.time_preset = 0 # 0: work 1: break 2:long braekcc
        self.round = 0
        self.long_break_need_round = None
        self.pomo_stop = False



    def check_state(self):
        if self.time_left <= 0:


            self.round = [1 if self.round == 0 else self.round][0]
            self.long_break_need_round = self.round % self.pomo_settings['loop']
            print(self.long_break_need_round, self.round)
            if self.long_break_need_round != 0 and self.time_preset <= 0: #Short Break
                self.time_left = self.pomo_settings['break'] * 60
                self.time_preset = 1
                window.ui.label.setStyleSheet(u"QLabel{\n"
"	border:1px solid rgb(198, 198, 198);\n"
"	border-radius:10px;\n"
"	background-color: rgb(32, 170, 178);\n"
"	font: 300 72pt \"Poppins\";\n"
"\n"
"\n"
"}")
            elif self.long_break_need_round == 0 and self.round > 0 and self.time_preset <= 0: #Long Break
                self.time_left = self.pomo_settings['long_break'] * 60
                self.time_preset = 2
                window.ui.label.setStyleSheet(u"QLabel{\n"
"	border:1px solid rgb(198, 198, 198);\n"
"	border-radius:10px;\n"
"	background-color: rgb(84, 9, 218);\n"
"	font: 300 72pt \"Poppins\";\n"
"\n"
"\n"
"}")
            elif self.time_preset >= 1:
                self.time_left = self.pomo_settings['pomo'] * 60
                self.time_preset = 0
                self.round += 1
                window.ui.label.setStyleSheet("QLabel{\n"
                "	border:1px solid rgb(198, 198, 198);\n"
                "	border-radius:10px;\n"
                "	background-color: rgb(176, 45, 40);\n"
                "	font: 300 72pt \"Poppins\";\n"
                "\n"
                "\n"
                "}")
            window.ui.startpomo.setText("Start")
            hours = self.time_left // 3600
            min = self.time_left // 60
            window.ui.label.setText(f"{hours:02}:{min:02}:00")



            return None
        else:
            return None
    def timer_help_for_start(self):
        threading.Thread(target=lambda: self.start_timer()).start()

    def change_timer_direction(self):
        self.pomo_stop = not self.pomo_stop

    def start_timer(self):
        while self.time_left >= 0:
            if self.pomo_stop:
                break
            countdown = datetime.timedelta(seconds=self.time_left)
            hours = self.time_left // 3600
            minutes = self.time_left // 60
            secs = self.time_left % 60
            window.ui.label.setText(f"{hours:02}:{minutes:02}:{secs:02}")

            time.sleep(1)
            self.time_left -= 1

            print(self.long_break_need_round, self.round, self.time_preset)
        window.ui.label_2.setText(f"#{self.round}")
        return self.check_state()
    def reset_timer(self):
        self.round = 0
        window.ui.label_2.setText(f"#{self.round}")
        if window.ui.startpomo.text() == "Pause":
            self.change_timer_direction()
        self.time_left = self.pomo_settings['pomo'] * 60
        hours = self.time_left // 3600
        min = self.time_left // 60
        window.ui.label.setText(f"{hours:02}:{min:02}:00")
        self.time_preset = 0  # 0: work 1: break 2:long braekcc
        self.long_break_need_round = None
        self.pomo_stop = False

class TaskManagement:
    def __init__(self):
        try:
            self.df_task = pd.read_csv("task_manage.csv")
            self.df_task = self.df_task.set_index("Date")
        except:
            #Creeate new df
            self.df_task = pd.DataFrame({"Date":["WELCOME"],
                                        "Name":["Welcome To torg"],
                                         "Description":["Thank you for choosing our app, if found any bug or glitch just tell as in saadstudios2008@gmail.com"],
                                         "custom_text":["do it man"]})
            self.df_task = self.df_task.set_index("Date")
            self.df_task.to_csv("task_manage.csv")
    def get_all_task_name(self):
        return list(self.df_task['Name']) , list(self.df_task.index), list(self.df_task['custom_text'])

    def create_new_task_item(self, name, description=None, custom_text=None):
        current_time = (datetime.datetime.now()).strftime("%H:%M:%S")
        self.df_task.loc[current_time] = [name, description, custom_text]
        self.df_task.to_csv("task_manage.csv", index=True)
        return current_time

    def complete_task(self, time_date):
        self.df_task = self.df_task.drop(time_date)
        self.df_task.to_csv("task_manage.csv")

class WidgetManager(QWidget):
    def __init__(self):
        super().__init__()
    def fill(self, widget, data, layout_name=None, index=None, check_button_text=None):
        if widget == QScrollArea:
            for item, time_item, custom_text_button in zip(data, index, check_button_text):
                frame = QFrame()
                frame.setObjectName(item)
                frame_layout = QGridLayout()
                add_item_name = QLabel(item)
                add_item_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
                add_item_check_button = QPushButton(["Check" if type(custom_text_button) == float or custom_text_button == "" else custom_text_button][0])
                add_item_check_button.setMinimumSize(QSize(100, 30))
                add_item_check_button.setStyleSheet(f"""
                    QPushButton{{
                        border:3px solid rgb(194, 15, 15);
                        border-radius:5px;
                        background-color:rgb(255, 255, 255);
                    }}
                    QPushButton::hover{{
                        border-color:rgb(0, 209, 101);
                    }}
                    
                """)
                add_item_check_button.setObjectName(time_item)
                add_item_check_button.clicked.connect(lambda : window.complete_task_process(add_item_check_button.objectName()))
                add_item_tool_button = QToolButton()
                add_item_tool_button.setText("...")
                add_item_tool_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                add_item_tool_button.setMinimumSize(QSize(90, 10))
                add_item_time = QLabel(f"{time_item}")
                add_item_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
                add_item_time.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
                add_item_time.setMinimumSize(QSize(90, 10))
                frame_layout.addWidget(add_item_name, 0, 0)
                frame_layout.addWidget(add_item_tool_button, 0, 1)
                frame_layout.addWidget(add_item_check_button, 1, 0)
                frame_layout.addWidget(add_item_time, 1, 1)
                frame.setLayout(frame_layout)
                layout_name.addWidget(frame)

                frame.setStyleSheet(f"""
                QFrame{{
                    border:1px solid rgb(189, 189, 189);
                    border-radius:{random.randint(0, 10)}px;
                }}
                
                """)
            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            layout_name.addItem(spacer)
    def delete_all_items(self, layout_name):
        for widget_position in range(layout_name.count()):
            layout_item = layout_name.itemAt(widget_position)
            try:
                if layout_item.widget() is not None:
                    layout_item.widget().deleteLater()
                elif layout_item.spacerItem():
                    window.ui.gridLayout_8.removeItem(layout_item)
                window.update()
            except:pass

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #App Settings
        self.ui = app.Ui_MainWindow()
        self.ui.setupUi(self)
        self.pomo_service = None
        self.task_management_service = TaskManagement()
        self.widget_service = WidgetManager()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.verify_tab()
        self.task_filling_proccessing()


        #Buttons
        self.ui.nw_task.clicked.connect(lambda: self.prepare_widgets_for_new_data())
        self.ui.addtask.clicked.connect(lambda: self.create_new_task_process(self.ui.taskname_add.text(),
                                                                             description="DELETED CUZ GIT",
                                                                             custom_text=self.ui.checkbuttontext.text()))
        self.ui.tabWidget.currentChanged.connect(lambda :self.verify_tab())
        self.ui.startpomo.clicked.connect(lambda : self.identify_status_pomodoro_and_perform_action())
        self.ui.pushButton.clicked.connect(lambda :self.pomo_service.reset_timer())
        self.ui.settingpomo.hide()
        self.ui.settingpomo.setDisabled(True)


        self.ui.webEngineView.stop()
    #Pomodoro Settings
    def identify_status_pomodoro_and_perform_action(self):
        if self.ui.startpomo.text() == "Pause" or self.ui.startpomo.text() == "Resume":
            if self.pomo_service.time_left >= 1:
                self.pomo_service.change_timer_direction()
                self.ui.startpomo.setDisabled(True)
                self.ui.startpomo.setText(["Resume" if self.ui.startpomo.text() == "Pause" else "Pause"][0])
                threading.Thread(target=lambda :self.protect_button_from_bugs()).start()
                self.pomo_service.timer_help_for_start()
            else:
                self.ui.startpomo.setChecked([False if self.ui.startpomo.isChecked() else True][0])
                self.pomo_service.timer_help_for_start()
        elif self.ui.startpomo.text() == "Start":
            self.ui.startpomo.setDisabled(True)

            self.ui.startpomo.setText("Pause")
            self.pomo_service.timer_help_for_start()
            threading.Thread(target=self.protect_button_from_bugs()).start()

    def protect_button_from_bugs(self):
        time.sleep(0.5)
        self.ui.startpomo.setEnabled(True)
        return None

    def verify_tab(self):
        if self.ui.tabWidget.currentIndex() == 1:
            self.pomo_service = POMODORO(self)
        if self.ui.tabWidget.currentIndex() == 2:
            QMessageBox.critical(self, "P Central Manager", "Sorry this feature is deleted")


    def prepare_widgets_for_new_data(self):
        self.ui.taskname_add.clear()
        self.ui.checkbuttontext.clear()
        self.ui.stackedWidget.setCurrentIndex(1)

    def create_new_task_process(self, name, description=None, custom_text=None):
        task_item_time = (self.task_management_service.create_new_task_item(name=name, description=description, custom_text=custom_text))
        self.task_filling_proccessing()
        self.ui.stackedWidget.setCurrentIndex(0)

    def task_filling_proccessing(self):
        task_data , dates, custom_text = self.task_management_service.get_all_task_name()
        for frame_time, count in zip(dates, range(self.ui.gridLayout_8.count())):
            item = self.ui.gridLayout_8.itemAt(count)
            print(item)
            try:
                if item.widget() is not None:
                    item.widget().deleteLater()
                elif item.spacerItem():
                    self.ui.gridLayout_8.removeItem(item)
                self.update()
            except:pass

        self.widget_service.fill(widget=QScrollArea, layout_name=self.ui.gridLayout_8,
                                 index=dates,
                                 data=task_data,
                                 check_button_text=custom_text)


    def complete_task_process(self, time_date):
        self.task_management_service.complete_task(time_date)
        self.widget_service.delete_all_items(self.ui.gridLayout_8)
        self.task_filling_proccessing()


        



if __name__ == "__main__":
    core = QApplication(sys.argv)
    window = Window()
    window.show()
    core.exec()
