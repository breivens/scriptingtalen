function stijgend(reeks) {
    return JSON.stringify(reeks) === JSON.stringify(reeks.sort((a, b) => a - b))
}

function frequentiereeks(reeks) {
    if (!stijgend(reeks)) {
        throw {name: "AssertionError", message: "gegeven array is niet stijgend"}
    }
    let frequentiereeks = []
    for (let i = 0; i <= reeks[reeks.length - 1]; i += 1) {
        frequentiereeks.push(reeks.map(value => value < i + 1 ? 1 : 0).reduce((x, y) => x + y))
    }
    return frequentiereeks;
}

function verhogen(reeks) {
    return reeks.map(((value, index) => value + index + 1))
}

function complementaireReeksen(reeks) {
    return [verhogen(reeks), verhogen(frequentiereeks(reeks))]
}

console.log(stijgend([4, 2, 3, 5, 7, 11, 13]));