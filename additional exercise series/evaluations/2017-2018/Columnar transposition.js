class Cijfer {
    constructor(string) {
        this.kolommen = [...new Set(string)];
        const sorted = [...this.kolommen].sort();
        this.kolommen = this.kolommen.map(kolom => sorted.indexOf(kolom));
        this.aantal_kolommen = this.kolommen.length;
    }

    codeer(plaintext) {
        // aanvullen met "?" indien nodig
        if (plaintext.length % this.aantal_kolommen !== 0) plaintext += '?'.repeat(this.aantal_kolommen);
        // string -> rooster (met n kolommen)
        plaintext = plaintext.match(new RegExp(".{" + this.aantal_kolommen + "}", "g")).map(rij => rij.split(""));
        // transponeer rooster
        plaintext = plaintext[0].map((kolom, i) => plaintext.map(rij => rij[i]).join(""));
        // map kolommen in juiste volgorde
        return plaintext.map((kolom, index) => plaintext[this.kolommen.indexOf(index)]).join("");
    }

    decodeer(encoded) {
        const aantal_rijen = encoded.length / this.aantal_kolommen
        // controleer
        if (!Number.isInteger(aantal_rijen)) throw {name: "AssertionError", message: "ongeldig bericht"};
        // string -> rooster (met n rijen)
        encoded = encoded.match(new RegExp(".{" + aantal_rijen + "}", "g")).map(row => row.split(""));
        // map rijen in juiste volgorde
        encoded = encoded.map((kolom, index) => encoded[this.kolommen[index]])
        // transponeer rooster
        return encoded[0].map((kolom, i) => encoded.map(rij => rij[i]).join("")).join("");
    }
}