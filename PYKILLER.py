import pygame
import sys

def pykiller():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("PYKILLER: Beware!")

    # Infinite Loop with No Event Handling (Unresponsive Window)
    def infinite_loop():
        while True:
            screen.fill((255, 0, 0))  # Fill the screen with red
            pygame.display.flip()  # Update the screen
            # No event handling, window is completely unresponsive

    # Memory Exhaustion (Creating huge surfaces continuously)
    def memory_bomb():
        try:
            while True:
                huge_image = pygame.Surface((10000, 10000))  # 10000x10000 surface ~400MB each
                screen.blit(huge_image, (0, 0))
                pygame.display.flip()
        except MemoryError:
            print("Out of memory! Game crashed.")

    # High CPU Usage (Maximum CPU load)
    def cpu_killer():
        while True:
            screen.fill((0, 255, 0))  # Fill screen with green
            pygame.display.flip()  # Update screen without delay or framerate cap

    # Uncomment the function you want to try:
    
    # Infinite loop causing unresponsiveness
    infinite_loop()  # Use this line to test infinite loop behavior
    
    # Memory bomb causing the program to crash with memory error
    # memory_bomb()  # Uncomment this to test memory exhaustion
    
    # High CPU usage causing lag and freezing
    # cpu_killer()  # Uncomment this to test CPU overload

# Run the PYKILLER function
pykiller()
