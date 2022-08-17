import sys
import argparse

from PySide6.QtWidgets import QApplication

from mainWindow import MainWindow
from radar import Radar


def main(debug_mode=False):
    app = QApplication([])
    radar = Radar() if not debug_mode else None
    win = MainWindow(radar)
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug',  action="store_true", help='debug mode')
    args = parser.parse_args()
    main(debug_mode=args.debug)
