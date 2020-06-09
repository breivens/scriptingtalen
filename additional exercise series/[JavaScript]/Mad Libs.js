String.prototype.capitalize = function () {
    return this[0].toUpperCase() + this.slice(1).toLowerCase()
}

class MadLibs {
    constructor() {
        this.woordenschat = {};
    }

    leren(categorie, woorden) {
        categorie = categorie.toLowerCase();
        if (this.woordenschat[categorie] === undefined) this.woordenschat[categorie] = [];
        if (Array.isArray(woorden)) {
            for (let woord of woorden) this.woordenschat[categorie].push(woord.toLowerCase());
        } else {
            this.woordenschat[categorie].push(woorden.toLowerCase());
        }
    }

    suggereren(categorie) {
        if (this.woordenschat[categorie.toLowerCase()] === undefined) throw {
            name: "MadLibsError",
            message: "onbekende categorie"
        };
        const woorden = this.woordenschat[categorie.toLowerCase()]
        let woord = woorden[Math.floor(Math.random() * woorden.length)];
        return categorie === categorie.toUpperCase() ? woord.toUpperCase() :
            categorie === categorie.capitalize() ? woord.capitalize() :
                woord.toLowerCase();
    }

    invullen(zin) {
        const self = this;
        return zin.replace(/_(.*?)_/g, (match, categorie) => self.suggereren(categorie))
    }
}

const madlib = new MadLibs();
madlib.leren('naam', 'god');
madlib.leren('ding', 'war');
madlib.leren('inwoners', 'Americans');
madlib.leren('discipline', 'geography');
console.log(madlib.invullen('_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.'));