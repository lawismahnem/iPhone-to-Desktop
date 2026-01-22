import os
import socket
from datetime import datetime
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 16GB limit effectively disables the limit for most phone transfers
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  

def get_local_ip():
    try:
        # Connect to an external server (doesn't actually send data) to get the local interface IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    files = request.files.getlist('files[]')
    
    saved_files = []
    
    # Create date-based folder
    today_str = datetime.now().strftime('%Y-%m-%d')
    target_dir = os.path.join(app.config['UPLOAD_FOLDER'], today_str)
    os.makedirs(target_dir, exist_ok=True)
    
    for file in files:
        if file.filename == '':
            continue
        
        filename = file.filename
        # Save exact filename; could add secure_filename() but user wants "exact same"
        # and this is a local private tool.
        file_path = os.path.join(target_dir, filename)
        
        # Handle duplicate filenames by appending a counter
        if os.path.exists(file_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(file_path):
                file_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                counter += 1
                
        file.save(file_path)
        saved_files.append(os.path.basename(file_path))
        print(f"Received: {file.filename} -> {os.path.basename(file_path)}")

    return jsonify({'message': f'Successfully uploaded {len(saved_files)} files', 'files': saved_files})

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5000
    print(f"\n YOUR APP IS RUNNING! \n")
    print(f" -> On your Desktop, files will appear in: {os.path.abspath(UPLOAD_FOLDER)}")
    print(f" -> On your iPhone, open Safari and go to: http://{local_ip}:{port}")
    print(f"\n---------------------------------------------------------\n")
    app.run(host='0.0.0.0', port=port, debug=False)
