class Pipopipette {
    constructor(m, n = undefined) {
        this.m = m;
        this.n = n || m;
        this.Score = [0, 0];
        this.Player = "A";

        this.dots = [...Array(this.m)].map(_ => [...Array(this.n)].map(_ => '+'));
        this.squares = [...Array(this.m - 1)].map(_ => [...Array(this.n - 1)].map(_ => '?'))
        this.hLine = [...Array(this.m)].map(_ => [...Array(this.n - 1)].map(_ => '.'))
        this.vLine = [...Array(this.m - 1)].map(_ => [...Array(this.n)].map(_ => '.'))
    }

    toString() {
        return this.merge(
            [...Array(this.m).keys()].map(i => this.merge(this.dots[i], this.hLine[i])),
            [...Array(this.m - 1).keys()].map(i => this.merge(this.vLine[i], this.squares[i]))
        ).map(row => row.join("")).join("\n");
    }

    merge(a, b) {
        return a.map((row, r) => b[r] ? [row, b[r]] : [row]).flat();
    }

    score() {
        return this.Score;
    }

    player() {
        return this.Player;
    }

    swapPlayer() {
        this.Player = this.Player === 'A' ? 'B' : 'A'
    }

    claim(position) {
        if (!position.match(/^[HV][0-9]+,[0-9]$/)) throw {name: "AssertionError", message: "invalid position"};
        let [player, scored] = [this.player(), false];
        let [direction, [r, c]] = [position[0], position.slice(1).split(",").map(i => Number(i))];
        if (r < -1 && r > this.m && c < -1 && c > this.n) throw {name: "AssertionError", message: "invalid position"};

        if (direction === "H") {
            if (this.hLine[r][c] !== ".") throw {name: "AssertionError", message: "dots already connected"};
            this.hLine[r][c] = "-";
            scored = this.check(r, c, player, true)
        } else if (direction === "V") {
            if (this.vLine[r][c] !== ".") throw {name: "AssertionError", message: "dots already connected"};
            this.vLine[r][c] = "|";
            scored = this.check(r, c, player, false)
        }
        if (!scored) this.swapPlayer();
        return this;
    }

    check(r, c, player, horizontal = true) {
        let squares_formed = 0;
        for (let i of [-1, 1]) {
            if (horizontal && r + i > -1 && r + i < this.m) {
                if (this.hLine[r + i][c] === '-'
                    && this.vLine[r - (i === -1)][c] === '|'
                    && this.vLine[r - (i === -1)][c + 1] === '|'
                    && this.squares[r - (i === -1)][c] === "?") {
                    this.squares[r - (i === -1)][c] = player;
                    squares_formed += 1;
                }
            } else if (!horizontal && c + i > -1 && c + i < this.n) {
                if (this.vLine[r][c + i] === '|'
                    && this.hLine[r][c - (i === -1)] === '-'
                    && this.hLine[r + 1][c - (i === -1)] === '-'
                    && this.squares[r][c - (i === -1)] === "?") {
                    this.squares[r][c - (i === -1)] = player;
                    squares_formed += 1;
                }
            }
        }
        this.Score[0] += squares_formed * (player === 'A')
        this.Score[1] += squares_formed * (player === 'B')
        return squares_formed > 0
    }
}