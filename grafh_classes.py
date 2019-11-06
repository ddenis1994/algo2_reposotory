class point:

    def __init__(self):
        global outvar
        self.id = str(outvar)
        outvar = outvar+1
        print("made point num : "+str(self.id))

class grafh:
    v=list()
    E={}
