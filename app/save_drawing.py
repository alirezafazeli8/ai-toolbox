#==================================#
# Function to save current drawing #
#==================================#

# Import Packages
import os, os.path
from datetime import datetime
import cv2

# Current date and time as in string format
date_time = datetime.now().strftime("%d-%m-%y_%H:%M")
# %d-%m-%y_%H:%M : day-month-year_hours:minutes

# Directory (folder) of drawings
dir_name = 'Drawings'
if not os.path.exists(dir_name):
    os.mkdir(dir_name) # Create folder if not exists

# Count the number of the saved drawings
number_of_drawings = len([drawings for drawings in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, drawings))])

# Name of new drawing : "drawing(number)_day-month-year_hour:minutes.jpg"
new_drawing = 'drawing' + str(number_of_drawings+1) + '_' + date_time + '.jpg'

def save_draw(image):
    cv2.imwrite(dir_name + '/' + new_drawing, image)
