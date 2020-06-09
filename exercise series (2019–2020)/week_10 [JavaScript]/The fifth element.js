class Rooster {
    constructor(reeks) {
        const lengte = reeks.length
        if (lengte !== Math.pow(Math.floor(Math.sqrt(lengte)), 2) ||
            lengte !== new Set(reeks).size ||
            reeks.some(i => !Number.isInteger(i))) {
            throw {name: "AssertionError", message: "ongeldige getallen"};
        }
        this.dimensie = Math.floor(Math.sqrt(lengte));
        this.rooster = [];
        for (const x in reeks) this.rooster.push(reeks.splice(0, this.dimensie))
        this.geselecteerd = new Set();
        this.geschrapt = new Set();
    }

    toString() {
        const n = Math.max.apply(null, this.rooster.flat()).toString().length;
        return this.rooster.map(rij => rij.map(
            getal => (this.isGeschrapt(...this.positie(getal)) ? '-' : getal.toString()).padStart(n, " ")
            ).join(" ")).join("\n")
    }

    getal(r, k) {
        if (r < 0 || r >= this.dimensie || k < 0 || k >= this.dimensie) {
            throw {name: "AssertionError", message: "ongeldige positie"};
        }
        return this.rooster[r][k]
    }

    positie(getal) {
        for (let [r, rij] of this.rooster.entries()) {
            if (rij.includes(getal)) return [r, rij.indexOf(getal)];
        }
        throw {name: "AssertionError", message: "getal niet gevonden"};
    }

    selecteer(getal) {
        const [r, k] = this.positie(getal);
        if (new Set([...this.geselecteerd, ...this.geschrapt]).has(JSON.stringify([r, k]))) {
            throw {name: "AssertionError", message: "ongeldige selectie"};
        }
        for (let i of Array(this.dimensie).keys()) {
            this.geschrapt.add(JSON.stringify([r, i]));
            this.geschrapt.add(JSON.stringify([i, k]));
        }
        this.geschrapt.delete(JSON.stringify([r, k]));
        this.geselecteerd.add(JSON.stringify([r, k]));
        return this;
    }

    isGeschrapt(r, k) {
        return this.geschrapt.has(JSON.stringify([r, k]));
    }
}