import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    message_received = str(message.payload.decode("utf-8"))
    print("received message: ", message_received)


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
    client.publish("Nathan/Etats", "alarm_on")
    print("Message published, alarm_on")
    # alarm_state.config(text="Armed", bg="green")


def on_alarm_off():
    client.publish("Nathan/Etats", "alarm_off")
    print("Message published, alarm_off")
    # alarm_state.config(text="Disarmed", bg="red")


def on_living_room_on():
    client.publish("Nathan/Etats", "living_room_on")
    print("Message published, living_room_on")
    # living_room_light_state.config(text="ON", bg="yellow")


def on_living_room_off():
    client.publish("Nathan/Etats", "living_room_off")
    print("Message published, living_room_off")
    # living_room_light_state.config(text="OFF", bg="red")


def on_kitchen_on():
    client.publish("Nathan/Etats", "kitchen_on")
    print("Message published, kitchen_on")
    # kitchen_light_state.config(text="ON", bg="yellow")


def on_kitchen_off():
    client.publish("Nathan/Etats", "kitchen_off")
    print("Message published, kitchen_off")
    # kitchen_light_state.config(text="OFF", bg="red")


def on_show_history():
    # Create a new window for the history
    history_window = tk.Toplevel(root)
    history_window.title("History")
    history_window.geometry("800x300")

    # Create a Treeview widget to display the history entries
    history_tree = ttk.Treeview(
        history_window, columns=("Time", "Date", "Action"), show="headings"
    )
    history_tree.heading("Time", text="Time")
    history_tree.heading("Date", text="Date")
    history_tree.heading("Action", text="Action")

    # Add some sample data to the Treeview
    sample_data = [
        ("12:30", "2023-07-19", "Armed"),
        ("13:45", "2023-07-19", "Disarmed"),
        ("14:10", "2023-07-19", "Light ON"),
        ("14:25", "2023-07-19", "Light OFF"),
    ]

    for entry in sample_data:
        history_tree.insert("", "end", values=entry)

    # Add the Treeview to the window
    history_tree.pack(fill=tk.BOTH, expand=True)


# Create the main window
root = tk.Tk()
root.title("Main GUI")
root.geometry("350x350")

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

history_button = tk.Button(root, text="SHOW", width=12, command=on_show_history)

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
