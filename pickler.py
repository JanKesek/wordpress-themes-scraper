import pickle
class Pickler:
    def __init__(self,name):
        self.name=name
    def save(self, obj, name):
            pickle_out=open(name + ".pickle", "wb")
            pickle.dump(obj, pickle_out)
            pickle_out.close()
    def retrieve(self):
        pickle_in=open(self.name+ ".pickle", "rb")
        return pickle.load(pickle_in)

