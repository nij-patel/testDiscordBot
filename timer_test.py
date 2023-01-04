# name file w _test at end

from timer import Timer


def test_start_initializes_vars_properly():
    # Setup
    timer = Timer()
    # Exercise
    timer.start()
    # Verify
    assert timer.is_running() == True
    assert timer.get_ticks() == 0


def test_init_initializes_vars_properly():
    # Setup
    timer = Timer()
    # Exercise
    # Verify
    assert not timer.is_running() == True
    assert timer.get_ticks() == 0


def test_tick_increases_ticks():
    # Setup
    timer = Timer()
    # Exercise
    timer.start()
    timer.tick()
    # Verify
    assert timer.is_running() == True
    assert timer.get_ticks() == 1
