var userChoice = prompt("rock, paper, or scissors?");
var computerChoice;

if (Math.random < .34) {
    computerChoice = "rock";
}
else if (Math.random <= .67) {
    computerChoice = "paper";
}
else {
    computerChoice = "scissors";
};

var choose = function(user, computer){
    user = userChoice
    computer = computerChoice
    if (user === computer) {
        console.log("tied!");
    }
    if (user === "rock") {
        if (computer === "scissors") {
            console.log("rock crushes scissors");
        }
        else {
            console.log("paper covers rock");
        }
    }
    if (user === "paper") {
        if (computer === "rock") {
            console.log("paper covers rock");
        }
        else {
            console.log("scissors cuts paper");
        }
    }
    if (user === "scissors") {
        if (computer === "paper") {
            console.log("scissors cuts paper");
        }
        else {
            console.log("rock crushes scissors");
        }
    }
};
choose();