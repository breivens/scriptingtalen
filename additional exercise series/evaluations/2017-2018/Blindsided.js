class Stapel {
    constructor(kaarten) {
        this.kaarten = [...kaarten];
    }

    toArray() {
        return this.kaarten;
    }

    toString() {
        return this.kaarten.map(kaart => kaart === kaart.toUpperCase() ? kaart : "**").join(" ")
    }

    beeldzijdeBoven() {
        return this.kaarten.filter(kaart => kaart === kaart.toUpperCase()).length
    }

    splitsen(n) {
        if (n === undefined) n = this.beeldzijdeBoven();
        return [new Stapel(this.kaarten.slice(0, n)), new Stapel(this.kaarten.slice(n))];
    }

    omdraaien(arg) {
        if (arg === undefined) arg = [...Array(this.kaarten.length).keys()];
        if (Number.isInteger(arg)) arg = [arg];
        if (Array.isArray(arg)) {
            for (const i of arg) {
                const kaart = this.kaarten[i];
                this.kaarten[i] = kaart === kaart.toUpperCase() ? kaart.toLowerCase() : kaart.toUpperCase();
            }
        }
        return this;
    }

    evenveelNaarBovenAls(stapel) {
        return this.beeldzijdeBoven() === stapel.beeldzijdeBoven();
    }
}