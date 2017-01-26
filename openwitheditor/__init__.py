from fman import DirectoryPaneCommand, show_alert, load_json
import os

class OpenWithEditor(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            scriptLoc = load_json("OpenWithEditor.json")["scriptLoc"]
            for file in selected_files:
                os.system("'" + scriptLoc + "' 'file' '" + file + "' &")
        else:
            show_alert("No files or directories selected")
