from __future__ import print_function
import sys
from flask import Flask, render_template, request
import hashlib
import subprocess
import os
from shutil import move

app = Flask(__name__)

videos_path = "/home/pi/Videos/"
#videos_path = "/tmp/"

@app.route('/')
def index():
    return render_template('download_video.html')

@app.route('/download_video', methods=['POST'])
def download_video():
    youtube_url = request.form['youtube_url']
    hash_object = hashlib.md5(youtube_url.encode('utf-8'))
    hash_string = hash_object.hexdigest() + '.mp4'
    #hash_string = "b56e60c61d72efd4022b7949f9b3a880.mp4"
    command_download = "youtube-dl -o '{0}' -f 22 '{1}'".format(hash_string, youtube_url)
    try:
        status = subprocess.check_output([command_download], shell=True)
        #status = "mock"
        move(hash_string, videos_path + hash_string)
        return render_template('register_card.html', status = status, filename = hash_string)
    except subprocess.CalledProcessError as e:
        return "An error occurred while trying to download youtube video"
    
@app.route('/register_card', methods=['POST'])
def register_card():
    filename = request.form['filename']
    print(filename, file=sys.stdout)
    os.system('python write.py ' + filename)
    return "Done"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')