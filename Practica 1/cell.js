class Cell {
    constructor(x, y, w) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.element = NOTHING;
    }

    draw() {
        fill(this.element);
        rect(this.x * this.w, this.y * this.w, this.w, this.w);
    }
}