import pathlib
from PIL import ImageGrab


def save_screenshot():
    screenshot = ImageGrab.grab(all_screens=False)
    # screenshot.save(str(pathlib.WindowsPath.cwd()).replace("\\test\\", "") + "\\src\\logs\\screenshots", format='PNG')
    screenshot.save("C:\\Users\\User\\PycharmProjects\\desktop-automation\\src\\logs\\screenshots\\screenshot.png", format='PNG')
    # screenshot.save("screenshot.png", format='PNG')
    return f"Скриншот сохранен в: {str(pathlib.WindowsPath.cwd())} + \\src\\logs\\screenshots\\screenshot.png"
