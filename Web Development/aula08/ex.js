
function verificarMaior(){
    let n1= parseInt(prompt('Digite um número:'));
    let n2= parseInt(prompt('Digite um segundo número:'));
    let op= prompt('Escolha a operação: \n + \n - \n* \n/');
    let maior=0;
    if(isNaN(numero)){
        alert("Por favor, digite um número válido.")
        return;
    }else if(n1>n2){
            maior=n1;
            alert("O maior número é "+maior);
    }else{
            maior=n2;
            alert("O maior número é "+maior);
    }
    calcular();
}
function calcular(n1, n2, op){
   if(op == '+'){
     return n1+ n2;
   }else if(op == '-'){
    return n1 - n2;
   }else if(op == '*'){
    return n1 * n2;
   }else if(op == '/'){
    return n1/n2;
   }else{
    return 0;
   }
}
verificarMaior();
alert(calcular(n1, n2 , op));