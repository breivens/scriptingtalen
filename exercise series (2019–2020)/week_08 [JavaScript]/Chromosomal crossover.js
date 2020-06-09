function crossoverpunten(sequence1, sequence2) {
    return _crossoverpunten(sequence1, sequence2).length;
}

function _crossoverpunten(sequence1, sequence2) {
    return sequence1.filter(value => sequence2.includes(value));
}

function chromosomale_deelsom(sequence, crosses) {
    let sum = 0;
    let seq = [];
    for (let value of sequence) {
        if (crosses.includes(value)) {
            seq.push(sum);
            seq.push(value);
            sum = 0;
        } else {
            sum += value;
        }
    }
    seq.push(sum);
    return seq;
}

function maximaleSom(sequence1, sequence2) {
    const crosses = _crossoverpunten(sequence1, sequence2);
    const [d1, d2] = [chromosomale_deelsom(sequence1, crosses), chromosomale_deelsom(sequence2, crosses)];
    return d1.map((value, index) => Math.max(value, d2[index])).reduce((x, y) => x + y, 0);
}

chromosome1 = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62];
chromosome2 = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100];
console.log(_crossoverpunten(chromosome1, chromosome2))
console.log(chromosomale_deelsom(chromosome1, _crossoverpunten(chromosome1, chromosome2)));
console.log(crossoverpunten(chromosome1, chromosome2));
console.log(maximaleSom(chromosome1, chromosome2));