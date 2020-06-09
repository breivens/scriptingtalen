class Vierkant {
    constructor(sleutelwoord = "") {
        this.sleutelwoord = sleutelwoord.toUpperCase();
        let plaintext = '';
        for (const letter of this.sleutelwoord + "ABCDEFGHIJKLMNOPQRSTUVWXYZ") {
            if (plaintext.concat("J").indexOf(letter) === -1) plaintext += letter;
        }
        this.rooster = plaintext.match(new RegExp(".{5}", "g")).map(rij => rij.split(""));
    }

    toString() {
        return this.rooster.map(rij => rij.join(" ")).join("\n");
    }

    letter(r, k) {
        if (r < -1 || r > 5 || k < -1 || k > 5) throw {name: "AssertionError", message: "ongeldige positie"};
        return this.rooster[r][k];
    }

    positie(letter) {
        letter = letter.toUpperCase().replace("J", "I");
        for (const [r, rij] of this.rooster.entries()) if (rij.includes(letter)) return [r, rij.indexOf(letter)];
        throw {name: "AssertionError", message: "ongeldige letter"};
    }
}

class VierVierkant {
    constructor(sleutelwoord1, sleutelwoord2) {
        this.vierkant0 = new Vierkant();
        this.vierkant1 = new Vierkant(sleutelwoord1);
        this.vierkant2 = new Vierkant(sleutelwoord2);
    }

    codeer(boodschap) {
        const bigrammen = boodschap.concat("Q")
            .replace(/[^a-z]/gi, "")
            .toUpperCase()
            .match(new RegExp(".{2}", "g"));
        boodschap = "";
        for (const [letter1, letter2] of bigrammen) {
            const [r1, k1] = this.vierkant0.positie(letter1);
            const [r2, k2] = this.vierkant0.positie(letter2);
            boodschap += this.vierkant1.letter(r1, k2) + this.vierkant2.letter(r2, k1);
        }
        return boodschap;
    }

    decodeer(boodschap) {
        const bigrammen = boodschap.toUpperCase().match(new RegExp(".{2}", "g"));
        boodschap = "";
        for (const [letter1, letter2] of bigrammen) {
            const [r1, k1] = this.vierkant1.positie(letter1);
            const [r2, k2] = this.vierkant2.positie(letter2);
            boodschap += this.vierkant0.letter(r1, k2) + this.vierkant0.letter(r2, k1);
        }
        return boodschap;
    }
}

const codec = new VierVierkant("VOORBEELD", "sleutelwoord");
console.log(codec.codeer("help me obi wan kenobi"));
// "FEMBMLHUDYRBFTKFBO"
console.log(codec.decodeer("FEMBMLHUDYRBFTKFBO"));
// "HELPMEOBIWANKENOBI"