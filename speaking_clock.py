import tkinter as tk

import time, pyttsx3

def speak(string):
    """This function accepts a string and then speaks it."""

    engine = pyttsx3.init('sapi5')
    type_voices = engine.getProperty('voices')
    engine.setProperty('voice', type_voices[0].id)  # 0 - male  #1 - female
    engine.say(string)
    engine.runAndWait()

root = tk.Tk()
root.title('Speaking Clock')
t = tk.StringVar()
t_label = tk.Label(textvariable=t, padx=20, pady=20, 
                    font='calibri 30 bold')
t_label.pack()

time_now = ""
while True:

    try:
        formatted_time = time.strftime('%I:%M:%S %p')

        time_hour = time.strftime('%I')
        if time_hour[0] == '0':
            time_hour = time_hour[1:]

        time_min = time.strftime('%M')
        if time_min[0] == '0':
            time_min = time_min[1:]

        time_meridian = time.strftime('%p')

        time_temp = f"{time_min} minutes past {time_hour} {time_meridian}"

        t.set(formatted_time)
        t_label.update()

        if time_now != time_temp:
            time_now = time_temp
            speak(time_now)

    except:
        pass

root.mainloop()


