

import PySimpleGUI as sg
import os.path
from PIL import Image
from PIL.ExifTags import TAGS
import pickle

sg.theme('DarkAmber')

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(60, 40), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
metadata_viewer_column =  [
            [sg.Text("Edit Metadata of the image:")],
            [sg.Multiline(default_text="", size=(60, 40), key="-METADATA-")],
            [sg.Button('Edit Metadata', key='-EDIT-')]
        ]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(metadata_viewer_column)
    ]
]

window = sg.Window('Metadata Viewer', layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".jpg", ".jpeg", ".bmp" ))
        ]
        window["-FILE LIST-"].update(fnames)
    if event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-METADATA-"].update(filename)
            
            # Open the image and extract the metadata
            img = Image.open(filename)
            metadata = img.getexif()
            
            # Iterate over all the metadata elements and display them
            metadata_text = ""
            for tag_id in metadata:
                # Get the tag name
                tag = TAGS.get(tag_id, tag_id)
                # Get the tag value
                data = metadata.get(tag_id)
                # Add the name and value of the tag to the metadata text
                metadata_text += f"{tag}: {data}\n"
            
            # Update the metadata text box with the metadata of the selected image
            window["-METADATA-"].update(metadata_text)

            # Enable the "Edit Metadata" button
            window["-EDIT-"].update(disabled=False)

        except:
            pass

    elif event == "-EDIT-":
        if filename == os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            ):
            
            # Open the image and extract the metadata
            img = Image.open(filename)
            metadata = img.getexif()

            # Iterate over all the metadata elements and display them
            metadata_text = ""
            for tag_id in metadata:
                # Get the tag name
                tag = TAGS.get(tag_id, tag_id)
                # Get the tag value
                data = metadata.get(tag_id)
                # Add the name and value of the tag to the metadata text
                metadata_text += f"{tag}: {metadata.get(tag_id)}\n"

            # Create a new layout for the Edit Metadata window
            edit_layout = [
                [sg.Text("Edit Metadata of the image:")],
                [sg.Multiline(default_text=metadata_text, size=(40, 20), key="-EDIT-METADATA-")],
                [sg.Button("Save Changes", key="-SAVE-CHANGES-", size=(15, 1))]
            ]

            # Create a new window for editing metadata
            edit_window = sg.Window('Edit Metadata', edit_layout)
            print("ventana edit creada")
            while True:
                edit_event, edit_values = edit_window.read()

                if edit_event == sg.WIN_CLOSED:
                    break
                elif edit_event == "-SAVE-CHANGES-":
                    print("uno")
                    # Parse the new metadata and update the image
                    new_metadata = {}
                    for line in edit_values["-EDIT-METADATA-"].split("\n"):
                        if ":" in line:
                            tag_name, tag_value = line.split(": ")
                            tag_id = TAGS.get(tag_name, tag_name)
                            new_metadata[tag_id] = tag_value
                            print ("dos")

                    edit_window.close()
                    print("tres")
                    window['-METADATA-'].update(edit_values['-EDIT-METADATA-'])
                    print("cuatro")
                    sg.popup("Metadata updated successfully!")
                    print("cinco")
                    break
        
        # sg.popup("Sale del programa inesperadamente")
            
        # img.save(filename, format="JPEG", exif=new_metadata)
            

        # Close the Edit Metadata window
window.close()