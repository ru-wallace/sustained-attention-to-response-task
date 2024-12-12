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

# If True, a practice block will be run before the main experiment
practice = True

# If True, the trial order will be fixed in sequence 
# (1,2,...8,9,1,2,..,)
fixed = False

# If True, the user will be prompted to select the output 
# file destination after entering participant details.
selectOutputFile = True

# Folder to save the output files (Will be created if it doesn't exist) 
# (If selectOutputFile is true, this is used as the default 
# path when opening the file dialog)
path = 'output'

# Default output file format (csv or txt) 
# (If selectOutputFile is true, this can be changed when 
# selecting the output file)
format = 'csv'

# Default delimiter for csv files (Separator between columns)
delimiter = ','


# Run the experiment
python_sart.sart(blocks=blocks, reps=reps, path=path, practice=practice, fixed=fixed, selectOutputFile=selectOutputFile, format=format, delimiter=delimiter)
