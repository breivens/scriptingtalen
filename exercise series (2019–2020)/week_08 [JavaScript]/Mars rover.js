Object.prototype.equals = function (that) {
    return JSON.stringify(this) === JSON.stringify(that);
}

function draaien(a, b, c) {
    if (a.equals(b) || b.equals(c) || a.equals(c)) {
        throw {name: "AssertionError", message: "drie punten moeten verschillend zijn"};
    }
    const waarde = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    return waarde ? waarde / Math.abs(waarde) : 0;
}

function volgende(a, punten, wijzerzin) {
    const afstand = (a, b) => Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2);
    let b = punten[0].equals(a) ? punten[1] : punten[0]
    for (let c of punten) {
        if (!a.equals(c) && !b.equals(c)) {
            const d = draaien(a, b, c);
            if (d === (wijzerzin ? 1 : -1) || (d === 0 && afstand(a, b) < afstand(a, c))) b = c;
        }
    }
    return b;
}

function contour(punten, wijzerzin) {
    const start = punten.reduce((a, b) => a.x < b.x || (a.x === b.x && a.y < b.y) ? a : b);
    const contour = [start];
    let punt = volgende(start, punten, wijzerzin);
    while (!punt.equals(start)) {
        contour.push(punt);
        punt = volgende(punt, punten, wijzerzin);
    }
    return contour;
}

punten = [{"x": 3, "y": 3}, {"x": 0, "y": 4}, {"x": 4, "y": 4}, {"x": 1, "y": 0}, {"x": 6, "y": 2}, {"x": 2, "y": 4},
    {"x": 5, "y": 5}, {"x": 1, "y": 2}, {"x": 5, "y": 2}];
console.log(contour(punten, true));
console.log(contour(punten, false));