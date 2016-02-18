# -*- coding: utf-8 -*-

import os
import mimetypes
from tempfile import mktemp
from werkzeug.utils import secure_filename
from flask import Flask, jsonify,request, render_template, redirect, url_for
import ctypes
from ctypes import *
import os.path 
import shutil 
import time,  datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'static/Uploads'
select_bank = 1
select_pic  = 1
SOURCE_FOLDER = 'static/compute'
ALLOWED_MIMETYPES = {'image/jpeg', 'image/png', 'image/gif'}
func = cdll.LoadLibrary('ocrDLL.dll')
Index_pic = ['login.jpg','abc1.jpg','abc2.gif','abc3.jpg','abc4.jpg','abc5.jpg','abc6.jpg','abc7.jpg', \
'abc8.jpg','abc9.jpg','abc10.jpg','abc11.jpg','abc12.jpg','abc13.jpg']
result_pic = ['login.jpg','abc1.jpg','abc2.gif','abc3.jpg','abc4.jpg','abc5.jpg','abc6.jpg','abc7.jpg', \
'abc8.jpg','abc9.jpg','abc10.jpg','abc11.jpg','abc12.jpg','abc13.jpg']


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
            return render_template('upload.html',img='%s/%s'%(UPLOAD_FOLDER,Index_pic[0]),img2='%s/%s'%(UPLOAD_FOLDER,Index_pic[1]))
    elif request.method == 'POST':
        #str0 = func.show()
        #size = -1
        #str0 = ctypes.string_at(str0,size)
        #str1 = str0.decode('utf-8')
        #result_pic = str1.split(',')
        #print(str1)
        
        str0 = func.initLibrary()
        f = request.files['file']
        #fname = mktemp(suffix='_', prefix='u', dir=UPLOAD_FOLDER) + \
        #    secure_filename(f.filename)
        #***************Get the name of Uploaded
        fname = secure_filename(f.filename)
        dir_f = 'static/Uploads/'
        fname_dir = dir_f+fname
        f.save(fname_dir)
        
        #process the file Uploaded
        os_path="<root><elem imgPath=\"D:\\Anaconda2.7\\Test_del\\static\\Uploads\\%s\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"李四\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>"%fname
        str1 = func.ocr(os_path,"")
        #str1 = func.ocr("<root><elem imgPath=\"D:\\Anaconda2.7\\Test_del\\static\\Uploads\\anxingle3.jpg\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"李四\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>","")
        shutil.copy("D:/Anaconda2.7/Test_del/binImage.jpg","D:/Anaconda2.7/Test_del/static/compute/%s"%fname)
        if mimetypes.guess_type(fname)[0] in ALLOWED_MIMETYPES:
            return render_template('upload.html',img=fname_dir,img2="static/compute/%s"%fname)
        else:
            os.remove(fname)
            return redirect(url_for('upload'), 302)


@app.route('/pro', methods=['GET', 'POST'])
def pro():
    if request.method == 'GET':
        return render_template('upload.html',img='%s/%s'%(UPLOAD_FOLDER,Index_pic[0]),img2='%s/%s'%(UPLOAD_FOLDER,Index_pic[1]))
    elif request.method == 'POST':
    	username = request.form.get('name_in')
        return "I love Jesus because Jesus love me first! %s" % username

@app.route('/')
def index():
    return redirect(url_for('upload'), 302)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
