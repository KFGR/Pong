#Balll class

from graphics import*
  
class Ball:
    """A Ball is drawn using the Rectangle obj in graphics, it have the name
        of the window and a color as parameters"""
    def __init__(self,win,color='black'):
        self.win = win
        w , h = self.win.getWidth() , self.win.getHeight()
        self.color = color
        self.obj = Rectangle(Point(w/2,h/2),Point(w/2+15,h/2+15))
        self.obj.setFill(color)
        self.obj.draw(win)
        
    
    def getHeight(self):
        """Returns the height of the object"""
        return abs(self.obj.getP1().getY() - self.obj.getP2().getY())
    
    def getWidth(self):
        """Returns the width of the object"""
        return abs(self.obj.getP1().getX() - self.obj.getP2().getX())
    
    def getX(self):
        """Returns the center Point in X axis"""
        return self.obj.getCenter().getX()
    
    def getY(self):
        """Returns the center Point in Y axis"""
        return self.obj.getCenter().getY()
    
    def getCenter(self):
        """Returns the center of the object"""
        return self.obj.getCenter()

    def move(self,dx=0,dy=0):
        """Move the object dx units in x axis and dy units in y axis"""
        self.obj.move(dx,dy)
    
    def delete(self):
        """Delete an instance created"""
        return self.obj.undraw()

    def Ylimit(self):
        """Changes the velocity in Y axis of the instance to negative"""
        vel = 1
        if (self.getY() <= self.getHeight()/2) or (self.getY() >= self.win.getHeight() - self.getHeight()/2):
            vel *= -1
        return vel
    
        
    def colission(self,paddle):
        vel = 1
        
        if((self.getCenter().getX() > paddle[1].getP2().getX() and self.getCenter().getX() < paddle[1].getP1().getX())
        and (self.getCenter().getY() < paddle[1].getCenter().getY() + paddle[1].getHeight()/2
             and self.getCenter().getY() > paddle[1].getCenter().getY() - paddle[1].getHeight()/2)):
            vel *= -1
            
        elif ((self.getCenter().getX() > paddle[0].getP1().getX() and self.getCenter().getX() < paddle[0].getP2().getX())
              and (self.getCenter().getY() < paddle[0].getCenter().getY() + paddle[0].getHeight()/2
              and self.getCenter().getY() > paddle[0].getCenter().getY() - paddle[0].getHeight()/2)):
            vel *= -1
            
        return vel
