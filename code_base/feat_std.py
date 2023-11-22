# feat_std.py
# standardization of numerical features
# sample usage:
# from feat_std import feat_std
# X_train, X_test = feat_std(X_train, X_test, num_cols)

from sklearn.preprocessing import StandardScaler

def feat_std(X_train, X_test, num_cols):
    scaler = StandardScaler()
    for col in num_cols:
        if col in X_train.columns:
            X_train[col] = scaler.fit_transform(X_train[[col]])
            if col in X_test.columns:
                X_test[col] = scaler.transform(X_test[[col]])
    return X_train, X_test