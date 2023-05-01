def test_balls():
    t = Ball()
    t.break_map[t.breaking_floor] = 0.0
    t.breaking_floor = 99
    t.break_map[t.breaking_floor] = 1.0
    assert [x[0] for x in enumerate(t.break_map == 1.0) if x[1] == True][0] == 75, "problem with manual floor setting"
    assert t.drop_ball(2) == False, "ball breaking before breaking floor"
    assert t.drop_ball(20) == False, "ball breaking before breaking floor"
    assert t.drop_ball(70) == False, "ball breaking before breaking floor"
    assert t.balls == [0, 1], "missing balls"
    assert t.drop_ball(80), "didnt break when it should"
    assert t.balls == [0], "missing balls"
    assert t.drop_ball(75), "didnt break when it should"
    assert t.balls == [], "balls not broken"
    assert t.drop_ball(99) == False, "class allowing drops with no balls remaining"
    assert t.tests == [2, 20, 70, 80, 75], "tests not found or invalid order"
