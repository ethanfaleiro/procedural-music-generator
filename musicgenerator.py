from music21 import stream, note, scale, tempo
from PIL import Image, ImageTk
import random
import tkinter
from tkinter import messagebox
import threading

def music_creator():
    global num_note, file_name, scale_type,bpm_value  # Assigning global variables to be used outside the function
    try:
        num_note = int(notes_entry.get()) #Uses notes_entry.get to obtain the user's number of notes
        if num_note <= 0:
            status_label["text"] = "Please enter a number of notes greater than 0." #Checks for whether num_note is greater than 0
            return
    except ValueError:
        status_label["text"] = "Please enter a number." #Checks whether num_note is a number. 
        return

    try:
        bpm_value = int(bpm_entry.get())
        if bpm_value <= 0:
            status_label["text"] = "Please input a BPM greater than 0."
            return
    except ValueError:
        status_label["text"] = "Please enter a valid BPM number."
        return

    file_name = filename_entry.get().strip() #.strip is used to remove empty space from text for the file_name
    if file_name == "":
        status_label["text"] = "Please enter a file name." #Checks whether the filename has been left blank
        return

    scale_type = scaletype_entry.get().strip().upper()

    def message1(): #Process messages before giving the final audio
        status_label["text"] = "Generating music..." 
        root.after(1000, message2)

    def message2():
        status_label["text"] = "Egregiously discomparatabilitating..."
        root.after(1000, message3)

    def message3():
        threading.Thread(target=music_process).start() #Stops the UI from freezing during the processing

    message1()

    status_label["fg"] = "blue"
    generate_btn["state"] = "disabled"

def music_process():
    global num_note, file_name, scale_type, bpm_value

    melody = stream.Stream()

    try:
        major_scale = scale.MajorScale(scale_type)
        notes = major_scale.getPitches(f"{scale_type}4", f"{scale_type}5")
    except:
        status_label["text"] = f"Please input a scale from C,D,E,F,G,A,B"
        status_label["fg"] = "red"
        generate_btn["state"] = "normal"
        return
    
    metronome = tempo.MetronomeMark(number=bpm_value)
    melody.insert(0,metronome)

    for _ in range(num_note):
        pitch = random.choice(notes)
        accnote = note.Note(pitch)
        accnote.quarterLength = random.choice([0.25, 0.5, 1])
        melody.append(accnote)

    melody.write("midi", fp=file_name + ".mid") #Writes the final MIDI file
    status_label.after(0, completed_process)

def completed_process():
    status_label["text"] = f"✅ Completed! File saved as {file_name}.mid"
    status_label["fg"] = "green"
    generate_btn["state"] = "normal"

root = tkinter.Tk() #Using Tinker to set up the UI
root.title("Music Generator")
root.geometry("1920x1080") #The window size 
image_bg = Image.open("backgroundimg.jpg")
photo_bg = ImageTk.PhotoImage(image_bg)
bg_label = tkinter.Label(root, image=photo_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#background: <a href="https://www.vecteezy.com/free-vector/white-background">White Background Vectors by Vecteezy</a>
#ChatGPT helped with the Tkinter code.
#.pack() tells Tkinter how to place the widget in the parent container.
tkinter.Label(root, text="Number of Notes:", font=("Arial", 16)).pack() #.Label creates a label widget which says "Number of Notes"
notes_entry = tkinter.Entry(root, font=("Arial", 16)) #.Entry creates an entry widget where the user can type
notes_entry.pack() 
tkinter.Label(root, text="File Name:", font=("Arial", 16)).pack() #.Label creates a label widget which says File Name
filename_entry = tkinter.Entry(root, font=("Arial", 16))  #.Entry creates an entry widget where the user can type
filename_entry.pack()
tkinter.Label(root, text="Scale: C, D, E, F, G, A, B", font=("Arial",16)).pack()
scaletype_entry = tkinter.Entry(root, font=("Arial",16))
scaletype_entry.pack()
tkinter.Label(root, text="BPM/Tempo:", font=("Arial", 16)).pack()
bpm_entry = tkinter.Entry(root, font=("Arial", 16))
bpm_entry.pack()
generate_btn = tkinter.Button( #.Button creates a button widget that can be clicked to call the function music_creator()
    root,
    text="Generate Music",
    command=music_creator,
    font=("Arial", 16),
    width=20,
    height=1,
    padx=10,
    pady=10
)
generate_btn.pack(pady=20)
 
status_label = tkinter.Label(root, text="", font=("Arial", 18, "bold")) #Label used to show the status messages like processing and Egregiously discomparatabilitating lol
status_label.pack()

root.mainloop() #Starts the Tkinter event loop