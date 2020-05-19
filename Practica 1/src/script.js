let board;
let rowSlider;
let columnSlider;
let canDraw;
let boardAlreadysolved;

let docElemsRow;
let docElemsCols;

// Constantes
const DEF_ROWS = 10;
const DEF_COLS = 10;
const DEF_SIZE = 40;

// El coste de penalización de pasar por esa celda
const DEF_PENALIZATION = 1;

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

    rowSlider.parent('options-section');
    columnSlider.parent('options-section');

    canDraw = true;
    boardAlreadysolved = false;

    updateDocElems();
}

function draw() {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            board[i][j].draw();
        }
    }

    if (mouseIsPressed && canDraw) drawOnBoard();

    updateDocElems()
}

function setupCanvas(cols = DEF_COLS, rows = DEF_ROWS) {
    let canvas = createCanvas(DEF_SIZE * cols, DEF_SIZE * rows);
    canvas.parent('canvas-board');
    background(0);
    board = setupBoard(rows, cols);
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

// Actualiza todo lo que tiene que ver con el contenido de la página (contenido de las spans, h2, etc)
function updateDocElems() {
    document.getElementById('rows').innerText = rowSlider.value();
    document.getElementById('columns').innerText = columnSlider.value();
}

function drawOnBoard() {
    let { i, j } = getCoordinatesFromMouseCoordinates();
    if (i == undefined || j == undefined) return;
    if (currentElement) {
        clearPath();
        board[i][j].element = currentElement;
        if (currentElement == PENALIZATION)
            board[i][j].penalization = DEF_PENALIZATION;
        else board[i][j].penalization = 0;
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
    if (canDraw)
        setupCanvas(columnSlider.value(), rowSlider.value());
}

function updateCurrentElement(element) {
    currentElement = element;
}

function runAStar() {
    clearPath();
    if (!canDraw) return;
    let errors = AStar.validate(board);
    if (errors.length > 0) {
        let errorMessage = "";
        errors.forEach((error, i) => errorMessage += `${i + 1}- ${error}\n`);
        alert("Se han encontrado los siguientes errores: \n" + errorMessage);
    }
    else {
        console.log("Validaciones hechas. Comenzamos A*Star");
        let { begin, end } = AStar.findBeginAndEnd(board);
        let path = AStar.resolve(board, begin, end);

        console.log("El camino encontrado es el siguiente:", path)
        if (path.length == 0) alert("No se ha llegado a una solución");
        else {
            canDraw = false;
            let i = 0;
            let timerId = setInterval(() => {
                let node = path[i];
                if (i < path.length - 1) {
                    board[node.x][node.y].element = PATH;
                }
                i++;
            }, 200);

            setTimeout(() => {
                canDraw = true;
                clearInterval(timerId);
                alert("El algoritmo ha terminado");
                restartboard();
            }, 200 * path.length - 1);
        }
    }
}

function clearPath() {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j].element == PATH)
                board[i][j].element = NOTHING;
        }
    }
}

function restartboard() {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            board[i][j].restart();
        }
    }
}
