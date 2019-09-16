from flask import Flask
from PIL import Image
from PIL import ImageOps
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
from datetime import datetime
import imutils
import time
from cv2 import *
from flask import render_template
import winsound

app = Flask(__name__)


@app.route('/barcode')
def barcode(image):
    image=request.form
    text=""
    image=cv2.imread(image)
    barcodes=pyzbar.decode(image)

    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        barcodeData=barcode.data.decode("utf-8")
        barcodeType=barcode.type
        text="{}({})".format(barcodeData,barcodeType)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    #cv2.imshow("Image",image)
    if(text is not ""):
        text=text.split("(")[0]
        return text
    else:
        return "no barcode found try again"
    stop=time.time()
    return (stop-start)
