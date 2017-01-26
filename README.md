## OpenWithEditor

Plugin for [fman.io](https://fman.io) to edit files using the editor specified in the [BitBar](https://getbitbar.com/) plugin [currentFiles.1h.rb](https://getbitbar.com/plugins/System/currentFiles.1h.rb).

Install by uploading "OpenWithEditor" to your [data directory](https://fman.io/docs/customizing-fman)`/Plugins`. You will need to have [BitBar](https://getbitbar.com/) installed and the [currentFiles.1h.rb](https://getbitbar.com/plugins/System/currentFiles.1h.rb) plugin installed and configured. You can also use the [Alfred BitBar Workflow](https://github.com/raguay/MyAlfred/blob/master/Alfred%203/BitBarWorkflow.alfredworkflow) to control the plugin.

Once you have the **BitBar** and plugin installed, get the full path to the plugin file and create a json file *OpenWithEditor.json* in the [data directory](https://fman.io/docs/customizing-fman)`/User` directory. Then add these line:

```
{
    "scriptLoc": "<Path to currentFiles.1h.rb>"
}
```

After restarting **fman**, you will be able to select the editor you are currently using to edit file.

### Usage

Pressing **F4** or **shift+e** with files selected or simply highlighted will open the file in the editor that you specify in the plugin. Changing the current editor in the **BitBar** plugin will change which editor is used instantly.

### Features

 - Opens selected files in the editor specified by the **BitBar** plugin.