import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
from db import add_action, get_records
from time import sleep

# Create the main window
root = tk.Tk()
root.title("Main GUI")
root.geometry("350x400")


def on_message(client, userdata, message):
    message_received = str(message.payload.decode("utf-8"))

    if message_received == "alarm_on":
        alarm_state.config(text="Armed", bg="red")
    elif message_received == "alarm_off":
        alarm_state.config(text="Disarmed", bg="green")
    elif message_received == "living_room_on":
        living_room_light_state.config(text="ON", bg="yellow")
    elif message_received == "living_room_off":
        living_room_light_state.config(text="OFF", bg="red")
    elif message_received == "kitchen_on":
        kitchen_light_state.config(text="ON", bg="yellow")
    elif message_received == "kitchen_off":
        kitchen_light_state.config(text="OFF", bg="red")


# MQTT

host = "node02.myqtthub.com"
port = 1883
clean_session = True
client_id = "thermo"
username = "natelufuluabo@yahoo.ca"
password = "Kylian2021!!"

client = mqtt.Client(client_id=client_id, clean_session=clean_session)
client.username_pw_set(username, password)
client.connect(host, port)

client.loop_start()

client.subscribe("Nathan/Etats")
client.on_message = on_message


def on_alarm_on():
    global history_tree
    client.publish("Nathan/Etats", "alarm_on")
    add_action("Alarm System Armed")
    update_history_window(history_tree)


def on_alarm_off():
    global history_tree
    client.publish("Nathan/Etats", "alarm_off")
    add_action("Alarm System Disarmed") 
    update_history_window(history_tree)


def on_living_room_on():
    global history_tree
    client.publish("Nathan/Etats", "living_room_on")
    add_action("Living room lights on") 
    update_history_window(history_tree)


def on_living_room_off():
    global history_tree
    client.publish("Nathan/Etats", "living_room_off")
    add_action("Living room lights off") 
    update_history_window(history_tree)


def on_kitchen_on():
    global history_tree
    client.publish("Nathan/Etats", "kitchen_on")
    add_action("Kitchen lights on") 
    update_history_window(history_tree)


def on_kitchen_off():
    global history_tree
    client.publish("Nathan/Etats", "kitchen_off")
    add_action("Kitchen lights off") 
    update_history_window(history_tree)

history_window = tk.Toplevel(root)
history_window.title("History")
history_window.geometry("800x300")
history_window.iconify()

# Create a Treeview widget to display the history entries
history_tree = ttk.Treeview(
        history_window, columns=("Time", "Date", "Action"), show="headings"
    )
   
history_tree.heading("Time", text="Time")
history_tree.heading("Date", text="Date")
history_tree.heading("Action", text="Action")


def create_history_window():
    global history_window
    history_window.deiconify()
    global history_tree
    update_history_window(history_tree)
    
def update_history_window(history_tree):
    # Get data from DB
    datas = get_records()

    # Clean up data for usage
    organized_data = []
    for data in datas:
        if data in organized_data:
            continue
        else:
            organized_data.append((data["time"], data["date"], data["action"]))
    
    # Remove all element before updating to avoid duplicate
    history_tree.delete(*history_tree.get_children())

    # Add data to the Treeview
    for entry in organized_data:
        history_tree.insert("", "end", values=entry)

    # Add the Treeview to the window
    history_tree.pack(fill=tk.BOTH, expand=True)


# Texts
font = ("Helvetica", 18)
alarm = tk.Label(root, text="Alarm System", font=font)
living_room_light = tk.Label(root, text="Living Room Light", font=font)
kitchen_light = tk.Label(root, text="Kitchen Light", font=font)
history = tk.Label(root, text="History", font=font)

# Buttons
alarm_on_button = tk.Button(root, text="ON", width=8, command=on_alarm_on)
alarm_off_button = tk.Button(root, text="OFF", width=8, command=on_alarm_off)

living_room_on_button = tk.Button(root, text="ON", width=8, command=on_living_room_on)
living_room_off_button = tk.Button(
    root, text="OFF", width=8, command=on_living_room_off
)

kitchen_on_button = tk.Button(root, text="ON", width=8, command=on_kitchen_on)
kitchen_off_button = tk.Button(root, text="OFF", width=8, command=on_kitchen_off)

history_button = tk.Button(root, text="SHOW", width=12, command=create_history_window)

# State containers
alarm_state = tk.Label(root, text="Disarmed", bg="red", fg="white", font=font)

living_room_light_state = tk.Label(root, text="OFF", bg="red", fg="white", font=font)

kitchen_light_state = tk.Label(root, text="OFF", bg="red", fg="white", font=font)

# Place all widgets on the grid
alarm.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
alarm_on_button.grid(row=1, column=0, padx=5, pady=5)
alarm_off_button.grid(row=1, column=1, padx=5, pady=5)
alarm_state.grid(row=1, column=2, padx=5, pady=5)

living_room_light.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
living_room_on_button.grid(row=3, column=0, padx=5, pady=5)
living_room_off_button.grid(row=3, column=1, padx=5, pady=5)
living_room_light_state.grid(row=3, column=2, padx=5, pady=5)

kitchen_light.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
kitchen_on_button.grid(row=5, column=0, padx=5, pady=5)
kitchen_off_button.grid(row=5, column=1, padx=5, pady=5)
kitchen_light_state.grid(row=5, column=2, padx=5, pady=5)

history.grid(row=6, column=0, padx=10, pady=10, columnspan=2)
history_button.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

root.mainloop()
