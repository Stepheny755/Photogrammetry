from image_utils import image_utils
import os,cv2
#os.environ['DISPLAY']=':0'
#import pyautogui

class reconstruction():

    def __init__(self):
<<<<<<< Updated upstream
        self.width,self.height = pyautogui.size()

    def get_width(self): return self.width
    def get_height(self): return self.height
=======
        #self.max_width,self.max_height = pyautogui.size()
        self.utils = image_utils()
        img = self.utils.print_screen((100,10,400,700))
        cv2.imwrite("test.png",img)
    #def move


if(__name__=="__main__"):
    #print(pyautogui.size())
    reconstruction()
>>>>>>> Stashed changes
