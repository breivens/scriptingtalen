function text2planguage(string) {
    let output = "";
    let vowel_group = "";
    for (let char of string) {
        if ("aeiou".indexOf(char.toLowerCase()) !== -1 || vowel_group + char === "ij") {
            vowel_group += char;
        } else {
            if (vowel_group) {
                output += vowel_group + "p" + vowel_group.toLowerCase();
                vowel_group = "";
            }
            output += char;
        }
    }
    if (vowel_group) {
        output += vowel_group + "p" + vowel_group.toLowerCase();
    }
    return output;
}

function planguage2text(string) {
    let output = "";
    let vowel_group = "";
    for (let i = 0; i < string.length; i += 1) {
        let char = string[i];
        if (char === "p" && vowel_group) {
            i += vowel_group.length;
            vowel_group = "";
        } else {
            output += char;
            if ("aeiou".indexOf(char.toLowerCase()) !== -1 || vowel_group + char === "ij") {
                vowel_group += char;
            } else {
                vowel_group = "";
            }
        }
    }
    return output;
}

function text2planguage2(string) {
    return string.replace(/([aeiou]+|ij)/ig, vowel_group => vowel_group + "p" + vowel_group.toLowerCase());
}

function planguage2text2(string) {
    return string.replace(/([aeiou]+|ij)p\1/ig, "$1");
}


console.log(text2planguage("koekoeksklok"));
console.log(planguage2text("koepoekoepoeksklopok"));

console.log(text2planguage2("koekoeksklok"));
console.log(planguage2text2("koepoekoepoeksklopok"));
