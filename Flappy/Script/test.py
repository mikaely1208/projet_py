import pygame
import random
pygame.init()

# Create colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create screen and set screen caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Loop until user clicks close button
done = False

# Used to manage how fast the screen is updated
clock = pygame.time.Clock()

# Create player class
class Player():

    # Initialize player paddles
    def __init__(self, x, y, color, height, width):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = width
        self.y_speed = 0
        self.score = 0
        self.font = pygame.font.SysFont('Calibri', 24, True, False)
        self.display_score = self.font.render("Score: %d " % (self.score), True, WHITE)

    # Updates with new position of paddle every frame
    def draw(self, y):
        pygame.draw.rect(screen, self.color, [self.x, y, self.height, self.width])

    # Keeps paddle from going off screen
    def keepOnScreen(self):
        if self.y < 0:
            self.y = 0
        elif self.y > 410:
            self.y = 410

# Create Ball class
class Ball():

    # Initialize ball in the middle of the screen with no movement
    def __init__(self, color, height, width):
        self.x = 325
        self.y = random.randrange(150, 350)
        self.color = color
        self.height = height
        self.width = width
        self.y_speed = 0
        self.x_speed = 0

    # Updates new position of ball every frame
    def draw(self, x, y):
        pygame.draw.rect(screen, self.color, [x, y, self.height, self.width])

# Create instances of both players and ball
player1 = Player(50, 100, WHITE, 25, 90)
player2 = Player(625, 100, WHITE, 25, 90)
ball = Ball(WHITE, 20, 20)

# --- Main Program Loop ---
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # We are done so we exit this loop

        if event.type == pygame.KEYDOWN: # Players utilize keyboard to move paddles
            if event.key == pygame.K_w:
                player1.y_speed = -6
            if event.key == pygame.K_UP:
                player2.y_speed = -6
            if event.key == pygame.K_s:
                player1.y_speed = 6
            if event.key == pygame.K_DOWN:
                player2.y_speed = 6
            if event.key == pygame.K_SPACE: # Starts the ball movement
                ball.x_speed = 3 * random.randrange(-1, 1, 2)
                ball.y_speed = 3 * random.randrange(-1, 1, 2)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.y_speed = 0
            if event.key == pygame.K_UP:
                player2.y_speed = 0
            if event.key == pygame.K_s:
                player1.y_speed = 0
            if event.key == pygame.K_DOWN:
                player2.y_speed = 0

    # Calculate the movement of the players
    player1.y += player1.y_speed
    player2.y += player2.y_speed

    # Prevents paddles from going off-screen
    player1.keepOnScreen()
    player2.keepOnScreen()

    # Checks to see if ball has made contact with paddle, then reverses direction of the ball
    # Had to give a 4 pixel buffer since the ball won't always exactly hit the same part of paddle in x direction
    if ball.x <= player1.x + 27 and (ball.x >= player1.x + 23):
        if ball.y >= player1.y and (ball.y <= player1.y + 100):
            ball.x_speed *= -1
    if ball.x >= player2.x - 27 and (ball.x <= player2.x - 23):
        if ball.y >= player2.y and (ball.y <= player2.y + 100):
            ball.x_speed *= -1

    # Checks to see if ball has made contact with top or bottom of screen
    if ball.y <= 0 or ball.y >= 480:
        ball.y_speed *= -1

    # Calculates movement of the ball
    ball.x += ball.x_speed
    ball.y += ball.y_speed

    # Updates score
    if ball.x < 0:
        player2.score += 1
        ball.__init__(WHITE, 20, 20)

    if ball.x > 700:
        player1.score += 1
        ball.__init__(WHITE, 20, 20)

    # Set background
    screen.fill(BLACK)

    # Draw players and ball on screen
    player1.draw(player1.y)
    player2.draw(player2.y)
    ball.draw(ball.x, ball.y)
    screen.blit(player1.display_score, [0, 0])
    screen.blit(player2.display_score, [615, 0])

    # Update display
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()