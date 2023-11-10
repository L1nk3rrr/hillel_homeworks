import logging


# 2. Створити context manager який буде фарбувати колір виведеного тексту
class colorizer:
    RESET = '\033[0m'

    def __init__(self, color: str, colors_pallet: dict = None):
        self.color = color
        self.colors_pallet = colors_pallet
        if colors_pallet is None:
            self.colors_pallet = {
                'reset': '\033[0m',
                'red': '\033[91m',
                'green': '\033[92m',
                'yellow': '\033[93m',
                'blue': '\033[94m',
                'purple': '\033[95m',
                'cyan': '\033[96m',
                'white': '\033[97m',
            }

    def __enter__(self):
        self._set_color(self.color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._reset_color()

    def _set_color(self, color: str):
        if color in self.colors_pallet:
            print(self.colors_pallet[color], end='')
        elif color == 'reset':
            # that option can be override on colors pallet, but by default it's set to reset/normal font effect
            print(self.RESET, end='')
        else:
            logging.info(f"There is no color = {str(color)}")

    def _reset_color(self):
        self._set_color('reset')


with colorizer('red'):
    print('printed in red')
print('printed in default color')

specific_colors = {
    'red': '\033[38;2;255;100;66m'
}

with colorizer('red', specific_colors):
    print('printed in specific red')
print('printed in default color')