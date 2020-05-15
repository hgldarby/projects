

def distribution(file, split):
    new_file = strip(file)
    qty_idx = new_file[0].index('Handled.units')
    new_file[0].append('New qty')
    new_data = []

    for row in new_file[1:]:
        if not row[qty_idx]:
            raise Exception
        elif row[qty_idx] == '1':
            row.append(0)
            new_data.append(row)
        else:
            row.append(1)
            for i in range(int(row[qty_idx])):
                new_data.append(row.copy())

    print(new_data)


def strip(file):
    f = []
    for row in file:
        new_row = row.strip()
        f.append(new_row.split(','))
    return f


def test_initial():
    file = open('D:\dry_fastmover_data_for_func.csv')
    percentage_split = [50, 50]
    distribution(file, percentage_split)
