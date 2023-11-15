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
