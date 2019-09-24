import os
import subprocess
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

returnString = "GRADING RESULT:"

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      retcode = subprocess.call("./test.sh", shell=True)
      return returnString + "\n Score: " + str(retcode) + " out of 2 correct."
		
if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 80, debug = True)
