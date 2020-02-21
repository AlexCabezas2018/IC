class AStar {
    static resolve(board, begin, end) {
        let openList = [];
        let closedList = [];

        openList.push(begin);

        while(openList.length > 0 && false) {
            // Escogemos el nodo con menor f(x)



        }

        return [];
    }

    static validate(board) {
        let errorsList = [];
        let begins = 0, ends = 0;

        board.forEach(column => {
            column.forEach(node => {
                if(node.element == BEGIN) begins++;
                else if(node.element == END) ends++;
            })
        });

        //Comprobacion 1 - Hay un inicio y final
        if(begins == 0) errorsList.push("No se han encontrado puntos de partida");
        if(ends == 0) errorsList.push("No se han encontrado puntos de meta");

        //Comprobacion 2 - Solo hay un inicio y final
        if(begins > 1) errorsList.push("Se ha encontrado más de un inicio");
        if(ends > 1) errorsList.push("Se ha encontrado más de un final");

        return errorsList;
    }

}