from Tower import Tower

def BFS(tower, start, goal):
    frontier = [[valid_move] for valid_move in tower.valid_moves()]

    while len(frontier) > 0:
        moves_list = frontier.pop(0)
        new_tower = Tower(start, goal)
        if new_tower.check_success_sequence(moves_list):
            print(moves_list)
            exit(0)
        if len(moves_list) < 8:
            valid_moves_lst = new_tower.valid_moves()
            for valid_move in valid_moves_lst:
                new_tower_list = moves_list[:]
                new_tower_list.append(valid_move)
                frontier.append(new_tower_list)

if __name__ == "__main__":

    start = [["green", "blue", "red"], [], []]
    goal = [["red"], ["green", "blue"], []]
    tower_manual = Tower(start, goal)
    
    BFS(tower_manual, start, goal)

    exit(0)