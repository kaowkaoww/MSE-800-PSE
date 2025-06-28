from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

#create a directory for static files if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

#main route to display the upload form
@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload Image - Activity W12-2</title>
        <style>
            body { font-family: Arial; text-align: center; margin: 50px; }
            h1 { color: #333; }
            input[type="file"] { margin: 20px; padding: 10px; }
            input[type="submit"] { 
                background: #007bff; color: white; 
                padding: 10px 20px; border: none; border-radius: 5px; 
            }
        </style>
    </head>
    <body>
        <h1>Upload Your Image</h1>
        <p>Activity W12-2 by Manisa</p>
        
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required>
            <br><br>
            <input type="submit" value="Upload Image">
        </form>
    </body>
    </html>
    '''
    return html

# Route to handle image upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        file = request.files['image']
        if file.filename != '':
            #save the file to the static directory
            filename = file.filename
            file.save(os.path.join('static', filename))
            
            #show success message with the uploaded image
            html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Image Uploaded!</title>
                <style>
                    body {{ font-family: Arial; text-align: center; margin: 50px; }}
                    img {{ max-width: 500px; border: 2px solid #ddd; margin: 20px; }}
                    a {{ 
                        background: #007bff; color: white; 
                        padding: 10px 20px; text-decoration: none; 
                        border-radius: 5px; margin: 10px;
                    }}
                </style>
            </head>
            <body>
                <h1>Upload Success!</h1>
                <p>Your image:</p>
                <img src="/static/{filename}" alt="Uploaded Image">
                <br><br>
                <a href="/">Upload Another Image</a>
            </body>
            </html>
            '''
            return html
    
    return "No file uploaded!"

if __name__ == '__main__':
    app.run(debug=True)