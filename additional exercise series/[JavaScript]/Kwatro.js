const VORMEN = ["cirkel", "driehoek", "kruis", "vierkant"]
const KLEUREN = ["blauw", "groen", "oranje", "rood"]
const GETALLEN = [1, 2, 3, 4]

class Kaart {
    constructor(vorm, kleur, getal) {
        if (!VORMEN.includes(vorm) || !KLEUREN.includes(kleur) || !GETALLEN.includes(getal)) {
            throw "AssertionError: ongeldige kaart";
        }
        this._vorm = vorm
        this._kleur = kleur
        this._getal = getal
    }

    get vorm() {
        return this._vorm
    }

    get kleur() {
        return this._kleur
    }

    get getal() {
        return this._getal
    }

    toString() {
        return (this.vorm[0] + this.kleur[0] + this.getal).toUpperCase();
    }
}

class Lijn {
    constructor(...kaarten) {
        if (!this.isGeldigeLijn(kaarten)) throw "AssertionError: ongeldige lijn";
        this.kaarten = kaarten;
    }

    toString() {
        return this.kaarten.join(" - ");
    }

    vkg(kaarten) {
        return [kaarten.map(kaart => kaart.vorm), kaarten.map(kaart => kaart.kleur), kaarten.map(kaart => kaart.getal)];
    }

    isGeldigeLijn(kaarten) {
        const length = kaarten.length;
        if (length < 2) return false;
        return (new Set(kaarten.map(value => value.toString())).size === length
            && this.vkg(kaarten).map(value => new Set(value).size).every(value => value === 1 || value === length));
    }

    aanleggen(kaart, vooraan = false) {
        const lijn = vooraan ? [kaart, ...this.kaarten] : [...this.kaarten, kaart];
        if (!this.isGeldigeLijn(lijn)) throw "AssertionError: ongeldige lijn";
        this.kaarten = lijn;
        return this;
    }

    kwatro() {
        if (this.kaarten.length !== 3) throw "AssertionError: lijn moet uit drie kaarten bestaan";
        let [v, k, g] = this.vkg(this.kaarten);
        v = (new Set(v).size === 1 ? v : VORMEN.filter(value => !v.includes(value)))[0];
        k = (new Set(k).size === 1 ? k : KLEUREN.filter(value => !k.includes(value)))[0];
        g = (new Set(g).size === 1 ? g : GETALLEN.filter(value => !g.includes(value)))[0];
        return new Kaart(v, k, g);
    }
}
