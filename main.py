from src.gpx_processor import GPXProcessor
import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def main():
    # Initialize GPX processing
    gpx_processor = GPXProcessor("data/sample_gpx/sample.gpx")
    data = gpx_processor.parse_gpx()
    
    # Initialize GUI
    app = QApplication(sys.argv)
    window = MainWindow(data)
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()