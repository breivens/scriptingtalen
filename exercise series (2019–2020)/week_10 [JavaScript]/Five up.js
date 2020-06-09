class Stapel {
    constructor(kaarten) {
        if (!Array.isArray(kaarten) ||
            kaarten.length !== new Set(kaarten).size ||
            !kaarten.every(kaart => kaart.match(/^((([2-9]|10)[cdhsCDHS])|([jqka][cdhs])|([JQKA][CDHS]))$/))) {
            throw {name: "AssertionError", message: "ongeldige kaarten"}
        }
        this.kaarten = [...kaarten]
    }

    toString() {
        return this.kaarten.map(kaart => (kaart === kaart.toUpperCase()) ? kaart : "**").join(" ")
    }

    selectie_omdraaien(posities) {
        this.kaarten = this.kaarten.map((value, index) => !posities || posities.includes(index + 1) ?
            value === value.toUpperCase() ? value.toLowerCase() : value.toUpperCase() : value);
        return this;
    }

    bovenste_omdraaien(aantal) {
        this.kaarten = [...this.kaarten.slice(0, aantal).reverse(), ...this.kaarten.slice(aantal)]
        return this.selectie_omdraaien([...Array(aantal).keys()].map(value => value + 1));
    }

    couperen(aantal) {
        this.kaarten = [...this.kaarten.slice(aantal), ...this.kaarten.slice(0, aantal)];
        return this;
    }
}