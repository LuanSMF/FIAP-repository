let nome;
let sobrenome;
let ano;
let idade = 0;


nomeDafuncao();
console.log("TESTE!");
function nomeDafuncao(nome="Luan",sobrenome="Sá Muniz",ano="2026"){
    console.log(`Olá tudo bom? Me chamo ${nome} ${sobrenome}`);
    idade= ano-2002;
    console.log(`Minha idade: ${idade}`);
}
