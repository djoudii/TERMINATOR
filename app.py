from flask import Flask, render_template
import xlrd
from xlwt import Workbook
from flask import Flask, request, jsonify
import sys
from Import_script import opening
from Import_script import export
import re
import pickle
from fonctions_terminator import pseudo_main

app = Flask(__name__, static_folder='static')
@app.route('/')
def index():
    return render_template('interface.html')  

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        source = request.form['source']
        processed_data = pseudo_main(source) 
        return render_template('result.html', processed_data=processed_data)
    

if __name__ == '__main__':
    app.run(debug=True)
