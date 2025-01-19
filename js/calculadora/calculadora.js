let number1 = document.querySelector("#n1");
let number2 = document.querySelector("#n2");
let select = document.querySelector("#operacao");
let resultado = document.querySelector("#result");


botao.addEventListener("click", (event) => {
    event.preventDefault();
 nsei()
});

function nsei(){
  const valor1 = parseInt(number1.value);
  const valor2 = parseInt(number2.value);
  const opcao = select.value;

  if(isNaN(valor1) || isNaN(valor2) ){
    console.log("Not a number")
  } else if (opcao == "1" ){
    resultado.innerHTML = valor1 + valor2
 }  else if(opcao == "2"){
    resultado.innerHTML = valor1 - valor2
 } else if (opcao == "3"){
    resultado.innerHTML = valor1 * valor2
 } else if (opcao == "4"){
    resultado.innerHTML = valor1 / valor2
 }
}



