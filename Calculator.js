let num1 = Number(window.prompt("Enter first number: "))
let op = String(window.prompt("Enter the operator: "))
let num2 = Number(window.prompt("Enter second number: "))
let result

switch (op) {
    case  "+":
        result = num1 + num2
        break;

    case  "-":
        result = num1 - num2
        break;

    case  "*":
        result = num1 * num2
        break;

    case  "/":
        result = num1 / num2
        break;

    default:
        result = "Invaild Operator"
        break;
}

console.log(result);