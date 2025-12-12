def normalise_review(reviews):
    unique = {r['id']: r for r in reviews}.values()
    for r in unique:
        r['text'] = r['text'].strip()
    return list(unique)
