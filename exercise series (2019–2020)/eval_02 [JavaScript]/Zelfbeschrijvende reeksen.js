function cijferfrequentie(string) {
    const freq = Array(10).fill(0);
    for (const s of string.replace(/\s/g , "")) {
        freq[s] += 1;
    }
    return freq;
}

function beschrijving(array) {
    const beschrijving = [];
    for (let i = 0; i < 10; i += 1) {
        const freq = array[i];
        beschrijving.push("" + (freq === 0 ? "" : freq) + i);
    }
    return beschrijving.join(" ");
}

function iszelfbeschrijvend(...args) {
    const beschrijvingen = [];
    for (const arg of args) {
        beschrijvingen.push(arg);
        if (arg !== beschrijving(cijferfrequentie(beschrijvingen.join(" ")))) {
            return false;
        }
    }
    return true;
}