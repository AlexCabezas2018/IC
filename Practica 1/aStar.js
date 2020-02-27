class AStar {
    static resolve(board, begin, end) {
        let openList = [begin];
        let closedList = [];

        while (openList.length > 0) {
            let currentNode = AStar.lowestF(openList);

            if (AStar.equalNodes(currentNode, end)) {
                return AStar.buildPath(currentNode);
            }

            openList.splice(openList.indexOf(currentNode), 1);
            closedList.push(currentNode);

            AStar.getNeighbours(board, currentNode)
            .forEach(neighbour => {
                const isInOpenList = openList.indexOf(neighbour) != -1;
                const isInClosedList = closedList.indexOf(neighbour) != -1;

                if (!isInClosedList && neighbour.element != OBSTACLE) {
                    let gScore = currentNode.g + (AStar.isDiagonalNeighbour(neighbour, currentNode) ? Math.sqrt(2) : 1);
                    let gScoreIsBest = false;

                    if (!isInOpenList) {
                        gScoreIsBest = true;
                        neighbour.h = AStar.heuristic(neighbour, end);
                        openList.push(neighbour);
                    }
                    else {
                        let nodeAux = new Cell(neighbour.x, neighbour.y, neighbour.w);
                        nodeAux.g = currentNode.g + (AStar.isDiagonalNeighbour(neighbour, currentNode) ? Math.sqrt(2) : 1);
                        nodeAux.h = AStar.heuristic(neighbour, end);
                        nodeAux.f = nodeAux.g + nodeAux.h;
                        if(nodeAux.f < neighbour.f) {
                            neighbour = nodeAux;
                            neighbour.parent = currentNode;
                        }
                    }
                    
                    if (gScore < neighbour.g) {
                        gScoreIsBest = true;
                    }

                    if (gScoreIsBest) {
                        neighbour.parent = currentNode;
                        neighbour.g = gScore;
                        neighbour.f = neighbour.g + neighbour.f;
                    }
                }
            });
        }

        return [];
    }

    static isDiagonalNeighbour(nodeA, nodeB) {
        return nodeA.x != nodeB.x && nodeA.y != nodeB.y;
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
            if (board[x - 1][y + 1]) ret.push(board[x - 1][y + 1]);
            if (board[x - 1][y - 1]) ret.push(board[x - 1][y - 1]);
        }
        if (board[x + 1] && board[x + 1][y]) {
            ret.push(board[x + 1][y]);
            if (board[x + 1][y + 1]) ret.push(board[x + 1][y + 1]);
            if (board[x + 1][y - 1]) ret.push(board[x + 1][y - 1]);
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

    static findBeginAndEnd(board) {
        let ret = {}
        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[0].length; j++) {
                if (board[i][j].element == BEGIN) {
                    ret.begin = board[i][j];
                }
                else if(board[i][j].element == END) {
                    ret.end = board[i][j];
                }
            }
        }

        return ret;
    }
}