
from flash import *
from werkzeug.utils import * #vThis will help us to import uploading files concept


app=Flask(__name__)
@app.route('/')
def upload():
    return render_template('file_upload.html')
@app.route('/uploader',methods=['POST','GET'])
def uploader():
    if request.method=='post':
        f=request.files['file']
        f.save(secure_filename(f.filename)) #will save to py uploaded files in our folder
    return 'file uploaded sucessfully'
if __name__=='__main__':
    app.run(debug=True)
