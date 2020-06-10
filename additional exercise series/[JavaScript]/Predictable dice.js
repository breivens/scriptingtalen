class Dobbelsteen {
    constructor() {
        this.dobbel = {"boven": 6, "onder": 1, "links": 2, "rechts": 5, "voor": 4, "achter": 3};
    }

    bovenkant() {
        return this.dobbel["boven"];
    }

    toJSON() {
        return JSON.stringify(this.dobbel);
    }

    draai(richting) {
        const [boven, onder, links, rechts, voor, achter] = Object.values(this.dobbel);
        switch (richting) {
            case "O":
                this.dobbel = {
                    "boven": links, "onder": rechts, "links": onder, "rechts": boven, "voor": voor, "achter": achter
                };
                break;
            case "W":
                this.dobbel = {
                    "boven": rechts, "onder": links, "links": boven, "rechts": onder, "voor": voor, "achter": achter
                };
                break;
            case "N":
                this.dobbel = {
                    "boven": voor, "onder": achter, "links": links, "rechts": rechts, "voor": onder, "achter": boven
                };
                break;
            case "Z":
                this.dobbel = {
                    "boven": achter, "onder": voor, "links": links, "rechts": rechts, "voor": boven, "achter": onder
                };
                break;
            default:
                throw "AssertionError: ongeldige richting";
        }
        return this.bovenkant();
    }

    reeks(eindwaarde) {
        const reeks = [];
        let bk = this.bovenkant();
        while (bk !== eindwaarde || reeks.length < 3) {
            bk = this.draai(bk % 2 ? "N" : "O");
            reeks.push(bk);
        }
        reeks.push(this.draai(bk % 2 ? "N" : "O"));
        return reeks;
    }
}

const dobbel = new Dobbelsteen();
console.log(dobbel.reeks(1));