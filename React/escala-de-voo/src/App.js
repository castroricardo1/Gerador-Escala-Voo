import React, { useState, useEffect } from 'react';
const data = require('./data.json');

function EscalaDeVoo() {
  const [origem, setOrigem] = useState('');
  const [numPernas, setNumPernas] = useState(0);
  const [escala, setEscala] = useState([]);

  function handleOrigemChange(event) {
    setOrigem(event.target.value.toUpperCase());
  }

  function handleNumPernasChange(event) {
    setNumPernas(parseInt(event.target.value));
  }

  function handleFormSubmit(event) {
    event.preventDefault();
    let escalaAtual = [];
    let origemAtual = origem;
    let destino = null;
    for (let i = 0; i < numPernas; i++) {
      const destinos = [];
      data.forEach(voo => {
        if (voo.origem === origemAtual) {
          destinos.push({ numVoo: voo.numero, destinoVoo: voo.destino });
        }
      });
      if (destinos.length === 0) {
        console.log('Não há destinos disponíveis para essa origem.');
        break;
      }
      const indiceSorteado = Math.floor(Math.random() * destinos.length);
      destino = destinos[indiceSorteado];
      escalaAtual.push({ origem: origemAtual, destino: destino.destinoVoo, numVoo: destino.numVoo });
      origemAtual = destino.destinoVoo;
    }
    setEscala(escalaAtual);
  }

  useEffect(() => {
    setOrigem('');
    setNumPernas(0);
    setEscala([]);
  }, []);

  return (
    <form onSubmit={handleFormSubmit}>
      <div>
        <label>Qual é a origem do seu primeiro voo?</label>
        <input type="text" value={origem} onChange={handleOrigemChange} />
      </div>
      <div>
        <label>Quantas pernas de trabalho você quer fazer?</label>
        <input type="number" value={numPernas} onChange={handleNumPernasChange} />
      </div>
      <button type="submit">Gerar Escala</button>
      <div>
        <h2>Escala de Voo:</h2>
        <ul>
          {escala.map((perna, index) => (
            <li key={index}>Na perna {index + 1}, você vai do voo {perna.origem} para {perna.destino} (voo {perna.numVoo})</li>
          ))}
        </ul>
      </div>
    </form>
  );
}

export default EscalaDeVoo;
