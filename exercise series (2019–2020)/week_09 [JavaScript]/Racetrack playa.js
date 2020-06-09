class Blok {
    constructor(lengte, hoogte, breedte, positie = [0, 0]) {
        this.lengte = lengte;
        this.hoogte = hoogte;
        this.breedte = breedte;
        this.positie = positie;
    }

    oppervlakte() {
        return 2 * (this.lengte * this.breedte + this.lengte * this.hoogte + this.hoogte * this.breedte);
    }

    volume() {
        return this.lengte * this.breedte * this.hoogte;
    }

    diagonaal() {
        return Math.sqrt(this.lengte * this.lengte + this.breedte * this.breedte + this.hoogte * this.hoogte);
    }

    schuif(richting) {
        if (!["V", "A", "R", "L"].includes(richting)) throw {"AssertionError": "ongeldige richting"};
        this.positie[0] += this.breedte * (richting === "V" ? 1 : richting === "A" ? -1 : 0);
        this.positie[1] += this.lengte * (richting === "R" ? 1 : richting === "L" ? -1 : 0);
        return this;
    }

    kantel(richting) {
        if (!["V", "A", "R", "L"].includes(richting)) throw {"AssertionError": "ongeldige richting"}
        if ("VA".includes(richting)) {
            this.positie[0] += richting === "V" ? this.hoogte : -this.breedte;
            [this.hoogte, this.breedte] = [this.breedte, this.hoogte];
        } else if ("RL".includes(richting)) {
            this.positie[1] += richting === "R" ? this.lengte : -this.hoogte;
            [this.lengte, this.hoogte] = [this.hoogte, this.lengte];
        }
        return this;
    }

    zeil(string) {
        for (let [beweging, richting] of string.match(/.{2}/g)) {
            if (beweging === "S") this.schuif(richting);
            else if (beweging === "K") this.kantel(richting);
            else throw {"AssertionError": "ongeldige beweging"}
        }
        return this;
    }
}
