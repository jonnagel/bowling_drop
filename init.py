import numpy as np
import seaborn as sns

class Ball:
    """ basic mechanics """
    def __init__(self, floors=100, balls=2, exact=True):
        self.balls = list(range(balls))
        self.ball_count = balls
        self.break_map = np.zeros(floors)
        self.breaking_floor = np.random.choice(floors)
        self.break_map[self.breaking_floor] = 1.0
        self.floors = floors
        self.tests = []
        # assert self.break_map.sum() == 1.0, "no breaking floor"


    def drop_ball(self, floor_number):
        """
        returns true if ball broken, not otherwise
        """
        if len(self.balls)>0:
            self.tests.append(floor_number)
            if self.break_map[floor_number]==1.0: # exact floor
                self.balls.pop()
                return True
            if self.break_map[:floor_number].sum()==1.0: # above breaking floor
                self.balls.pop()
                return True
            if self.break_map[floor_number:].sum()==1.0: # below breaking floor
                return False
        else:
                return False


class BinarySplit:
    """ create a list of places to split """
    def __init__(self, window=100):
        self.window = window
        self.calc()

    def half(self, window):
        if window>0:
            return int(window/2)
        else:
            return None

    def calc(self):
        half_int = self.half(self.window)
        out = [half_int]
        while half_int>0:
            half_int = self.half(half_int)
            if half_int>0:
                out.append(half_int)
        upper = [self.window-x for x in out]
        lower = sorted(out)
        self.splits = [0] + lower + upper[1:]


def binary_splitting(debug=False):
    """ glue to join splits and balls """
    t = Ball()
    test_points = BinarySplit().splits
    array_index = test_points.index(int(t.floors/2))
    print_info = debug
    while t.balls:

        # 2 balls
        if len(t.balls)==2:
            if t.drop_ball(test_points[array_index]):
                print('ball broke') if print_info else None
                if len(t.balls)<t.ball_count: # lost a ball go down
                    array_index-=1
                    print('down') if print_info else None
                if len(t.balls)==t.ball_count: # didn't lose a ball go up
                    array_index+=1
                    print('up') if print_info else None
            else:
                print('ball unbroken') if print_info else None
                array_index+=1
                print('up') if print_info else None

        # only one ball left
        if len(t.balls)==1:
            idx = min(test_points[:array_index])
            t.drop_ball(0)
            while len(t.balls) > 0:
                idx += 1
                t.drop_ball(idx)
            assert idx == t.breaking_floor, "exact floor not found"

    return({'breaking_floor': idx, 'count_floors_checked': len(t.tests), 'tested_floors': t.tests, 'test_type': 'binary_splitting', 'steps': 0})


def gradient_ascent(steps):
    """ generate splits and test on balls """
    t = Ball()
    test_points = [t.floors-1] + list(reversed(range(steps-1, t.floors, steps)))
    assert t.floors-1 == max(test_points), "be sure top floor is in list"
    while t.balls:
        # 2 balls remain
        if len(t.balls)==t.ball_count:
            while len(t.balls)==t.ball_count:
                t.drop_ball(test_points.pop())

        # only one ball left
        if len(t.balls)==1:
            if len(t.tests)==1: 
                last_unbroken_floor = 0
            else:
                last_unbroken_floor =  max(t.tests[:-1])
            while len(t.balls) > 0:
                last_unbroken_floor += 1
                t.drop_ball(last_unbroken_floor)

    return({'breaking_floor': t.breaking_floor, 'count_floors_checked': len(t.tests), 'tested_floors': t.tests, 'test_type': 'gradient_ascent', 'steps': steps})
