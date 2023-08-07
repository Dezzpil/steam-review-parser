columns = [
    'review',  # string - текст обзора
    'votes_up',  # int - пользователей, посчитавших этот обзор полезным
    'votes_funny',  # int - посчитавших этот обзор забавным
    'weighted_vote_score',  # float - не пойму что, вероятно какая-то интегральная оценка стима
    'comment_count',  # int
    'author.playtime_at_review',  # int количество часов в игре к моменту написания отзыва
    'author.num_games_owned',  # int
    'author.num_reviews',  # int
    'received_for_free',  # boolean - товар получен бесплатно? может указывать на куратора
    'written_during_early_access',  # boolean
    'voted_up',  # boolean - одобряю? наш таргет
]