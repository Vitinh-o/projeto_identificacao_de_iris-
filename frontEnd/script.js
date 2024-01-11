
function enviarFormulario() {
    // Coletar dados do formulário
    let form = {
                comprimento_sepala: document.getElementById("comprimentoSepala").value,
                largura_sepala: document.getElementById("larguraSepala").value,
                comprimento_petala: document.getElementById("comprimentoPetala").value,
                largura_petala: document.getElementById("larguraPetala").value
              }

    console.log(form)

    // Enviar dados para o backend usando fetch
    fetch('http://127.0.0.1:8000/endpoint', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json', // Defina o cabeçalho Content-Type para application/json
      },
      body: JSON.stringify(form), // Converte o objeto para JSON
  })
  .then(response => response.json())
  .then(data => {
      console.log('Resposta do servidor:', data);
  })
  .catch(error => {
      console.error('Erro ao enviar formulário:', error);
  });

}



  document.addEventListener('DOMContentLoaded', function() {
    const botao = document.getElementById('enviar');

    botao.addEventListener('click', function() {
    enviarFormulario()
    });
  });