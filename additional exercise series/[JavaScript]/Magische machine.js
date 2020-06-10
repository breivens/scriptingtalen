class Machine {
    constructor() {
        this.bellen = {};
        this.knoppen = {};
    }

    toString() {
        return Object.keys(this.bellen).map(bel => bel + ": " + this.bellen[bel]).join("\n");
    }

    nieuweBel(label, aantal) {
        if (this.bellen.hasOwnProperty(label)) throw "AssertionError: bel bestaat reeds";
        this.bellen[label] = aantal;
        return this;
    }

    nieuweKnop(label, bronnen, bestemmingen) {
        if (this.knoppen.hasOwnProperty(label)) throw "AssertionError: knop bestaat reeds";
        if (![...bronnen, ...bestemmingen].every(bel => this.bellen.hasOwnProperty(bel))) {
            throw "AssertionError: onbekende bel";
        }
        this.knoppen[label] = {"bronnen": bronnen, "bestemmingen": bestemmingen};
        return this;
    }

    druk([...knoppen]) {
        if (!knoppen.every(knop => this.knoppen.hasOwnProperty(knop))) throw "AssertionError: onbekende knop";
        for (let knop of knoppen) {
            knop = this.knoppen[knop];
            if (knop["bronnen"].every(bron => this.bellen[bron] > 0)) {
                knop["bronnen"].forEach(bron => this.bellen[bron] -= 1)
                knop["bestemmingen"].forEach(bestemming => this.bellen[bestemming] += 1)
            }
        }
        return this;
    }
}