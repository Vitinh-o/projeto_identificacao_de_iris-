function colocarResposta(respostaServidor){

  resposta = document.getElementById("resultado")

  imagem = document.getElementById("imagemFlor")

  console.log(resposta)

  resposta.innerText = respostaServidor 

  if(respostaServidor == "Setosa")
    imagem.innerHTML = '<img src="./imagens/iris_setosa.png" height="400" alt="iris_setosa" srcset="">'

  else if(respostaServidor == "Virgínica")
    imagem.innerHTML = '<img src="./imagens/iris_virginica.png"  height="400" alt="flor virgínica">'

  else if(respostaServidor == "Versicolor")
    imagem.innerHTML = '<img src="./imagens/iris_vesicolor.jpg"  height="400" alt="iris versicolor" srcset="">'

  else{ resposta.innerText = "Algo deu errado, tente novamente"} 

}










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

      respostaServidor = data.resposta
      colocarResposta(respostaServidor)

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


