class Cell {
    constructor(x, y, w) {
        this.x = x;
        this.y = y;
        this.w = w;
    }

    draw() {
        fill(255);
        rect(this.x * this.w, this.y * this.w, this.w, this.w);
    }
}