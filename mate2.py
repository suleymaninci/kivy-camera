
# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)
import cv2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import cv2
from PIL import Image, ImageDraw, ImageFilter

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (584, 620)
        play: False
    ToggleButton:
        text: 'Play/Stop  (foto cekmeden once stop basınız)'
        background_color: (242/255,143/255,58/255,1)
        background_normal:''
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture and Add frame'
        background_color: (88/255,139/255,139/255,1)
        background_normal:''
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Button:
        text: 'Close'
        background_color: (200/255,88/255,58/255,1)
        background_normal:''
        size_hint_y: None
        height: '48dp'
        on_press: root.close()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        # import time
        
        cam = cv2.VideoCapture(0)

        ret, frame = cam.read()
        
        timestr = time.strftime("%Y%m%d_%H%M%S")
        fr=Image.open('fr2.png')
        offset=(110,90)
        img2=cv2.resize(frame,(584,620))
        
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img2=Image.fromarray(img2,mode='RGB')
        
        
        
        fr.paste(img2,offset)
        # cv2.imshow("test",fr)
        img_name = "output_frame_{}.png".format(timestr)
        fr.save(img_name)
        cam.release()
        
        return print("{} written!".format(img_name))
        # return CameraClick().add_frame(self)
        # timestr = time.strftime("%Y%m%d_%H%M%S")
        # imgn="IMG_{}.png".format(timestr)
        # camera.export_to_png(imgn)
    def close(self):
        App.get_running_app().stop()
        
        
        
        

class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()

"""
import time
import cv2
from PIL import Image, ImageDraw, ImageFilter

cam = cv2.VideoCapture(0)

img_counter = 0
ret, frame = cam.read()

from PIL import Image, ImageDraw, ImageFilter
timestr = time.strftime("%Y%m%d_%H%M%S")
fr=Image.open('fr2.png')
back=fr.copy()
offset=(110,90)
img2=cv2.resize(frame,(584,620))

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2=Image.fromarray(img2,mode='RGB')



fr.paste(img2,offset)
# cv2.imshow("test",fr)
img_name = "output_frame_{}.png".format(timestr)
fr.save(img_name)
print("{} written!".format(img_name))

cam.release()

# cv2.destroyAllWindows()
"""
