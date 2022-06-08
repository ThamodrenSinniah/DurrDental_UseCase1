from behave import *

import scenario


@given(u'launch browser "{brwser}"')
def launch_browser(context, brwser):
    step = scenario.Scenario(context)
    step.open_browser(brwser)


@given(u'open vistasoft homepage')
def open_vistasoft_homepage(context):
    step = scenario.Scenario(context)
    step.got_to_url('https://vsmonitor.com/')


@step(u'input email "{mail}"')
def input_email(context, mail):
    step = scenario.Scenario(context)
    step.wait_for_id_to_be_present('email')
    step.input_using_id('email', mail)


@step(u'input password "{pwd}"')
def input_password(context, pwd):
    step = scenario.Scenario(context)
    step.input_using_id('password', pwd)
    # Missing Field Error
    if step.css_is_present('#q-app > div > div > div.login-page-content.flex.justify-center > div > div > div > form > div > div:nth-child(1) > div > div > ul > li'):
        raise Exception(step.get_text_from_xpath('//*[@id="q-app"]/div/div/div[2]/div/div/div/form/div/div[1]/div/div/ul/li'))
    else:
        pass


@step(u'click login button')
def click_login_button(context):
    step = scenario.Scenario(context)
    step.click_using_id('login-button')


@step(u'verify successful login')
def verify_login(context):
    step = scenario.Scenario(context)
    # Error Pop Up
    if step.css_is_present('body > div.q-notifications > div.q-notifications__list.q-notifications__list--bottom.fixed.column.no-wrap.items-center > div > div > div > i'):
        message = step.get_text_from_xpath('/html/body/div[2]/div[6]/div/div/div/div')
        raise Exception(message)
    else:
        step.wait_for_id_to_be_present('nav-user-button')


@then(u'close browser')
def close_browser(context):
    step = scenario.Scenario(context)
    step.close_browser()
