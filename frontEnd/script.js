
function enviarFormulario() {
    // Coletar dados do formulário
    const formulario = document.getElementById('formIris');
    let formData = new FormData(formulario);
  
    console.log(formData)

    // Enviar dados para o backend usando fetch
    fetch('http://127.0.0.1:8000/endpoint', {
      method: 'POST',
      body: formData,
    })
    
    .then(response => response.json())
    .then(data => {
      console.log('Resposta do servidor:', data);
      // Faça algo com a resposta do servidor, se necessário
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