from src.modules.editor_app_main import TextEditor


class TextEditorMain(TextEditor):
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = TextEditorMain()
    app.run()
