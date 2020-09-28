from score import Score


def test_constructor():
    sc = Score('test.txt')
    assert sc.file == 'test.txt'
    # Because test_read_file method is called upon
    # initialization, we can expect the list_name_score
    # to be updated with the expected tuple
    assert sc.list_name_score == [('Shaun', 50)]
    assert sc.score_flag


def test_read_file():
    # If file does not exist, nothing happens
    sc = Score('doesnotexist.txt')
    assert sc.read_file('doesnotexist.txt') == None


def test_score_to_list():
    # Tests the parameters of score_to_list method
    # if score is larger than the score in score_to_list[0]
    # insert the tuple at index 0, if not append the tuple
    # to score_to_list
    sc = Score('test.txt')
    sc.score_to_list('John', 56)
    assert sc.list_name_score == [('John', 56), ('Shaun', 50)]
    sc.score_to_list('Andy', 10)
    assert sc.list_name_score == [('John', 56), ('Shaun', 50), ('Andy', 10)]


def test_list_to_file():
    # After writing to the file, test to make sure
    # score_flag is False
    sc = Score('test.txt')
    assert sc.score_flag
    sc.list_to_file()
    assert not sc.score_flag
