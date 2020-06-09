class BifidError extends Error {
    constructor(message) {
        super(message);
        this.name = "BifidError";
    }
}

class Bifid {
    constructor(n, string) {
        if (n < 2 || n > 10) throw new BifidError("er moet gelden dat 1 <= n <= 10")
        if (n * n !== string.length) throw new BifidError("aantal symbolen komt niet overeen met grootte van het rooster");
        this.n = n;
        this.rooster = string.match(new RegExp('.{' + n + '}', 'g'));
    }

    symbool(r, k) {
        if (r < 0 || r > this.n || k < 0 || k > this.n) throw new BifidError("ongeldige positie in rooster")
        return this.rooster[r][k];
    }

    positie(symbool) {
        if (symbool.length !== 1) throw new BifidError("symbool moet uit 1 karakter bestaan");
        for (let [r, rij] of this.rooster.entries()) if (rij.includes(symbool)) return [r, rij.indexOf(symbool)];
        throw new BifidError(`onbekend symbool: ${symbool}`);
    }

    codeer(tekst) {
        let [rij, kolom] = ["", ""];
        for (const symbool of tekst) {
            const [r, k] = this.positie(symbool);
            rij += r;
            kolom += k;
        }
        return (rij + kolom).match(/.{2}/g).map(value => this.symbool(value[0], value[1])).join("");
    }

    decodeer(tekst) {
        const [midden, gedecodeerd] = [tekst.length, tekst.split("").map(value => this.positie(value).join("")).join("")];
        const [rij, kolom] = [gedecodeerd.slice(0, midden), gedecodeerd.slice(midden)];
        return rij.split("").map((value, index) => this.symbool(value, kolom[index])).join("");
    }
}

let bifid = new Bifid(9, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz .,;:?!"\'-()[]{}$=%');
console.log(bifid.codeer("This is a dead parrot!"))
console.log(bifid.decodeer("WgwygeexfozQ(%II5D$I}O"))