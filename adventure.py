import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Text Adventure")

def display_text(text):
    screen.fill(WHITE)
    text_surface = FONT.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (20, 20))
    pygame.display.flip()

def introduction():
    display_text("Welcome to the Pygame Text Adventure!")
    time.sleep(2)
    start_game()

def start_game():
    display_text("You find yourself in a mysterious forest. You can choose different paths.")
    time.sleep(2)
    display_text("You are at a crossroads. Which path will you choose?\n1. Go left\n2. Go right\n3. Go straight\n4. Quit")

def left_path():
    display_text("You chose to go left and encounter a river.")
    time.sleep(2)
    display_text("You can choose to swim across or look for a bridge.\n1. Swim across\n2. Look for a bridge\n3. Go back")

def right_path():
    display_text("You chose to go right and enter a dark cave.")
    time.sleep(2)
    display_text("You can choose to explore the cave or leave it.\n1. Explore the cave\n2. Leave the cave\n3. Go back")

def straight_path():
    display_text("You chose to go straight and come across a vast meadow.")
    time.sleep(2)
    display_text("You see a suspicious-looking rock and a small shack.\n1. Examine the rock\n2. Visit the shack\n3. Go back")

def treasure_room():
    display_text("You finally arrive at the treasure room!")
    time.sleep(2)
    display_text("Congratulations, you've won the game!")

def quit_game():
    display_text("Thanks for playing the Pygame Text Adventure. Goodbye!")

def main():
    introduction()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    left_path()
                elif event.key == pygame.K_2:
                    right_path()
                elif event.key == pygame.K_3:
                    straight_path()

                elif event.key == pygame.K_4:
                    quit_game()

    pygame.quit()

if __name__ == "__main__":
    main()