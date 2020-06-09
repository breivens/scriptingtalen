class AssertionError extends Error {
    constructor(boodschap) {
        super(boodschap);
        this.name = "AssertionError";
    }
}

class Combinatieslot {
    constructor(combinatie, maxwaarde = 9) {
        if (combinatie.length === 0 || combinatie.some(value => value < 0 || value > maxwaarde))
            throw new AssertionError("ongeldige combinatie");
        this.combinatie = combinatie;
        this.maxwaarde = maxwaarde;
        this.schijven = new Array(this.combinatie.length).fill(0);
    }

    toString() {
        return this.schijven.join("-");
    }

    roteer(schijven, aantal) {
        if (!Array.isArray(schijven)) schijven = [schijven];
        if (schijven.some(value => value < 0 || value >= this.combinatie.length))
            throw new AssertionError("ongeldige schijf");
        for (let schijf of schijven) this.schijven[schijf] = (this.schijven[schijf] + aantal) % (this.maxwaarde + 1);
    }

    open() {
        return JSON.stringify(this.combinatie) === JSON.stringify(this.schijven);
    }
}

const slot = new Combinatieslot([1, 2, 3, 4, 5], 4);
