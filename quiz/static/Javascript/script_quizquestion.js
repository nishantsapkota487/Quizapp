$(document).ready(function(e){
  console.log('hello');
  checked = false
  $('#next').click(function(e){
    if (checked === false) {
      e.preventDefault()
      alert("First you need to answer the question before going to next one.")
    }
  })
  $('#answer').click(function(e){
    userAnswer = ''
    checked = true
    e.preventDefault();
    first_option = document.getElementById('choice1')
    second_option = document.getElementById('choice2')
    third_option = document.getElementById('choice3')
    console.log(first_option.value);
    if (first_option.checked === false && second_option.checked === false && third_option.checked === false) {
      alert("You need to select some option")
      checked = false
    }if (first_option.checked === true || second_option.checked === true || third_option.checked === true) {
      if (first_option.checked === true) {
        userAnswer = first_option.value
      }else if (second_option.checked === true) {
        userAnswer = second_option.value
      }else {
        userAnswer = third_option.value
      }$.ajax({
        type: 'POST',
        url: 'check/'+ userAnswer,
        data:{
          'user_answer':userAnswer
        },
        success: function(response){
          alert(response.message)
        }
      })
    }
  })
})
