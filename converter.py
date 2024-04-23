import pandas as pd


def to_df(trainset):
    data = {'userId': [], 'movieId': [], 'rating': []}
    for (uid, iid, rating) in trainset.all_ratings():
        data['userId'].append(trainset.to_raw_uid(uid))
        data['movieId'].append(trainset.to_raw_iid(iid))
        data['rating'].append(rating)
    df = pd.DataFrame(data)
    return df
