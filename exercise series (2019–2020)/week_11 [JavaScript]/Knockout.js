function letterfrequenties(string) {
    return string.toUpperCase().replace(/[^A-Z]/g, "").split("")
        .reduce((word, letter) => {
            word[letter] ? word[letter] += 1 : word[letter] = 1;
            return word;
        }, {});
}


class Knockout {
    constructor() {
        this.landen = [];
        this.hoofdsteden = {};
    }

    land_toevoegen(land, hoofdstad) {
        this.landen.push(land);
        this.hoofdsteden[land] = hoofdstad;
    }

    hoofdstad(land) {
        if (!this.landen.includes(land)) throw {name: "AssertionError", message: "onbekend land"}
        return this.hoofdsteden[land];
    }

    reguliere_speeltijd(thuis, uit) {
        const [ts, us, t_freq, ts_freq, u_freq, us_freq] = this.info(thuis, uit);
        const [T, U] = this.intersectie(thuis, ts, uit, us);
        return [
            T.length > 0 ? T.map(letter => Math.min(t_freq[letter], us_freq[letter])).reduce((x, y) => x + y) : 0,
            U.length > 0 ? U.map(letter => Math.min(u_freq[letter], ts_freq[letter])).reduce((x, y) => x + y) : 0];
    }

    extra_speeltijd(thuis, uit) {
        const [ts, us, t_freq, ts_freq, u_freq, us_freq] = this.info(thuis, uit);
        const [T, U] = this.intersectie(thuis, ts, uit, us);
        return [
            T.length > 0 ? T.map(letter => t_freq[letter] * us_freq[letter]).reduce((x, y) => x + y) : 0,
            U.length > 0 ? U.map(letter => u_freq[letter] * ts_freq[letter]).reduce((x, y) => x + y) : 0];
    }

    wedstrijd(thuis, uit) {
        let [t, u] = this.reguliere_speeltijd(thuis, uit);
        if (t !== u) return t > u ? thuis : uit;
        [t, u] = this.extra_speeltijd(thuis, uit);
        if (t !== u) return t > u ? thuis : uit;
        return thuis.toUpperCase() < uit.toUpperCase() ? thuis : uit;
    }

    winnaar() {
        if (Math.log2(this.landen.length) % 1 !== 0) throw {
            name: "AssertionError",
            message: "ongeldig aantal landen"
        };
        let landen = [...this.landen]
        for (const _ of Array(Math.log2(landen.length))) {
            landen = [...Array(landen.length / 2).keys()].map(i => [landen[2 * i], landen[2 * i + 1]])
            for (const [i, [thuis, uit]] of landen.entries()) landen[i] = this.wedstrijd(thuis, uit);
        }
        return landen[0]
    }

    info(thuis, uit) {
        const [ts, us] = [this.hoofdstad(thuis).toUpperCase(), this.hoofdstad(uit).toUpperCase()]
        return [ts, us, letterfrequenties(thuis), letterfrequenties(ts), letterfrequenties(uit), letterfrequenties(us)]
    }

    intersectie(thuis, thuisstad, uit, uitstad) {
        return [
            [...new Set(thuis.toUpperCase().split(""))].filter(letter => letter.match(/[A-Z]/) && uitstad.includes(letter)),
            [...new Set(uit.toUpperCase().split(""))].filter(letter => letter.match(/[A-Z]/) && thuisstad.includes(letter))]
    }
}


const toernooi = new Knockout();
toernooi.land_toevoegen("Switzerland", "Bern");
toernooi.land_toevoegen("Estonia", "Tallinn");
toernooi.land_toevoegen("Belgium", "Brussels");
toernooi.land_toevoegen("Denmark", "Copenhagen");
toernooi.land_toevoegen("Portugal", "Lisbon");
toernooi.land_toevoegen("Austria", "Vienna");
toernooi.land_toevoegen("Netherlands", "Amsterdam");
toernooi.land_toevoegen("Lithuania", "Vilnius");
console.log(toernooi.hoofdstad("Switzerland"));
// "Bern"
console.log(toernooi.hoofdstad("Estonia"));
// "Tallinn"
console.log(toernooi.reguliere_speeltijd("Switzerland", "Estonia"));
// [5, 2]
console.log(toernooi.reguliere_speeltijd("Belgium", "Denmark"));
// [2, 2]
console.log(toernooi.reguliere_speeltijd("Portugal", "Austria"));
// [1, 2]
console.log(toernooi.reguliere_speeltijd("Netherlands", "Lithuania"));
// [3, 3]
console.log(toernooi.extra_speeltijd("Belgium", "Denmark"));
// [3, 2]
console.log(toernooi.extra_speeltijd("Netherlands", "Lithuania"));
// [4, 5]
console.log(toernooi.wedstrijd("Switzerland", "Estonia"));
// "Switzerland"
console.log(toernooi.wedstrijd("Belgium", "Denmark"));
// "Belgium"
console.log(toernooi.wedstrijd("Portugal", "Austria"));
// "Austria"
console.log(toernooi.wedstrijd("Netherlands", "Lithuania"));
// "Lithuania"
console.log(toernooi.winnaar());
// "Switzerland"