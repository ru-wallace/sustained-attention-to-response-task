"""
This is a template script for running the SART experiment 
using the python_sart module. Ensure that the python_sart.py script
is in the same directory as this script or in the Python path, and 
that PsychoPy is installed, then run this script to start the experiment.

Modify the parameters below to customize the experiment settings.

See the instructions at https://github.com/ru-wallace/sustained-attention-to-response-task for more information.

"""



import python_sart

### Define the parameters for the experiment

# Number of blocks (There is a 60 second break between blocks)
blocks = 1

# Number of reps per block (Each rep has 45 trials - 
# each combination of 5 font sizes and 9 numbers)
reps = 5

#The number at which the user should withhold input
#If you set this to 'number_to_omit=None', a random number between 1 and 9 will be picked.
#This number is recorded in the output file
number_to_omit=3

# If True, a practice block will be run before the main experiment
practice = True

# If True, the trial order will be fixed in sequence 
# (1,2,...8,9,1,2,..,)
fixed_order = False

# Run the experiment
sart = python_sart.SART(blocks=blocks, reps=reps, omit_number=number_to_omit, show_practice=practice, fixed_order=fixed_order)