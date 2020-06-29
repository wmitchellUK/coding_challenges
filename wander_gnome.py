# good eggs interview question
# wandering gnome - show the final possible location of a wandering gnome
# gnome can go up, down, left or right 1 cord value in each time period.
# display where gnome could end up

class Question(object):
    def __init__(self):
        pass

    result = []

    def solution(self, tick: int, param_result_list) -> str:

        if tick < 0:
            return "error"
        if tick == 0:
            return
        else:
            # new tick blow away result list
            self.result = []
            while len(param_result_list) > 0:
                # removes an item and assigns it to list
                element = param_result_list.pop(len(param_result_list)-1)
                # add items from one list to another
                for cord in self.derive_cords(element):
                    self.result.append(cord)

            self.solution(tick-1, self.result)


    def derive_cords(self, cord_tuple) -> list:
        """
        Given a cord tuple return list of possible destinations
        :param cord_tuple_list:
        :return:
        """
        # up
        my_cord_tuple_up_x = cord_tuple[0]
        my_cord_tuple_up_y = cord_tuple[1]+1
        my_cord_tuple_up = (my_cord_tuple_up_x, my_cord_tuple_up_y)

        # down
        my_cord_tuple_down_x = cord_tuple[0]
        my_cord_tuple_down_y = cord_tuple[1]-1

        my_cord_tuple_down = (my_cord_tuple_down_x, my_cord_tuple_down_y)

        # left
        my_cord_tuple_left_x = cord_tuple[0]-1
        my_cord_tuple_left_y = cord_tuple[1]

        my_cord_tuple_left = (my_cord_tuple_left_x, my_cord_tuple_left_y)

        # right
        my_cord_tuple_right_x = cord_tuple[0]+1
        my_cord_tuple_right_y = cord_tuple[1]

        my_cord_tuple_right = (my_cord_tuple_right_x, my_cord_tuple_right_y)

        my_list = []

        my_list.append(my_cord_tuple_up)
        my_list.append(my_cord_tuple_down)
        my_list.append(my_cord_tuple_left)
        my_list.append(my_cord_tuple_right)

        return my_list


solution = Question()
solution.solution(1, [(0,0)])
print(solution.result)

# tick 1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# tick 2 []
