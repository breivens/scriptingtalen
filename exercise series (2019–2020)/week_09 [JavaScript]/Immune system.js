class Organisme {
    constructor(...antilichamen) {
        this.aspecifiek = {}
        this.adaptief = {}
        for (const antilichaam of antilichamen) this.aspecifiek[antilichaam] = 1;
    }

    isResistent(virus) {
        if (virus in this.aspecifiek) return true;
        if (!this.adaptief.hasOwnProperty(virus)) this.adaptief[virus] = 0;
        this.adaptief[virus] += 1;
        return this.adaptief[virus] >= 3;
    }

    mutatie(virus) {
        if (virus in this.aspecifiek) delete this.aspecifiek[virus];
        else if (virus in this.adaptief) delete this.adaptief[virus];
    }
}

class AltOrganisme {
    constructor(...sequentie) {
        this.aspecifiek = sequentie
        this.adaptief = []
    }

    isResistent(virus) {
        if (this.aspecifiek.includes(virus)) {
            return true;
        }
        this.adaptief.push(virus);
        return this.adaptief.filter(value => value === virus).length >= 3;
    }

    mutatie(virus) {
        this.aspecifiek = this.aspecifiek.filter(value => value !== virus);
        this.adaptief = this.adaptief.filter(value => value !== virus);
    }
}

let organisme = new Organisme(1, 2, 3, 4, 5);
console.log(organisme.aspecifiek);
console.log(organisme.isResistent(88));
console.log(organisme.isResistent(88));
console.log(organisme.isResistent(88));
console.log(organisme.adaptief);
console.log(organisme.mutatie(88));
console.log(organisme.adaptief);
