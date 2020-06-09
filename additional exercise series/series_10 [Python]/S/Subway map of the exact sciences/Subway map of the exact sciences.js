class Station {
    constructor(naam, jaar, omschrijving) {
        this.naam = naam;
        this.jaar = jaar;
        this.omschrijving = omschrijving;
        this.verbindingen = {};
    }

    toString() {
        return this.naam + " (" + this.jaar + ", " + this.omschrijving + ")";
    }

    verbind(metrolijn, metrostation) {
        if (!(metrolijn in this.verbindingen)) {
            this.verbindingen[metrolijn] = metrostation;
        } else {
            throw {
                name: "AssertionError",
                message: `station is reeds verbonden op lijn ${metrolijn}`
            }
        }
    }

    metrolijnen() {
        return Object.keys(this.verbindingen).sort();
    }

    volgende(lijn) {
        return this.verbindingen[lijn];
    }
}

class Metrokaart {
    constructor() {
        this.metrolijnen = {};
        this.metrostations = {};
    }

    beginstation(lijn) {
        if (!(lijn in this.metrolijnen)) {
            return undefined;
        }
        return this.metrolijnen[lijn][0];
    }

    eindstation(lijn) {
        if (!(lijn in this.metrolijnen)) {
            return undefined;
        }
        return this.metrolijnen[lijn][this.metrolijnen[lijn].length - 1];
    }

    uitbreiden(metrolijn, metrostation) {
        if (metrostation.toString() in this.metrostations) {
            metrostation = this.metrostations[metrostation.toString()];
        } else {
            this.metrostations[metrostation.toString()] = metrostation;
        }
        if (!(metrolijn in this.metrolijnen)) {
            this.metrolijnen[metrolijn.toString()] = [metrostation];
        } else {
            this.metrolijnen[metrolijn.toString()][this.metrolijnen[metrolijn].length - 1].verbind(metrolijn, metrostation);
            this.metrolijnen[metrolijn.toString()].push(metrostation);
        }
    }

    metrolijn(lijn) {
        if (!(lijn in this.metrolijnen)) {
            return [];
        }
        let output = [];
        for (let station of this.metrolijnen[lijn]) {
            output.push(station["naam"]);
        }
        return output;
    }
}