# desktop-automation
This is a framework created using desktop-automation, a wrapper made by victorkipruto (github.com/victorkipruto/desktop-automation) to make a workaround for the Bad Capabilities error. I used this framework to demonstrate to my colleagues that appium and selenium aren't used just for web and mobile automation. But can also be used to automate desktop apps! The only last thing remaining is to learn to write your own webdriver for your apps. But that's a whole another story. Please see victorkipruto's solution, it's actually incredibly simple but requires some research.

## About this project
This is a project that I used for demonstrating how Windows can be automated. For that reason it may seem raw, some methods were implemented inside classes, such as teardowns instead of being set in capabilities and used as pytest fixtures. Besides that, some file paths are set here too, instead of using `os.cwd()` method, or something like it. So please bear with me here.
