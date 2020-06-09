class Pearson {
    constructor(tabel, combineer = (h, v) => (h + v) % 256) {
        const permutaties = [...Array(256).keys()];
        this.tabel = tabel || permutaties;
        this.combineer = combineer;
        if (tabel && !permutaties.every(value => tabel.includes(value))) throw "AssertionError: ongeldige tabel";
    }

    hash(string) {
        let h = 0;
        for (const s of string) h = this.tabel[this.combineer(h, s.charCodeAt(0))];
        return h;
    }
}

class Blok {
    constructor(hf = new Pearson(), vorige = null, index = 0, datum = "Genesis Block", vorige_hash = 0) {
        Object.defineProperties(this, {
            "index": {
                get() {
                    return index
                },
                set() {
                    throw "AssertionError: can't set attribute"
                }
            }, "vorige_hash": {
                get() {
                    return vorige_hash
                },
                set() {
                    throw "AssertionError: can't set attribute"
                }
            }
        });
        this.hf = hf;
        this.vorige = vorige;
        this.datum = datum;
        this.hash = this.hf.hash(this.index + this.datum + this.vorige_hash);
    }

    toevoegen(datum) {
        return new Blok(this.hf, this, this.index + 1, datum, this.hash);
    }

    is_geldig() {
        if (this.hash === this.hf.hash(this.index + this.datum + this.vorige_hash)) {
            return this.vorige === null ? true : this.vorige.is_geldig();
        }
        return false;
    }
}

const genesis = new Blok();
console.log(genesis)
console.log(genesis.is_geldig())