import pygame
import math
from datetime import datetime

# Initializes pygame and creates a window to draw on
pygame.init()
window_size = 600
screen = pygame.display.set_mode((window_size, window_size))

# Defines colors to be used when drawing the clock
background_color = (255, 255, 255)
line_color = (0, 0, 0)
seconds_hand_color = (255, 0, 0)
clock_body_color = (150, 150, 150)

# Defines the size of the clock elements based on the screen size.
# Ensures results are ints to better fit the pixel grid
middle = (window_size // 2, window_size // 2)
radius = window_size // 3
segment_length = radius // 5
hour_length = radius - (radius // 3)
minute_length = radius - (radius // 12)


# Function for calculating the coordinates of a point radiation from another point based on the angle
def calculate_point(start_pos, length, angle):
    x = start_pos[0] + length * math.cos(math.radians(angle))
    y = start_pos[1] + length * math.sin(math.radians(angle))
    point = (x, y)
    return point


# Function for drawing a hand of the clock
def draw_hand(start_pos, length, angle, color):
    end = calculate_point(start_pos, length, angle)

    pygame.draw.aaline(screen, color, start_pos, end)


# Function for drawing the segmented lines in the clock
def draw_segmented_lines(start_pos, length, amount, seg_length, color):
    for i in range(amount):
        angle = 360 / amount * i
        end = calculate_point(start_pos, length, angle)

        # Makes the lines slightly longer at the 4 quarters
        if i % (amount / 4) == 0:
            segment_start = calculate_point(start_pos, length - seg_length, angle)
        else:
            segment_start = calculate_point(start_pos, length - seg_length // 2, angle)

        pygame.draw.aaline(screen, color, segment_start, end)


while True:
    screen.fill(background_color)

    # Drawing the 3 circles that make up the clock body
    pygame.draw.circle(screen, clock_body_color, middle, radius)
    pygame.draw.circle(screen, line_color, middle, (segment_length // 8))
    pygame.draw.circle(screen, line_color, middle, radius, width=1)

    current_time = datetime.now()

    # Drawing the segments
    draw_segmented_lines(middle, radius, 12, segment_length, line_color)
    # Drawing the seconds hand
    draw_hand(middle, radius, current_time.second * 6 - 90, seconds_hand_color)
    # Drawing the hour hand
    draw_hand(middle, hour_length, current_time.hour * 6 - 210, line_color)
    # Drawing the minute hand
    draw_hand(middle, minute_length, current_time.minute * 6 - 90, line_color)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
