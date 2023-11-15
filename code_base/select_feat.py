# select features based on f-score

# sample usage:
#from select_feat import select_feat
#X_train_selected = select_feat(X_train, y_train)

from sklearn.feature_selection import f_classif
from sklearn.model_selection import KFold

def select_feat(X, y, n_splits=10, n_features=100):
    f_score_sums = dict.fromkeys(X.columns, 0.0)
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=1)
    for train_index, test_index in kf.split(X):
        X_batch, y_batch = X.iloc[test_index], y.iloc[test_index]
        f_values, p_values = f_classif(X_batch, y_batch)
        for i, feature in enumerate(X.columns):
            f_score_sums[feature] += f_values[i]
    f_score_avgs = {feature: f_score_sum / n_splits for feature, f_score_sum in f_score_sums.items()}
    top_features = sorted(f_score_avgs, key=f_score_avgs.get, reverse=True)[:n_features]
    return X[top_features]
