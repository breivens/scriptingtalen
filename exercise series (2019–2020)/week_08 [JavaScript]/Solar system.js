function assert(condition, message) {
    if (!condition) throw {name: "AssertionError", message: message};
}

function letterwaarde(letters) {
    const lengte = letters.length;
    assert(letters.match(/^[a-z]+$/i) && lengte % 2 && lengte === new Set(letters).size, "ongeldige letterreeks");
    const m = Math.floor(lengte / 2);
    let afbeelding = {};
    for (let [index, letter] of letters.toUpperCase().split("").entries()) afbeelding[letter] = index - m;
    return afbeelding;
}

function woordwaarde(woord, letters) {
    const waarde = letterwaarde(letters);
    let som = 0;
    for (const letter of woord.toUpperCase()) {
        assert(waarde.hasOwnProperty(letter), "ontbrekende letters");
        som += waarde[letter];
    }
    return som;
}

function alignering(woorden, letters) {
    for (let i = 0; i < woorden.length; i += 1) if (woordwaarde(woorden[i], letters) !== i) return false;
    return true;
}

function rangschik1(woorden, letters) {
    function comparartor(x, y) {
        [x, y] = [x.toUpperCase(), y.toUpperCase()];
        if (x == y) return 0;
        const [wx, wy] = [woordwaarde(x, letters), woordwaarde(y, letters)];
        if (wx < wy || (wx === wy && x < y)) return -1;
        return 1;
    }

    woorden.sort(comparartor);
}

function rangschik2(woorden, letters) {
    woorden = [...woorden];
    rangschik1(woorden, letters);
    return woorden;
}