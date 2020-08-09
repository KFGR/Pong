#Paddle class
from Ball import*
class Paddle(Ball):
    """A paddle is drawn using Rectangle class in graphics, it have the name
        of the window, 2 points and a color as a parameter"""
    def __init__(self,win,pt1,pt2,color='Black'):
        self.win = win
        self.color = color
        self.obj = Rectangle(pt1,pt2)
        self.obj.setFill(color)
        self.obj.draw(win)
        
    def getP1(self):
        """Returns the first point of the object"""
        return self.obj.getP1()
    
    def getP2(self):
        """Returns the second point of the object"""
        return self.obj.getP2()
    
    def control(self,key,letter1="",letter2=""):
        """Move the object 50 units down and -50 units up"""
        #key = self.win.checkKey()
        if key == str(letter1):
            self.move(0,-50)
        if key == str(letter2):
            self.move(0,50)

    def setControl(self,key,letter1='',letter2=''):
        """Allows to manipulate the velocity in Y axis for the movemment of the object,
            and returns it"""
        vel = 1
        if key == str(letter1):
            vel  *= -1
        if key == str(letter2):
            vel *= -1
        return vel

    def setYlimit(self,vel):
        """stop the object when this has reach the maximun or minimun in Y axis,
            allows manipulate the velocity for stopping the object"""
        if (self.getY() <= self.getHeight()/2):
            self.move(0,vel)
        elif (self.getY() >= self.win.getHeight() - self.getHeight()/2):
            self.move(0,-vel)
