# STAT3612_2023_1A_GroupProject
Group project for HKU course STAT3612 Statistical Machine Learning (2023 1A, Coordinator: Dr. Yu Lequan)  
Refer to the corresponding kaggle competition for more details: [30-day All-Cause Hospital Readmission Prediction](https://www.kaggle.com/competitions/30-day-all-cause-hospital-readmission-prediction)

## Timeline
- ✅ [Proposal](https://github.com/zxyao5148/STAT3612_2023_1A_GroupProject/blob/main/proposal.pdf): 5 November, 2023  
- ✅ [Presentation](https://github.com/zxyao5148/STAT3612_2023_1A_GroupProject/blob/main/presentation.pdf): 24 November, 2023
- ✅ [Report](https://github.com/zxyao5148/STAT3612_2023_1A_GroupProject/blob/main/report.pdf): 7 December, 2023  

## Group Member

| Name | UID | Account |
| ------------- | ------------- | ----------------- |
| Yao Zixuan  | 3035845148  | zxyao5148 |
| Wang Ziyu  | 3035777547 | ZiyuWang1121 |
| Fang Jiahe | 3035772482 | fang0908 |
| Huang Yining | 3035662522 | YuniGE  |
| Huang Zixun | 3035844522 | Jessie31111 |

## Workload Distribution
:smile: The authors declared that the workload is evenly distributed.

## Instruction
Please refer to the following steps to evaluate our best-performing model:  
1. Download all the files and make sure that the directories are in original order.
2. Run the first code chunck to load libraries, the second and thrid to load processed data, and the fourth to construct `X_train`, `y_train`, and `X_test`, no need for adjusting class imblance, feature selection, etc.
3. Go to `model_fitting/bayes_optim.ipynb` and run the bayesian optimization for Extra Trees (please note that this is the best model submitted to the kaggle comptition, but not the one with highest AUC in our report). The optimized hyperparameter values turned out to be __'max_depth' = 1135, 'min_samples_leaf' = 2, 'min_samples_split' = 2, 'n_estimators' = 1614__.
4. Execute the last code chunck to generate predictions (predicted positive class probabilities).


