let board;
let rowSlider;
let columnSlider;

let docElemsRow;
let docElemsCols;

// Constantes
const DEF_ROWS = 10;
const DEF_COLS = 10;
const DEF_SIZE = 40;

// Elementos (los representamos con colores)
const NOTHING = '#ffffff';
const BEGIN = '#00ff00';
const OBSTACLE = '#ff0000';
const PENALIZATION = '#ffb700';
const END = '#0000ff';
const PATH = '#cf91ff';

let currentElement;

function setup() {
    setupCanvas()

    rowSlider = createSlider(3, 25, DEF_ROWS, 1);
    columnSlider = createSlider(3, 25, DEF_COLS, 1);

    rowSlider.parent('options-section')
    columnSlider.parent('options-section')

    currentElement = PATH; // Para debug, por defecto no hay elemento seleccionado

    updateDocElems();
}

function draw() {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            board[i][j].draw();
        }
    }

    if (mouseIsPressed) drawOnBoard();

    updateDocElems()
}

function setupBoard(rows = DEF_ROWS, cols = DEF_COLS) {
    let board = new Array(cols);
    for (let i = 0; i < board.length; i++) {
        board[i] = new Array(rows);
    }

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            board[i][j] = new Cell(i, j, DEF_SIZE);
        }
    }

    return board;
}

function setupCanvas(cols = DEF_COLS, rows = DEF_ROWS) {
    let canvas = createCanvas(DEF_SIZE * cols, DEF_SIZE * rows);
    canvas.parent('canvas-board');
    background(0);
    board = setupBoard(rows, cols);
}

// Actualiza todo lo que tiene que ver con el contenido de la página (contenido de las spans, h2, etc)
function updateDocElems() {
    document.getElementById('rows').innerText = rowSlider.value();
    document.getElementById('columns').innerText = columnSlider.value();
}

function drawOnBoard() {
    let { i, j } = getCoordinatesFromMouseCoordinates();
    if (i == undefined || j == undefined) return;
    if (currentElement) {
        board[i][j].element = currentElement;
    }
}

function getCoordinatesFromMouseCoordinates() {
    if (isMouseInTheBoard()) {
        let i = Math.floor(mouseX / DEF_SIZE);
        let j = Math.floor(mouseY / DEF_SIZE);

        return { i, j }
    }
    else return { i: undefined, j: undefined };
}

function isMouseInTheBoard() {
    return mouseX > 0 && mouseX < DEF_SIZE * board.length && mouseY > 0 && mouseY < DEF_SIZE * board[0].length;
}

// Funciones llamadas desde el html
function changeSize() {
    setupCanvas(columnSlider.value(), rowSlider.value());
}

function updateCurrentElement(element) {
    currentElement = element;
}
