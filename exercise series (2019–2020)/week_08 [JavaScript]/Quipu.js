function assert(condition) {
    if (!condition) {
        throw {name: "AssertionError", message: "ongeldige knopen"};
    }
}

function quipu(integer) {
    const ascher = integer.toString().slice(0, -1).split("").map(digit => digit === "0" ? "X" : digit + "s");
    const last = integer % 10;
    return ascher.concat(last === 0 ? "EE" : last === 1 ? "E" : last + "L").join(" ");
}

function decimaal2quipu(sequence) {
    return sequence.map(quipu).join(" ");
}

function quipu2decimaal(sequence) {
    let group = "";
    let integers = [];
    for (const knot of sequence.split(" ")) {
        assert(knot.match(/^([1-9]s|[2-9]L|X|EE?)$/))
        if (knot.includes("E")) {
            group += knot === "EE" ? "0" : "1";
            integers.push(Number(group));
            group = "";
        } else {
            group += knot.replace("X", "0").replace(/\D/g, "");
            if (knot.includes("L")) {
                integers.push(Number(group));
                group = "";
            }
        }
    }
    assert(group === "")
    return integers
}

console.log(decimaal2quipu([327, 609, 2461]));
console.log(quipu2decimaal("3s 2s 7L 6s 9s EE 2s 4s 6s E"));