from flask import Flask, render_template
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt5.QtCore import QTimer
from threading import Thread
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('interface.html')

if __name__ == '__main__':
    app.run(debug=True)

