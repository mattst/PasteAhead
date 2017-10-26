
## PasteAhead (Sublime Text Plugin)

### Description

*PasteAhead* is a Sublime Text plugin which inserts the contents of the clipboard ahead of the cursor's position as opposed to behind it. Put another way, the cursor remains where it is and the pasted text is inserted in front of it.

This is useful to avoid the annoyance of pasting text and then having to press the `Ctrl+Left` keys repeatedly to move the cursor back to the original insertion point, a tedious task familiar to programmers.

The plugin is, of course, fully compatible with multiple selections.

### Requirements

Sublime Text version 2 or 3.

### Installing

Use [Package Control](https://packagecontrol.io/):

- Open the command palette and select: `Package Control: Install Package`
- Wait for the package list to be updated and then select: `PasteAhead`

Users can download the [zip file](https://github.com/mattst/SublimePasteAhead/archive/master.zip) and install the plugin [manually](http://docs.sublimetext.info/en/latest/extensibility/packages.html) if they prefer.

### Key Bindings

Users must manually add a key binding, which calls the `paste_ahead` command, to their user keys file. The plugin provides no default key binding because of the impossibility of choosing keys that would suit all users.

    { "keys": ["???+???"], "command": "paste_ahead" },

#### Key Binding Suggestions

I use `ctrl+shift+v` which steals the keys from the `paste_and_indent` command, which I rarely use because the `auto_indent` setting works so well. In fact I've remapped the various paste commands like this:

    { "keys": ["ctrl+shift+v"], "command": "paste_ahead" },
    { "keys": ["ctrl+k", "ctrl+v"], "command": "paste_and_indent" },
    { "keys": ["ctrl+k", "ctrl+shift+v"], "command": "paste_from_history" },

Those who use `ctrl+insert` and `shift+insert` to copy and paste may want to consider `ctrl+shift+insert` which is not mapped to anything by default.

    { "keys": ["ctrl+shift+insert"], "command": "paste_ahead" },

OSX users might simply use the unmapped `ctrl+v` since cut, copy, and paste are mapped using the `super` key. While Linux and Windows users could use `super+v` which is similarly unmapped on those OSes.

    OSX:       { "keys": ["ctrl+v"], "command": "paste_ahead" },
    Linux/Win: { "keys": ["super+v"], "command": "paste_ahead" },

### License

This package is licensed under The MIT License (MIT).