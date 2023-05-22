import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from typing import Optional

class GUI(ttk.Frame):
    def __init__(self, master: Optional[tk.Tk] = None):
        if master is None:
            raise ValueError("master cannot be None")
        super().__init__(master)
        self.master = master
        self.grid(sticky='nsew')
        self.master.geometry('1000x800')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.master.title("DubDib Music Organiser")
        self.master.tk.call("source", "./themes/azure.tcl")
        self.master.tk.call("set_theme", "light")
    
        # Set up Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(sticky='nsew', padx=10, pady=10)

        # Create Notebook Tabs
        self.music_library_frame = ttk.Frame(self.notebook)
        self.music_library_frame.grid(sticky='nsew', padx=2)

        self.organise_frame = ttk.Frame(self.notebook)
        self.organise_frame.grid(sticky='nsew')

        self.settings_frame = ttk.Frame(self.notebook)
        self.settings_frame.grid(sticky='nsew')

        # Add frames to Notebook
        self.notebook.add(self.organise_frame, text='Organiser   ')
        self.notebook.add(self.music_library_frame, text='Music Library   ')
        self.notebook.add(self.settings_frame, text='Settings   ')

        # Variable to hold directory paths
        self.default_input_directory = tk.StringVar()
        self.default_output_directory = tk.StringVar()

        # Setup each tab
        self.organise()
        self.music_library()
        self.settings()
    
    # Settings screen
    def settings(self):
        
        # Label for input directory button
        self.input_dir_label = ttk.Label(self.settings_frame, text="Select Default Input Directory:")
        self.input_dir_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        
        # Button for the default input directory
        self.select_input_button = ttk.Button(
            self.settings_frame,
            text="Browse",
            command=self.select_input_directory
        )
        self.select_input_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        # Display default input directory
        self.input_dir_selected = ttk.Label(self.settings_frame, textvariable=self.default_input_directory)
        self.input_dir_selected.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        #Label for output directory button
        self.output_dir_label = ttk.Label(self.settings_frame, text="Select Default Output Directory:")
        self.output_dir_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        # Button for the default output directory
        self.select_output_button = ttk.Button(
            self.settings_frame,
            text="Browse",
            command=self.select_output_directory
        )
        self.select_output_button.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.output_dir_selected = ttk.Label(self.settings_frame, textvariable=self.default_output_directory)
        self.output_dir_selected.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # Separator
        self.separator = ttk.Separator(self.settings_frame, orient='horizontal')
        self.separator.grid(row=4, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

        # Button to change theme
        self.theme_button = ttk.Button(self.settings_frame, text="Toggle Light/Dark Mode", command=self.change_theme)
        self.theme_button.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    def select_input_directory(self):
        dir_path = filedialog.askdirectory()
        self.default_input_directory.set(dir_path)

    def select_output_directory(self):
        dir_path = filedialog.askdirectory()
        self.default_output_directory.set(dir_path)

    # Change theme function provided by Azure theme creator https://github.com/rdbende/Azure-ttk-theme
    def change_theme(self):
        # Theme change function
        if self.master.tk.call("ttk::style", "theme", "use") == "azure-dark":
            # Set light theme
            self.master.tk.call("set_theme", "light")
        else:
            # Set dark theme
            self.master.tk.call("set_theme", "dark")

    def music_library(self):
        ttk.Label(self.music_library_frame, text="Here's Your Music Library").grid()

        # Define Columns
        self.columns = ('track_name', 'artist', 'album', 'genre', 'tags', 'location')

        # Create treeview widget
        self.table = ttk.Treeview(self.music_library_frame, columns=self.columns, show='headings')

        # Specify column headings
        self.table.heading('track_name', text='TRACK NAME')
        self.table.heading('artist', text='ARTIST')
        self.table.heading('album', text='ALBUM')
        self.table.heading('genre', text='GENRE')
        self.table.heading('tags', text='TAGS')
        self.table.heading('location', text='LOCATION')

        self.table.bind('<<TreeviewSelect>>', self.item_selected)

        # Make the table expand to the frame
        self.music_library_frame.grid_rowconfigure(1, weight=1)
        self.music_library_frame.grid_columnconfigure(0, weight=1)
        self.table.grid(row=1, column=0, sticky='nsew')
        
        # Add a vertical scrollbar
        self.scrollbar_y = ttk.Scrollbar(self.music_library_frame, orient='vertical')
        self.scrollbar_y.configure(command=self.table.yview)
        self.scrollbar_y.grid(row=1, column=1, sticky='ns')

        # Add a horizontal scrollbar
        self.scrollbar_x = ttk.Scrollbar(self.music_library_frame, orient='horizontal')
        self.scrollbar_x.configure(command=self.table.xview)
        self.scrollbar_x.grid(row=2, column=0, sticky='ew')

        # Add save button
        self.save_button = ttk.Button(
            self.music_library_frame,
            text="SAVE CHANGES",
            command=self.edit_metadata
        )
        self.save_button.grid(row=3, column=0, sticky='ew')

        # Generate dummy data
        tracks = []
        for n in range (1, 100):
            tracks.append((f'Track {n}', f'Artist {n}', f'Album {n}', f'Genre {n}', f'Tags {n}', f'Location {n}'))

        # Add data to treeview
        for track in tracks:
            self.table.insert('', tk.END, values=track)

        return self.table
    
    def item_selected(self, event):
        pass

    def edit_metadata(self):
        pass

    def organise(self):
        ttk.Label(self.organise_frame, text="Organise Tab").grid()

        # Prompt for source directory button
        self.source_dir_prompt = ttk.Label(self.organise_frame, text="Select Source Folder:")
        self.source_dir_prompt.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        # Button browsing for the source directory
        self.source_browse_button = ttk.Button(
            self.organise_frame,
            text="Browse",
            command=self.select_input_directory
        )
        self.source_browse_button.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Display input directory
        self.source_dir_selected = ttk.Label(self.organise_frame, textvariable=self.default_input_directory)
        self.source_dir_selected.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        # Prompt for destination directory button
        self.destination_dir_prompt = ttk.Label(self.organise_frame, text="Select Destination Folder:")
        self.destination_dir_prompt.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        # Button browsing for the destination directory
        self.destination_browse_button = ttk.Button(
            self.organise_frame,
            text="Browse",
            command=self.select_output_directory
        )
        self.destination_browse_button.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Display destination directory
        self.destination_dir_selected = ttk.Label(self.organise_frame, textvariable=self.default_output_directory)
        self.destination_dir_selected.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        # Scan button to find files

        # Label for organisation options
        self.organisation_options = ttk.Label(self.organise_frame, text="Organise tracks by:")
        self.organisation_options.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        # Radio Buttons
        self.selected_sort = tk.StringVar()
        self.option1 = ttk.Radiobutton(self.organise_frame, text='Artist', value='artist', variable=self.selected_sort)
        self.option1.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.option2 = ttk.Radiobutton(self.organise_frame, text='Genre', value='genre', variable=self.selected_sort)
        self.option2.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.option3 = ttk.Radiobutton(self.organise_frame, text='Tag', value='tag', variable=self.selected_sort)
        self.option3.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        # Sort Button
        self.organise_button = ttk.Button (
            self.organise_frame,
            text="DubDib",
            command=self.organise_files
        )
        self.organise_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    def organise_files(self):
        pass