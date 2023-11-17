# select features based on f-score

# sample usage:
#from select_feat import select_feat
#X_train_selected = select_feat(X_train, y_train, method='p_value')

from sklearn.feature_selection import f_classif

def select_feat(X, y, method='f_score', n_features=100, p_value_threshold=0.05):
    f_values, p_values = f_classif(X, y)
    if method == 'f_score':
        f_scores = dict(zip(X.columns, f_values))
        top_features = sorted(f_scores, key=f_scores.get, reverse=True)[:n_features]
        return X[top_features]
    elif method == 'p_value':
        p_values_dict = dict(zip(X.columns, p_values))
        selected_features = [feature for feature, p_value in p_values_dict.items() if p_value < p_value_threshold]
        return X[selected_features]
