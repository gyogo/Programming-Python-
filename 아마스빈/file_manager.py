import pickle

class FileManager():
    def __init__(self,filename):
        self.filename = filename
    def save(self,data):
        with open(self.filename,"wd") as f:
            pickle.dump(data.f)
    def load(self):
        try:
            with open(self.filename,"rb") as f:
                data = pickle.load(f)
        except FileNotFoundError:
            print("내역이 없스비다.")
        print("----------------------------------------------------")
        return data