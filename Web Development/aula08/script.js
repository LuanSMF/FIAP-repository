function verificarPar(){
    let numero=parseInt(prompt('Digite um número:'));

    if(isNaN(numero)){
        alert("Por favor, digite um número válido.")
        return;
    }else if(numero%2){
            alert(numero+ "é par.");
    }else{
            alert(numero+ "é impar.");
    }
}

verificarPar();
verificarPar();
verificarPar();