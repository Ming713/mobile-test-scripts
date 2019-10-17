from gmail_android_app.common.driver_manager import DriverManager

# some initialized activities or methods can be organized here before entering each page object.

class BasicPage:

    def __init__(self):
        self.driver = DriverManager.start_appium_in_local()


    def quit(self):
        self.driver.quit()

