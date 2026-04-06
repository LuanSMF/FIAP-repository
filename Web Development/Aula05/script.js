/*let num = 5;

if(num == 5){
    console.log("Variável é igual a 5!");
}
if(num == 6){
    console.log("A variável não tem esse valor");
}

let umaCor = prompt("Digite uma cor:");

if( umaCor == "vermelho"){
    alert('A cor é vermelho');
}else{
    alert('A cor não é vermelho');
}
let =veri=false;
do{
let NomeUsuario = prompt('Digite seu nome');

if((NomeUsuario == '') || (NomeUsuario == null)){
    alert('Nome não inserido');
}else{
    veri=true;
}

}while(veri==false);


let combustivel = prompt('Digite o tipo de combustível');
if(combustivel == 'gnv'){
    alert('O veiculo sem move á gás')
}else if(combustivel == 'disel'){
    alert('O veiculo sem move á disel')
}else if(combustivel == 'gasolina'){
    alert('O veiculo se move á gasolina')
}else if(combustivel == 'alcool'){
    aler('O veiculo se move á alcool')
}else{

}*/

let veri=false;
do{
let numero = parseInt(prompt('Digite um número:'));
if(numero>=1 && numero<=5){
    veri=true;
    if(numero==1){
        alert('UM');
    }else if(numero==2){
        alert('Dois');
    }else if(numero==3){
        alert('Três');
    }else if(numero==4){
        alert('Quatro');
    }else if(numero==5){
        alert('Cinco');
    }
}
}while(veri==false);
