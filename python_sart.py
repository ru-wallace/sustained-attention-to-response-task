
import random
import pathlib

from psychopy import visual, core, data, event, gui, localization
import pandas as pd
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QComboBox

class Participant:
    def __init__(self, number:str, gender:str, age:int, year_of_study:str, normal_vision:str, researcher_initials:str):
        """
        Initializes a new Participant.
        Parameters:
        number (str): The participant's number.
        gender (str): The participant's gender.
        age (int): The participant's age.
        year_of_study (str): The participant's year of study.
        normal_vision (str): Indicates if the participant has normal vision.
        researcher_initials (str): The initials of the researcher conducting the study.
        """

        self.number = number
        self.gender = gender
        self.age = age
        self.year_of_study = year_of_study
        self.normal_vision = normal_vision
        self.researcher_initials = researcher_initials

    def open_info_dialogue(participant_number:int=None, gender:int=None, age:int=None, year_of_study:int=None, normal_vision:int=None, researcher_initials:int=None):
        """
        Opens a dialog box to collect participant information.
        Parameters:
        participant_number (int, optional): The participant's number. Defaults to None.
        gender (int, optional): The participant's gender index. Defaults to None.
        age (int, optional): The participant's age. Defaults to None.
        year_of_study (int, optional): The participant's year of study index. Defaults to None.
        normal_vision (int, optional): The participant's vision status index. Defaults to None.
        researcher_initials (int, optional): The researcher's initials. Defaults to None.
        errors (bool, optional): Flag to indicate if there were errors in the previous input. Defaults to False.
        Returns:
        Participant: An instance of the Participant class with the collected information if the user pressed OK.
        None: If the user pressed Cancel.
        """

        # Create a dialog box to collect participant information

        gender_options = ["Please Select", 'Male', 'Female', 'Other']
        year_options = ["Please Select", "N/A", 
                            "1st Year Undergraduate",
                            "2nd Year Undergraduate",
                            "3rd Year Undergraduate",
                            "4th Year Undergraduate",
                            "5th Year Undergraduate",
                            "6th Year (or higher) Undergraduate",
                            "1st Year Post-graduate",
                            "2nd Year Post-graduate", 
                            "3rd Year Post-graduate", 
                            "4th Year Post-graduate",
                            "5th Year Post-graduate", 
                            "6th Year (or higher) Post-graduate"]
        vision_options = ["Please Select", "Yes", "No"]

        fields = {

            'participant_number': [participant_number, 'Participant Number:', 'number', None, True],
            'gender': [gender, 'Gender:', 'dropdown', gender_options, True],
            'age': [age, 'Age:',  'number', None, True],
            'year_of_study': [year_of_study, 'Year of Study:', 'dropdown', year_options, True],
            'normal_vision': [normal_vision, 'Do you have normal or corrected-to-normal vision?', 'dropdown', vision_options, True],
            'researcher_initials': [researcher_initials, 'Researcher Initials:', 'text', None, False]
        }


        myDlg = gui.Dlg(title="SART")
        myDlg.addText('Participant Information').setStyleSheet("font-weight: bold; font-size: 16px")

        def validate(arg=None):

            all_valid=True
            for data_field in myDlg.inputFields:
                if not data_field.required:
                    continue
                if isinstance(data_field, QComboBox):
                    if data_field.currentIndex() == 0:
                        all_valid = False

                else:
                    if len(data_field.text()) == 0:
                        all_valid == False

            myDlg.okBtn.setEnabled(all_valid)

        def add_field(field_name:str):
            field_info = fields[field_name]
            value, label, field_type, choices, required = field_info
            initial_str=""
  
            if field_type == 'text':
                    initial_str=value or ""

            if required:
                label = f"{label} *"
            print(label)
            
            field = myDlg.addField(field_name, initial_str, choices=choices, label=label, required=required)
            

            if field_type == 'dropdown':
                field.setCurrentIndex(value or 0)
                field.currentIndexChanged.connect(validate)

        
            else:
                field.textChanged.connect(validate)

            if field_type == 'number':
                validator = QIntValidator(0, 999)
                field.setValidator(validator)

            return field
        



        participant_number_field = add_field('participant_number')


        gender_dropdown = add_field('gender')
        gender_dropdown.setEditable(True)

        age_field =add_field('age')
        
        year_of_study_dropdown = add_field('year_of_study')

        normal_vision_dropdown = add_field('normal_vision')

        myDlg.addText('\nResearcher Information').setStyleSheet("font-weight: bold; font-size: 16px")

        researcher_initials_field = add_field('researcher_initials')
        #myDlg.validate()
        myDlg.show()  # show dialog and wait for OK or Cancel
        

        if myDlg.OK:  # then the user pressed OK
            info = myDlg.data

            err_msg = ""
            try:
                participant_number = int(participant_number_field.text())
            except:
                err_msg += "Participant number must be an integer.\n"
                participant_number = None

            gender_index = gender_dropdown.currentIndex()
            gender = gender_dropdown.currentText()
            if gender_index == 0:
                gender_index = None
                err_msg += "Please select an option in the Gender field.\n"
            
            try:
                age = int(age_field.text())
            except:
                err_msg += "Age must be an integer number.\n"
                age = None
            
            year_index = year_of_study_dropdown.currentIndex()
            year_of_study = year_options[year_index]
            if year_index == 0:
                err_msg += "Please select an option in the Year of Study field.\n"
                year_index = None


            vision_index = normal_vision_dropdown.currentIndex()
            normal_vision = vision_options[vision_index]

            if vision_index == 0:
                err_msg += "Please select an option in the Vision field.\n"
                vision_index = None

            researcher_initials = researcher_initials_field.text()

            if len(err_msg) > 0:
                err_dlg = gui.Dlg(title="Error")
                err_dlg.addText(err_msg)
                err_dlg.show()
                return Participant.open_info_dialogue(participant_number=participant_number, 
                                                      gender=gender_index, 
                                                      age=age, 
                                                      year_of_study=year_index, 
                                                      normal_vision=vision_index, 
                                                      researcher_initials=researcher_initials)
            
            


            participant = Participant(
                number=participant_number,
                gender=gender,
                age=age,
                year_of_study=year_of_study,
                normal_vision=normal_vision,
                researcher_initials=researcher_initials
            )

            return participant
        else:
            return None


