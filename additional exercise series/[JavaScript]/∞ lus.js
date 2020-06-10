class Tegel {
    constructor(n = 0) {
        if (n < 0 || n > 15) throw "AssertionError: ongeldige tegel";
        this.n = n;
        this.b = n.toString(2).padStart(4, "0");
        this.zetRichtingen();
    }

    toString() {
        return {
            0: " ", 1: "╹", 2: "╺", 3: "┗", 4: "╻", 5: "┃", 6: "┏", 7: "┣",
            8: "╸", 9: "┛", 10: "━", 11: "┻", 12: "┓", 13: "┫", 14: "┳", 15: "╋"
        }[this.n];
    }

    zetRichtingen() {
        this.boven = this.b[3] == 1;
        this.rechts = this.b[2] == 1;
        this.onder = this.b[1] == 1;
        this.links = this.b[0] == 1;
    }

    draai(wijzerzin = true) {
        if (wijzerzin) {
            this.b = this.b.slice(1) + this.b[0]
        } else {
            this.b = this.b[3] + this.b.slice(0, 3)
        }
        this.zetRichtingen(this.b);
        this.n = parseInt(this.b, 2);
        return this;
    }
}

class OneindigeLus {
    constructor(tegels, kolommen) {
        if (tegels.some(tegel => tegel < 0 || tegel > 15)) throw "AssertionError: ongeldig rooster";
        tegels = tegels.map(value => new Tegel(value));
        this.rooster = [];
        for (let i = 0; i < tegels.length; i += kolommen) this.rooster.push(tegels.slice(i, i + kolommen));
    }

    toString() {
        return this.rooster.map(rij => rij.join("")).join("\n");
    }

    draai(r, k, wijzerzin = true) {
        if (this.rooster[r][k] === undefined) throw "AssertionError: ongeldige positie";
        this.rooster[r][k] = this.rooster[r][k].draai(wijzerzin)
        return this;
    }

    opgelost() {
        for (const [r, rij] of this.rooster.entries()) {
            for (const [k, tegel] of rij.entries()) {
                // up but no down
                if (tegel.boven && (!this.rooster[r - 1] || !this.rooster[r - 1][k].onder)) return false;
                // right but no left
                if (tegel.rechts && (!this.rooster[r][k + 1] || !this.rooster[r][k + 1].links)) return false;
                // down but no up
                if (tegel.onder && (!this.rooster[r + 1] || !this.rooster[r + 1][k].boven)) return false;
                // left but no right
                if (tegel.links && (!this.rooster[r][k - 1] || !this.rooster[r][k - 1].rechts)) return false;
            }
        }
        return true;
    }
}