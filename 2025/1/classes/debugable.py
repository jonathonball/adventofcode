class Debugable:
    def __init__(self):
        self.debug_mode = False

    def debug(self, message):
        if self.debug_mode:
            print(f"{message}")
