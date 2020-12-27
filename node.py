class Node:
    def __init__(self, parent=None, state=None, path=None,  g=0, h=0):
        self.parent = parent
        self.state = state
        self.path = path
        self.g = g
        self.h = h
        self.f = g + h

    def __eq__(self, obj):
        try:
            if(self.parent == obj.parent and self.state == obj.state):
                return True
            else:
                return False
        except:
            return False