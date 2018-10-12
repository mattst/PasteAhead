
import sublime
import sublime_plugin

class PasteAheadCommand(sublime_plugin.TextCommand):
    """
    The PasteAheadCommand class is a Sublime Text plugin which inserts the
    contents of the clipboard ahead of the cursor's position as opposed to
    behind it. It mimics ST's behaviour concerning multiple selections; if
    the clipboard contains the appropriate number of lines to individually
    match the selections, then each of the cursor positions will have its
    corresponding clipboard line inserted ahead of it, otherwise the whole
    clipboard will be inserted ahead of all of the cursor positions.
    """

    def run(self, edit):

        view = self.view
        selections = view.sel()
        num_selections = len(selections)

        if num_selections < 1:
            return

        clipboard = sublime.get_clipboard()
        num_clipboard_lines = clipboard.count("\n") + 1

        # Handle multiple selections; insert the clipboard line
        # which corresponds to each of the multiple selections.

        if num_selections > 1 and num_selections == num_clipboard_lines:
            clipboard = clipboard.split("\n")
            for i, sel in enumerate(selections):
                view.replace(edit, sel, clipboard[i])
                selections.subtract(sel)
                selections.add(sel.begin())

        # Handle single selections and multiple selections with
        # out clipboard line pairs; insert the whole clipboard.

        else:
            for sel in selections:
                view.replace(edit, sel, clipboard)
                selections.subtract(sel)
                selections.add(sel.begin())
