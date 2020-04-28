import requests
import tkinter as tk
import time

# Requests to get the data

# Using http://covid19api.xapix.io/v2/locations?country_code=US for the
# total cases in the country

# Make a request for the state and country information and convert it into a json object
states = requests.get("https://covidtracking.com/api/states").json()
country = requests.get("https://covidtracking.com/api/states").json()

# Tkinter GUI

app = tk.Tk()

# Scrollbar

# Master frame to control everything
frame = tk.Frame(app, width = 1500, height = 1080)

# Create canvas within that frame to display everything
canvas = tk.Canvas(frame, width = 1500, height = 1080)

# Create the frame that we want to see and to add information on
scrollable_frame = tk.Frame(canvas, width= 1500, height = 1080)

# Function that allows the canvas to be updated to new configurations made
def update_scrollregion(event):
    canvas.configure(scrollregion = canvas.bbox("all"))

#Binds whenever the canvas is updared the function is run

canvas.bind("<Configure>", update_scrollregion)

#Create the scrollbar
scrollbar = tk.Scrollbar(frame, orient = "vertical", command = canvas.yview)

# Puts the frame in view of the canvas
canvas.create_window((0,0), window = scrollable_frame, anchor = "nw")

# Configures canvas to set scrollbar 
canvas.configure(yscrollcommand = scrollbar.set)

# tkinter labels

# HEADER
# Set all the headers
headers = ["State", "Positive", "Negative", "Deaths", "Totals"]

# Iterate over all headers
for x in range(0, len(headers)):
    # Create labels
    var = tk.Label(scrollable_frame, text = "     " + headers[x] + "     ", font = ('calibri', 40, 'bold') )
    #Add in grid form
    var.grid(row = 0, column = x)

# Remove all null values in the json to be N/A
# Iterate through all states
for state in states:
    # Iterates over all keys in the dictionary within each state object
    for key in state.keys():
        if state[key] == None:
            state[key] = "N/A"

# All of the keys for the data points we will be using in this application
dataPoints = ["state", "positive", "negative", "death", "total"]

# Iterates over all states / rows
for x in range(0, len(states)):
    for y in range(0, len(dataPoints)):
        # Create a label containing the vaule in the column for the state
        tmpLabel = tk.Label(scrollable_frame, font = ('calibri', 16), text = states[x][dataPoints[y]])
        # Grids the label to the right section of the gui
        tmpLabel.grid(row = x+1, column = y)

# Scrollbar cont.

# Put the master frame in 0,0
frame.grid(row = 0, column = 0)

# Puts canvas that contains the viewable frame at 0,0 of master frame
canvas.grid(row = 0, column = 0)

# Put scrollbar into view
scrollbar.grid(row = 0, column = 5, sticky = "ne")

# Run
app.mainloop()




