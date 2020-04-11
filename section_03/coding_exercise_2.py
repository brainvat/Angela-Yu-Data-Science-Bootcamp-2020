def top_three(scores):
    scores = scores
    top_scores = []

    scores.sort()
    scores.reverse()
    top_scores.append(scores[0])
    top_scores.append(scores[1])
    top_scores.append(scores[2])


    # Leave this line alone
    return top_scores
