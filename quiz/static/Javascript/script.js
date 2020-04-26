window.onload=function(event){
  var name, nickname, number, button;
  button = document.getElementById('button')
  button.addEventListener('click', function(event){
    name = document.getElementById('first').value
    nickname = document.getElementById('second').value
    number = document.getElementById('number').value
    bool = false
    boolPrime = false
    if (name === '') {
      alert("You need to fill the name option")
      event.preventDefault()
    }else{
      boolPrime = true
    }
    if ((number === '') && boolPrime === true) {
      alert("you need to fill the number option")
      event.preventDefault()
    }else{
      bool = true
    }
    if ((number < 5 || number > 10) && bool === true && boolPrime === true) {
      alert("you need to fill the number between 5 and 10")
      event.preventDefault()
    }
  })
}
