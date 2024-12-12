""" Sustained Attention to Response Task (SART)

Author: Cary Stothart (cary.stothart@gmail.com)
Date: 05/11/2015
Version: 2.0
Tested on StandalonePsychoPy-1.82.01-win32

################################# DESCRIPTION #################################

This module contains the standard SART task as detailed by Robertson et al. 
(1997). 

The following task attributes can be easily modified (see the sart()
function documentation below for details):
    
1) Number of blocks (default is 1)
2) Number of font size by number repetitions per trial (default is 5)
3) Target number (default is 3)
4) The presentation order of the numbers. Specifically, the
   numbers can be presented randomly or in a fixed fashion. (default is random)
5) Whether or not practice trials should be presented at the beginning of the 
   task.
   
How to use:

1. Install PsychoPy if you haven't already.
2. Load this file and run it using PsychoPy. Participants will be run on the 
   classic SART task (Robertson et al, 1997) unless one of the sart()
   function parameters is changed.

Reference:

Robertson, H., Manly, T., Andrade, J.,  Baddeley, B. T., & Yiend, J. (1997). 
'Oops!': Performance correlates of everyday attentional failures in traumatic 
brain injured and normal subjects. Neuropsychologia, 35(6), 747-758.

################################## FUNCTIONS ##################################

Self-Contained Functions (Argument=Default Value):

sart(monitor="testMonitor", blocks=1, reps=5, omitNum=3, practice=True, 
     path="", fixed=False, selectOutputFile=False)
     
monitor.............The monitor to be used for the task.
blocks..............The number of blocks to be presented.
reps................The number of repetitions to be presented per block.  Each
                    repetition equals 45 trials (5 font sizes X 9 numbers).
omitNum.............The number participants should withhold pressing a key on.
practice............If the task should display 18 practice trials that contain 
                    feedback on accuracy.
path................The directory in which the output file will be placed. Defaults
                    to the directory in which the task is placed.
fixed...............Whether or not the numbers should be presented in a fixed
                    instead of random order (e.g., 1, 2, 3, 4, 5, 6, 7, 8 ,9,
                    1, 2, 3, 4, 5, 6, 7, 8, 9...).
selectOutputFile....If True, a dialog box will appear to allow the user to
                    select the output file name and location.
format="txt"........The format of the output file. Can be "txt" or "csv". Default
                    is "txt".
             
################################### CITATION ##################################

How to cite this software in APA:

Stothart, C. (2015). Python SART (Version 2) [software]. Retrieved from 
https://github.com/cstothart/python-cog-tasks.  

For a DOI and other citation information, please see 
http://figshare.com/authors/Cary_Stothart/394277
     
################################## COPYRIGHT ##################################

The MIT License (MIT)

Copyright (c) 2015 Cary Robert Stothart

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.     

"""

import time
import random
import pathlib
import sys 
from psychopy import visual, core, data, event, gui




def sart(monitor="testMonitor", blocks:int=1, reps:int=5, omitNum:int=3, practice:bool=True, 
                  path:str="output", fixed:bool=False, selectOutputFile:bool=False, format:str=".txt", delimiter:str="\t"):
    """SART Task.


    Parameters:
        monitor (str): The monitor to be used for the task.
        blocks (int): The number of blocks to be presented.
        reps (int): The number of repetitions to be presented per block. Each
        omitNum (int): The number participants should withhold pressing a key on.
        practice (bool): If the task should display 18 practice trials that contain 
        path (str): The directory in which the output file will be placed. Defaults
        fixed (bool): Whether or not the numbers should be presented in a fixed
                        instead of random order (e.g., 1, 2, 3, 4, 5, 6, 7, 8, 9,
        selectOutputFile (bool): If True, a dialog box will appear to allow the user to
                        select the output file name and location.   
        format (str): The format of the output file. Can be "txt" or "csv".

    Returns:
        None
        """

    partInfo = part_info_gui()
    fileName = "SART_" + str(partInfo[0]) + format
    if selectOutputFile:
        fileName = select_output_file(path, fileName)

    write_to_file(fileName, delimiter, 
                "part_num", "part_gender", "part_age", "part_school_yr",
                "part_normal_vision", "exp_initials", "block_num",
                "trial_num", "number", "omit_num", "resp_acc", "resp_rt",
                "trial_start_time_s", "trial_end_time_s", "mean_trial_time_s",
                "timing_function")
    mainResultList = []
    
    win = visual.Window(size=(1920,1080),fullscr=True, color="black", units='cm',
                        monitor=monitor)
    sart_init_inst(win, omitNum)
    if practice == True:
        practiceResultList = []
        sart_prac_inst(win, omitNum)
        practiceResultList.extend(sart_block(win, fb=True, omitNum=omitNum, 
                              reps=1, bNum=0, fixed=fixed))
        for line in practiceResultList:
            write_to_file(fileName, delimiter, *partInfo, *line)
    sart_act_task_inst(win)
    for block in range(1, blocks + 1):
        mainResultList.extend(sart_block(win, fb=False, omitNum=omitNum,
                              reps=reps, bNum=block, fixed=fixed))
        if (blocks > 1) and (block != blocks):
            sart_break_inst(win)

    print(mainResultList)
    for line in mainResultList:
        write_to_file(fileName, delimiter, *partInfo, *line)
    #fileName.close()
    
