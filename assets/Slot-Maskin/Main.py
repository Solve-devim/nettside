import customtkinter as ui
import tkinter as tk
import random
import time
import math
from PIL import Image, ImageTk
from playsound import playsound

# Function to get high score for a username
def get_high_score(filename, username):
    with open(filename, 'r') as file:
        for line in file:
            stored_username, stored_score = line.strip().split(',')
            if stored_username == username:
                return int(stored_score) 
    return None 

# Get username
username = input("Enter your username: ")

# set filepath
filename = 'users.txt'
soundpathwin = "sounds/winning.mp3"
soundpathloss = "sounds/loss.mp3"

# play sounds
def soundplaywin():
    playsound(soundpathwin)

def soundplayloss():
    playsound(soundpathloss)


# sett start value of slot numbers
slot1 = 0
slot2 = 0
slot3 = 0
slot4 = 0

# give slider a value
slider_value = 5000
rounded_value = 5000

# set balance of user
userbal = 10

# set reward
reward = 3

# Function to store high scores
def store_high_score(filename, username, new_score):
    scores = []
    user_found = False

    # Read current scores from the file
    with open(filename, 'r') as file:
        for line in file:
            stored_username, stored_score = line.strip().split(',')
            if stored_username == username:
                # Update high score if the new one is greater
                if new_score > int(stored_score):
                    scores.append(f"{username},{new_score}\n")
                    user_found = True
                else:
                    scores.append(line)  # Keep the old score if it's higher
            else:
                scores.append(line)

    # If user wasn't found, add new entry
    if not user_found:
        scores.append(f"{username},{new_score}\n")

    # Write all scores back to the file
    with open(filename, 'w') as file:
        file.writelines(scores)

# get the user's highscore
userbalhigh = get_high_score(filename, username)

# Check if userbalhigh is None
if userbalhigh is not None and userbalhigh > 1:
    pass
else:
    userbalhigh = 10

# Output number when sliding
def sliding(value):
    global slider_value
    global reward
    slidenr.configure(text=int(value))
    my_check.configure(text=int(value))
    slider_value = int(value)

    # round up the calue to first thousand
    global rounded_value
    rounded_value = math.ceil(slider_value / 1000) * 1000

    # calcualte risk
    if check_var.get() == "over":
        if rounded_value == 1000:
            reward = 0
        elif rounded_value == 2000:
            reward = 0  
        elif rounded_value == 3000:
            reward = 1  
        elif rounded_value == 4000:
            reward = 2
        elif rounded_value == 5000:
            reward = 3
        elif rounded_value == 6000:
            reward = 5  
        elif rounded_value == 7000:
            reward = 6
        elif rounded_value == 8000:
            reward = 7
        elif rounded_value == 9000:
            reward = 8
        else:
            reward = 9  
    else:  # for "under" condition
        if rounded_value == 1000:
            reward = 9 
        elif rounded_value == 2000:
            reward = 8
        elif rounded_value == 3000:
            reward = 6
        elif rounded_value == 4000:
            reward = 4
        elif rounded_value == 5000:
            reward = 3 
        elif rounded_value == 6000:
            reward = 2 
        elif rounded_value == 7000:
            reward = 1
        elif rounded_value == 8000:
            reward = 0 
        elif rounded_value == 9000:
            reward = 0
        else:
            reward = 0 

    
    # display current risk
    message = "Current Risk " + str(reward)
    rewardshow.configure(text=message)

# calcualte the risk and reward
def updaterisk():
    global reward
    if check_var.get() == "over":
        if rounded_value == 1000:
            reward = 0
        elif rounded_value == 2000:
            reward = 0  
        elif rounded_value == 3000:
            reward = 1  
        elif rounded_value == 4000:
            reward = 2
        elif rounded_value == 5000:
            reward = 3
        elif rounded_value == 6000:
            reward = 5  
        elif rounded_value == 7000:
            reward = 6
        elif rounded_value == 8000:
            reward = 7
        elif rounded_value == 9000:
            reward = 8
        else:
            reward = 9  
    else:  # for "under" condition
        if rounded_value == 1000:
            reward = 9 
        elif rounded_value == 2000:
            reward = 8
        elif rounded_value == 3000:
            reward = 6
        elif rounded_value == 4000:
            reward = 4
        elif rounded_value == 5000:
            reward = 3 
        elif rounded_value == 6000:
            reward = 2 
        elif rounded_value == 7000:
            reward = 1
        elif rounded_value == 8000:
            reward = 0 
        elif rounded_value == 9000:
            reward = 0
        else:
            reward = 0
    
    # display current risk
    message = "Current Risk " + str(reward)
    rewardshow.configure(text=message)

# When user is out of credits
def loss():
    pass

