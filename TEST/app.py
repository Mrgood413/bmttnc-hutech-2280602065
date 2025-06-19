from flask import Flask, render_template, request, Response
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def launch_caesar_script():
    try:
        script_path = os.path.join('C:\\Users\\Administrator\\Desktop\\bmttnc-hutech-2280602065\\TEST', 'caesar_cipher.py')
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return Response(result.stdout, mimetype='text/plain')
        else:
            return Response(result.stderr, mimetype='text/plain', status=500)
    except FileNotFoundError:
        return "File not found", 404

@app.route("/vigenere")
def launch_vigenere_script():
    try:
        script_path = os.path.join('C:\\Users\\Administrator\\Desktop\\bmttnc-hutech-2280602065\\TEST', 'vigenere_cipher.py')
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return Response(result.stdout, mimetype='text/plain')
        else:
            return Response(result.stderr, mimetype='text/plain', status=500)
    except FileNotFoundError:
        return "File not found", 404

@app.route("/railfence")
def launch_railfence_script():
    try:
        script_path = os.path.join('C:\\Users\\Administrator\\Desktop\\bmttnc-hutech-2280602065\\TEST', 'railfence_cipher.py')
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return Response(result.stdout, mimetype='text/plain')
        else:
            return Response(result.stderr, mimetype='text/plain', status=500)
    except FileNotFoundError:
        return "File not found", 404

@app.route("/playfair")
def launch_playfair_script():
    try:
        script_path = os.path.join('C:\\Users\\Administrator\\Desktop\\bmttnc-hutech-2280602065\\TEST', 'playfair_cipher.py')
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return Response(result.stdout, mimetype='text/plain')
        else:
            return Response(result.stderr, mimetype='text/plain', status=500)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
