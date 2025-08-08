# desktop-automation
This is a framework created using desktop-automation, a wrapper made by victorkipruto (github.com/victorkipruto/desktop-automation) to make a workaround for the Bad Capabilities error. I used this framework to demonstrate to my colleagues that appium and selenium aren't used just for web and mobile automation. But can also be used to automate desktop apps! The only last thing remaining is to learn to write your own webdriver for your apps. But that's a whole another story. Please see victorkipruto's solution, it's actually incredibly simple but requires some research.

## About this project
This is a project that I used for demonstrating how Windows can be automated. For that reason it may seem raw, some methods were implemented inside classes, such as teardowns instead of being set in capabilities and used as pytest fixtures. Besides that, some file paths are set here too, instead of using `os.cwd()` method, or something like it. So please bear with me here.

 ## Goal of this project
 The goal of this project was to show how some things that are common in automation with Selenium can be done easier, or otherwise in a different approach than using Page Object Model, which is mostly derived from Java and is inapplicable for Python, when in reality it can be simplified.
