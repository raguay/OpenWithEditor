from fman import DirectoryPaneCommand, show_alert
import os
from fman.url import as_human_readable


class MyOpenWithEditor(DirectoryPaneCommand):
    def __call__(self, url=None):
        selected_files = []
        editor = None
        with open(os.path.expanduser('~') + "/.myeditorchoice", 'r') as content_file:
            editor = content_file.read().strip()

        if (editor is not None) and (editor != ''):
            if url is None:
                selected_files = self.pane.get_selected_files()
                if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
                    if len(selected_files) == 0 and self.get_chosen_files():
                        selected_files.append(self.get_chosen_files()[0])
                        for file in selected_files:
                            editFile(editor, file)
                    else:
                        show_alert("No files or directories selected")
            else:
                editFile(editor, url)
        else:
            show_alert("Editor not configured.")


def editFile(editor, file):
    if editor == 'oni2':
        os.system("/Applications/Onivim2.App/Contents/MacOS/Oni2 '" + as_human_readable(file) + "' &")
    else:
        os.system("/usr/bin/open -a '" + editor + "' '" + as_human_readable(file) + "' &")
