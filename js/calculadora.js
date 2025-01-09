const number1 = document.querySelector("#n1");
const number2 = document.querySelector("#n2");
const select = document.querySelector("#operacao");
const resultado = document.querySelector("#result");


botao.addEventListener("click", (event) => {
    event.preventDefault();

 nsei()
});

function nsei(){
  const valor1 = parseInt(number1.value);
  const valor2 = parseInt(number2.value);
  const operacao = select.value;

  if(valor1 || valor2 == "NaN" || "null"){
    resultado.innerHTML = "Opção invalida!"
  }
  else if (operacao == "1" ){
    resultado.innerHTML = valor1 + valor2
 }  else if(operacao == "2"){
    resultado.innerHTML = valor1 - valor2
 } else if (operacao == "3"){
    resultado.innerHTML = valor1 * valor2
 } else if (operacao == "4"){
    resultado.innerHTML = valor1 / valor2
 }

}



