from graphics import*
from Ball import*
from Paddle import*

class Game():
    def __init__(self,win):
        self.win = win
        self.width = win.getWidth()
        self.height = win.getHeight()
        self.pt1 , self.pt2 = self.width/2 , self.height/2
        self.Line = Line(Point(self.pt1,0),Point(self.pt1,self.height))
        self.Line.setWidth(3)
        

        
    def delete(self):
        """Delete an instance created"""
        return self.obj.undraw()

    def Text(self,pt,txt,color=''):
        """Draws a text somewhere in the window"""
        self.obj = Text(pt,txt) ; self.obj.setTextColor(color)
        self.obj.setFace('helvetica') ; self.obj.setSize(16)
        self.obj.setStyle('bold') ; self.obj.draw(self.win)

    def instruction(self,name1,name2):
        """Set the game instructions for each player"""
        self.Text(Point(self.pt1,self.pt2),"{0} use lower case 'w' to move up the paddle \n and lower case 's' to move down the paddle\n\n"
                  " {1} use the arrow 'Up' to move up the paddle \n and the arrow 'Down' to move down the paddle\n\n"
                  "Click on the screen to play...".format(name1.title(),name2.title()),"white")
        self.win.getMouse()
        self.delete()
        

    def getNames(self):
        """Display an entry box for 2 usernames, shows the instructions and returns both usernames"""
        n1 , n2 = '' , ''
        inputBox = Entry(Point(self.pt1,self.pt2),15)
        inputBox.setText('Player1_name')
        inputBox.draw(self.win)
        
        for i in range (1):
            self.win.getMouse()
            n1 = inputBox.getText()
            inputBox.setText('Player2_name')
            self.win.getMouse()
            n2 = inputBox.getText()
            inputBox.undraw()
            
        self.instruction(n1,n2)
        return n1,n2

    def Score(self,ball,points):
        """Add a point to a player if the ball passes X limit and move the ball to the middle of the screen
            ex: if ball >= window width: add 1 point to player 1"""
        if ball.getX() - ball.getWidth()/2 == 0.0:
            ball.move(self.pt1,0)
            points[1]+=1
        elif ball.getX() + ball.getWidth()/2 == self.width:
            ball.move(-self.pt1,0)
            points[0]+=1
    
    def gameOver(self,points):
        """Returns false if the game is not over"""
        return points[0]==3 or points[1]==3

    def getWinner(self,points,players):
        """Announce the winner """
        if points[0]==3 and points[0] > points[1]:
            Text(Point(self.pt1/2,self.pt2),players[0] + ' won the match').draw(self.win).setFill('white')
        elif points[1]==3 and points[1] > points[0]:
            Text(Point(self.win.getWidth()/1.33,self.pt2),players[1] + ' won the match').draw(self.win).setFill('white')

            
    def pongBasic(self,ball,bspeed,paddles):
        """Contains the basic movemment of pong game and allows
            to change the game sources (velocities,sizes,limits...)
            NOTE: bspeed and paddles are arrays or lists"""
        update(150)
        key = self.win.checkKey()

        ball.move(bspeed[0],bspeed[1])
        paddles[0].control(key,'w','s')
        paddles[1].control(key,'Up','Down')

        bspeed[1] *= ball.Ylimit()
        paddles[0].setYlimit(10)
        paddles[1].setYlimit(10)

        bspeed[0] *= ball.colission(paddles)


    def PlayOnegame(self):
        """This method lets you play the game with all the sources by default,
            this means that you can only change the size of the window,
            another method gives you the ability to change the sources (velocities,sizes,limits...)"""
        Lscore = Game(self.win) ; Rscore = Game(self.win)
        players = [] ; players = self.getNames()
        
        self.Line.draw(self.win).setFill('white')

        ball = Ball(self.win,'White')
        paddles = [Paddle(self.win,Point(self.width/80,self.pt2+50),Point(self.width/40,self.pt2-50),'white'),
                   Paddle(self.win,Point(self.width-10,self.pt2+50),Point(self.width-20,self.pt2-50),'white')]
        bspeed = [1,1]
        points = [0,0]
        
        self.Text(Point(self.width/5 , 20),players[0].upper() + ':','white')
        Lscore.Text(Point(self.width/5+100 , 20),str(points[0]),'white')
        self.Text(Point(self.width/1.50 , 20),players[1].upper() + ':','white')
        Rscore.Text(Point(self.width/1.50+100 , 20),str(points[1]),'white')
        
        L,R=0,0
        
        while not self.gameOver(points):
            self.pongBasic(ball,bspeed,paddles)
            self.Score(ball,points)
            if points[0] != L:
                Lscore.delete()
                Lscore.Text(Point(self.width/5+100 , 20),str(points[0]),'white')
                L += 1
            if points[1]!=R:
                Rscore.delete()
                Rscore.Text(Point(self.width/1.50+100 , 20),str(points[1]),'white')
                R+=1
            if self.gameOver(points):
                self.getWinner(points,players)
