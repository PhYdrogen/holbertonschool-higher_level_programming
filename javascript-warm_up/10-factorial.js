#!/usr/bin/node
function factorial (n) {
    if (n === 1) {
        return 1;
    }
    return (n * factorial(n-1));
}

const argv = process.argv;
let userNum = Number(argv[2]);
if (isNaN(userNum)) {
    userNum = 1;
}
console.log(factorial(userNum));