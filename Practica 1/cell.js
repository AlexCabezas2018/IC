class Cell {
    constructor(x, y, w) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.element = NOTHING;

        // Parámetros para el A*
        this.restart();
    }

    restart() {
        this.f = 0;
        this.g = 0;
        this.h = 0;
        this.parent = undefined;
    }

    draw() {
        fill(this.element);
        rect(this.x * this.w, this.y * this.w, this.w, this.w);
    }
}