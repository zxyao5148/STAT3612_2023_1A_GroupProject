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

## Testing Instruction
Please refer to the following steps to evaluate our best-performing model:  
1. Download all the files and make sure that the directories are in original order.
2. Go to `model_fitting/best-model.ipynb`. Followings are description for each code chunck.
   - the first code chunck is to load libraries 
   - the second code chunck is to load processed data, including latest, mean, sd, min, and max of the time series data (check out `data_processing/preprocessing.ipynb` for details)
   - the third code chunck is to separate features and response
   - the fourth code chunk utilizes Bayesian Optimization to tune hyperparameters
   - the fifth code chunk makes prediction based on the optimal parameters  

Note that the optimized hyperparameter values turned out to be __'max_depth' = 1135, 'min_samples_leaf' = 2, 'min_samples_split' = 2, 'n_estimators' = 1614__, under 'random_state=42', which gives rise to our best kaggle submission - test AUC score of 0.809 and 0.805 on private and public leaderboard, respectively.

## Inquiry
For any question w.r.t. to this project, please email to u3584514@connect.hku.hk and we will reply at earliest convenience.

