from behave import *

import scenario
import time
import os


# timestr = time.strftime("%Y%m%d-%H%M%S")
# os.mkdir(os.getcwd() + '\\Screenshots\\' + timestr)
# screenshot_directory = 'Screenshots\\' + timestr + '\\'


@given(u'launch browser "{brwser}"')
def launch_browser(context, brwser):
    step = scenario.Scenario(context)
    step.open_browser(brwser)


@given(u'open vistasoft homepage')
def open_vistasoft_homepage(context):
    step = scenario.Scenario(context)
    step.got_to_url('https://vsmonitor.com/')


@step(u'input email "{mail}"')
def step_impl(context, mail):
    step = scenario.Scenario(context)
    step.wait_for_id_to_be_present('email')
    step.input_using_id('email', mail)  # dd_test_1@outlook.com  #testing email


@step(u'input password "{pwd}"')
def step_impl(context, pwd):
    step = scenario.Scenario(context)
    step.input_using_id('password', pwd)  # }krK,gdC6
    # step.take_screenshot(screenshot_directory, "Login Credentials Inputted")
    if step.css_is_present('#q-app > div > div > div.login-page-content.flex.justify-center > div > div > div > form > div > div:nth-child(1) > div > div > ul > li'):  # Missing Field Error
        # step.take_screenshot(screenshot_directory, step.get_text_from_xpath('//*[@id="q-app"]/div/div/div[2]/div/div/div/form/div/div[1]/div/div/ul/li'))
        raise Exception(step.get_text_from_xpath('//*[@id="q-app"]/div/div/div[2]/div/div/div/form/div/div[1]/div/div/ul/li'))
        step.close_browser()
    else:
        pass


@step(u'click login button')
def click_login_button(context):
    step = scenario.Scenario(context)
    step.click_using_id('login-button')


@step(u'verify successful login')
def verify_login(context):
    step = scenario.Scenario(context)
    if step.css_is_present('body > div.q-notifications > div.q-notifications__list.q-notifications__list--bottom.fixed.column.no-wrap.items-center > div > div > div > i'): #Error Pop Up
        message = step.get_text_from_xpath('/html/body/div[2]/div[6]/div/div/div/div')
        # step.take_screenshot(screenshot_directory, message)
        raise Exception(message)
        step.close_browser()
    else:
        step.wait_for_id_to_be_present('nav-user-button')
        # step.take_screenshot(screenshot_directory, 'Successfully Logged In')


@then(u'close browser')
def close_browser(context):
    step = scenario.Scenario(context)
    step.close_browser()
