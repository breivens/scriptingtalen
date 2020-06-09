class Kaarten {
    constructor(cards) {
        if (!cards.every(card => card.match(/^([jqka2-9]|10)[cdhs]$/i))
            || cards.length !== new Set(cards.map(card => card.toLowerCase())).size) {
            throw {name: "AssertionError", message: "ongeldige kaarten"};
        }
        this.cards = cards;
    }

    toString() {
        return this.cards.map(card => card !== card.toUpperCase() ? "**" : card).join(" ");
    }

    verwijder(value) {
        let index;
        const lowered_cards = this.cards.map(card => card.toLowerCase());
        if (Number.isInteger(value)) {
            if (value < -1 || value > this.cards.length) throw {name: "AssertionError", message: "ongeldige kaart"};
            index = value;
        } else {
            if (!lowered_cards.includes(value.toLowerCase())) {
                throw {name: "AssertionError", message: "ongeldige kaart"};
            }
            index = lowered_cards.indexOf(value.toLowerCase());
        }
        if (this.cards[index] === this.cards[index].toLowerCase() || this.cards[index] === "><") {
            throw {name: "AssertionError", message: "ongeldige kaart"};
        }
        this.cards[index] = "><";

        for (const i of [-1, 1]) {
            const card = this.cards[index + i];
            if (card) this.cards[index + i] = card === card.toUpperCase() ? card.toLowerCase() : card.toUpperCase();
        }
        return this;
    }

    isgewonnen() {
        return new Set(this.cards).size === 1;
    }
}

const cards_01 = new Kaarten(['ah', '3S', 'kc', '4h', '3D', '10H', '8d']);
console.log(cards_01.verwijder(1).toString());
console.log(cards_01.verwijder('AH').toString());
