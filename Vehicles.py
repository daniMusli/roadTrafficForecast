class Vehicles:
    tracks = [] # vehicles being tracked 
    def __init__(self, i, xi, yi, max_weight):
        # initialize class attributes 
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        #self.R = randint(0,255)
        #self.G = randint(0,255)
        #self.B = randint(0,255)
        self.done = False
        self.state = '0'
        self.weight = 0
        self.max_weight = max_weight
        self.dir = None
    def getTracks(self):
        return self.tracks
    def getId(self):
        return self.i
    def getState(self):
        return self.state
    def getDir(self):
        return self.dir
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def updateCoords(self, xn, yn):
        self.weight = 0
        self.tracks.append([self.x,self.y])
        self.x = xn
        self.y = yn
    def setDone(self):
        self.done = True
    def timedOut(self):
        return self.done
    def going_UP(self,mid_start,mid_end):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] < mid_end and self.tracks[-2][1] >= mid_end:
                    state = '1'
                    self.dir = 'up'
                    return True
            else:
                return False
        else:
            return False
    def going_DOWN(self,mid_start,mid_end):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] > mid_start and self.tracks[-2][1] <= mid_start: 
                    state = '1'
                    self.dir = 'down'
                    return True
            else:
                return False
        else:
            return False
    def get_weight(self):
        self.weight += 1
        if self.weight > self.max_weight:
            self.done = True
        return True