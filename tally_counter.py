import rumps

class TallyCounterApp(rumps.App):
    def __init__(self):
        super(TallyCounterApp, self).__init__("0", quit_button=None)
        self.load_count()
        self.title = str(self.count)
        self.count_menu_item = rumps.MenuItem(str(self.count))
        self.menu = [
            rumps.MenuItem('Add'),
            rumps.MenuItem('Edit Count', callback=self.edit_count),
            rumps.MenuItem('Reset'),
            rumps.MenuItem('Quit')
        ]

    def save_count(self):
        with open('count.txt', 'w') as f:
            f.write(str(self.count))

    def load_count(self):
        try:
            with open('count.txt', 'r') as f:
                self.count = int(f.read().strip())
        except FileNotFoundError:
            self.count = 0

    @rumps.clicked('Add')
    def add(self, _):
        self.count += 1
        self.count_menu_item.title = str(self.count)
        self.title = str(self.count)
        self.save_count()

    @rumps.clicked('Reset')
    def reset(self, _):
        self.count = 0
        self.count_menu_item.title = str(self.count)
        self.title = str(self.count)
        self.save_count()

    def edit_count(self, _):
        response = rumps.Window(
            message='Enter new count:',
            default_text=str(self.count),
            dimensions=(100, 24)
        ).run()
        try:
            self.count = int(response.text)
            self.count_menu_item.title = str(self.count)
            self.title = str(self.count)
            self.save_count()
        except ValueError:
            pass

    @rumps.clicked('Quit')
    def on_quit(self, _):
        rumps.quit_application()

if __name__ == '__main__':
    TallyCounterApp().run()
