import os
import shutil
from dataclasses import dataclass
from pathlib import Path

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from util.core_algorithm import GenerateLicense, LicenseType
from util.get_file_version_info import get_file_version_info
from util.Ui_gui import Ui_gui


@dataclass
class LicenseInfo:
    Type: LicenseType
    Count: int
    UserName: str
    MajorVersion: int
    MinorVersion: int


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_gui()
        self.ui.setupUi(self)
        self.setWindowTitle("MobaXterm Keygen v0.1.0")
        self.resize(400, 200)
        self.setMaximumSize(400, 200)
        self.ui.lineEdit_Name.setText(os.getlogin())
        self.ui.spinBox_Major.setRange(1, 99)
        self.ui.spinBox_Major.setValue(24)
        self.ui.spinBox_Minor.setRange(0, 99)
        self.ui.spinBox_Minor.setValue(1)
        self.ui.spinBox_Users.setRange(1, 99)
        self.ui.spinBox_Users.setValue(99)
        self.ui.comboBox_License.addItems(["Professional", "Educational", "Personal"])
        self.mobaxterm_folder_path = Path("C:/Program Files (x86)/Mobatek/MobaXterm")
        self.setup_signals()

    def setup_signals(self):
        self.ui.pushButton_GetVersionfromFile.clicked.connect(
            self.get_mobaxterm_version
        )
        self.ui.pushButton_Activate.clicked.connect(self.activate)

    def get_mobaxterm_version(self):
        mobaxterm_exe_path, _ = QFileDialog.getOpenFileName(
            self, "Open MobaXterm.exe", str(self.mobaxterm_folder_path), "MobaXterm.exe"
        )

        if not mobaxterm_exe_path:
            QMessageBox.warning(
                self, "Error", "Failed to open MobaXterm.exe to get version."
            )
            return

        self.mobaxterm_folder_path = Path(mobaxterm_exe_path).parent
        major, minor, *_ = get_file_version_info(mobaxterm_exe_path)

        if major == -1 or minor == -1:
            QMessageBox.warning(self, "Error", "MobaXterm version error.")
        else:
            self.ui.spinBox_Major.setValue(major)
            self.ui.spinBox_Minor.setValue(minor)

    def activate(self):
        name = self.ui.lineEdit_Name.text() or "Default Name"
        license_type = {
            "Professional": LicenseType.Professional,
            "Educational": LicenseType.Educational,
            "Personal": LicenseType.Personal,
        }[self.ui.comboBox_License.currentText()]
        users = self.ui.spinBox_Users.value()
        major = self.ui.spinBox_Major.value()
        minor = self.ui.spinBox_Minor.value()

        license_info = LicenseInfo(license_type, users, name, major, minor)

        try:
            GenerateLicense(**license_info.__dict__)
            custom_mxtpro_path = Path("Custom.mxtpro")
            shutil.copy2(custom_mxtpro_path, self.mobaxterm_folder_path)
            self.ui.pushButton_Activate.setText(
                "😀 Activated, close this window and restart MobaXterm to take effect."
            )
            self.ui.pushButton_Activate.setEnabled(False)
            self.ui.pushButton_Activate.setStyleSheet(
                "color: #00C589; background-color: #333333;"
            )
            os.remove(custom_mxtpro_path)
        except IOError as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to copy license file to MobaXterm folder. \n\nError message: {e}. \n\nYou can copy the 'Custom.mxtpro' file to \n{self.mobaxterm_folder_path}\n manually.",
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected error: {e}")


def main():
    app = QApplication([])
    main_window = Gui()
    main_window.show()
    app.exec()
