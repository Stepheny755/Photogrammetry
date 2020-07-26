from image_utils import image_utils
import os,cv2
#os.environ['DISPLAY']=':0'
#import pyautogui

class reconstruction():

    def __init__(self):
        self.width,self.height = pyautogui.size()
        self.utils = image_utils()
        img = self.utils.print_screen((100,10,400,700))
        cv2.imwrite("test.png",img)

    def get_width(self): return self.width
    def get_height(self): return self.height


if(__name__=="__main__"):
    r = reconstruction()
