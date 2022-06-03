from behave import given, when, then
import scenario


@given(u'launch chrome')
def launch_chrome(context):
    step = scenario.Scenario(context)
    step.open_browser("Edge")


@given(u'open vistasoft homepage')
def open_vistasoft_homepage(context):
    step = scenario.Scenario(context)
    step.got_to_url('https://vsmonitor.com/')


@when(u'input email')
def input_email(context):
    step = scenario.Scenario(context)
    step.wait_for_id_to_be_present('email')
    step.input_using_id('email', 'dd_test_1@outlook.com')


@when(u'input password')
def input_password(context):
    step = scenario.Scenario(context)
    step.input_using_id('password', '}krK,gdC6')
    step.take_screenshot("Login Credentials Inputted")


@when(u'click login button')
def click_login_button(context):
    step = scenario.Scenario(context)
    step.click_using_id('login-button')


@then(u'verify successful login')
def verify_login(context):
    step = scenario.Scenario(context)
    step.wait_for_id_to_be_present('nav-user-button')
    step.take_screenshot("Successfully Logged In")


@then(u'close browser')
def close_browser(context):
    context.driver.close()
