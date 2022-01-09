# This is a Python script to create EdgeTX Sound files
# Author Michael Ansorge - Michael@believeinrelaty.com
# Version 0.1

import os
import shutil
import git
import click
import csv
from gtts import gTTS
import subprocess
import glob
import time

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


def create_sound(filename, text, language, accent):
    tts = gTTS(text, lang=language, tld=accent)  # create voice mp3 file with google TTS
    tts.save(filename + ".mp3")
    cmd = "ffmpeg -i " + filename + ".mp3 -y -ac 1 -ar 32000 -af \"volume=6.0dB,silenceremove=start_periods=1:" \
                                    "start_silence=0.1:start_threshold=-50dB,areverse,silenceremove=start_periods=1" \
                                    ":start_silence=0.1:start_threshold=-50dB,areverse\" " + filename
    subprocess.run(cmd, shell=True)  # Run ffmpeg command.
    os.remove(filename + ".mp3")  # Delete MP3 file.

def process_csv():
    with open(filenames_voices[x]) as csv_file:  # Open csv file.
        csv_read = list(csv.reader(csv_file, delimiter=';'))  # import csv file and create list of csv lines
        language_from_csv = csv_read[0][3]
        accent_from_csv = csv_read[0][4]
        google_lang = ""
        google_accent = ""
        for y in range(len(language_map)):
            if language_from_csv == language_map[y][0]:  # Match the language to google code
                google_lang = language_map[y][1]
                print("google lang " + google_lang)
        for y in range(len(accent_map)):
            if accent_from_csv == accent_map[y][0]:  # Match the accent to google code
                google_accent = accent_map[y][1]
                print("google acce " + google_accent)
        for row in range(len(csv_read)):  # replace 5 with row         # Loop through all lines of the csv file.
            if os.path.isdir(fullpath + "/" + csv_read[row][0]):  # Check if folder is already existing, if not
                # create folder.
                print("Folder existing, nothing to do here.")
            else:
                print("Create output folder.")
                os.makedirs(fullpath + "/" + csv_read[row][0])
            fullfilename = fullpath + "/" + csv_read[row][0] + "/" + csv_read[row][1]
            create_sound(fullfilename, csv_read[row][2], google_lang, google_accent)
            time.sleep(10)

# Get the current working directory
cwd = os.getcwd()
process = 0

# Print the current working directory
print("Current working directory: {0}".format(cwd))

#  Check if the git repository subfolder exists. If not, clone repoistory.
subfolder = "edgetx-sdcard-sounds"          # subfolder name of cloned repository
fullpath = cwd + "/" + subfolder            # create full path

if os.path.isdir(fullpath):                 # Test if subfolder exists.
    print("No need to clone repository, subfolder exists localy.")
else:
    print("Clone github repository")
    git.Git(cwd).clone("https://github.com/EdgeTX/edgetx-sdcard-sounds.git")
    print("Clone github repository done")

# After cloning a subfolder voices should exist.
# Read all csv files in currenty directory.
filenames_voices = []
for file in glob.glob(fullpath + "/voices/*.csv"):
    filenames_voices.append(file)
filenames_voices.sort()         # sort alphabetically


# Print all detected languages
print("Following languages detected:")
print(*filenames_voices, sep="\n")

if click.confirm('Do you want to process all files?', default=True):    # User Interaction if all files should be
                                                                        # processed.
    print('Do  all files')
    for x in range(len(filenames_voices)):
        print(filenames_voices[x])
        process = 1
        process_csv()

else:
    for x in range(len(filenames_voices)):
        if click.confirm("Do you want to process " + filenames_voices[x] + "?", default=True):  # User Interaction
                                                                            # if specifiv files should be processed.
            process = 1
            process_csv()


if process == 1:
    # Create zipfile for all languages
    print("Creating the ZIP file.")
    print("Please type in the current version:")
    version = input()
    output_filename = fullpath + "/edgetx-sdcard-sounds-" + version
    shutil.make_archive(output_filename, 'zip', fullpath + "/SOUNDS")

print("Done")
