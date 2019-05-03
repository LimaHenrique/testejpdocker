@given(u'que estou na tela principal do Gmail')
def step_impl(context):
    context.home_page.go_home()

@when(u'coloco as credenciais')
def step_impl(context):
    context.home_page.put_data()

@then(u'entra na conta do Gmail')
def step_impl(context):
    pass

@then(u'carrega a tela do inbox do Gmail')
def step_impl(context):
    pass

@when(u'que seleciono o botão COMPOSE')
def step_impl(context):
    context.home_page.open_compose()

@then(u'abre a aba de envio de email')
def step_impl(context):
    pass


@when(u'que preencho os campos do para envio de email')
def step_impl(context):
    context.home_page.bodyEmail()


@when(u'seleciono botão enviar')
def step_impl(context):
    context.home_page.sendEmail()


@then(u'envio o email')
def step_impl(context):
    pass
