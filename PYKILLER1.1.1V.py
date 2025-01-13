import time
import logging
import psutil
import pygame
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Limit settings
MAX_CPU_USAGE = 90  # Max CPU usage percentage before triggering warning
MAX_MEMORY_USAGE = 80  # Max memory usage percentage before triggering warning
SAFE_MODE = False  # Set this to True to limit resource usage during testing

# Function to check system resources (CPU, Memory) during the stress test
def check_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    if cpu_usage > MAX_CPU_USAGE:
        logger.warning(f"High CPU usage detected: {cpu_usage}%")
    if memory_usage > MAX_MEMORY_USAGE:
        logger.warning(f"High memory usage detected: {memory_usage}%")

    if SAFE_MODE:
        # If SAFE_MODE is True, limit the stress-test loop speed to avoid overwhelming the system
        if cpu_usage > MAX_CPU_USAGE or memory_usage > MAX_MEMORY_USAGE:
            logger.info("SAFE_MODE activated: Slowing down to prevent system overload.")
            time.sleep(1)  # Introduce a slight delay to reduce load
        else:
            # If resource usage is back to normal, adjust accordingly
            logger.info("SAFE_MODE deactivated: Resuming normal operation.")

# Stress-test function to simulate CPU and memory usage
def stress_test():
    logger.info("Starting stress test...")

    # Initialize Pygame for graphics rendering to simulate high CPU usage
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    try:
        while True:
            # Draw circles to simulate heavy graphics processing and CPU usage
            for _ in range(100000):  # Adjust the range for stress level
                pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
                pygame.display.flip()

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
        logger.info("PYKILLER execution finished.")

# Entry point of the program
if __name__ == "__main__":
    stress_test()
