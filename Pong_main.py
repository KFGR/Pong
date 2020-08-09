from Game import*

"""creates a window"""
def Play__Ground():
    win = GraphWin("PONG GAME 1.5", 700,500)
    win.setBackground('black')
    return win,win.getWidth(),win.getHeight()


def lines(window,width,height):
    l = Line(Point(width/2,0),Point(width/2,height))
    l.setWidth(3)
    l.draw(window).setFill('lightgrey')



def main():
    """This main start the game but you cannot change the sources(velocities,sizes,limits...)"""
    window , width , height = Play__Ground()

    pong = Game(window)
    pong.PlayOnegame()
    window.getMouse()
    window.close()
    
main()



"""
Be aware that this is a program based on the game PONG made by Allan Alcorn in 1972.

K.F.F
23/4/2020
"""


