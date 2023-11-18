# feat_engin.py
# feature engineering with polynomical/interaction terms
# sample usage:s
# from feat_engin import feat_engins
# X_train, X_test = feat_engin(X_train, X_test, num_cols, interaction_only=False)

from sklearn.preprocessing import PolynomialFeatures, StandardScaler

def feat_engin(X_train, X_test, num_cols, interaction_only=False):
    poly = PolynomialFeatures(degree=3, include_bias=False, interaction_only=interaction_only)
    scaler = StandardScaler()
    for col in X_train.columns:
        if col in num_cols: 
            train_terms = poly.fit_transform(X_train[[col]])
            test_terms = poly.transform(X_test[[col]])
            train_terms_scaled = scaler.fit_transform(train_terms)
            test_terms_scaled = scaler.transform(test_terms)
            term_type = 'interact' if interaction_only else 'poly'
            train_terms_df = pd.DataFrame(train_terms_scaled, columns=[f"{col}_{term_type}_{i}" for i in range(train_terms_scaled.shape[1])])
            test_terms_df = pd.DataFrame(test_terms_scaled, columns=[f"{col}_{term_type}_{i}" for i in range(test_terms_scaled.shape[1])])
            X_train = pd.concat([X_train, train_terms_df], axis=1)
            X_test = pd.concat([X_test, test_terms_df], axis=1)
    return X_train, X_test