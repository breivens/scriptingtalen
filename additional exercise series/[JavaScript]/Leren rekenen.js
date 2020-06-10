function randomNumber(max) {
    return Math.floor(Math.random() * (max + 1))
}


function randomNumbers(n, min, max, different = false) {
    if (different && n > max - min + 1) throw `RangeError: interval [${min}, ${max}] bevat geen ${n} getallen`
    nums = [];
    for (let i = 0; i < n; i += 1) {
        r = randomNumber(max - min) + min;
        while (different && nums.includes(r)) r = randomNumber(max - min) + min;
        nums.push(r);
    }
    return nums;
}

function randomElement(array) {
    if (array.length === 0) throw "RangeError: array bevat geen elementen"
    return array[randomNumber(array.length - 1)];
}


function divisors(n) {
    return [...Array(n + 1).keys()].filter(div => n % div === 0)
}


function multiples(n, max) {
    const mults = [];
    for (let i = n; i <= max; i += n) mults.push(i);
    return mults;
}


function randomExpression(operator, result, max) {
    if (!"+-*/".includes(operator)) throw "RangeError: ongeldige operator";
    let [a, b] = randomNumbers(2, 0, max);
    while (eval(a + operator + b) !== result) [a, b] = randomNumbers(2, 0, max);
    return [a, b];
}