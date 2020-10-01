$('#mensagemSenha').html('').hide();    
    

    function verificaSenha(){
        // Verifica se as senhas são iguais
        if($('#senha').val() != $('#confirmaSenha').val()){

            $('#mensagemSenha').html('Senhas não conferem!').show(); // Mostra mensagem de alerta se não forem
            $('#botaoSubmit').attr('disabled', true)
        }
        else{
            $('#mensagemSenha').html('').hide();
            $('#botaoSubmit').attr('disabled', false)
        }
    }

    $('#confirmaSenha').keyup(function(){

        verificaSenha()
    })