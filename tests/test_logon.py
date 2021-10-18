from time import sleep
from appium import webdriver

from omo_tests.pages import omo

phone = '921921921'
phone_with_zero = '0' + phone
password = 'Qwe123'
wrong_password = password.swapcase()
ua_phone_code = '+380'


def test_success_logon():
    omo.open()
    omo.logon(phone, password)
    assert omo.check_save_pass_form_text()


def test_wrong_password():
    omo.open()
    omo.logon(phone, wrong_password)
    assert omo.check_wrong_pass_form_text()


def test_cut_zero_from_clipboard():
    omo.open()
    omo.copy_paste_phone_from_clipboard(phone_with_zero)
    assert omo.phone_should_be(phone)


def test_cut_zero_when_type():
    omo.open()
    omo.type_phone(phone_with_zero)
    assert omo.phone_should_be(phone)


def test_clear_button():
    omo.open()

    omo.type_phone(phone)
    omo.clear_phone()

    assert omo.phone_should_be_empty()


def test_choose_country():
    omo.open()
    omo.set_ua_country()
    assert omo.phone_prefix_should_be(ua_phone_code)


def test_sign_up():
    omo.open()
    omo.signup()
    omo.sign_up_button_is_displayed()
