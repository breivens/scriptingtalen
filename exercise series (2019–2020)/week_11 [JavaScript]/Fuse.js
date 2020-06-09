Array.prototype.includesArray = function (array) {
    return this.map(JSON.stringify).includes(JSON.stringify(array));
}

Number.prototype.between = function (min, max) {  // excludes bounds
    return this > min && this < max;
}

class Rooster {
    constructor(sequence, rijen, kolommen = null) {
        this.rijen = rijen;
        this.kolommen = kolommen || rijen;
        this.rooster = sequence
            .match(new RegExp(".{" + this.kolommen + "}", "g"))
            .map(row => row.split("").map(Number));
    }

    toArray() {
        return this.rooster;
    }

    toString() {
        return this.rooster.map(row => row.join("")).join("\n");
    }

    groep(r, k) {
        const gegroepeerd = [[r, k]];
        while (true) {
            let subgegroepeerd = [];
            for (const [r, k] of gegroepeerd) subgegroepeerd.push(...this.naburig(r, k)
                .filter(array => ![...gegroepeerd, ...subgegroepeerd].includesArray(array)));
            if (subgegroepeerd.length === 0) break;
            gegroepeerd.push(...subgegroepeerd);
        }
        return gegroepeerd.sort();
    }

    naburig(r, k) {
        let buren = [];
        for (let [x, y] of [[-1, 0], [0, 1], [1, 0], [0, -1]]) {
            [x, y] = [r + x, k + y];
            if (x.between(-1, this.rijen) && y.between(-1, this.kolommen) &&
                this.rooster[r][k] === this.rooster[x][y]) buren.push([x, y]);
        }
        return buren;
    }

    is_opgelost() {
        return new Set(this.rooster.flat()).size === 1;
    }

    zet(r, k, i = true) {
        i = i ? 1 : -1;
        for (const [x, y] of this.groep(r, k)) this.rooster[x][y] += i;
        return this;
    }
}

const rooster = new Rooster("1221133113322222", 4);
console.log(rooster.zet(1, 1, false).zet(3, 2, false).toString());
console.log(rooster.is_opgelost());