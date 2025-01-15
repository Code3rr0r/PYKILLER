import time
import logging
import psutil
import pygame
import sys

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Limit settings (can be adjusted dynamically)
MAX_CPU_USAGE = 90  # Max CPU usage percentage before triggering warning
MAX_MEMORY_USAGE = 80  # Max memory usage percentage before triggering warning
SAFE_MODE = False  # Set this to True to limit resource usage during testing

# Function to check system resources (CPU, Memory) during the stress test
def check_resources():
    """
    Monitors the CPU and memory usage, logging warnings if usage exceeds the thresholds.
    In SAFE_MODE, it throttles the loop to prevent system overload.
    """
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    # Log warnings if usage exceeds thresholds
    if cpu_usage > MAX_CPU_USAGE:
        logger.warning(f"High CPU usage detected: {cpu_usage}%")
    if memory_usage > MAX_MEMORY_USAGE:
        logger.warning(f"High memory usage detected: {memory_usage}%")

    # Handle SAFE_MODE behavior
    if SAFE_MODE:
        if cpu_usage > MAX_CPU_USAGE or memory_usage > MAX_MEMORY_USAGE:
            logger.info("SAFE_MODE activated: Slowing down to prevent system overload.")
            time.sleep(1)  # Slow down the loop to avoid overwhelming the system
        else:
            logger.info("SAFE_MODE deactivated: Resuming normal operation.")

# Function to simulate stress test with heavy CPU and memory usage
def stress_test():
    """
    Simulates a stress test by rendering graphics using Pygame to load the CPU and memory.
    It continuously checks the system resources and adjusts the behavior accordingly.
    """
    logger.info("Starting stress test...")

    # Initialize Pygame for graphics rendering to simulate high CPU usage
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    try:
        while True:
            # Draw circles to simulate heavy graphics processing and CPU usage
            for _ in range(100000):  # Adjust the range for desired stress level
                pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
                pygame.display.flip()  # Update the screen

            # Continuously check system resources and adjust behavior accordingly
            check_resources()

            # Add a small delay between iterations to prevent system lockups in safe mode
            if SAFE_MODE:
                time.sleep(0.5)

    except KeyboardInterrupt:
        logger.info("Stress test interrupted by user.")
    except Exception as e:
        logger.error(f"Error during stress test: {str(e)}")
    finally:
        # Clean up and quit Pygame when done
        pygame.quit()
        logger.info("Stress test finished and resources released.")

# Entry point of the program
if __name__ == "__main__":
    # Starting the stress test
    stress_test()
