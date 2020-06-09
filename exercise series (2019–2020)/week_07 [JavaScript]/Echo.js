function echo(arg) {
    return arg;
}

const echo2 = arg => arg;

console.log(echo(5));
console.log(echo("ok"));

console.log(echo2(5));
console.log(echo2("ok"));