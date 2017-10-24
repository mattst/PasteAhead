
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

        self.new_selections = []
        self.selections = self.view.sel()
        num_selections = len(self.selections)

        if num_selections < 1:
            return

        clipboard = sublime.get_clipboard()
        num_clipboard_lines = clipboard.count("\n") + 1

        # Handle multiple selections; insert the clipboard line
        # which corresponds to each of the multiple selections.

        if num_selections > 1 and num_selections == num_clipboard_lines:
            clipboard_lines = clipboard.split("\n")
            for i, sel in enumerate(self.selections):
                self.store_new_selection(sel)
                self.view.replace(edit, sel, clipboard_lines[i])

        # Handle single selections and multiple selections with
        # out clipboard line pairs; insert the whole clipboard.

        else:
            for sel in self.selections:
                self.store_new_selection(sel)
                self.view.replace(edit, sel, clipboard)

        self.replace_selections()


    def store_new_selection(self, sel):

        new_cursor = sublime.Region(sel.begin())
        self.new_selections.append(new_cursor)


    def replace_selections(self):

        self.selections.clear()

        # Do not use add_all() to add the new selections, since
        # it will fail on ST2, and it is no more efficient - it
        # just calls add() in a loop, as below (see sublime.py).

        for sel in self.new_selections:
            self.selections.add(sel)
