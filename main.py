import sys
from src.nameConfigTool import NameConfigToolUI
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = NameConfigToolUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
