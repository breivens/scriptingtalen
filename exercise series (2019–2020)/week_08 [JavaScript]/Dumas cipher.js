function codeersleutel(sleuteltekst) {
    sleuteltekst = sleuteltekst.replace(/\s+/g, "").toUpperCase();
    let sleutel = {};
    for (const [index, letter] of sleuteltekst.split("").entries()) {
        if (!sleutel.hasOwnProperty(letter)) sleutel[letter] = [];
        sleutel[letter].push(index + 1);
    }
    return sleutel;
}

function codeer(tekst, sleuteltekst) {
    const [encoded, indices, sleutel] = [[], {}, codeersleutel(sleuteltekst)];
    for (const letter in sleutel) indices[letter] = 0;
    for (const letter of tekst.toUpperCase()) {
        const sleutel_letter = sleutel[letter];
        encoded.push(sleutel_letter[indices[letter] % sleutel_letter.length]);
        indices[letter] += 1;
    }
    return encoded;
}

const sleuteltekst = 'Lost time is never found again.';
console.log(codeer('nondeterminativeness', sleuteltekst));
console.log(codeer('interdenominationalism', sleuteltekst));
console.log(codeer('gastroenteroanastomosis', sleuteltekst));