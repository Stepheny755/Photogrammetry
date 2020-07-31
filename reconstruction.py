import subprocess,os

class reconstruction():

    def __init__(self):
        self.script_name = "run.bat"
        pass

    def run_auto_reconstruction(self,work_path,image_path):
        if not (os.path.exists(work_path)):
            os.makedirs(work_path)
        subprocess.call([self.script_name,work_path,image_path])


if(__name__=="__main__"):
    r = reconstruction()
    r.run_auto_reconstruction("data\workspace1v2","data\photos1")
