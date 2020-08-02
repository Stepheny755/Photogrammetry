import subprocess
import os
import skimage.exposure as skie
from wand.image import Image

class reconstruction():

    def __init__(self):
        self.script_name = "run.bat"
        pass

    def run_auto_reconstruction(self,work_path,image_path):
        if not (os.path.exists(work_path)):
            os.makedirs(work_path)
        subprocess.call([self.script_name,work_path,image_path])

    def run_preprocessing(self,image_path):
        for f in os.listdir(path):
            with Image(filename=f) as img:
                img = np.array(img)

if(__name__=="__main__"):
    r = reconstruction()
    r.run_preprocessing("data\drive-download-20200716T225425Z-001")
