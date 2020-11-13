    $(".itens-principal").toggle();
    $(document).ready(function(){
        $("#principal").click(function(){
        $(".itens-principal").toggle();
        });
    });

    $(".itens-administrador").toggle();
    $(document).ready(function(){
        $("#administrador").click(function(){
        $(".itens-administrador").toggle();
        });
    });

    $(".itens-comandas").toggle();
    $(document).ready(function(){
        $("#comandas").click(function(){
        $(".itens-comandas").toggle();
        });
    });

    $tamanhoTela = $(window).width();

    if($tamanhoTela < 768){
        console.log("aqui")
        $(".sidebar-container").toggle();
        $(document).ready(function(){
            $(".menu-bars").click(function(){
            $(".sidebar-container").toggle();
            });
        });
    }

    