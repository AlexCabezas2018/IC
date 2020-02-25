class AStar {
    static resolve(board, begin, end) {
        let openList = [begin];
        let closedList = [];

        while (openList.length > 0) {
            let lowestFXNode = AStar.lowestF(openList);
            if (AStar.equalNodes(lowestFXNode, end)) {
                return AStar.buildPath(lowestFXNode);
            }

            openList.splice(openList.indexOf(lowestFXNode), 1);
            closedList.push(lowestFXNode);

            let neighbours = AStar.getNeighbours(board, lowestFXNode);
            for (let i = 0; i < neighbours.length; i++) {
                let index = closedList.indexOf(neighbours[i]);
                if (index == -1 && neighbours[i].element != OBSTACLE) {
                    let gScore = lowestFXNode.g + 1;
                    let gScoreIsBest = false;

                    if (openList.indexOf(neighbours[i]) == -1) {
                        gScoreIsBest = true;
                        neighbours[i].h = AStar.heuristic(neighbours[i], end);
                        openList.push(neighbours[i]);
                    }
                    else if (gScore < neighbours[i].g) {
                        gScoreIsBest = true;
                    }

                    if (gScoreIsBest) {
                        neighbours[i].parent = lowestFXNode;
                        neighbours[i].g = gScore;
                        neighbours[i].f = neighbours[i].g + neighbours[i].f;
                    }
                }
            }
        }

        return [];
    }

    static heuristic(nodeA, nodeB) {
        let d1 = Math.abs(nodeB.x - nodeA.x);
        let d2 = Math.abs(nodeB.y - nodeA.y);

        return d1 + d2;
    }

    static buildPath(node) {
        let ret = [];
        while (node.parent) {
            ret.push(node);
            node = node.parent;
        }
        return ret.reverse();
    }

    static lowestF(list) {
        let lowestIndex = 0;
        for (let i = 0; i < list.length; i++) {
            if (list[i].f < list[lowestIndex].f) lowestIndex = i;
        }
        return list[lowestIndex];
    }

    static getNeighbours(board, node) {
        let ret = [];
        let x = node.x;
        let y = node.y;

        if (board[x - 1] && board[x - 1][y]) {
            ret.push(board[x - 1][y]);
            if (board[x - 1] && board[x - 1][y + 1]) ret.push(board[x - 1][y + 1]);
            if (board[x - 1] && board[x - 1][y - 1]) ret.push(board[x - 1][y - 1]);
        }
        if (board[x + 1] && board[x + 1][y]) {
            ret.push(board[x + 1][y]);
            if (board[x + 1] && board[x + 1][y + 1]) ret.push(board[x + 1][y + 1]);
            if (board[x + 1] && board[x + 1][y - 1]) ret.push(board[x + 1][y - 1]);
        }
        if (board[x][y - 1] && board[x][y - 1]) {
            ret.push(board[x][y - 1]);
        }
        if (board[x][y + 1] && board[x][y + 1]) {
            ret.push(board[x][y + 1]);
        }

        return ret;
    }

    static equalNodes(nodeA, nodeB) {
        return nodeA.x == nodeB.x && nodeA.y == nodeB.y;
    }

    static validate(board) {
        let errorsList = [];
        let begins = 0, ends = 0;

        board.forEach(column => {
            column.forEach(node => {
                if (node.element == BEGIN) begins++;
                else if (node.element == END) ends++;
            })
        });

        //Comprobacion 1 - Hay un inicio y final
        if (begins == 0) errorsList.push("No se han encontrado puntos de partida");
        if (ends == 0) errorsList.push("No se han encontrado puntos de meta");

        //Comprobacion 2 - Solo hay un inicio y final
        if (begins > 1) errorsList.push("Se ha encontrado más de un inicio");
        if (ends > 1) errorsList.push("Se ha encontrado más de un final");

        return errorsList;
    }

    static findElement(board, elementToFind) {
        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[0].length; j++) {
                if (board[i][j].element == elementToFind) {
                    return board[i][j];
                }
            }
        }

        return false;
    }
}