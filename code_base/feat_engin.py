# feat_engin.py
# feature engineering with polynomical/interaction terms
# sample usage:
# from feat_engin import feat_engins
# X_train, X_test = feat_engin(X_train, X_test, num_cols, interaction_only=False)

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

def feat_engin(X_train, X_test, num_cols):
    poly_interact = PolynomialFeatures(degree=3, include_bias=False, interaction_only=True)
    poly_poly = PolynomialFeatures(degree=3, include_bias=False, interaction_only=False)
    scaler = StandardScaler()
    
    new_train_cols = []
    new_test_cols = []
    
    for col in num_cols: 
        if col in X_train.columns: 
            # Interaction terms
            train_terms_interact = poly_interact.fit_transform(X_train[[col]])
            test_terms_interact = poly_interact.transform(X_test[[col]])
            train_terms_interact_scaled = scaler.fit_transform(train_terms_interact)
            test_terms_interact_scaled = scaler.transform(test_terms_interact)
            train_terms_interact_df = pd.DataFrame(train_terms_interact_scaled, columns=[f"{col}_interact_{i}" for i in range(train_terms_interact_scaled.shape[1])])
            test_terms_interact_df = pd.DataFrame(test_terms_interact_scaled, columns=[f"{col}_interact_{i}" for i in range(test_terms_interact_scaled.shape[1])])
            new_train_cols.append(train_terms_interact_df)
            new_test_cols.append(test_terms_interact_df)
            
            # Polynomial terms
            train_terms_poly = poly_poly.fit_transform(X_train[[col]])
            test_terms_poly = poly_poly.transform(X_test[[col]])
            train_terms_poly_scaled = scaler.fit_transform(train_terms_poly)
            test_terms_poly_scaled = scaler.transform(test_terms_poly)
            train_terms_poly_df = pd.DataFrame(train_terms_poly_scaled, columns=[f"{col}_poly_{i}" for i in range(train_terms_poly_scaled.shape[1])])
            test_terms_poly_df = pd.DataFrame(test_terms_poly_scaled, columns=[f"{col}_poly_{i}" for i in range(test_terms_poly_scaled.shape[1])])
            new_train_cols.append(train_terms_poly_df)
            new_test_cols.append(test_terms_poly_df)
    
    X_train = pd.concat([X_train] + new_train_cols, axis=1)
    X_test = pd.concat([X_test] + new_test_cols, axis=1)
    
    return X_train, X_test
