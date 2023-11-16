# adjust_imbl.py
# address class imbalance issue (training set)
# oversampling the minority class
# note: pip install -U threadpoolctl to debug if necessary

# sample usage:
# from adjust_imbl import adjust_imbl
# X_train_adj, y_train_adj = adjust_imbl(X_train, y_train)

from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

def adjust_imbl(X, y, option='under'):
    if option == 'over':
        sampler = RandomOverSampler(random_state=42)
    elif option == 'under':
        sampler = RandomUnderSampler(random_state=42)
    else:
        raise ValueError("Invalid option parameter. \nPlease choose either 'over' or 'under'.")
    print('Original dataset shape %s' % Counter(y))
    X_resampled, y_resampled = sampler.fit_resample(X, y)
    print('Resampled dataset shape %s' % Counter(y_resampled))
    return X_resampled, y_resampled
