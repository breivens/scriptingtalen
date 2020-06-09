function assert(condition, message) {
    if (!condition) throw {name: "AssertionError", message: message};
}

Number.prototype.between = function (min, max) {  // excludes bounds
    return this > min && this < max;
}

class Qlocktwo {
    constructor(woorden, kolommen) {
        if (kolommen) {
            this.rijen = Math.floor(woorden.length / kolommen);
            this.kolommen = kolommen;
        } else {
            this.rijen = Math.floor(Math.sqrt(woorden.length));
            this.kolommen = this.rijen;
        }
        assert(this.rijen * this.kolommen === woorden.length, "ongeldig rooster");
        this.rooster = woorden.toUpperCase().match(new RegExp(".{" + this.kolommen + "}", "g"));
    }

    toString() {
        return this.rooster.join("\n");
    }

    posities(woord, start) {
        const [rs, ks] = start || [0, 0];
        assert(rs.between(-1, this.rijen) && ks.between(-1, this.kolommen), "ongeldige positie");
        woord = woord.toUpperCase();
        const posities = [];
        for (let [r, rij] of this.rooster.entries()) {
            if (rs <= r) {
                let k = rij.indexOf(woord);
                while (k.between(-1, this.kolommen)) {
                    if (rs < r || ks <= k) posities.push([r, k]);
                    k = rij.indexOf(woord, k + 1);
                }
            }
        }
        return posities;
    }

    weergave(tijdstip, message = "ongeldig tijdstip") {
        tijdstip = tijdstip.split(":");
        assert(tijdstip.length === 2 && tijdstip.every(value => value.match(/^[0-9]{1,2}$/)), message)
        let [u, m] = tijdstip.map(Number);
        assert(u.between(-1, 24) && m.between(-1, 60) && m % 5 === 0, message);
        u = m <= 15 ? u : u + 1;
        return this.minuut(this.uur(u % 12), m / 5);
    }

    visueel(tijdstip) {
        const string = this.rooster.map(row => "-".repeat(this.kolommen).split(""));
        let start;
        for (const woord of this.weergave(tijdstip, "onmogelijke weergave").split(" ")) {
            const posities = this.posities(woord, start);
            assert(posities.length !== 0, "onmogelijke weergave")
            const [length, [sr, sk]] = [woord.length, posities[0]];
            start = sk + length + 1 < this.kolommen ? [sr, sk + length + 1] : [sr + 1, 0];
            string[sr].splice(sk, length, ...woord.split(""))
        }
        return string.map(row => row.join("")).join("\n");
    }

    uur(u) {
        return ["TWAALF", "EEN", "TWEE", "DRIE", "VIER", "VIJF", "ZES", "ZEVEN", "ACHT", "NEGEN", "TIEN", "ELF", "TWAALF"][u]
    }

    minuut(u, m) {
        return [
            `HET IS ${u} UUR`,
            `HET IS VIJF OVER ${u}`,
            `HET IS TIEN OVER ${u}`,
            `HET IS KWART OVER ${u}`,
            `HET IS TIEN VOOR HALF ${u}`,
            `HET IS VIJF VOOR HALF ${u}`,
            `HET IS HALF ${u}`,
            `HET IS VIJF OVER HALF ${u}`,
            `HET IS TIEN OVER HALF ${u}`,
            `HET IS KWART VOOR ${u}`,
            `HET IS TIEN VOOR ${u}`,
            `HET IS VIJF VOOR ${u}`,
        ][m]
    }
}