# This is a Python script to convert EdgeTX CSV files from the old to the new format.
# Author Michael Ansorge - Michael@believeinrelaty.com
# Version 0.1


import csv
import json
import glob


languages_names = [
    ('aa', 'Afar'),
    ('ab', 'Abkhazian'),
    ('af', 'Afrikaans'),
    ('ak', 'Akan'),
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('an', 'Aragonese'),
    ('hy', 'Armenian'),
    ('as', 'Assamese'),
    ('av', 'Avaric'),
    ('ae', 'Avestan'),
    ('ay', 'Aymara'),
    ('az', 'Azerbaijani'),
    ('ba', 'Bashkir'),
    ('bm', 'Bambara'),
    ('eu', 'Basque'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('bh', 'Bihari languages'),
    ('bi', 'Bislama'),
    ('bo', 'Tibetan'),
    ('bs', 'Bosnian'),
    ('br', 'Breton'),
    ('bg', 'Bulgarian'),
    ('my', 'Burmese'),
    ('ca', 'Catalan; Valencian'),
    ('cs', 'Czech'),
    ('ch', 'Chamorro'),
    ('ce', 'Chechen'),
    ('zh', 'Chinese'),
    ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
    ('cv', 'Chuvash'),
    ('kw', 'Cornish'),
    ('co', 'Corsican'),
    ('cr', 'Cree'),
    ('cy', 'Welsh'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('dv', 'Divehi; Dhivehi; Maldivian'),
    ('nl', 'Dutch; Flemish'),
    ('dz', 'Dzongkha'),
    ('el', 'Greek, Modern (1453-)'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('eu', 'Basque'),
    ('ee', 'Ewe'),
    ('fo', 'Faroese'),
    ('fa', 'Persian'),
    ('fj', 'Fijian'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('fy', 'Western Frisian'),
    ('ff', 'Fulah'),
    ('Ga', 'Georgian'),
    ('de', 'German'),
    ('gd', 'Gaelic; Scottish Gaelic'),
    ('ga', 'Irish'),
    ('gl', 'Galician'),
    ('gv', 'Manx'),
    ('el', 'Greek, Modern (1453-)'),
    ('gn', 'Guarani'),
    ('gu', 'Gujarati'),
    ('ht', 'Haitian; Haitian Creole'),
    ('ha', 'Hausa'),
    ('he', 'Hebrew'),
    ('hz', 'Herero'),
    ('hi', 'Hindi'),
    ('ho', 'Hiri Motu'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('hy', 'Armenian'),
    ('ig', 'Igbo'),
    ('is', 'Icelandic'),
    ('io', 'Ido'),
    ('ii', 'Sichuan Yi; Nuosu'),
    ('iu', 'Inuktitut'),
    ('ie', 'Interlingue; Occidental'),
    ('ia', 'Interlingua (International Auxiliary Language Association)'),
    ('id', 'Indonesian'),
    ('ik', 'Inupiaq'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('jv', 'Javanese'),
    ('ja', 'Japanese'),
    ('kl', 'Kalaallisut; Greenlandic'),
    ('kn', 'Kannada'),
    ('ks', 'Kashmiri'),
    ('ka', 'Georgian'),
    ('kr', 'Kanuri'),
    ('kk', 'Kazakh'),
    ('km', 'Central Khmer'),
    ('ki', 'Kikuyu; Gikuyu'),
    ('rw', 'Kinyarwanda'),
    ('ky', 'Kirghiz; Kyrgyz'),
    ('kv', 'Komi'),
    ('kg', 'Kongo'),
    ('ko', 'Korean'),
    ('kj', 'Kuanyama; Kwanyama'),
    ('ku', 'Kurdish'),
    ('lo', 'Lao'),
    ('la', 'Latin'),
    ('lv', 'Latvian'),
    ('li', 'Limburgan; Limburger; Limburgish'),
    ('ln', 'Lingala'),
    ('lt', 'Lithuanian'),
    ('lb', 'Luxembourgish; Letzeburgesch'),
    ('lu', 'Luba-Katanga'),
    ('lg', 'Ganda'),
    ('mk', 'Macedonian'),
    ('mh', 'Marshallese'),
    ('ml', 'Malayalam'),
    ('mi', 'Maori'),
    ('mr', 'Marathi'),
    ('ms', 'Malay'),
    ('Mi', 'Micmac'),
    ('mk', 'Macedonian'),
    ('mg', 'Malagasy'),
    ('mt', 'Maltese'),
    ('mn', 'Mongolian'),
    ('mi', 'Maori'),
    ('ms', 'Malay'),
    ('my', 'Burmese'),
    ('na', 'Nauru'),
    ('nv', 'Navajo; Navaho'),
    ('nr', 'Ndebele, South; South Ndebele'),
    ('nd', 'Ndebele, North; North Ndebele'),
    ('ng', 'Ndonga'),
    ('ne', 'Nepali'),
    ('nl', 'Dutch; Flemish'),
    ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
    ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
    ('no', 'Norwegian'),
    ('oc', 'Occitan (post 1500)'),
    ('oj', 'Ojibwa'),
    ('or', 'Oriya'),
    ('om', 'Oromo'),
    ('os', 'Ossetian; Ossetic'),
    ('pa', 'Panjabi; Punjabi'),
    ('fa', 'Persian'),
    ('pi', 'Pali'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ps', 'Pushto; Pashto'),
    ('qu', 'Quechua'),
    ('rm', 'Romansh'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('rn', 'Rundi'),
    ('ru', 'Russian'),
    ('sg', 'Sango'),
    ('sa', 'Sanskrit'),
    ('si', 'Sinhala; Sinhalese'),
    ('sk', 'Slovak'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('se', 'Northern Sami'),
    ('sm', 'Samoan'),
    ('sn', 'Shona'),
    ('sd', 'Sindhi'),
    ('so', 'Somali'),
    ('st', 'Sotho, Southern'),
    ('es', 'Spanish; Castilian'),
    ('sq', 'Albanian'),
    ('sc', 'Sardinian'),
    ('sr', 'Serbian'),
    ('ss', 'Swati'),
    ('su', 'Sundanese'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('ty', 'Tahitian'),
    ('ta', 'Tamil'),
    ('tt', 'Tatar'),
    ('te', 'Telugu'),
    ('tg', 'Tajik'),
    ('tl', 'Tagalog'),
    ('th', 'Thai'),
    ('bo', 'Tibetan'),
    ('ti', 'Tigrinya'),
    ('to', 'Tonga (Tonga Islands)'),
    ('tn', 'Tswana'),
    ('ts', 'Tsonga'),
    ('tk', 'Turkmen'),
    ('tr', 'Turkish'),
    ('tw', 'Twi'),
    ('ug', 'Uighur; Uyghur'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('ve', 'Venda'),
    ('vi', 'Vietnamese'),
    ('vo', 'Volapük'),
    ('cy', 'Welsh'),
    ('wa', 'Walloon'),
    ('wo', 'Wolof'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('yo', 'Yoruba'),
    ('za', 'Zhuang; Chuang'),
    ('zh', 'Chinese'),
    ('zu', 'Zulu')
]

sounddata = {
    "language": [],
    "name": [],
    "description": [],
    "directory": []
}
# Read all csv files in currenty directory.
filenames_voices = []
for file in glob.glob("*.csv"):
    filenames_voices.append(file)
filenames_voices.sort()         # sort alphabetically

for x in range(len(filenames_voices)):
    print("###################################################################")
    print("Converting: " + filenames_voices[x])
    language = filenames_voices[x][:2]
    print("language = " + language)
    country_code = filenames_voices[x][3:5]
    print("country code = " + country_code)
    gender = filenames_voices[x][6:7]
    print("gender = " + gender)
    voice_name = filenames_voices[x][8: filenames_voices[x].find(".csv")]
    print("voice Name = " + voice_name)

    # Create sounds.json data example:
    #  "language": "en-GB",
    #  "name": "British English Female",
    #  "description": "British English Female Voice (en-GB-Libby)",
    #  "directory": "en_gb-libby"
    if gender == "f":
        gender_long = "Female"
    else:
        gender_long = "Male"
    for y in range(len(languages_names)):
        if language == languages_names[y][0]:           # Get language name from 2 letter code
            language_noun = languages_names[y][1]
    print("language: " + language + "-" + country_code)
    print("name: " + " " + language_noun + " " + gender_long)
    print("description: " + " " + language_noun + " " + gender_long + " Voice (" + language + "-" +
          country_code + "-" + voice_name + ")")
    if voice_name == "":        # Check if voice name exists.
        print("directory " + language + "-" + country_code)
    else:
        print("directory " + language + "-" + country_code + "-" + voice_name)

    # add data to dictonary for export in json
    sounddata["language"].append(language + "-" + country_code)
    sounddata["name"].append(language_noun + " " + gender_long)
    if voice_name == "":        # Check if voice name exists.
        sounddata["description"].append(language_noun + " " + gender_long + " Voice (" + language + "-" +
                                        country_code + ")")
        sounddata["directory"].append(language + "-" + country_code)
    else:
        sounddata["description"].append(language_noun + " " + gender_long + " Voice (" + language + "-" +
                                        country_code + "-" + voice_name + ")")
        sounddata["directory"].append(language + "-" + country_code + "-" + voice_name)
    json_object = json.dumps(sounddata, indent=4)

    # Converting csv file.
    with open(filenames_voices[x]) as csv_input:    # open original csv file
        with open(filenames_voices[x][:-4] + "-new.csv", 'w') as csv_output:  # create new csv file
            # CSV converting
            csv_read = list(csv.reader(csv_input, delimiter=';'))  # import csv file and create list of csv lines
            """ 
            Field 0: 	File location on SD Card. Subfolder SOUNDS + langauge + if applicable: „-“ followed by 
                        gender followed by „-“ followed by country code in Alpha 2 letter Capital followed „-“ 
                        followed by Name of voice with starting with capital Letter + subfolder SYSTEMS 
            Field 1: 	Filename
            Field 2:    Spoken Text
            Field 3:	Language 
            Field 4:	country code / Accent in Alpha 2 letter Capital
            Field 5:	Gender of voice either m or f
            Field 6:	Name of voice with starting with Capital letter.
            Field 7:	Written description.
            """
            for row in range(len(csv_read)):           # Loop through all lines of the csv file.
                output = list()  # Create an empty list.
                # Filed 0 Assignment: Check if original location is a SYSTEM location
                if voice_name == "":
                    if csv_read[row][0][-6:] == "SYSTEM":
                        output.append(str("SOUNDS/" + language + "-" + country_code + "-" + gender + "/SYSTEM"))
                    else:
                        output.append(str("SOUNDS/" + language + "-" + country_code + "-" + gender))
                else:
                    if csv_read[row][0][-6:] == "SYSTEM":
                        output.append(str("SOUNDS/" + language + "-" + country_code + "-" + gender + "-" +
                                          voice_name + "/SYSTEM"))
                    else:
                        output.append(str("SOUNDS/" + language + "-" + country_code + "-" + gender + "-" +
                                          voice_name))

                # Add Field 1 filename
                output.append(str(csv_read[row][1]))
                # Add Field 2 spoken text
                output.append(str(csv_read[row][2]))
                # Add Field 3 language
                output.append(str(language))
                # Add Field 4 country code
                output.append(str(country_code))
                # Add Field 5 gender
                output.append(str(gender))
                # Add Field 6 voice name
                output.append(str(voice_name))

                # Write into new .csv file
                writer = csv.writer(csv_output, delimiter=';')
                writer.writerow(output)

        print("Saving: " + filenames_voices[x])

print("Write Sound.json file")
with open("sample.json", "a") as outfile:
    outfile.write(json_object)
