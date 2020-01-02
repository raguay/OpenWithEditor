from fman import DirectoryPaneCommand, show_alert, show_prompt, load_json, save_json, QuicksearchItem, show_quicksearch, show_status_message, clear_status_message
from core.quicksearch_matchers import contains_chars
import subprocess, os
from fman.url import as_human_readable

#
# Setup globals:
#
MYEDITORCHOICE = ".myeditorchoice"      # File containing the editor to use.
MYEDITORS = ".myeditors"                # File containing the list of editors to choose from.
editors = None                          # Dictionary of editor names and paths.

#
# Class:        MyOpenWithEditor
#
# Description:  This command is used to edit files in an editor the 
#               user selected and stored in the MYEDITORCHOICE file. 
#               This file is set by this plugin, Alfred workflow, a 
#               TextBar script, or a BitBar script.
#
class MyOpenWithEditor(DirectoryPaneCommand):
    def __call__(self, url=None):
        global MYEDITORCHOICE
        selected_files = []
        editor = None
        with open(os.path.join(os.path.expanduser('~'), MYEDITORCHOICE), 'r') as content_file:
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

#
# Function:         editFile
#
# Description:      This function is used to open a file with the specified editor.
#                   If the editor specified is an alias, then use the path assigned
#                   to the alias.
#
# Inputs:           editor      The editor to use
#                   file        The file to edit
#
def editFile(editor, file):
    global editors
    if editors is None:
        #
        # Get the alias list or create a empty list if none have been specified.
        #
        editors = load_json('editors.json')
        if editors is None:
            editors = dict()
            save_json('editors.json',editors)
    if editor in editors:
        #
        # It's an alias, use the program path for the proper command line to use.
        #
        subprocess.run(editors[editor] + " '" + as_human_readable(file) + "'",shell=True)
    else:
        #
        # Call using the OS's open command.
        #
        subprocess.run(["/usr/bin/open", "-a", editor, as_human_readable(file)])

#
# Class:        AddEditorAliasPath
#
# Description:  This directory command allows the user to add a new path for
#               an editor alias. An editor alias is when the executable for an
#               editor in MYEDITORS doesn't point to a true program.
#
class AddEditorAliasPath(DirectoryPaneCommand):
    def __call__(self, url=None):
        global editors
        name = None
        loc = None
        name, ok = show_prompt("What alias name do you want for the editor?")
        if name and ok:
            loc, ok = show_prompt("What is the path to the alias?")
            if loc and ok:
                #
                # Save the editor alias for future use.
                #
                if editors is None:
                    editors = dict()
                editors[name] = loc
                save_json('editors.json',editors)
            else:
                show_alert('A path is necessary for this function.')
        else:
            show_alert('A alias name is necessary for this function.')

#
# Class:        AddEditorToUse
#
# Description:  This command allows the user to add to the list of editors
#               to use.
#
class AddEditorToUse(DirectoryPaneCommand):
    def __call__(self, url=None):
        global MYEDITORS
        show_status_message("Adding an Editor to use...")
        edName, ok = show_prompt("What do you want to call your editor?")
        if edName and ok:
            edPath, ok = show_prompt("What is the path or alias for the editor?")
            if edPath and ok:
                pathEditorList = os.path.join(os.path.expanduser('~'), MYEDITORS)
                with open(pathEditorList,"a") as f:
                    f.write(edName + "|" + edPath + "\n")
            else:
                show_alert("A path or alias has to be given.")
        else:
            show_alert("I need a name for your editor.")
        clear_status_message()

#
# Class:        SetEditorToUse
#
# Description:  This command sets the editor to use for editing files. It
#               get the list of editors in MYEDITORS and shows the names
#               to the user. The one the user selects has MYEDITORCHOICE
#               set to the path.
#
class SetEditorToUse(DirectoryPaneCommand):
    def __call__(self, url=None):
        global MYEDITORCHOICE, MYEDITORS
        show_status_message('Set Editor...')
        result = show_quicksearch(self._suggest_editor)
        if result:
            query, editorName = result
            pathEditorList = os.path.join(os.path.expanduser('~'), MYEDITORS)
            if os.path.isfile(pathEditorList):
                with open(pathEditorList, "r") as f:
                    editorsList = f.readlines()
            for editorTuple in editorsList:
                if '|' in editorTuple:
                    edName, editorPath = editorTuple.strip().split('|')[0:2]
                    if edName == editorName:
                        pathEditorChoice = os.path.join(os.path.expanduser('~'), MYEDITORCHOICE)
                        with open(pathEditorChoice,"w") as f:
                            f.write(editorPath)
                        break
        clear_status_message()

    def _suggest_editor(self, query):
        editorList = []
        pathEditorList = os.path.join(os.path.expanduser('~'), MYEDITORS)
        if os.path.isfile(pathEditorList):
            with open(pathEditorList, "r") as f:
                editorList = f.readlines()
        for editorTuple in editorList:
            if '|' in editorTuple:
                editorName = editorTuple.split('|')[0]
                match = contains_chars(editorName.lower(), query.lower())
                if match or not query:
                    yield QuicksearchItem(editorName, highlight=match)

#
# Class:        RemoveEditor
#
# Description:  This command removes an editor to use for editing files. It
#               get the list of editors in MYEDITORS and shows the names
#               to the user. The one the user selects has MYEDITORCHOICE
#               set to the path.
#
class RemoveEditor(DirectoryPaneCommand):
    def __call__(self, url=None):
        global MYEDITORCHOICE, MYEDITORS
        show_status_message('Remove Editor...')
        result = show_quicksearch(self._suggest_editor)
        if result:
            query, editorName = result
            pathEditorList = os.path.join(os.path.expanduser('~'), MYEDITORS)
            if os.path.isfile(pathEditorList):
                with open(pathEditorList, "r") as f:
                    editorsList = f.readlines()
                newEditorList = []
                for editorTuple in editorsList:
                    if '|' in editorTuple:
                        edName, editorPath = editorTuple.strip().split('|')[0:2]
                        if edName != editorName:
                            newEditorList.append(editorTuple)
                with open(pathEditorList,"w") as f:
                    f.write("".join(newEditorList))
        clear_status_message()

    def _suggest_editor(self, query):
        editorList = []
        pathEditorList = os.path.join(os.path.expanduser('~'), MYEDITORS)
        if os.path.isfile(pathEditorList):
            with open(pathEditorList, "r") as f:
                editorList = f.readlines()
        for editorTuple in editorList:
            if '|' in editorTuple:
                editorName = editorTuple.split('|')[0]
                match = contains_chars(editorName.lower(), query.lower())
                if match or not query:
                    yield QuicksearchItem(editorName, highlight=match)


