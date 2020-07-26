import image_utils,pyautogui

class reconstruction():

    def __init__(self):
        self.width,self.height = pyautogui.size()

    def get_width(self): return self.width
    def get_height(self): return self.height
