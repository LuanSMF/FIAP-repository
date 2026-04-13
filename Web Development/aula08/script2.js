/*let n1= parseInt(prompt('Digite um número:'));
let n2= parseInt(prompt('Digite um número:'));

let resultado=0;

function somar(primeiro, segundo){
    resultado = primeiro + segundo;
}

function mostrar(mensagem){
    alert(`O resultado da soma é: ${mensagem}`);
}
somar(n1,n2);
mostrar(resultado);*/

let n1= parseInt(prompt('Digite um número:'));
let n2= parseInt(prompt('Digite um segundo número:'));
let op= prompt('Escola a operação: \n + \n - \n* \n/');

function calcular(primeiroNum, segundoNum, operacao){
   if(operacao == '+'){
     return primeiroNum+ segundoNum;
   }else if(operacao == '-'){
    return primeiroNum - segundoNum;
   }else if(operacao == '*'){
    return primeiroNum * segundoNum;
   }else if(operacao == '/'){
    return primeiroNum/segundoNum;
   }else{
    return 0;
   }
}
alert(calcular(n1, n2 , op));