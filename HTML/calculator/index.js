let num1 = 8
let num2 = 2
document.getElementById("firstNum").textContent = num1
document.getElementById("secondNum").textContent = num2
function addFunc(){
    total = num1 + num2
    document.getElementById("answer").textContent = "Sum: " + total
}
function subFunc(){
    total = num1 - num2
    document.getElementById("answer").textContent = "Subtract: " + total
}
function mulFunc(){
    total = num1 * num2
    document.getElementById("answer").textContent = "Multiply: " + total
}
function divFunc(){
    total = num1 / num2
    document.getElementById("answer").textContent = "Divide: " + total
}
let sentence = ["hello","my","name","is","Wiseman"]
let greetingEl = document.getElementById("greeting-el")
for (let i = 0; i < sentence.length; i ++){
    greetingEl.textContent += sentence[i] + " "
}