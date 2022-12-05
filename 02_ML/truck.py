import pygame

# Define the size of the window
width = 800
height = 600

# Initialize the Pygame library
pygame.init()

# Create a window with the specified dimensions
window = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Python Truck")

# Define the colors that will be used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the truck cab
cab = pygame.Rect(250, 200, 300, 150)

# Create the truck wheels
wheel1 = pygame.Circle(100, 350, 50)
wheel2 = pygame.Circle(500, 350, 50)

# Create the truck trailer
trailer = pygame.Rect(500, 100, 200, 200)

# Draw the truck cab
pygame.draw.rect(window, WHITE, cab)

# Draw the truck wheels
pygame.draw.circle(window, BLACK, wheel1.center, wheel1.radius)
pygame.draw.circle(window, BLACK, wheel2.center, wheel2.radius)

# Draw the truck trailer
pygame.draw.rect(window, WHITE, trailer)

# Update the screen to display the drawn elements
pygame.display.flip()

# Keep the window open until it is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()