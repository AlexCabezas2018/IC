let board;
let rowSlider;
let columnSlider;

// Constantes
const DEF_ROWS = 9;
const DEF_COLS = 10;
const DEF_SIZE = 40;

function setup() {
    let canvas = createCanvas(DEF_SIZE * DEF_COLS, DEF_SIZE * DEF_ROWS);
    canvas.parent('canvas-board');
    const x = (windowWidth - width) / 2;
    const y = (windowHeight - height) / 2;
    canvas.position(x, y);

    rowSlider = createSlider(3, 25, 10, 1);
    columnSlider = createSlider(3, 25, 10 ,1);

    rowSlider.position(20, 50);
    rowSlider.style('width', '80px');

    background(0);
    board = setupBoard();
}

function setupBoard() {
    let board = new Array(DEF_COLS);
    for(let i = 0; i < board.length; i++) {
        board[i] = new Array(DEF_ROWS);
    }

    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            board[i][j] = new Cell(i, j, DEF_SIZE);
        }
    }

    return board;
}


function draw() {
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            board[i][j].draw();
        }
    }

}