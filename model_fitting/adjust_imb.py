# adjust_imb.py
# address class imbalance issue (training set)
# oversampling the minority class
# note: pip install -U threadpoolctl to debug if necessary

# sample usage:
# from adjust_imb import adjust_imb
# X_train_adj, y_train_adj = adjust_imb(X_train, y_train)

from collections import Counter
from imblearn.over_sampling import SMOTE

def adjust_imb(X, y):
    print('Original dataset shape %s' % Counter(y))
    smo = SMOTE(random_state=42)
    X_smo, y_smo = smo.fit_resample(X, y)
    print('Resampled dataset shape %s' % Counter(y_smo))
    return X_smo, y_smo

