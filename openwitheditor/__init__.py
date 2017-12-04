from fman import DirectoryPaneCommand, show_alert, load_json
import os
from fman.url import as_human_readable
from fman.url import as_url


class OpenWithEditor(DirectoryPaneCommand):
    def __call__(self, url=None):
        selected_files = []
        scriptLoc = load_json("OpenWithEditor.json")["scriptLoc"]
        if url is None:
            selected_files = self.pane.get_selected_files()
            if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
                if len(selected_files) == 0 and self.get_chosen_files():
                    selected_files.append(self.get_chosen_files()[0])
                    for file in selected_files:
                        os.system("'" + scriptLoc + "' 'file' '" + as_human_readable(file) + "' &")
                else:
                    show_alert("No files or directories selected")
        else:
            selected_files[0] = url
            for file in selected_files:
                os.system("'" + scriptLoc + "' 'file' '" + as_human_readable(file) + "' &")
