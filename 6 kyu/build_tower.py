def tower_builder(n_floors):
    floors = []
    for floor, num in enumerate(range(1, n_floors ** 2 + 1, 2), 1):
        spaces = ' ' * (((n_floors * 2 - 1) - num) // 2)
        string = spaces + ('*' * num) + spaces
        floors.append(string)
        if floor == n_floors:
            break
    return floors


# print(tower_builder(6))
