# train
- __all_feat__: only exculded features with constant values
    - `train_latest.csv`: latest feature value in train set
    - `train_median.csv`: median feature value in train set
    - `train_valid_latest.csv`: latest feature value in train+valid (merged) set
    - `train_valid_median.csv`: median feature value in train+valid (merged) set
    - `sequece_data.zip`:
        - `train_all.csv`: all feature values in train set
        - `train_valid_all.csv`: all feature values in train+valid (merged) set
- __selected_feat__: excluded features with contant values, low correlation with response (<0.1) or high correlation with others (>0.7),
   same structure as all_feat

  For resampling: call `adjust_imb.py`
  ```
  from adjust_imb import adjust imb
  X_train_adj, y_train_adj = adjust_imb(X_train, y_train)
  ```
# valid
(to be used if not merged with train; should not be resampled)
- __all_feat__: correspond to `train/all_feat`
- __selected_feat__: correspond to  `train/selected_feat`
  
