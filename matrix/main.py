def main():

    # Setup matrix
    rows = int(input('Rows: '))
    columns = int(input('Columns: '))
    matrix = []

    data = int

    for i in range(rows):
        # Create new row (array[]) per each iteration [rows]
        matrix.append([])
        for j in range(columns):
            data = int(input(f'Fila {i+1}, Columna {j+1}: '))
            # Insert data per each column [columns]
            matrix[i].append(data)

    # Pass each row in [matrix] to [row]
    # [row] <= [1, 2, 3] from [matrix] <= [[1, 2, 3], [4, 5, 6]]
    for row in matrix:
        print('[', end='')
        # Per each element in [row]
        for element in row:
           print(f' {element} ', end='')
        print(']')


if __name__ == "__main__":
    main()
