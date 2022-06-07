from behave import given, when, then

import scenario
import time
import logging


@when(u'click user profile')
def step_impl(context):
    step = scenario.Scenario(context)
    # time.sleep(3)
    step.click_using_id('nav-user-button')
    # time.sleep(3)



@when(u'select my user account')
def step_impl(context):
    step = scenario.Scenario(context)
    step.click_using_id('user-profile')
    # time.sleep(3)


@then(u'verify name "{nm}" and email "{mail}" is correct')
def step_impl(context, nm, mail):
    step = scenario.Scenario(context)
    username = step.get_attribute_from_id('username')
    email = step.get_attribute_from_id('email')

    if username == nm:
        if email == mail:
            pass
        else:
            raise Exception(fr"Email: {email} do not match")
    else:
        raise Exception(fr"Username: {username} do not match")







