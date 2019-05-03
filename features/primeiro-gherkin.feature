#language: pt

Funcionalidade:Enviar um email
    Cenario: Entrar no Gmail e enviar um email

        Dado que estou na tela principal do Gmail
        Quando coloco as credenciais
        Entao entra na conta do Gmail
        E carrega a tela do inbox do Gmail
        Quando que seleciono o botão COMPOSE
        Entao abre a aba de envio de email
        Quando que preencho os campos do para envio de email
        E seleciono botão enviar
        Entao envio o email

