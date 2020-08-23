import os
import subprocess
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread

import ConverterDesign

KEY = "ffdsffdsffdsffds"


class FFmpegThread(QThread):
    def __init__(self, main_window, command_h264, command_hevc, parent=None):
        super().__init__()
        self.main_window = main_window
        self.command_h264 = command_h264
        self.command_hevc = command_hevc

    def run(self):
        self.main_window.listWidget.addItem("Running conversion... Please wait...")

        try_h264 = subprocess.Popen(self.command_h264)
        exit_code_h264 = try_h264.wait()
        if exit_code_h264 == 0:
            self.main_window.listWidget.addItem("Conversion completed successfully (h264)")
        try_hevc = subprocess.Popen(self.command_hevc)
        exit_code_hevc = try_hevc.wait()
        if exit_code_hevc == 0:
            self.main_window.listWidget.addItem("Conversion completed successfully (hevc)")
        if exit_code_hevc == exit_code_h264:
            self.main_window.listWidget.addItem("FFmpeg command error. Check FFmpeg installation.")


class AppConverter(QtWidgets.QMainWindow, ConverterDesign.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации UI
        self.file_dir = None
        self.work_dir = os.getcwd()
        self.cmd_h264 = None
        self.cmd_hevc = None
        self.External_command_thread = FFmpegThread(main_window=self, command_h264=self.cmd_h264,
                                                    command_hevc=self.cmd_hevc)

        # обработчик действий
        self.FileSelectButton.clicked.connect(self.browse_videofile)  # Выполнить функцию browse_videofile
        self.action_2.triggered.connect(self.browse_workdir)  # выполнить browse_workdir
        self.h264Button.clicked.connect(self.start_conversion_h264)
        self.action_3.triggered.connect(self.help_window)

    def help_window(self):
        help_message = QMessageBox()
        help_message.setIcon(QMessageBox.Information)
        help_message.setText("Инструкция по работе с конвертером")
        help_message.setInformativeText("1. Выбрать необходимый видеофайл с помощью соответствующей кнопки.\n"
                                        "2. Запустить конвертацию.\n"
                                        "3. Дождаться сообщения об успешном завершении конвертации. \n"
                                        "4. Конвертированное видео будет находиться в той же папке что и программа"
                                        " или в выбранной рабочей директории.\n\n"
                                        "(Для работы скрипта необходима утилита FFmpeg, добавленная в переменные \n"
                                        "параметры среды PATH.)\n"
                                        "https://ffmpeg.zeranoe.com/builds/ - Загрузить FFmpeg. \n"
                                        "https://www.wikihow.com/Install-FFmpeg-on-Windows - Настроить среду PATH.")
        help_message.setWindowTitle("Справка")
        help_message.setStandardButtons(QMessageBox.Ok)

        help_message.exec_()

    def browse_videofile(self):
        self.file_dir = None
        # добавление опций для выбора видеофайла
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        # выбор видеофайла для последующего конвертирования в m3u8
        self.file_dir, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Укажите путь к видеофайлу", "",
                                                                 "Video File (*.mp4)",
                                                                 options=options)

        # print(self.file_dir)
        if self.file_dir:  # не продолжать выполнение, если пользователь не выбрал видеофайл
            self.listWidget.addItem("Selected: " + self.file_dir)

    def browse_workdir(self):
        self.work_dir = None
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.work_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите новую рабочую директорию (в ней "
                                                                         "будут создаваться папки с "
                                                                         "конвертированным видео)")
        print(self.work_dir)

    def start_conversion_h264(self):
        if self.file_dir is None:
            QMessageBox.about(self, "Исходный видеофайл не выбран.", "Укажите путь к видеофайлу.")
        else:
            full_path = self.file_dir  # /path/to/file.mp4
            full_name = os.path.basename(self.file_dir)  # полное имя файла file.mp4
            name = os.path.splitext(full_name)[0]  # имя без расширения file
            new_folder_name = name.replace(" ", "_")
            path = full_path.replace(full_name, new_folder_name)
            try:
                # Создание новой output папки
                os.mkdir(self.work_dir + "\\" + name.replace(" ", "_"))

                # Создание файла key
                key_file_path = self.work_dir + "\\" + name.replace(" ", "_") + "\\" + name.replace(" ", "_") + ".key"
                key_file = open(key_file_path, "w")
                # key_file.truncate()
                key_file.write(KEY)
                key_file.close()

                # Создание файла keyinfo
                keyinfo_file_path = self.work_dir + "\\file.keyinfo"
                keyinfo_file = open(keyinfo_file_path, 'w')
                keyinfo_file.write("\'" + name.replace(" ", "_") + ".key\'\n" + key_file_path)
                keyinfo_file.close()

                # Рабочие комманды для запуска стороннего процесса
                self.cmd_h264 = "ffmpeg -i \"" + full_path + "\" -c copy -bsf:v h264_mp4toannexb -hls_time 10 " + \
                                "-hls_key_info_file \"" + keyinfo_file_path + "\" " + "-hls_list_size 0 " + \
                                name.replace(" ", "_") + "\\" + name.replace(" ", "_") + ".m3u8"

                self.cmd_hevc = "ffmpeg -i \"" + full_path + "\" -c copy -bsf:v hevc_mp4toannexb -hls_time 10 " + \
                                "-hls_key_info_file \"" + keyinfo_file_path + "\" " + "-hls_list_size 0 " + \
                                name.replace(" ", "_") + "\\" + name.replace(" ", "_") + ".m3u8"

                self.listWidget.addItem(self.cmd_hevc)
                self.listWidget.addItem(self.cmd_h264)
                self.listWidget.addItem("...")
                self.listWidget.scrollToBottom()

            except OSError:
                self.listWidget.scrollToBottom()
                self.listWidget.addItem("Command error.")

            else:
                self.listWidget.addItem(f"Command ready.")
                self.External_command_thread.command_h264 = self.cmd_h264
                self.External_command_thread.command_hevc = self.cmd_hevc
                self.listWidget.scrollToBottom()
                # self.h264Button.
                self.launch_command()

    def launch_command(self):
        self.External_command_thread.start()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AppConverter()  # Создаём объект
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