def part_info_gui():
    
    info = gui.Dlg(title='SART')
    info.addText('Participant Info')
    info.addField('Participant Number: ')
    info.addField('Gender: ', 
                  choices=["Please Select", "Male", "Female", "Other"])
    info.addField('Age:  ')
    info.addField('Year in School: ', 
                  choices=["Please Select", "1st Year", "2nd Year", "3rd Year", 
                           "4th Year", "1st Year Graduate Student",
                           "2nd Year Graduate Student", 
                           "3rd Year Graduate Student", 
                           "4th Year Graduate Student",
                           "5th Year Graduate Student", 
                           "6th Year Graduate Student"])
    info.addField('Do you have normal or corrected-to-normal vision?', 
                  choices=["Please Select", "Yes", "No"])
    info.addText('')
    info.addText('Experimenter Info')
    info.addField('DIS Initials:  ')
    info.show()
    if info.OK:
        infoData = info.data
    else:
        sys.exit()
    return infoData
    
def sart_init_inst(win, omitNum):
    inst = visual.TextStim(win, text=("In this task, a series of numbers will" +
                                      " be presented to you.  For every" +
                                      " number that appears except for the" +
                                      " number " + str(omitNum) + ", you are" +
                                      " to press the space bar as quickly as" +
                                      " you can.  That is, if you see any" +
                                      " number but the number " +
                                      str(omitNum) + ", press the space" +
                                      " bar.  If you see the number " +
                                      str(omitNum) + ", do not press the" +
                                      " space bar or any other key.\n\n" +
                                      "Please give equal importance to both" +
                                      " accuracy and speed while doing this" + 
                                      " task.\n\nPress the b key when you" +
                                      " are ready to start."), 
                           color="white", height=0.7, pos=(0, 0))
    event.clearEvents()
    while 'b' not in event.getKeys():
        inst.draw()
        win.flip()
        
def sart_prac_inst(win, omitNum):
    inst = visual.TextStim(win, text=("We will now do some practice trials " +
                                      "to familiarize you with the task.\n" +
                                      "\nRemember, press the space bar when" +
                                      " you see any number except for the " +
                                      " number " + str(omitNum) + ".\n\n" +
                                      "Press the b key to start the " +
                                      "practice."), 
                           color="white", height=0.7, pos=(0, 0))
    event.clearEvents()
    while 'b' not in event.getKeys():
        inst.draw()
        win.flip()
        
def sart_act_task_inst(win):
    inst = visual.TextStim(win, text=("We will now start the actual task.\n" +
                                      "\nRemember, give equal importance to" +
                                      " both accuracy and speed while doing" +
                                      " this task.\n\nPress the b key to " +
                                      "start the actual task."), 
                           color="white", height=0.7, pos=(0, 0))
    event.clearEvents()
    while 'b' not in event.getKeys():
        inst.draw()
        win.flip()
        
def sart_break_inst(win):
        inst = visual.TextStim(win, text=("You will now have a 60 second " +
                                          "break.  Please remain in your " +
                                          "seat during the break."),
                               color="white", height=0.7, pos=(0, 0))
        nbInst = visual.TextStim(win, text=("You will now do a new block of" +
                                            " trials.\n\nPress the b key " +
                                            "bar to begin."),
                                 color="white", height=0.7, pos=(0, 0))
        startTime = time.time()
        while 1:
            eTime = time.time() - startTime
            inst.draw()
            win.flip()
            if eTime > 60:
                break
        event.clearEvents()
        while 'b' not in event.getKeys():
            nbInst.draw()
            win.flip()

