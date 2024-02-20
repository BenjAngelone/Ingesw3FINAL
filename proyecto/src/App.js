import React, { useState, useEffect } from 'react';

const MiComponente = () => {
  const [valorInput, setValorInput] = useState('');
  const [palabraEnEspejo, setPalabraEnEspejo] = useState('');
  const [frecuencias, setFrecuencias] = useState([]);

  const handleInputChange = (event) => {
    setValorInput(event.target.value);
  };

  const enviarTextoAlBackend = () => {
    const urlBackend = 'http://localhost:5000/backend';

    fetch(urlBackend, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ texto: valorInput }),
    })
      .then(response => response.json())
      .then(data => {
        setPalabraEnEspejo(data.palabra_en_espejo);
        setFrecuencias(data.frecuencias);
      })
      .catch(error => {
        console.error('Error al enviar datos http://ingesw3-backend-1:5000/ al backend:', error);
      });
  };

  useEffect(() => {
    // Llamar a la API cuando se monta el componente
    enviarTextoAlBackend();
  }, []); // [] significa que se ejecutará solo una vez al montar el componente

  return (
    <div style={{ textAlign: 'center' }}>
      <input
        type="text"
        value={valorInput}
        onChange={handleInputChange}
        placeholder="Escribe algo..."
      />
      <button onClick={enviarTextoAlBackend}>Enviar al Backend</button>

      {palabraEnEspejo && (
        <p>Palabra en espejo: {palabraEnEspejo}</p>
      )}

      <table style={{ margin: '20px auto', borderCollapse: 'collapse', width: '50%' }}>
        <thead>
          <tr>
            <th>Palabra</th>
            <th>Frecuencia</th>
          </tr>
        </thead>
        <tbody>
          {frecuencias.map((item, index) => (
            <tr key={index}>
              <td>{item.palabra}</td>
              <td>{item.frecuencia}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MiComponente;
