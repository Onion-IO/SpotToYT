from logging import root
import tkinter as tk
import App 

#declaring variables
window = tk.Tk()
output_URL = tk.StringVar(value='Youtube Playlist URL will appear here')
current_state = tk.StringVar(value='Awaiting input')
ID_text = tk.StringVar(window)
USR_text = tk.StringVar(window)
playlist_link = 'potato'
out_URL = tk.StringVar(window)

#functions for buttons
def change_output_URL():
    print("Output URL")
    App.main()
    output_URL.set(App.final_URL)

def confirm_ID():
    print('Confirming ID')
    print(current_state)
    App.playlist_link = ID_text.get()
    print('confirmed playlist ID as: ' + App.playlist_link)

def set_username():
    print('setting username')
    App.username = USR_text.get()
    print('confirmed playlist ID as: ' + App.username)


#Spotify playlist ID
frame_a = tk.Frame(bg = '#191414')
Namelabel = tk.Label(master = frame_a, bg='#191414', fg='White', text="SpotToYT GUI")
IDlabel = tk.Label(master = frame_a, bg='#191414', fg='LimeGreen', text="Enter Spotify playlist ID (comes after /playlist/ in the URL)")
IDentry = tk.Entry(master = frame_a, width=60, exportselection=0, textvariable=ID_text)
IDbutton = tk.Button(master = frame_a, bg='#191414', fg='white', text="Set ID", command = confirm_ID)
IDlabel.configure(font=("Franklin", 14, "bold"))
Namelabel.configure(font=("Miriam", 18, "bold", "underline"))

#Spotify username
frame_b = tk.Frame(bg = '#191414')
USRlabel = tk.Label(master = frame_b, bg='#191414', fg='LimeGreen', text="Enter Spotify username (the one used at login)")
USRentry = tk.Entry(master = frame_b, width=60, exportselection=0, textvariable=USR_text)
USRbutton = tk.Button(master = frame_b, bg='#191414', fg='white', text="Set Username", command = set_username)
USRlabel.configure(font=("Franklin", 14, "bold"))

#URL output
frame_c = tk.Frame(bg = '#191414')
YTlabel1 = tk.Label(master = frame_c, bg='#191414', fg='Red', text="Created playlist URL:")
YTentry = tk.Entry(master = frame_b, width=60,exportselection=0, textvariable=output_URL)
YTlabel1.configure(font=("Franklin", 14, "bold"))

#launch button
main_frame = tk.Frame(bg = '#191414')
main_button = tk.Button(master = main_frame, bg='#191414', fg='white', text="Launch Conversion", command = change_output_URL)



Namelabel.pack()
IDlabel.pack()
IDentry.pack()
IDbutton.pack()
frame_a.pack()

USRlabel.pack()
USRentry.pack()
USRbutton.pack()
frame_b.pack()

YTlabel1.pack()
YTentry.pack()
frame_c.pack()

main_button.pack()
main_frame.pack()

window.configure(background='#191414')

window.mainloop()