# importing only  those functions
# which are needed
import tkinter
from tkinter import *
import os
from gtts import gTTS
import subprocess
import webbrowser

accent_map = [
    ('US', 'com'),
    ('CN', 'any'),
    ('RU', 'ru'),
    ('BR', 'com.br'),
    ('IT', 'it'),
    ('FR', 'fr'),
    ('ES', 'es'),
    ('GB', 'co.uk'),
    ('DE', 'de'),
    ('CZ', 'cz')
]
accent_options = [
    "US",
    "CN",
    "RU",
    "BR",
    "IT",
    "FR",
    "ES",
    "GB",
    "DE",
    "CZ"
]

sample_rate_options = [
    "8",
    "16",
    "32"
]


db_options = [
    "0.0",
    "1.0",
    "2.0",
    "3.0",
    "4.0",
    "5.0",
    "6.0",
    "7.0",
    "8.0",
]


language_map = [
    ('zh', 'zh-CN'),
    ('ru', 'ru'),
    ('pt', 'pt'),
    ('it', 'it'),
    ('fr', 'fr'),
    ('es', 'es'),
    ('en', 'en'),
    ('de', 'de'),
    ('cs', 'cs')
]

language_options = [
    "cs",
    "de",
    "en",
    "es",
    "fr",
    "it",
    "pt",
    "ru",
    "zh"
]


def callback(url):
   webbrowser.open_new_tab(url)


def status(status_text):
    frame_status = tkinter.Frame(master=root)
    frame_status.grid(row=7, column=2)
    label3 = tkinter.Label(master=frame, text=status_text)
    label3.pack()


def onclick(event):

    if len(text.get()) == 0:
        status("Text Empty.")
        return

    if len(filename.get()) == 0:
        status("Filename Empty.")
        return

    if filename.get()[-4:] == ".wav":
        filename_out = filename.get()
    else:
        filename_out = filename.get() + ".wav"
    if len(filename_out) > 10:
        status("Filename to long.")
        return

    google_lang = ""
    google_accent = ""
    for y in range(len(language_map)):
        if language_select.get() == language_map[y][0]:  # Match the language to google code
            google_lang = language_map[y][1]
            print("google lang " + google_lang)
    for y in range(len(accent_map)):
        if accent_selcet.get() == accent_map[y][0]:  # Match the accent to google code
            google_accent = accent_map[y][1]
            print("google acce " + google_accent)
    create_sound(filename_out, text.get(), google_lang, google_accent, sample_select.get(), db_select.get())
    status("File " + filename_out + " created.")


def create_sound(filename_cs, text_cs, language_cs, accent_cs, khz_cs, db_cs):
    samplerate_out = int(khz_cs) * 1000
    print(samplerate_out)
    tts = gTTS(text_cs, lang=language_cs, tld=accent_cs)  # create voice mp3 file with google TTS
    tts.save(filename_cs + ".mp3")
    cmd = "ffmpeg -i " + filename_cs + ".mp3 -y -ac 1 -ar " + str(samplerate_out) + " -af \"volume=" + db_cs + "dB," \
                                    "silenceremove=" \
                                    "start_periods=1:" \
                                    "start_silence=0.1:" \
                                    "start_threshold=-50dB," \
                                    "areverse," \
                                    "silenceremove=start_periods=1" \
                                    ":start_silence=0.1:" \
                                    "start_threshold=-50dB," \
                                    "areverse\" " + filename_cs
    subprocess.run(cmd, shell=True)  # Run ffmpeg command.
    os.remove(filename_cs + ".mp3")  # Delete MP3 file.


