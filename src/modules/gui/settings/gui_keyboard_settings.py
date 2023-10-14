import tkinter as tk


class Keyboard:
    def __init__(self, text: tk.Text):
        self.text = text

    def tab_forward(self, _):
        """
        Inserts 4 spaces when the Tab key is pressed.

        Args:
            _ : An argument to capture the event (not used).

        Returns:
            str: 'break' to prevent the default tab behavior in the text widget.
        """
        self.text.insert(tk.INSERT, chars="    ")
        return 'break'

    def tab_backward(self, event):
        """
        Remove 4 spaces when the combination Shift + Tab is pressed.

        Args:
            event: An argument that captures the event.

        Returns:
            str: 'break' to prevent the default behavior.
        """
        current_position = self.text.index(tk.INSERT)

        # Check if the cursor is at the beginning of the line
        if current_position.endswith(".0"):
            return 'break'

        prev_char_index = self.text.index(f"{current_position} - 4 chars")

        # Check if the previous 4 characters are spaces, and if they are, remove them
        if self.text.get(prev_char_index, current_position) == "    ":
            self.text.delete(prev_char_index, current_position)
            self.text.mark_set(tk.INSERT, prev_char_index)

        return 'break'