# When user clicks button
def roll():

    # Disable the button to prevent multiple clicks
    button.configure(state="disabled")

    global countt
    countt = 1

    # Function to update each slot with a delay
    def roll_slots():
        global countt
        if countt < 10:
            global slot4
            slot4 = random.randint(0, 9)
            label4.configure(text=slot4)
            countt = countt + 1  
            root.after(50, roll_slots)  
        else:
            root.after(50, roll_slot2)
            countt = 0


    def roll_slot2():
        global countt
        if countt < 10:
            global slot3
            slot3 = random.randint(0, 9)
            label3.configure(text=slot3)
            countt = countt + 1  
            root.after(50, roll_slot2)  
        else:
            root.after(50, roll_slot3)
            countt = 0
    
    def roll_slot3():
        global countt
        if countt < 10:
            global slot2
            slot2 = random.randint(0, 9)
            label2.configure(text=slot2)
            countt = countt + 1  
            root.after(50, roll_slot3)  
        else:
            root.after(50, roll_slot4)
            countt = 0

    def roll_slot4():
        global countt
        if countt < 10:
            global slot1
            slot1 = random.randint(0, 9)
            label1.configure(text=slot1)
            countt = countt + 1  
            root.after(50, roll_slot4)  
        else:
            root.after(50, check)

    def check(): 
        global userbal  
        global gifs
        global userbalhigh
        # Combine to one string after rolling all slots
        number = str(slot1) + str(slot2) + str(slot3) + str(slot4)
        rounded_value = math.ceil(slider_value / 1000) * 1000
        number1 = int(number)

        # Check if button over or under 5000
        if check_var.get() == "over":
            if number1 > slider_value:
                status = "win"
            else:
                status = "loss"
        else:
            if number1 < slider_value:
                status = "win"
            else:
                status = "loss"

        # Check if user won or lost
        if status == "win":
            headline.configure(text="You win :)")
            userbal = userbal + reward
            root.after(50, soundplaywin)
        else:
            headline.configure(text="You lose :(")
            userbal = userbal - reward
            root.after(50, soundplayloss)

        balancesh.configure(text=userbal)

        # Set highscore
        if userbal > userbalhigh:
            userbalhigh = userbal
            userlabel = f"{username}: {userbalhigh}"
            usernamelabel.configure(text=userlabel)
            store_high_score(filename, username, userbalhigh)
        else:
            pass

        # Check if the user has more balance left
        if userbal <= 0:
            root.after(0, update, 0)
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            headline.destroy()
            balancesh.destroy()
            button.destroy()
            frame.destroy()
            frame2.destroy()
            root.title("Game Over")
            root.geometry("450x300")
        else:
            button.configure(state="normal")  # Re-enable the button after rolling

    # Start rolling slots
    roll_slots()

# Update the rest of the script as needed

# set style
ui.set_appearance_mode("dark")
ui.set_default_color_theme("dark-blue")

# make main frame
root = ui.CTk()
root.geometry("350x770")
root.title("Slot Machine")
root.iconbitmap('images/icon.ico')
  
# make frame
frame = ui.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# make frame2
frame2 = ui.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

# load gif
gifs = ["images/i-lost-all-my.gif", "images/i-lost-it-all-lostitall.gif", "images/ponke-ponkesol.gif", "images/rage.gif"]
gif = random.choice(gifs)
gif_image = Image.open(gif)

# Create a list to store frames
frames = []

# Extract the frames from the GIF
try:
    while True:
        frames.append(ImageTk.PhotoImage(gif_image.copy()))
        gif_image.seek(len(frames))  # Move to the next frame
except EOFError:
    pass  # No more frames

# Function to update the label with the next frame
def update(index):
    labelgif.configure(image=frames[index])
    root.after(50, update, (index + 1) % len(frames))

labelgif = ui.CTkLabel(root, text=" ")
labelgif.pack()

# make headline
headline = ui.CTkLabel(master=frame, text="Slot Machine", font=("Roboto", 24))
headline.pack(pady=12, padx=10)

# Show username
usernametext = f"{username}: {userbalhigh}"
usernamelabel = ui.CTkLabel(master=root, text=usernametext, font=("Roboto", 24))
usernamelabel.pack(pady=12, padx=10)
usernamelabel.place(x=60, y=416)

# show slot1
label1 = ui.CTkLabel(master=frame, text=slot1, font=("Roboto", 24))
label1.pack(pady=12, padx=10)

# show slot2
label2 = ui.CTkLabel(master=frame, text=slot2, font=("Roboto", 24))
label2.pack(pady=12, padx=10)

# show slot 3
label3 = ui.CTkLabel(master=frame, text=slot3, font=("Roboto", 24))
label3.pack(pady=12, padx=10)

# show slot 4
label4 = ui.CTkLabel(master=frame, text=slot4, font=("Roboto", 24))
label4.pack(pady=12, padx=10)

# make roll button
button = ui.CTkButton(master=frame, text="Roll", command=roll)
button.pack(pady=12, padx=10)

# show balance
balancesh = ui.CTkLabel(master=frame, text=userbal, font=("Roboto", 24))
balancesh.pack(pady=12, padx=10)

# Checkbox state
check_var = ui.StringVar(value="off")


# Checkbox Text
text_var = ui.StringVar(value="Over")
my_check = ui.CTkCheckBox(frame2, text="Over",
	variable=check_var, onvalue="over", offvalue="under",
	checkbox_width=35,
	checkbox_height=35,
	font=("helvetica", 18),
	corner_radius=50,
	fg_color="white",
	hover_color="gray",
	text_color="white",
	hover=True,
	textvariable=text_var,
    command=updaterisk,
	)
my_check.pack(pady=20)

# Make slider
slide = ui.CTkSlider(frame2,
    from_=1,
    to=9999,
    command=sliding,
    number_of_steps=1000,
)

slide.pack(pady=20)

# Set initial value for slider
slide.set(5000)

# make number for the slider
slidenr = ui.CTkLabel(frame2, text="5000", font=("Roboto", 15)) 
slidenr.pack(pady=20)

# Show about of reward the user will get on win
rewardshow = ui.CTkLabel(master=frame2, text="Current risk: 3", font=("Roboto", 24))
rewardshow.pack(pady=12, padx=10)

root.mainloop()
