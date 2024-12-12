# sustained-attention-to-response-task

=============

## SART

A Python version of the Sustained Attention to Response Task (SART) as detailed by Robertson et al. (1997). Requires [PsychoPy](http://www.psychopy.org/).

![SART task flow](/python-sustained-attention-to-response-task-sart.png?raw=true "SART Task Flow")

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
6) path: The directory in which the output file will be placed. Defaults to a subfolder named 'output' in the directory in which the task is placed.
7) selectOutputFile: If True, a dialog box will appear after entering participant details to allow the user to select the output file name and location. If False, the output file will be saved to the path specified in the path parameter.
8) format: The default file format of the output file. Can be ".txt" or ".csv". Default is ".txt".
9) delimiter: The delimiter to use in the output file. Default is tab specified by "\t".

### Function Details

Self-Contained Functions (Argument=Default Value):

sart(monitor="testMonitor", blocks=1, reps=5, omitNum=3, practice=True,
     path="", fixed=False)

* **monitor** (str): The monitor to be used for the task.
* **blocks** (int): The number of blocks to be presented.
* **reps** (int): The number of repetitions to be presented per block.  Each  repetition equals 45 trials (5 font sizes X 9 numbers).
* **omitNum** (int): The number participants should withhold pressing a key on.
* **practice** (bool): If the task should display 18 practice trials that contain feedback on accuracy.
* **path** (str): The directory in which the output file will be placed. Defaults to a subfolder named 'output' in the directory in which the task is placed.
* **fixed** (bool): Whether or not the numbers should be presented in a fixed instead of random order (e.g., 1, 2, 3, 4, 5, 6, 7, 8 ,9, 1, 2, 3, 4, 5, 6, 7, 8, 9,...).
* **selectOutputFile** (bool): If True, a dialog box will appear after entering participant details to allow the user to select the output file name and location. If False, the output file will be saved to the path specified in the path parameter.
* **format** (str): The default file format of the output file. Can be ".txt" or ".csv". Default is ".txt".
* **delimiter** (str): The delimiter to use in the output file. Default is tab specified by "\t".

### Reference

Robertson, H., Manly, T., Andrade, J.,  Baddeley, B. T., & Yiend, J. (1997).
'Oops!': Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. Neuropsychologia, 35(6), 747-758.

### Fork Notes

I forked this repository to make a few changes to the original code. I updated some of the code to work with more recent releases of Python and PsychoPy. I also added a few more parameters to the sart() function to allow for more customization of the task.

* The user can specify whether a manual file selection dialog should be used to select the output directory. If the user does not want to use the dialog, the user can specify the output directory in the path parameter.

* The user can also specify whether the filename shouild have a txt extension or a csv extension. The user can also specify the filename.

* The user can also specify the delimiter for the output file. The default delimiter is a tab, specified by '\t'.
  