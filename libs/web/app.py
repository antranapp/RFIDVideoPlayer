from flask import Flask, render_template, request
import hashlib
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('download_video.html')

@app.route('/download_video', methods=['POST'])
def download_video():
    youtube_url = request.form['youtube_url']
    hash_object = hashlib.md5(youtube_url.encode('utf-8'))
    hash_string = hash_object.hexdigest() + '.mp4'
    #command_download = "youtube-dl -o '{0}' -f 22 '{1}'".format(hash_string, youtube_url)
    try:
        #result_success = subprocess.check_output([command_download], shell=True)
        return render_template('register_card.html', filename = hash_string)
    except subprocess.CalledProcessError as e:
        return "An error occurred while trying to download youtube video"
    
@app.route('/register_card', methods=['POST'])
def register_card():
    os.system('python write.py')
    return "Done"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')