# Shared Code Base
functions to implement feature selection and address class imblance

1. addressing class imblance:
```
import sys
sys.path.append('../code_base') # relative path to code base
from adjust_imbl import adjust_imbl
X_train_adj, y_train_adj = adjust_imbl(X_train, y_train)
```

2. implement feature selection:
```
from select_feat import select_feat
X_train_sel = select_feat(X_train, y_train, n_features=100)
```

Note that the input `X_train` should be a dataframe only consists of features, i.e., remember to drop information columns as well as the target before applying the above functions; `y_train` should be the response variable 'readmitted_within_30days'. The output `X_train_adj`, `y_train_adj` are the feature dataframe and response varaible after resampling, respectively; `X_train_sel` refers to the returned feature dataframe after feature selection.
