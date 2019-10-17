from appium import webdriver


class DriverManager(object):

    # define and start driver
    @classmethod
    def start_appium_in_local(cls):
        caps = {
            "deviceName": "Pixel 2 API 29",
            "platformName": "Android",
            "appiumVersion": "1.13.0",
            "deviceOrientation": "portrait",
            "deviceType": "phone",
            "newCommandTimeout": 600,
            "platformVersion": "10",
            "app": "/Users/mingli/autotestestexercise/mobile-test-scripts/gmail_android_app/resources/applications/android/gmail.apk",
            "autoGrantPermissions": True
        }

        cls._driver = webdriver.Remote(desired_capabilities=caps,
                                  command_executor='http://127.0.0.1:4723/wd/hub')
        return cls._driver