def About():
    # Toplevel object which will
    # be treated as a new window
    newwindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newwindow.title("About")

    # sets the geometry of toplevel
    newwindow.geometry("430x280")

    # A Label widget to show in toplevel
    tkinter.Frame(master=newwindow)
    tkinter.Label(newwindow, text="Edge TX Custom Sound Creator", font=('Helveticabold', 12)).\
        grid(row=1, column=2, sticky="N")
    tkinter.Label(newwindow, text="Version 0.1", font=('Helveticabold', 12)). \
        grid(row=2, column=2, sticky="N")
    tkinter.Label(newwindow, text="Date Jan. 16 2022", font=('Helveticabold', 12)). \
        grid(row=3, column=2, sticky="N")
    tkinter.Label(newwindow, text="Designed by Michael Ansorge", font=('Helveticabold', 12)).\
        grid(row=4, column=2, sticky="N")

    link1 = Label(newwindow, text="Discord", font=('Helveticabold', 12), fg="blue", cursor="hand2")
    link1.grid(row=5, column=2, sticky="N")
    link1.bind("<Button-1>", lambda e: callback("https://discord.gg/wF9wUKnZ6H"))

    link2 = Label(newwindow, text="http://edgetx.org/", font=('Helveticabold', 12), fg="blue", cursor="hand2")
    link2.grid(row=6, column=2, sticky="N")
    link2.bind("<Button-1>", lambda e: callback("http://edgetx.org"))

    link3 = Label(newwindow, text="Github", font=('Helveticabold', 12), fg="blue", cursor="hand2")
    link3.grid(row=7, column=2, sticky="N")
    link3.bind("<Button-1>", lambda e: callback("https://github.com/xsnoopy/edgetx-sdcard-sounds"))


# creating tkinter window
root = Tk()
root.title('EdgeTX Custom Sound Creator')
root.geometry('900x300')

# Creating Menubar
menubar = Menu(root)


# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
# file.add_command(label='Open...', command=None)
# file.add_separator()
file.add_command(label='Exit', command=root.destroy)

# Adding Help Menu and commands
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='About', command=About)

menubar.add_cascade(label='File', menu=file)
menubar.add_cascade(label='?', menu=help_menu)

# display Menu
root.config(menu=menubar)

tkinter.Label(root, text="Select langauge").grid(row=0, column=0, sticky="e")
frame = tkinter.Frame(master=root)
frame.grid(row=0, column=1, sticky="w")
language_select = StringVar(root)
language_select.set("en")
OptionMenu(frame, language_select, *language_options).pack()

frame = tkinter.Frame(master=root)
frame.grid(row=1, column=0, sticky="e")
tkinter.Label(master=frame, text="Select accent").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=1, column=1, sticky="w")
accent_selcet = StringVar(root)
accent_selcet.set("US")
OptionMenu(frame, accent_selcet, *accent_options).pack()


frame = tkinter.Frame(master=root)
frame.grid(row=2, column=0, sticky="e")
tkinter.Label(master=frame, text="Please select sample rate ").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=2, column=1, sticky="w")
sample_select = StringVar(root)
sample_select.set("32")
OptionMenu(frame, sample_select, *sample_rate_options).pack()

frame = tkinter.Frame(master=root)
frame.grid(row=2, column=2, sticky="w")
tkinter.Label(master=frame, text="khz").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=3, column=0, sticky="e")
tkinter.Label(master=frame, text="Please decibel gain ").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=3, column=1, sticky="w")
db_select = StringVar(root)
db_select.set("6.0")
OptionMenu(frame, db_select, *db_options).pack()

frame = tkinter.Frame(master=root)
frame.grid(row=3, column=2, sticky="w")
tkinter.Label(master=frame, text="dB").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=4, column=0, sticky="w")
tkinter.Label(master=frame, text="Please enter text to convert:").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=4, column=2)
text = tkinter.Entry(master=frame, width=50)
text.pack()

frame = tkinter.Frame(master=root)
frame.grid(row=5, column=0, sticky="e")
tkinter.Label(master=frame, text="Please enter filename:").pack()

frame = tkinter.Frame(master=root)
frame.grid(row=5, column=2)
filename = tkinter.Entry(master=frame, width=50)
filename.pack()

frame = tkinter.Frame(master=root)
frame.grid(row=6, column=2)
convert = tkinter.Button(master=frame, text="convert")
convert.bind("<Button-1>", onclick)
convert.pack()

mainloop()
