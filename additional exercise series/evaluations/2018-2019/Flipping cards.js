class Kaarten {
    constructor(cards) {
        const assert = require("assert");
        cards.forEach(card => assert(card.match(/^([jqka2-9]|10)[cdhs]$/i), "ongeldige kaarten"));
        assert(cards.length === new Set(cards.map(card => card.toLowerCase())).size, "ongeldige kaarten");
        this.cards = cards
    }

    toString() {
        return this.cards.map(card => card.replace(/([jqka2-9]|10)[cdhs]/, "**")).join(" ")
    }

    verwijder(value) {
        const assert = require("assert");
        let index;
        const lowered_cards = this.cards.map(card => card.toLowerCase());
        if (Number.isInteger(value)) {
            assert(value > -1 && value < this.cards.length, "ongeldige kaart");
            index = value;
        } else {
            assert(typeof value === 'string' && lowered_cards.includes(value.toLowerCase()), "ongeldige kaart");
            index = lowered_cards.indexOf(value.toLowerCase());
        }
        assert(this.cards[index] === this.cards[index].toUpperCase() && this.cards[index] !== "><", "ongeldige kaart");
        this.cards[index] = "><";
        if (index - 1 > -1) {
            this.cards[index - 1] = this.cards[index - 1] === this.cards[index - 1].toUpperCase() ?
                this.cards[index - 1].toLowerCase() : this.cards[index - 1] = this.cards[index - 1].toUpperCase();
        }
        if (index + 1 < this.cards.length) {
            this.cards[index + 1] = this.cards[index + 1] === this.cards[index + 1].toUpperCase() ?
                this.cards[index + 1].toLowerCase() : this.cards[index + 1] = this.cards[index + 1].toUpperCase();
        }
        return this;
    }

    isgewonnen() {
        return new Set(this.cards).size === 1;
    }
}
