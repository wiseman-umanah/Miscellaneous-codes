let firstCard = 0
let cards = [firstCard]
document.getElementById("cardsNum").textContent = "Cards: " + cards[0]
let playerName = prompt("Please enter your name")
let playerDetails = {
    name : playerName,
    chips : 500
}
moneyEL = document.getElementById("player-el").textContent  = playerDetails.name + ":  $" + playerDetails.chips
function changecard(){
    cards[0] = Math.ceil(Math.random()* 13)
    document.getElementById("cardsNum").textContent = "Cards: " + cards[0]
    sum = cards[0]
    document.getElementById("cardSum").textContent = "Sum: " + sum
}
function newHand(){
    playerName = prompt("Please enter your name")
    cards[0] = 0 
    sum = 0
    document.getElementById("player-el").textContent  = playerDetails.name + ":  $" + playerDetails.chips
    document.getElementById("cardSum").textContent = "Sum: " + sum
    document.getElementById("cardsNum").textContent = "Cards: " +  cards[0]
}
function addcard(){
    if (sum === 20){
       alert("You won this round!!!")
       playerDetails.chips += 50
       moneyEL = document.getElementById("player-el").textContent  = playerDetails.name + ":  $" + playerDetails.chips
    }
    else if (sum < 20){
    let newCard = Math.ceil(Math.random()* 11)
    document.getElementById("cardsNum").textContent += " " + newCard
    sum += newCard
    document.getElementById("cardSum").textContent = "Sum: " + sum
    }
    else{
        alert('You lost this round')
        playerDetails.chips -= 50
        moneyEL = document.getElementById("player-el").textContent  = playerDetails.name + ":  $" + playerDetails.chips
        cards[0] = 0 
        sum = 0
        document.getElementById("cardSum").textContent = "Sum: " + sum
        document.getElementById("cardsNum").textContent = "Cards: " +  cards[0]
    }
    if (money <= 0){
        alert("GAME OVER")
        newHand()
    }
}
