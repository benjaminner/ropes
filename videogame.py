import pygame
import curses 
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ropes Video Game")

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRY      = ( 127, 127, 127)
x = 325
screen.fill(WHITE)
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
     
# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 50, True, True)
    
# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.
text = font.render("RopesVideo Game", True, BLACK)
 
# Put the image of the text on the screen at 250x250
screen.blit(text, [250, 250])

pygame.display.flip()   
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit()
            done = True # Flag that we are done so we exit this loop
            
    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[325,450,75,32.5])
    
    def main(win):
        win.nodelay(True)
        key=""
        win.clear()                
        while 1:          
            try:                 
               key = win.getkey()         
               win.clear()                
               win.addstr("Detected key:")
               win.addstr(str(key)) 
               if key == os.linesep:
                  break           
            except Exception as e:
               # No input   
               pass         

    curses.wrapper(main)
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")