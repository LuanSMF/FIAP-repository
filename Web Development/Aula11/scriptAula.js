//JSON.stringify(): objeto JavaScript → string JSON.
//JSON.parse(): string JSON → objeto JavaScript.

//

//localStorage.setItem('boas vindas',' Olá, Dev!');
//localStorage.setItem('valido',true);

// let mensagem = localStorage.getItem('boas-vindas');
// console.log('Mensagem vinda do localStorage:' + mensagem);

// let tipo = localStorage.getItem('valido');
// console.log('o usuário é valido?' + tipo);


// sessionStorage.setItem('selecionados', [1, 2, 3]);

// let lista = sessionStorage.getItem('selecionados').split(',');
// console.log(selecionados);

// localStorage.removeItem('boas-vindas');
// localStorage.clear()

const produto1 = {
    id: 1, produto: 'Arroz'
};
localStorage.setItem('produto1', produto1);

const produto2 =
{
    id: 1, produto: 'Arroz'
};
const emJson = JSON.stringify(produto2)
localStorage.setItem('laEle', emJson);

const produto3 = JSON.parse(emJson);
console.log(produto3);

const produtos = [
    { id: 1, produto: 'Arroz', preco: 125 },
    { id: 2, produto: 'Macarrão', preco: 70 },
    { id: 3, produto: 'Pão', preco: 50 },
    { id: 4, produto: 'Pudim', preco: 100 },
];

const armazenarLocal = (chave, valor) => {
    localStorage.setItem(chave, valor)
};

for (const produto of produtos) {
    armazenarLocal(produto.id, JSON.stringify(produto));
}

armazenarLocal('listaProdutos', JSON.stringify(produtos));


class Produtos {

    constructor(obj) {
        this.nome = obj.produto.toUpperCase();
        this.preco = parseFloat(obj.preco);
    }
    somaICMS() {
        this.preco = this.preco * 1.21;
    }
}

const armazenados = JSON.parse(localStorage.getItem('listaProdutos'));
const produtosLista = [];

for (const objeto of armazenados) {
    produtosLista.push(new Produto(objeto));
}

for (const objeto of produtosLista) {
    objeto.somaICMS()
}

console.log(produtosLista);


