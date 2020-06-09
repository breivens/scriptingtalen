Array.prototype.equals = function (that) {
    return JSON.stringify(this) === JSON.stringify(that);
}

Array.prototype.isEmpty = function () {
    return this.length === 0;
}

class Gebied {
    constructor(array) {
        this.cellen = [...array].sort((x, y) => x[0] == y[0] ? x[1] - y[1] : x[0] - y[0]);
    }

    toString() {
        return `Gebied(${JSON.stringify(this.cellen).replace(/,/g, ", ")})`;
    }

    grootte() {
        return this.cellen.length;
    }

    bevat(c) {
        return this.cellen.some(value => value.equals(c));
    }

    doorsnede(h) {
        return new Gebied(this.cellen.filter(value => h.bevat(value)));
    }

    unie(h) {
        return new Gebied([...this.cellen, ...h.cellen.filter(value => !this.doorsnede(h).bevat(value))]);
    }

    isGelijkAan(h) {
        return this.cellen.length === h.cellen.length && this.isIngeslotenIn(h);
    }

    isIngeslotenIn(h) {
        return this.cellen.every(value => h.bevat(value));
    }

    overlaptMet(h) {
        return !this.doorsnede(h).cellen.isEmpty();
    }

    isVerspreid() {
        for (const cell of this.cellen) {
            for (const [dr, dk] of [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, -1]]) {
                const [r, k] = cell;
                if (this.bevat([r + dr, k + dk])) {
                    return false;
                }
            }
        }
        return true
    }

    isSamenhangend() {
        if (!this.cellen) return true;

        const [A, B] = [new Array(), [...this.cellen]];
        A.push(B.shift());

        while (!A.isEmpty() && !B.isEmpty()) {
            const [r, k] = A.shift();
            for (const [dr, dk] of [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, -1]]) {
                const cel = [r + dr, k + dk];
                const index = B.findIndex(value => value.equals(cel));
                if (index !== -1) {
                    if (A.every(value => !value.equals(cel))) A.push(cel);
                    B.splice(index, 1);
                }
            }
        }
        return B.isEmpty();
    }
}

class Rooster {
    constructor(s, reeks) {
        this.aantal = undefined;
        this.dimensie = s;
        this.gebieden = new Gebied([]);
        this.sterren = new Gebied(reeks);
        this.rooster = new Gebied([...Array(Math.pow(this.dimensie, 2))]
            .map((value, index) => [Math.floor(index / this.dimensie), index % this.dimensie]));

        if (reeks.length % s !== 0
            || !this.sterren.isIngeslotenIn(this.rooster)
            || !this.sterren.isVerspreid()) {
            throw {name: "AssertionError", message: "ongeldig rooster"};
        }
    }

    toString() {
        const string = this.rooster.cellen
            .map(value => ".").join("")
            .match(new RegExp(`.{${this.dimensie}}`, "g"))
            .map(value => value.split(""));
        for (const [r, k] of this.sterren.cellen) string[r][k] = "*";
        return string.map(value => value.join("")).join("\n");
    }

    aantalSterren(g) {
        return this.sterren.doorsnede(g).cellen.length;
    }

    voegGebiedToe(g) {
        if (!this.aantal) this.aantal = this.aantalSterren(g);
        if (!g.isIngeslotenIn(this.rooster)
            || !g.isSamenhangend()
            || this.aantal !== this.aantalSterren(g)
            || this.gebieden.overlaptMet(g)) {
            throw {name: "AssertionError", message: "ongeldig gebied"};
        }
        this.gebieden = this.gebieden.unie(g);
    }

    isBedekt() {
        return this.gebieden.isGelijkAan(this.rooster);
    }
}