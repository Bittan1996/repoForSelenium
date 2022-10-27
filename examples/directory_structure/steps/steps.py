from behave import given, when, then




@given(u'I navigate to login page')
def step_impl(context):
    context.browser.get('https://www.google.com/')



@when(u'I enter valid username and password')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@title='Search']").send_keys("ice cream")





@when(u'I click on Submit button')
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@title='Search']").submit()

@then(u'login is successful')
def step_impl(context):
    assert context.browser.find_element_by_xpath("//span[.='Ice Cream']").is_displayed()==True