def sart_block(win, fb, omitNum, reps, bNum, fixed):
    mouse = event.Mouse(visible=0)
    xStim = visual.TextStim(win, text="X", height=3.35, color="white", 
                            pos=(0, 0))
    circleStim = visual.Circle(win, radius=1.50, lineWidth=8,
                               lineColor="white", pos=(0, -.2))
    numStim = visual.TextStim(win, font="Arial", color="white", pos=(0, 0))
    correctStim = visual.TextStim(win, text="CORRECT", color="green", 
                                  font="Arial", pos=(0, 0))
    incorrectStim = visual.TextStim(win, text="INCORRECT", color="red",
                                    font="Arial", pos=(0, 0))                                 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if fb == True:
        fontSizes=[1.20, 3.00]
    else:
        fontSizes=[1.20, 1.80, 2.35, 2.50, 3.00]
    list= data.createFactorialTrialList({"number" : numbers,
                                         "fontSize" : fontSizes})
    seqList = []
    for i in range(len(fontSizes)):
        for number in numbers:
            random.shuffle(list)
            for trial in list:
                if trial["number"] == number and trial not in seqList:
                    seqList.append(trial)
                    break
    if fixed == True:
        trials = data.TrialHandler(seqList, nReps=reps, method='sequential')
    else:
        trials = data.TrialHandler(list, nReps=reps, method='random')
    clock = core.Clock()
    tNum = 0
    resultList =[]
    startTime = time.time()
    for trial in trials:
        tNum += 1
        resultList.append(sart_trial(win, fb, omitNum, xStim, circleStim,
                              numStim, correctStim, incorrectStim, clock, 
                              trials.thisTrial['fontSize'], 
                              trials.thisTrial['number'], tNum, bNum, mouse))
    endTime = time.time()
    totalTime = endTime - startTime
    for row in resultList:
        row.append(totalTime/tNum)
    print ("\n\n#### Block " + str(bNum) + " ####\nDes. Time Per P Trial: " +
           str(2.05*1000) + " ms\nDes. Time Per Non-P Trial: " +
           str(1.15*1000) + " ms\nActual Time Per Trial: " +
           str((totalTime/tNum)*1000) + " ms\n\n")
    return resultList
    
def sart_trial(win, fb, omitNum, xStim, circleStim, numStim, correctStim, 
               incorrectStim, clock, fontSize, number, tNum, bNum, mouse):
    startTime = time.time()
    mouse.setVisible(0)
    respRt = "NA"
    numStim.setHeight(fontSize)
    numStim.setText(number)
    numStim.draw()
    event.clearEvents()
    clock.reset()
    stimStartTime = time.time()
    win.flip()
    xStim.draw()
    circleStim.draw()
    waitTime = .25 - (time.time() - stimStartTime)
    core.wait(waitTime, hogCPUperiod=waitTime)
    maskStartTime = time.time()
    win.flip()
    waitTime = .90 - (time.time() - maskStartTime)
    core.wait(waitTime, hogCPUperiod=waitTime)
    win.flip()
    allKeys = event.getKeys(timeStamped=clock)
    if len(allKeys) != 0:
        respRt = allKeys[0][1]
    if len(allKeys) == 0:
        if omitNum == number:
            respAcc = 1
        else:
            respAcc = 0
    else:
        if omitNum == number:
            respAcc = 0
        else:
            respAcc = 1
    if fb == True:
        if respAcc == 0:
            incorrectStim.draw()
        else:
            correctStim.draw()
        stimStartTime = time.time()
        win.flip()
        waitTime = .90 - (time.time() - stimStartTime) 
        core.wait(waitTime, hogCPUperiod=waitTime)
        win.flip()
    endTime = time.time()
    totalTime = endTime - startTime
    return [str(bNum), str(tNum), str(number), str(omitNum), str(respAcc),
            str(respRt), str(startTime), str(endTime)]

def write_to_file(fileName, delimiter:str, *data):
    with open(fileName, "a") as f:
            f.write("\t".join([str(x) for x in data]) + "\n")

def select_output_file(path, fileName:str):
    # Get the file name and path using a dialog box
    # If the file already exists, add a number to the end of the file name
    file = gui.fileSaveDlg(prompt="Save Data File As", allowed="Text Files (*.txt)|*.txt|CSV Files (*.csv)|*.csv", initFileName=fileName, initFilePath=path)

    if file is not None and file != "":
        fileName = file

    file_stem, extension = fileName.rsplit(".", 1)

    attempts = 0
    while pathlib.Path(fileName).exists():
        attempts += 1
        fileName = file_stem + f"_{attempts}." + extension

    return fileName


def main():
    sart(selectOutputFile=True, format=".csv", delimiter=",")

if __name__ == "__main__":
    main()