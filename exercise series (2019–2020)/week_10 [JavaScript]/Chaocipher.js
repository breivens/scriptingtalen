class Disk {
    constructor(alphabet) {
        this.alphabet = alphabet.toUpperCase();
        if ([...this.alphabet].sort().join("") !== "ABCDEFGHIJKLMNOPQRSTUVWXYZ") {
            throw {name: "AssertionError", message: "invalid alphabet"}
        }
    }

    toString() {
        return this.alphabet;
    }

    locate(letter) {
        return this.alphabet.indexOf(letter.toUpperCase()) + 1;
    }

    letter(index) {
        return this.alphabet[index - 1];
    }

    rotate(count) {
        count = ((count % 26) + 26) % 26;
        this.alphabet = this.alphabet.slice(count) + this.alphabet.slice(0, count);
        return this;
    }

    roll(start, stop) {
        this.alphabet = this.alphabet.slice(0, start - 1)
            + this.alphabet.slice(start, stop)
            + this.alphabet[start - 1]
            + this.alphabet.slice(stop);
        return this;
    }
}

class Chaocipher {
    constructor(leftAlphabet, rightAlphabet) {
        this.left = new Disk(leftAlphabet);
        this.right = new Disk(rightAlphabet);
    }

    toString() {
        return `            +            *`
            + `\n LEFT (ct): ${this.left.toString()}`
            + `\nRIGHT (pt): ${this.right.toString()}`
            + `\n            --------------------------`
            + `\n  Position: 12345678911111111112222222`
            + `\n                     01234567890123456`
    }

    encode(plaintext) {
        let encoded = "";
        for (const letter of plaintext) {
            const index = this.right.locate(letter);
            encoded += this.left.letter(index);
            this.permute(index);
        }
        return encoded;
    }

    decode(encoded) {
        let decoded = "";
        for (const letter of encoded) {
            const index = this.left.locate(letter);
            decoded += this.right.letter(index);
            this.permute(index);
        }
        return decoded;
    }

    permute(index) {
        this.left.rotate(index - 1).roll(2, 14);
        this.right.rotate(index).roll(3, 14)
    }
}