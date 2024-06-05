import time
import winsound
from gitagameaprentis import bhaktisystem as bks

def yes_scene(state,g = "would you like  continue [type yes to continue]"):
    if state == True:
        while True:
            answer = str(input(g))
            answer = answer.lower()
            if "yes" in answer:
                 print("your reply:"+ answer)
                 break
            else:
                print("your reply"+ answer)
                print("system:sorry but can you write corectly")


def play_conch():
    # Define frequencies for the notes of the conch sound
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

    # Play each note sequentially
    for note in notes:
        winsound.Beep(int(note), 500)  # Play the note for 500 milliseconds
        time.sleep(0.2)  # Add a small delay between notes


def correct_answer_sound():
    # Define the frequency and duration for the correct answer sound
    frequency = 1000  # Adjust frequency as needed
    duration = 300  # Adjust duration as needed

    winsound.Beep(frequency, duration)  # Play the correct answer sound


def chapter_completion_sound():
    # Define frequencies for a soothing and uplifting sound
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

    # Play the completion sound sequence
    for note in notes:
        winsound.Beep(int(note), 300)  # Play each note for 300 milliseconds
        time.sleep(0.1)  # Add a small delay between notes

def loadscreen():
    loadscreen = "loading..........."
    for i in range(0,5):
      print(loadscreen)
      time.sleep(0.5)


