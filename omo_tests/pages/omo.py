from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0',
    'deviceName': '8dc5d226',
    'appPackage': 'com.omo.systems.stage',
    'appActivity': 'com.omo.systems.MainActivity',
    'language': 'ru',
    'locale': 'UA'
}
wrong_password_dict = {
    'en': 'Wrong password',
    'ua': 'Невірний пароль',
    'ru': 'Неправильный пароль'
}
wrong_password_text = wrong_password_dict.get(desired_caps.get('language'))

empty_phone_text_dict = {
    'en': 'Phone number',
    'ua': 'Номер телефону',
    'ru': 'Номер телефона'
}
empty_phone_text = empty_phone_text_dict.get(desired_caps.get('language'))


class OmoPage:
    def __init__(self):
        self.driver = self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_caps)

    def open(self):
        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        return self

    def logon(self, phone, password):
        self.driver.find_element_by_accessibility_id('loginPhoneInput').click()
        self.driver.find_element_by_accessibility_id(
            'loginPhoneInput').send_keys(phone)
        self.driver.find_element_by_accessibility_id(
            'loginPasswordInput').click()
        self.driver.find_element_by_accessibility_id(
            'loginPasswordInput').send_keys(password)
        self.driver.back()
        self.driver.find_element_by_accessibility_id('enterAppButton').click()
        return self

    def check_save_pass_form_text(self):
        status: bool = False
        if self.driver.find_element_by_id('android:id/alertTitle'). \
                get_attribute('text') == 'Save password':
            status = True
        return status

    def check_wrong_pass_form_text(self):
        status: bool = False
        if self.driver.find_element_by_id('android:id/message'). \
                get_attribute('text') == wrong_password_text:
            status = True
        return status

    def copy_paste_phone_from_clipboard(self, phone: str):
        self.driver.find_element_by_accessibility_id('loginPhoneInput').click()
        self.driver.set_clipboard_text(phone)
        self.driver.find_element_by_accessibility_id(
            'loginPhoneInput').set_text(self.driver.get_clipboard_text())

    def type_phone(self, phone: str):
        self.driver.find_element_by_accessibility_id('loginPhoneInput').click()
        self.driver.find_element_by_accessibility_id(
            'loginPhoneInput').send_keys(phone)
        return self

    def clear_phone(self):
        self.driver.find_element_by_xpath(
            '//android.view.ViewGroup[@content-desc="loginPhoneInputClear"]'
            '/android.view.ViewGroup').click()

    def phone_should_be(self, phone: str):
        status: bool = False
        if self.driver.find_element_by_accessibility_id(
                'loginPhoneInput').get_attribute('text') == phone:
            status = True
        return status

    def phone_should_be_empty(self):
        return self.phone_should_be(empty_phone_text)

    def set_ua_country(self):
        dropdown = (
            '/hierarchy/android.widget.FrameLayout/android.widget.'
            'LinearLayout/android.widget.FrameLayout/android.widget.'
            'LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/android.widget.'
            'FrameLayout/android.view.ViewGroup/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/android.view.'
            'ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.'
            'view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/'
            'android.widget.ScrollView/android.view.ViewGroup/android.view.'
            'ViewGroup[1]/android.view.ViewGroup')
        country_list_ua = (
            '/hierarchy/android.widget.FrameLayout/android.widget.'
            'LinearLayout/android.widget.FrameLayout/android.widget.'
            'FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.'
            'LinearLayoutCompat/android.widget.FrameLayout/android.widget.'
            'ListView/android.widget.CheckedTextView[1]')
        self.driver.find_element_by_xpath(dropdown).click()
        self.driver.find_element_by_xpath(country_list_ua).click()

    def phone_prefix_should_be(self, phone_code):
        phone_prefix = (
            '/hierarchy/android.widget.FrameLayout/android.widget.'
            'LinearLayout/android.widget.FrameLayout/android.widget.'
            'LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/android.widget.'
            'FrameLayout/android.view.ViewGroup/android.view.ViewGroup/'
            'android.view.ViewGroup/android.view.ViewGroup/android.view.'
            'ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.'
            'view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/'
            'android.widget.ScrollView/android.view.ViewGroup/android.view.'
            'ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView')
        status: bool = False
        if self.driver.find_element_by_xpath(
                phone_prefix).get_attribute('text') == phone_code:
            status = True
        return status

    def signup(self):
        self.driver.find_element_by_accessibility_id(
            'loginRegistrationButton').click()

    def sign_up_button_is_displayed(self):
        self.driver.find_element_by_accessibility_id(
            'registerCreateAccountButton').is_displayed()
