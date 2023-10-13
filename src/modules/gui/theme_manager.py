class ThemeManager:
    def __init__(self, themes, text):
        self.text = text
        self.themes = themes

    def set_theme(self, chosen_theme: str):
        """
        Set the color theme of the Text Editor.

        :param chosen_theme: A string specifying the theme name (e.g., 'light' or 'dark').
        """
        if chosen_theme in self.themes:
            current_theme = self.themes[chosen_theme]

            # [Fix-needed]
            # supposed to set dark theme for header and menus, but only menus are affected
            """
            self.root.configure(bg=current_theme["background"])

            self.menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            self.file_menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            self.edit_menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            """

            self.text.configure(bg=current_theme["text_background"], fg=current_theme["text_foreground"])
            self.text.configure(insertbackground=current_theme["text_foreground"])  # Set cursor color to text color

