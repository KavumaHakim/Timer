import ttkbootstrap as tb 
from customtkinter import CTkButton, CTkSwitch, CTkInputDialog
import pygame
from ttkbootstrap.dialogs.dialogs import Messagebox


window = tb.Window(themename='cyborg', title='Timer', maxsize=(500,500))
window.iconbitmap("icon1.ico")
window.geometry('600x600+550+150')
#Title label
Label = tb.Label(window, text='TIMER', font=('Arial', 15), padding='12')
Label.pack()


def Start():
    pygame.mixer.quit()
    pygame.mixer.init()
    Dialog = CTkInputDialog(title='Timer', text='Enter Limit time')
    try:
        global set_time
        set_time = int(Dialog.get_input())
    except:
        Messagebox.show_info(message='Invalid Value.', title='Error', alert=True, bootstyle='danger', font=('Anydore', 50))

    meter.configure(amountused=0)
    meter.configure(amounttotal=set_time)
    tm()

def Stop():
    meter.after_cancel(tm_id)
    switch.configure(state='normal')
    pygame.mixer.quit()
    pygame.mixer.init()

pygame.mixer.init()

def tm():
    if meter.amountusedvar.get() <= (set_time - 1):
        meter.amountusedvar.set(meter.amountusedvar.get() + 1)
        switch.configure(state='disabled')
        global tm_id
        tm_id = meter.after(1000 if not on.get() else 60000, tm)
    elif meter.amountusedvar.get() == (set_time):
        pygame.mixer.music.load('Alarm.mp3')
        pygame.mixer.music.play(loops = 1, fade_ms=3000)


tm_id = None  # to store the timer ID


def switched():
    if on.get():
        meter.configure(subtext = 'MINUTES')
    else:
        meter.configure(subtext = 'SECONDS')





on = tb.BooleanVar(value=False)

switch = CTkSwitch(window,
                    text='Minutes',
                    text_color='#52cc00',
                    font=('Arial', 15), variable=on,
                    switch_height=20, 
                    switch_width=40, 
                    progress_color='blue', 
                    button_hover_color='red', 
                    button_color='green',
                    command = switched
                    )
switch.place(x = 20,y = 20)

meter = tb.Meter(window,
                textfont=('Arial', 20),
                bootstyle='danger',
                meterthickness=20,
                #wedgesize=1,
                stripethickness=2,
                interactive=False,
                subtextstyle='success',
                subtext='SECONDS',
                metersize=300,
                metertype='full'
                )
meter.pack()

controls = tb.Frame(window)

start_button = CTkButton(controls, text='Start', corner_radius=50, hover_color="#52cc00", cursor='hand2', fg_color="blue", command = Start)
start_button.pack(side = tb.LEFT)
start_button.bind('<Enter>', lambda e: start_button.configure(text_color='white', fg_color="#52cc00"))
start_button.bind('<Leave>', lambda e: start_button.configure(text_color='white', fg_color="blue" ))

stop_button = CTkButton(controls, text='Stop', corner_radius=50, hover_color="red", cursor='hand2', fg_color="blue", command = Stop)
stop_button.pack(side = tb.RIGHT, padx=10)

controls.pack(pady = 40)

window.mainloop()