class SART:
    def __init__(self, blocks:int=1, 
                 reps:int=5, 
                 omit_number:int=None, 
                 show_practice:bool=True, 
                 break_between_blocks_secs:float=60.0,
                   stimulus_visible_secs:float=0.90, 
                   stimulus_masked_secs:float=0.25, 
                   show_countdown:bool=False,
                   fixed_order:bool=False, 
                   output_dir:str="", 
                   monitor:str|None="testMonitor", 
                   exit_key:str='escape') -> None:
        """
        Initializes a new SART experiment.
        Parameters:
        blocks (int): The number of blocks to run.
        reps (int): The number of repetitions per block.
        omit_number (int): The number to omit. If None, a random number between 1 and 9 will be chosen.
        show_practice (bool): If True, a practice block will be run before the main experiment.
        break_between_blocks_secs (float): The duration of the break between blocks.
        stimulus_visible_secs (float): The duration for which the stimulus is visible.
        stimulus_masked_secs (float): The duration for which the stimulus is masked.
        show_countdown (bool): If True, a countdown will be displayed 5 seconds before the start of a block (or less if the break is shorter).
        fixed_order (bool): If True, the trial order will be fixed in sequence.
        output_dir (str): The directory to save the output file.
        monitor (str): The monitor to use.
        exit_key (str): The key to press to exit the experiment.
        """



        self.blocks = blocks
        self.reps = reps
        
        self.omit_number = omit_number
        
        if self.omit_number is None:
            self.omit_number = random.randint(1, 9)
        elif self.omit_number < 1 or self.omit_number > 9:
            raise ValueError("The number to omit must be between 1 and 9")
        self.break_between_blocks_secs = break_between_blocks_secs
        self.stimulus_visible_secs = stimulus_visible_secs
        self.stimulus_masked_secs = stimulus_masked_secs
        self.countdown = show_countdown
        self.countdown_secs = min(5, self.break_between_blocks_secs)

        self.break_between_blocks_secs = self.break_between_blocks_secs - self.countdown_secs

        self.fixed_order = fixed_order
        self.show_practice = show_practice
        self.output_dir = output_dir
        self.monitor = monitor
        self.participant:Participant = None
        self.window = None
        self.output_file:pathlib.Path = None
        self.results_df:pd.DataFrame = None
        self.columns = ['block', 'trial', 'number_shown', 'response_correct', 'response_time', 'last_four_avg']
        self.results = {}
        self.exit_key = exit_key
        for col in self.columns:
            self.results[col] = []

    def update_result(self, block_num:int, trial_num:int, number_shown:int, response_correct:bool, response_time:float|None, last_four_avg:float|None) -> None:
        """
        Updates the results dictionary with the trial data.
        Parameters:
        block_num (int): The block number.
        trial_num (int): The trial number.
        number_shown (int): The number shown in the trial.
        response_correct (bool): Indicates if the response was correct.
        response_time (float|None): The response time.
        last_four_avg (float|None): The average response time for the last four trials.
        """

        self.results['block'].append(block_num)
        self.results['trial'].append(trial_num)
        self.results['number_shown'].append(number_shown)
        self.results['response_correct'].append(response_correct)
        self.results['response_time'].append(response_time)
        self.results['last_four_avg'].append(last_four_avg)

    def get_output_file_path(self, initial_dir:str=""):
        """
        Generates the output file path for saving SART data.
        Args:
            initial_dir (str): The initial directory to open the file save dialog. Defaults to an empty string.
        Returns:
            str: The full path of the file where the SART data will be saved.
        """

        filename = f"SART_{self.participant.number}.xlsx"
        filename = gui.fileSaveDlg(initial_dir, filename, allowed="Excel Worksheet (*.xlsx)|*.xlsx)", prompt="Save SART Data As:")

        return filename

    def save_and_quit(self):
        """
        Save the experiment results to an Excel file and quits the application.
        If no trials have been completed, the application will quit without saving any data.
        If fewer trials than the expected number of trials (given the blocks and reps settings) have been completed, the application will save the data and indicate that it is incomplete.
        Parameters:
        arg (optional): An optional argument that is not used in the function.
        This function performs the following steps:
        1. Checks the number of trials completed.
        2. If there are any trials completed, it calculates the expected number of trials if the experiment is complete.
        3. Converts the results dictionary to a pandas DataFrame.
        4. Adds participant information to the DataFrame.
        5. Adds a column indicating whether the experiment was completed.
        6. Reorders the columns in the DataFrame.
        7. Saves the DataFrame to an Excel file with the specified output file path.
        8. Prints a message indicating the data has been saved and the number of trials completed.
        9. Closes the experiment window if it exists.
        10. Quits the core application.
        """

        n_trials = len(self.results['number_shown'])
        if n_trials > 0:
            length_if_complete = 45*self.reps*self.blocks #45 trials per rep, multiplied by number of blocks

            self.results_df = pd.DataFrame(self.results)
            self.results_df['participant_number'] = self.participant.number
            self.results_df['gender'] = self.participant.gender
            self.results_df['age'] = self.participant.age
            self.results_df['year_of_study'] = self.participant.year_of_study
            self.results_df['normal_vision'] = self.participant.normal_vision
            self.results_df['researcher_initials'] = self.participant.researcher_initials
            self.results_df['experiment_completed'] = n_trials < length_if_complete
            self.results_df['number_to_omit'] = self.omit_number

            #Reorder columns
            column_order = ['participant_number', 'gender', 'age', 'year_of_study', 'normal_vision', 'researcher_initials', 'experiment_completed', 'block', 'trial', 'number_to_omit', 'number_shown', 'response_correct', 'response_time', 'last_four_avg']
            self.results_df = self.results_df[column_order]
            self.results_df.to_excel(self.output_file, freeze_panes=(1, 0))
            print(f"Data saved to {self.output_file}")
            print("Number of trials completed: ", n_trials)
        if self.window is not None:
            self.window.close()
        core.quit()
        

    def show_message(self, message:str, key:str='b'):
        """
        Displays a message on the screen and waits for a specific key press to continue.
        Parameters:
        message (str): The message to be displayed on the screen.
        key (str): The key that the user must press to continue. Default is 'b'.
        Behavior:
        - Displays the provided message in white color with a height of 0.7.
        - Waits for the user to press the specified key or the exit key.
        - If the exit key is pressed, the function calls `self.save_and_quit()`.
        - If the specified key is pressed, the function continues execution.
        Note:
        - The screen is flipped (updated) before and after waiting for the key press.
        - All events are cleared before waiting for the key press.
        """

        message_screen = visual.TextStim(self.window, text=message, color="white", height=0.7)
        message_screen.draw()
        self.window.flip()

        event.clearEvents()
        response = False
        while not response:
            try:
                keys_pressed =event.waitKeys(keyList=[key, self.exit_key])
            except:
                keys_pressed = []
            if self.exit_key in keys_pressed:
                self.save_and_quit()
            for key in keys_pressed:
                if key == key:
                    response = True
                    break
        self.window.flip()
        

    def show_intro_message(self):
        initial_message = ("In this task, a series of numbers will"
                                      " be presented to you.  For every"
                                      " number that appears except for the"
                                      f" number {self.omit_number}, you are"
                                      " to press the space bar as quickly as"
                                      " you can.  That is, if you see any"
                                      " number but the number "
                                      f"{self.omit_number}, press the space"
                                      " bar.  If you see the number "
                                      f"{self.omit_number}, do not press the"
                                      " space bar or any other key.\n\n"
                                      "Please give equal importance to both"
                                      " accuracy and speed while doing this"
                                      " task.\n\nPress Esc to exit at any point\n\n"
                                      "Press the b key when you are ready to start.")
        
        self.show_message(initial_message)
        
    def show_practice_message(self):
        practice_message = ("We will now do some practice trials "
                                      "to familiarize you with the task.\n"
                                      "\nRemember, press the space bar when"
                                      " you see any number except for the "
                                      f" number {self.omit_number}.\n\n"
                                      "Press the b key to start the "
                                      "practice.")
        if self.countdown:
            practice_message += f"\n\nA countdown bar will be displayed from {self.countdown_secs} seconds before the start."
        
        self.show_message(practice_message)

    def show_task_start_message(self):
        start_message = ("We will now start the task.\n"
                                      "\nRemember, give equal importance to"
                                      " both accuracy and speed while doing"
                                      " this task.\n\nPress the b key to "
                                      "begin.")
        if self.countdown:
            start_message += f"\n\nA countdown bar will be displayed from {self.countdown_secs} seconds before the start of each block."
        
        self.show_message(start_message)

    def create_trial_list(self, practice=False)->data.TrialHandler:
        """
        Creates a list of trials for the experiment.
        If fixed_order is True, the trials will be in a fixed sequence of numbers with randomised font sizes.
        Parameters:
        practice (bool): If True, uses a reduced set of font sizes for practice trials. Defaults to False.
        Returns: 
        data.TrialHandler: A TrialHandler object containing the trial list. This is an iterable object that can be used to loop through the trials.
        For each item in the trial list, the parameters are a dictionary with the following keys
        - number: The number to display in the trial.
        - font_size: The font size to use for the number.
        """

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        font_sizes=[1.20, 1.80, 2.35, 2.50, 3.00]
        if practice:
            font_sizes=[1.20, 3.00]
        
        trial_list = data.createFactorialTrialList({
                                                    "number": numbers,
                                                    "font_size": font_sizes
                                                    })
        if self.fixed_order:

            seq_list = []
            for i in range(len(font_sizes)):
                for number in numbers:
                    random.shuffle(trial_list)
                    for trial in trial_list:
                        if trial["number"] == number and trial not in seq_list:
                            seq_list.append(trial)
                            break
            
            return data.TrialHandler(seq_list, nReps=self.reps, method='sequential')
            
        
        else:
            return data.TrialHandler(trial_list, nReps=self.reps, method='random')
        



    def run(self):
        """
        Executes the main experiment workflow.
        This method performs the following steps:
        1. Opens a dialogue box to collect participant information and creates a Participant object.
           If the participant information is not provided, the method saves the current state and exits.
        2. Determines the output file path for saving results.
        3. Initializes a full-screen window for displaying visual stimuli.
        4. Displays an introductory message to the participant.
        5. If practice trials are enabled, shows a practice message and runs a practice block.
        6. Displays a message indicating the start of the main task.
        7. Iterates through the specified number of blocks, running each block in sequence.
        8. Saves the results and exits the experiment.
        Returns:
            None
        """
        
        
        self.participant = Participant.open_info_dialogue() #Open the dialogue box to collect participant information and create a participant object when OK is pressed
        if self.participant is None:
            self.save_and_quit()
        self.output_file = self.get_output_file_path(self.output_dir)
        
        self.window = visual.Window(size=(1920,1080),
                            fullscr=True,
                            color="black",
                            units='cm',
                monitor=self.monitor)
        self.show_intro_message()

        if self.show_practice:
            self.show_practice_message()
            self.block(practice=True)

        self.show_task_start_message()

        for block_n in range(self.blocks):
            self.block(block_number=block_n+1)
        
        self.save_and_quit()


    def show_countdown_bar(self, seconds:float):
        """
        Displays a loading bar on the screen.
        Parameters:
        seconds (float): The number of seconds to display the loading bar.
        """

        backgroundBar = visual.Rect(self.window, width=20, height=1, pos=(0, 0), fillColor="gray")
        bg_bar_left = 0 - backgroundBar.width/2
        loadingBar = visual.Rect(self.window, width=0, height=1, pos=(bg_bar_left, 0), fillColor="green", anchor="left")
        countdown = visual.TextStim(self.window, text="", pos=(0, -2), color="white")
        start_time = core.getTime()
        while core.getTime() - start_time < seconds:
            countdown.setText(f"{int(seconds - (core.getTime() - start_time))+1}")
            progress = (core.getTime() - start_time) / seconds
            loadingBar.width = 20 * progress
            countdown.draw()
            backgroundBar.draw()
            loadingBar.draw()
            self.window.flip()
        self.window.flip()


    def block(self, block_number:int=0, practice:bool=False):
        """
        Executes a block of trials for the sustained attention to response task (SART).
        Args:
            block_number (int, optional): The number of the current block. Defaults to 0.
            practice (bool, optional): Indicates whether this is a practice block. Defaults to False.
        This method sets up the visual objects for the task, creates a list of trials,
        and iterates through each trial, executing them in sequence.
        Results for each trial are recorded in the results dictionary, unless practice is True.
        The method also initializes a clock to keep track of the timing for each trial.
        """
        
        event.Mouse(visible=False)
        self.x_stim = visual.TextStim(self.window, text="X", height=3.35, color="white", 
                            pos=(0, 0))
        self.circle_stim = visual.Circle(self.window, radius=1.50, lineWidth=8,
                                lineColor="white", pos=(0, -0.2))
        self.num_stim = visual.TextStim(self.window, font="Arial", color="white", pos=(0, 0))
        self.correct_stim = visual.TextStim(self.window, text="CORRECT", color="green", 
                                    font="Arial", pos=(0, 0))
        self.incorrect_stim = visual.TextStim(self.window, text="INCORRECT", color="red",
                                        font="Arial", pos=(0, 0))
        if self.countdown:
            self.show_countdown_bar(self.countdown_secs)

        trials = self.create_trial_list(practice)
        self.clock = core.Clock()
        for trial_number, trial in enumerate(trials):
            self.trial(trial, trial_number=trial_number+1, block_number=block_number, practice=practice)


    def trial(self, parameters:dict, trial_number:int, block_number:int, practice:bool=False)->None:
        """
        Conducts a single trial of the sustained attention to response task (SART).
        Parameters:
        -----------
        parameters : dict
            A dictionary containing the parameters for the trial, including 'font_size' and 'number'.
        trial_number : int
            The trial number within the current block.
        block_number : int
            The block number within the experiment.
        practice : bool, optional
            Indicates whether the trial is a practice trial (default is False).
        Returns:
        --------
        None
        """

        
        font_size=parameters['font_size']
        number = parameters['number']
        
        self.num_stim.setHeight(font_size)
        self.num_stim.setText(number)
        self.num_stim.draw()
        event.clearEvents()
        self.clock.reset()
        self.window.flip()
        stimulus_start_time = self.clock.getTime()
        self.x_stim.draw()
        self.circle_stim.draw()
        core.wait(self.stimulus_visible_secs - (self.clock.getTime()- stimulus_start_time))
        mask_start_time = self.clock.getTime()
        self.window.flip()
        core.wait(self.stimulus_masked_secs - (self.clock.getTime() - mask_start_time))
        self.window.flip()
        if len(event.getKeys(self.exit_key)) > 0:
            self.save_and_quit()
        keys_pressed = event.getKeys(['space'], timeStamped=self.clock)
        should_press = number != self.omit_number
        pressed = len(keys_pressed) > 0
        response_time = None if not pressed else keys_pressed[0][1]
        correct_response=(should_press==pressed)

        if practice:
            if correct_response:
                self.correct_stim.draw()
            else:
                self.incorrect_stim.draw()
            feedback_start_time=self.clock.getTime()
            self.window.flip()
            core.wait(self.stimulus_masked_secs-(self.clock.getTime()-feedback_start_time))
            self.window.flip()
        last_four_avg = None

        """
        If the omitted number was shown, and the response time was not None, 
        calculate the average of the last four trials (Unless any of the last
        four trials had the omitted number or had no response time)
        """

        if not should_press:
            prev_response_times = self.results['response_time'][-4:]
            prev_shown_numbers = self.results['number_shown'][-4:]
            if all([num != self.omit_number for num in prev_shown_numbers]) and all([time is not None for time in prev_response_times]):
                last_four_avg = sum(prev_response_times)/4
                
        if not practice:
            self.update_result(block_num=block_number, trial_num=trial_number, number_shown=number, response_correct=correct_response, response_time=response_time, last_four_avg=last_four_avg)

        
if __name__ == "__main__":
    sart = SART(blocks=1, reps=1, omit_number=3, show_practice=False, show_countdown=True)
    sart.run()


