const data = require('./data.json');
const readline = require('readline-sync');

let origem = readline.question('Qual é a origem do seu primeiro voo? ');
const numPernas = parseInt(readline.question('Quantas pernas de trabalho você quer fazer? '));

let destino = null;
for (let i = 0; i < numPernas; i++) {
  const destinos = [];
  data.forEach(voo => {
    if (voo.origem === origem) {
      destinos.push({ numVoo: voo.numero, destinoVoo: voo.destino });
    }
  });
  if (destinos.length === 0) {
    console.log('Não há destinos disponíveis para essa origem.');
    break;
  }
  const indiceSorteado = Math.floor(Math.random() * destinos.length);
  destino = destinos[indiceSorteado];
  console.log(`Na perna ${i+1}, você vai do voo ${destino.numVoo} para ${destino.destinoVoo}.`);
  origem = destino.destinoVoo;
}
