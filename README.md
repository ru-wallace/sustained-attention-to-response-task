# sustained-attention-to-response-task

=============

## SART

A Python version of the Sustained Attention to Response Task (SART) as detailed by Robertson et al. (1997). Requires [PsychoPy](http://www.psychopy.org/).

![SART task flow](/python-sustained-attention-to-response-task-sart.png?raw=true "SART Task Flow")

Originally created by [Cary Stothart](https://github.com/cstothart), forked by [Ru Wallace](https://github.com/ru-wallace)

Modified significantly from the [original version](https://github.com/cstothart/sustained-attention-to-response-task) to work with more recent releases of Python and PsychoPy. An earlier iteration much closer to the original code can be found [here](python_sart_old.py).

### How to Use

1. Install PsychoPy if you haven't already.
2. Download the [python_sart.py](python_sart.py) file from this repository and save it to a desired location on your computer.
3. Open the PsychoPy application, and if you are not already in the Coder view, open it by clicking on the Coder icon in the top right corner of the PsychoPy window or by selecting "Window" -> "Show Coder" from the top menu bar.
4. Load the python_sart.py file into the PsychoPy Coder view by clicking on "File" -> "Open" in the top menu bar and navigating to the location of the python_sart.py file.
5. Create a second python script in the same folder as the python_sart.py file (Select "File" -> "New" from the top menu bar). This script will be used to run the SART task with your choice of customisation parameters. The file [template_sart_script.py](template_sart_script.py) contains a template script that can be used to run the SART task. You can copy the contents of this file and modify the parameters as needed.
6. Run the script by clicking on the green "Run" button in the "Desktop" section of the toolbar at the top of the PsychoPy window.
7. Participants will be run on the classic SART task (Robertson et al, 1997) unless one of the sart() function parameters is changed.
8. If you want to make this process easier, you can save the script as part of a task list:
   - Open the Runner view by clicking on the Runner icon in the top right corner of the PsychoPy window or by selecting "Window" -> "Show Runner" from the top menu bar.
   - If the script is not already in the task list, add it by clicking on the red "+" button in the "Manage List" section of the Runner view toolbar and selecting the script file.
   - Save the task list ("File" -> "Save List") to somewhere convenient on your computer. (On your desktop if you are that way inclined.)
   - Next time you want to run the script, double-click on the task list file to open it in PsychoPy and then click on the green "Run" button in the "Desktop" section of the toolbar at the top of the PsychoPy window.
   - If the "run" button is coloured orange, you will need to select and deselect "Pilot" mode in the "Experiment" section of the Runner view toolbar before you run the task.

#### Note for manual PsychoPy installation using pip or conda (Ignore if using the standalone PsychoPy application)

The max NumPy version that PsychoPy supports is 1.23.5. If you are installing PsychoPy manually using pip or conda, you may need to manually install an older version of NumPy. You can install the correct version of NumPy using the following command:

```bash
pip install numpy==1.23.5
```

After installing the correct version of NumPy, you can install PsychoPy using the following command:

```bash
pip install psychopy
```

For optimal performance of the GUI, install PyQt5 using the following command:

```bash
pip install pyqt5
```

### Task Details

The following task attributes can be easily modified (see the sart()
function documentation below for details):

1) Number of blocks (default is 1)
2) Number of font size by number repetitions per trial (default is 5)
3) Target number (default is 3)
4) The presentation order of the numbers. Specifically, the
   numbers can be presented randomly or in a fixed fashion. (default is random)
5) Whether or not practice trials should be presented at the beginning of the task.
6) The default directory in which the output file will be placed. Defaults to a subfolder named 'output' in the directory in which the task is placed.


### Function Details

To run a SART experiment, create an instance of the SART class with the desired parameters and call the run() method. The SART class has the following parameters:

- **blocks** (int): The number of blocks to be presented.
- **reps** (int): The number of repetitions to be presented per block.  Each  repetition equals 45 trials (5 font sizes X 9 numbers).
- **omitted_num** (int): The number on which participants should withhold pressing a key. If not specified, a random number will be chosen between 1 and 9.
- **show_practice** (bool): If the task should display 18 practice trials that contain feedback on accuracy before the main task (default is True).
- **break_between_blocks_secs** (float): The number of seconds to wait between blocks (default is 60s).
- **stimulus_visible_secs** (float): The number of seconds the stimulus is visible (default is 0.90s).
- **stimulus_masked_secs** (float): The number of seconds the stimulus is masked (default is 0.25s).
- **output_dir** (str): The  default directory in which the save file dialog will open. If not specified, the save file dialog will open in the current working directory.
- **fixed_order** (bool): Whether or not the numbers should be presented in a fixed instead of random order (e.g., 1, 2, 3, 4, 5, 6, 7, 8 ,9, 1, 2, 3, 4, 5, 6, 7, 8, 9,...).
- **monitor** (str): The monitor to be used for the task. (default is "testMonitor", the PsychoPy default monitor)
- **exit_key** (str): The key that will exit the task. (default is 'escape')

For example, to run a SART task with 2 blocks, 3 repetitions per block, and a target number of 4, you would use the following code:

```python
from python_sart import SART

sart = SART(blocks=2, reps=3, omitted_num=4)
sart.run()
```

The run() method will open a dialogue to enter the participant details, then prompt you to select a directory to save the output file.
Once these details are entered, the task will begin.

### Reference

Robertson, H., Manly, T., Andrade, J.,  Baddeley, B. T., & Yiend, J. (1997).
'Oops!': Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. Neuropsychologia, 35(6), 747-758.

### Fork Notes

I forked this repository to make a few changes to the original code. I updated some of the code to work with more recent releases of Python and PsychoPy. I also added a few more parameters to allow for more customization of the task.

- The participant information section is updated with changed fields for stage of study (aligned to UK terminology). The dialog now has required sections, will not allow the user to proceed without filling in the required fields, and will not allow the user to proceed if the participant ID and ages are not a number. The gender field is still an option dropdown menu, but the user can also type in a custom answer if they wish.
- The output file is now saved as an Excel file (.xlsx) instead of a CSV file. There are fewer columns in the output file, and the columns are now named with more descriptive titles.
- The output file now includes a column in which the average of the previous 4 reaction times is calculated for each trial in which the participant should have withheld a response. 
  If any of these 4 trials was also one in which they should have withheld a response, or one in which the participant did not respond, the average is not calculated and the cell is left blank.