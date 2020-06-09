class FlowFree {
    constructor(rijen, kolommen, punten) {
        this.rijen = rijen;
        this.kolommen = kolommen;
        if (punten.length % 2
            || punten.length !== new Set(punten).size
            || punten.some(punt => !this.ispositie(punt))) {
            throw "AssertionError: ongeldige configuratie";
        }
        this.rooster = [...Array(this.rijen)].map(_ => [...Array(this.kolommen)].map(_ => "."));
        for (let [i, [r, c]] of punten.entries()) this.rooster[r][c] = String.fromCharCode(65 + i / 2 << 0);
    }

    toString() {
        return this.rooster.map(row => row.join("")).join("\n");
    }


    ispositie(array) {
        const [r, k] = array;
        return r > -1 && r < this.rijen && k > -1 && k < this.kolommen && array.length === 2;
    }

    pijpleiding(startpositie, rightingen) {
        const route = [startpositie];
        const [sr, sk] = startpositie;
        rightingen = rightingen.toUpperCase();

        if (!this.ispositie([sr, sk])
            || !this.rooster[sr][sk].match(/[A-Z]/)
            || !rightingen
            || rightingen.split("").some(char => !char.match(/[UDRL]/))) {
            throw "AssertionError: ongeldige pijpleiding";
        }
        for (const char of rightingen) {
            let [[r, k], [x, y]] = [route[route.length - 1],
                {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}[char]];
            r += x;
            k += y;
            if (!this.ispositie([r, k])
                || !this.rooster[r][k].match(new RegExp("[\.|" + this.rooster[sr][sk] + "]"))
                || route.map(p => JSON.stringify(p)).includes(JSON.stringify([r, k]))) {
                throw "AssertionError: ongeldige pijpleiding";
            }
            route.push([r, k]);
        }
        const [er, ek] = route[route.length - 1];
        if (this.rooster[sr][sk] !== this.rooster[er][ek]) throw "AssertionError: ongeldige pijpleiding";
        return route;
    }

    verbinden(startpositie, rightingen) {
        let [prev_char, pijpleiding] = [undefined, this.pijpleiding(startpositie, rightingen)];
        for (const [i, char] of rightingen.toUpperCase().split("").entries()) {
            if (prev_char) {
                const [r, k] = pijpleiding[i];
                if (char === prev_char) {
                    this.rooster[r][k] = {"U": "|", "D": "|", "R": "━", "L": "━"}[char];
                } else {
                    this.rooster[r][k] = {
                        "UR": "┏", "LD": "┏", "UL": "┓", "RD": "┓", "RU": "┛", "DL": "┛", "LU": "┗", "DR": "┗"
                    }[prev_char + char];
                }
            }
            prev_char = char;
        }
        return this;
    }

    isgevuld() {
        return this.rooster.flat().every(value => value !== ".");
    }
}

const spel = new FlowFree(5, 5, [[0, 1], [3, 0], [0, 2], [4, 0], [0, 3], [4, 3], [1, 3], [2, 2], [4, 2], [3, 3]]);
console.log(spel.toString());