import os
import shutil
from mutagen.easyid3 import EasyID3

class MusicOrganiser:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def organise(self):
        pass
        # TODO: Implement organization logic

    def edit_metadata(self, filename, metadata):
        pass
        # TODO: Implement your metadata editing logic here
