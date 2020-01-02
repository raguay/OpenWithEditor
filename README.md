## OpenWithEditor

Plugin for [fman.io](https://fman.io) to edit files using the editor specified in the [BitBar](https://getbitbar.com/) plugin [currentFiles.1h.rb](https://getbitbar.com/plugins/System/currentFiles.1h.rb).

Install with [fman's built-in command for installing plugins](https://fman.io/docs/installing-plugins).

To use with the **BitBar** plugin, you will need to have [BitBar](https://getbitbar.com/) installed and the [currentFiles.1h.rb](https://getbitbar.com/plugins/System/currentFiles.1h.rb) plugin installed and configured. You can also use the [Alfred BitBar Workflow](https://github.com/raguay/MyAlfred/blob/master/Alfred%203/BitBarWorkflow.alfredworkflow) to control the plugin.

Alternatively, you can use the [TextBar](http://richsomerfield.com/apps/textbar/) program with the [Current Files and Editor](https://github.com/raguay/TextBarScripts/blob/master/Current%20Files%20and%20Editor.textbar) plugin installed. You can use the [Alfred](https://www.alfredapp.com/) with the [My Editor Workflow](https://github.com/raguay/MyAlfred/blob/master/Alfred%203/My%20Editor%20Workflow.alfredworkflow) to control the editor and edit files.

After restarting **fman**, you will be able to select the editor you are currently using to edit file.

Since this plugin used files from the above two mentioned plugins for TextBar or BitBar, this plugin is intended for and usable mostly on a macOS system. It should be usable on other systems if you create the needed files in your home directory yourself.

These commands described in the **Usage** area can be used to create the editor list. Therefore, the other programs are not necessary to use this plugin anymore.

### Usage

Pressing **F4** with files selected or simply highlighted will open the file in the editor that you specify in the plugin. Changing the current editor in the **BitBar** plugin will change which editor is used instantly.

The following Commands are available as well:

| -- | ----- |
| My open with editor | This will open the currently selected or file under the cursor to edit in the editor already chosen. |
| Set editor to use | This will list all the editors in the `~/.myeditors` file allowing the user to pick one. That editor will be used to open files. |
| Add editor to use | This will ask for an editor display name and path. This will be saved in the `~/.myeditors` file and used to display in the `Set editor to use` command. |
| Add editor alias path | This allows the user to set a command line path to a command to open the editor. This alias should be used for the path in `Add editor to use` command. |
| Remove editor | This allows the user to remove an editor from the list of editors. |

### Features

 - Opens selected files in the editor specified by the **BitBar** plugin, **TextBar** plugin, or Alfred workflow.
 - Add and remove editors to be used.
 - Add editor aliases to use for running command line programs for the editor.

## Things to Add

 - Specify a different command then `open -a` to open programs so that the plugin can be used on other OSes.

