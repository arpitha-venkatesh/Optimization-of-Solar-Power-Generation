# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:23:12 2024

@author: Admin
"""

import pandas as pd
solar_dataset=pd.read_csv("Solar Dataset.csv",encoding="latin")
solar_dataset
solar_dataset.columns
solar_dataset.describe()
solar_dataset.info()
solar_dataset.count()

 # ------------------------------------------------------------------------------------
 # duplicate handling:
solar_dataset.shape
# Out[17]: (366, 23)

solar_dataset.duplicated().sum()
# Out[21]: 0

#-------------------------------------------------------------------------------
# droping column
# In the dataset, the 'Grid Downtime HH' column contains only 2 non-null values, 
# thus providing limited information for analysis. 
# Similarly, the 'Plant Downtime HH' column, having the same value for all entries, 
# lacks variability and useful information for analysis.
# so we are droping that column
columns_to_drop = ['Grid Downtime HH:MM','Plant Downtime HH:MM']
solar_dataset.drop(columns=columns_to_drop, inplace=True)

solar_dataset.shape
# Out[64]: (366, 21)

# ------------------------------------------------------------------------------
# handling missing values
# before droping
total_missing_values=solar_dataset.isna().sum()
print(total_missing_values)
# output:
# Date                                                                0
# ICR-3 - INV1                                                       18
# ICR-3 - INV2                                                       18
# ICR-3 - INV3                                                       18
# ICR-3 - INV4                                                       18
# ICR-4 - INV1                                                       18
# ICR-4 - INV2                                                       18
# ICR-4 - INV3                                                       18
# ICR-4 - INV4                                                       18
# Total Daily Integrated Generation MWh                              18
# PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH     18
# PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh     18
# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh    18
# PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh    18
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh      19
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh      19
# Daily Generation Plant end meter (net)MWh                          19
# Global Tilted Irradiation/Irradiance (GTI)kWh/m2                   18
# Global horizontal irrradiance (GHI)kMh/m2                          18
# Performance Ratio (PR) %                                           19
# Remarks                                                            18
# dtype: int64

percentage_of_missing_values=solar_dataset.isna().mean()*100
print(percentage_of_missing_values)
# output:
# Date                                                               0.000000
# ICR-3 - INV1                                                       4.918033
# ICR-3 - INV2                                                       4.918033
# ICR-3 - INV3                                                       4.918033
# ICR-3 - INV4                                                       4.918033
# ICR-4 - INV1                                                       4.918033
# ICR-4 - INV2                                                       4.918033
# ICR-4 - INV3                                                       4.918033
# ICR-4 - INV4                                                       4.918033
# Total Daily Integrated Generation MWh                              4.918033
# PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH     4.918033
# PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh     4.918033
# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh    4.918033
# PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh    4.918033
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh      5.191257
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh      5.191257
# Daily Generation Plant end meter (net)MWh                          5.191257
# Global Tilted Irradiation/Irradiance (GTI)kWh/m2                   4.918033
# Global horizontal irrradiance (GHI)kMh/m2                          4.918033
# Performance Ratio (PR) %                                           5.191257
# Remarks                                                            4.918033
# dtype: float64


# In the dataset, we observed that the bottom 18 rows contain only date values, 
# while all other 19 columns do not contain any values, so we just dropped those rows.


solar_dataset.dropna(subset=["ICR-3 - INV1"],inplace=True,axis=0)

# after droping
total_missing_values=solar_dataset.isna().sum()
print(total_missing_values)
# output:
# Date                                                               0
# ICR-3 - INV1                                                       0
# ICR-3 - INV2                                                       0
# ICR-3 - INV3                                                       0
# ICR-3 - INV4                                                       0
# ICR-4 - INV1                                                       0
# ICR-4 - INV2                                                       0
# ICR-4 - INV3                                                       0
# ICR-4 - INV4                                                       0
# Total Daily Integrated Generation MWh                              0
# PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH     0
# PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh     0
# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh    0
# PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh    0
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh      1
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh      1
# Daily Generation Plant end meter (net)MWh                          1
# Global Tilted Irradiation/Irradiance (GTI)kWh/m2                   0
# Global horizontal irrradiance (GHI)kMh/m2                          0
# Performance Ratio (PR) %                                           1
# Remarks                                                            0
# dtype: int64

# there are still missing values in 
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh
# Daily Generation Plant end meter (net)MWh 
# Performance Ratio (PR) %


# imputation 
# first we check for the outliers 
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
sns.boxplot(y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh")

plt.subplot(2,2,2)
sns.boxplot(y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")

plt.subplot(2,2,3)
sns.boxplot(y=solar_dataset["Daily Generation Plant end meter (net)MWh"])
plt.title("Daily Generation Plant end meter (net)MWh")

plt.subplot(2,2,4)
sns.boxplot(y=solar_dataset["Performance Ratio (PR) %"])
plt.title("Performance Ratio (PR) %")

plt.tight_layout()
plt.show()

# there is not outliers present in 
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh
# Daily Generation Plant end meter (net)MWh 
# here we go for mean imputer 

from sklearn.impute import SimpleImputer
import numpy as np
mean_imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
solar_dataset[["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh",
              "PSS Main Meter (Daily Generation Plant end meter )(Import)MWh",
              "Daily Generation Plant end meter (net)MWh"]]=pd.DataFrame(mean_imputer.fit_transform(
                  solar_dataset[["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh",
                            "PSS Main Meter (Daily Generation Plant end meter )(Import)MWh",
                            "Daily Generation Plant end meter (net)MWh"]]))

# In Performance Ratio (PR) % column there are outlier
# here we go for median imputer 
median_imputer=SimpleImputer(missing_values=np.nan,strategy="median")
solar_dataset["Performance Ratio (PR) %"]=pd.DataFrame(median_imputer.fit_transform(solar_dataset[["Performance Ratio (PR) %"]]))
      
# after imputation:
total_missing_values=solar_dataset.isna().sum()
print(total_missing_values)
# output:
# Date                                                               0
# ICR-3 - INV1                                                       0
# ICR-3 - INV2                                                       0
# ICR-3 - INV3                                                       0
# ICR-3 - INV4                                                       0
# ICR-4 - INV1                                                       0
# ICR-4 - INV2                                                       0
# ICR-4 - INV3                                                       0
# ICR-4 - INV4                                                       0
# Total Daily Integrated Generation MWh                              0
# PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH     0
# PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh     0
# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh    0
# PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh    0
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh      0
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh      0
# Daily Generation Plant end meter (net)MWh                          0
# Global Tilted Irradiation/Irradiance (GTI)kWh/m2                   0
# Global horizontal irrradiance (GHI)kMh/m2                          0
# Performance Ratio (PR) %                                           0
# Remarks                                                            0
# dtype: int64


                    
# -------------------------------------------------------------------------------------------------------------
# outliers treatment
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["ICR-3 - INV1"])
plt.title("ICR-3 - INV1")

plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["ICR-3 - INV2"])
plt.title("ICR-3 - INV2")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["ICR-3 - INV3"])
plt.title("ICR-3 - INV3")

plt.subplot(2,3,4)
sns.boxplot(y=solar_dataset["ICR-3 - INV4"])
plt.title("ICR-3 - INV4")

plt.subplot(2,3,5)
sns.boxplot(y=solar_dataset["ICR-4 - INV1"])
plt.title("ICR-4 - INV1")

plt.subplot(2,3,6)
sns.boxplot(y=solar_dataset["ICR-4 - INV2"])
plt.title("ICR-4 - INV2")

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------
plt.figure(figsize=(20,12))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["ICR-4 - INV3"])
plt.title("ICR-4 - INV3")

plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["ICR-4 - INV4"])
plt.title("ICR-4 - INV4")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["Total Daily Integrated Generation MWh"])
plt.title("Total Daily Integrated Generation MWh")

plt.subplot(2,3,4)
sns.boxplot(y=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"])
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH")

plt.subplot(2,3,5)
sns.boxplot(y=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"])
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")

plt.subplot(2,3,6)
sns.boxplot(y=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"])
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh")

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
sns.boxplot(y=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"])
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")

plt.subplot(2,2,2)
sns.boxplot(y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh")

plt.subplot(2,2,3)
sns.boxplot(y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")

plt.subplot(2,2,4)
sns.boxplot(y=solar_dataset["Daily Generation Plant end meter (net)MWh"])
plt.title("Daily Generation Plant end meter (net)MWh")

plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"])
plt.title("Global Tilted Irradiation/Irradiance (GTI)kWh/m2")


plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"])
plt.title("Global horizontal irrradiance (GHI)kMh/m2")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["Performance Ratio (PR) %"])
plt.title("Performance Ratio (PR) %")

plt.tight_layout()
plt.show()

# columns which contain outliers are
# 'ICR-3 - INV1', 
# 'ICR-3 - INV2', 
# 'ICR-3 - INV3', 
# 'ICR-3 - INV4',
# 'ICR-4 - INV1', 
# 'ICR-4 - INV2', 
# 'ICR-4 - INV3', 
# 'ICR-4 - INV4',
# 'Total Daily Integrated Generation MWh'
# 'Global Tilted Irradiation/Irradiance (GTI)kWh/m2',
# 'Global horizontal irrradiance (GHI)kMh/m2', 
# 'Performance Ratio (PR) %

# here we are replacing outliers by winsorizer technique by iqr method
from feature_engine.outliers import Winsorizer
iqr_winsorizor=Winsorizer(capping_method="iqr",fold=1.5,tail="both",
                          variables=['ICR-3 - INV1','ICR-3 - INV2','ICR-3 - INV3','ICR-3 - INV4',
                                     'ICR-4 - INV1','ICR-4 - INV2','ICR-4 - INV3','ICR-4 - INV4',
                                     'Total Daily Integrated Generation MWh',
                                     'Global Tilted Irradiation/Irradiance (GTI)kWh/m2',
                                     'Global horizontal irrradiance (GHI)kMh/m2',
                                     'Performance Ratio (PR) %'])

solar_dataset[['ICR-3 - INV1','ICR-3 - INV2','ICR-3 - INV3','ICR-3 - INV4',
           'ICR-4 - INV1','ICR-4 - INV2','ICR-4 - INV3','ICR-4 - INV4',
           'Total Daily Integrated Generation MWh',
           'Global Tilted Irradiation/Irradiance (GTI)kWh/m2',
           'Global horizontal irrradiance (GHI)kMh/m2',
           'Performance Ratio (PR) %']]=iqr_winsorizor.fit_transform(
                                                solar_dataset[['ICR-3 - INV1','ICR-3 - INV2','ICR-3 - INV3','ICR-3 - INV4',
                                                              'ICR-4 - INV1','ICR-4 - INV2','ICR-4 - INV3','ICR-4 - INV4',
                                                              'Total Daily Integrated Generation MWh',
                                                              'Global Tilted Irradiation/Irradiance (GTI)kWh/m2',
                                                              'Global horizontal irrradiance (GHI)kMh/m2',
                                                              'Performance Ratio (PR) %']])
# after replacing outliers
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["ICR-3 - INV1"])
plt.title("ICR-3 - INV1")

plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["ICR-3 - INV2"])
plt.title("ICR-3 - INV2")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["ICR-3 - INV3"])
plt.title("ICR-3 - INV3")

plt.subplot(2,3,4)
sns.boxplot(y=solar_dataset["ICR-3 - INV4"])
plt.title("ICR-3 - INV4")

plt.subplot(2,3,5)
sns.boxplot(y=solar_dataset["ICR-4 - INV1"])
plt.title("ICR-4 - INV1")

plt.subplot(2,3,6)
sns.boxplot(y=solar_dataset["ICR-4 - INV2"])
plt.title("ICR-4 - INV2")

plt.tight_layout()
plt.show()                                                


plt.figure(figsize=(20,12))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["ICR-4 - INV3"])
plt.title("ICR-4 - INV3")

plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["ICR-4 - INV4"])
plt.title("ICR-4 - INV4")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["Total Daily Integrated Generation MWh"])
plt.title("Total Daily Integrated Generation MWh")

plt.subplot(2,3,4)
sns.boxplot(y=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"])
plt.title("Global Tilted Irradiation/Irradiance (GTI)kWh/m2")

plt.subplot(2,3,5)
sns.boxplot(y=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"])
plt.title("Global horizontal irrradiance (GHI)kMh/m2")

plt.subplot(2,3,6)
sns.boxplot(y=solar_dataset["Performance Ratio (PR) %"])
plt.title("Performance Ratio (PR) %")

plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------------
# NORMALISATION
# TO CHCEK WHETHWER VARIABLE IS NORMAL OR NOT
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab

plt.figure(figsize=(20,12))
plt.subplot(2,3,1)
stats.probplot(solar_dataset["ICR-3 - INV1"],dist="norm",plot=pylab)
plt.title("ICR-3 - INV1")
plt.subplot(2,3,2)
stats.probplot(solar_dataset["ICR-3 - INV2"],dist="norm",plot=pylab)
plt.title("ICR-3 - INV2")
plt.subplot(2,3,3)
stats.probplot(solar_dataset["ICR-3 - INV3"],dist="norm",plot=pylab)
plt.title("ICR-3 - INV3")
plt.subplot(2,3,4)
stats.probplot(solar_dataset["ICR-3 - INV4"],dist="norm",plot=pylab)
plt.title("ICR-3 - INV4)
plt.subplot(2,3,5)
stats.probplot(solar_dataset["ICR-4 - INV1"],dist="norm",plot=pylab)
plt.title("ICR-INV1)
plt.subplot(2,3,6)
stats.probplot(solar_dataset["ICR-4 - INV2"],dist="norm",plot=pylab)
plt.title("ICR-3 - INV1")
plt.show()

plt.figure(figsize=(12,8))
plt.subplot(2,3,1) 
stats.probplot(solar_dataset["ICR-4 - INV3"],dist="norm",plot=pylab)
plt.subplot(2,3,2)
stats.probplot(solar_dataset["ICR-4 - INV4"],dist="norm",plot=pylab)
plt.subplot(2,3,3)
stats.probplot(solar_dataset["Total Daily Integrated Generation MWh"],dist="norm",plot=pylab)
plt.subplot(2,3,4)
stats.probplot(solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"],dist="norm",plot=pylab)
plt.subplot(2,3,5)
stats.probplot(solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"],dist="norm",plot=pylab)
plt.subplot(2,3,6)
stats.probplot(solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"],dist="norm",plot=pylab)
plt.show() 

plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
stats.probplot(solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"],dist="norm",plot=pylab)
plt.subplot(2,2,2)
stats.probplot(solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"],dist="norm",plot=pylab)
plt.subplot(2,2,3)
stats.probplot(solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"],dist="norm",plot=pylab)
plt.subplot(2,2,4)
stats.probplot(solar_dataset["Daily Generation Plant end meter (net)MWh"],dist="norm",plot=pylab)
plt.show()

plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
stats.probplot(solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"],dist="norm",plot=pylab)
plt.subplot(1,3,2)
stats.probplot(solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"],dist="norm",plot=pylab)
plt.subplot(1,3,3)
stats.probplot(solar_dataset["Performance Ratio (PR) %"],dist="norm",plot=pylab)
plt.show()

# ---------------------------------------------------------------------------------------
# zero variance:
numerical_column=solar_dataset.select_dtypes(include=["number"]).columns
variance=solar_dataset[numerical_column].var()
print(variance)   
# output
# ICR-3 - INV1                                                       1.803113e+01
# ICR-3 - INV2                                                       1.694709e+01
# ICR-3 - INV3                                                       1.774817e+01
# ICR-3 - INV4                                                       1.796175e+01
# ICR-4 - INV1                                                       1.653503e+01
# ICR-4 - INV2                                                       1.816582e+01
# ICR-4 - INV3                                                       1.795578e+01
# ICR-4 - INV4                                                       1.759624e+01
# Total Daily Integrated Generation MWh                              1.118359e+03
# PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH     2.346321e+08
# PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh     6.251415e+03
# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh    1.018560e+07
# PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh    2.519911e+02
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh      4.424224e+03
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh      1.407927e-01
# Daily Generation Plant end meter (net)MWh                          4.410367e+03
# Global Tilted Irradiation/Irradiance (GTI)kWh/m2                   2.188774e+00
# Global horizontal irrradiance (GHI)kMh/m2                          2.157219e+00
# Performance Ratio (PR) %                                           3.386022e+01
# dtype: float64  

solar_dataset.to_csv('preprocessed_solar_dataset.csv', index=False)

# --------------------------------------------------------------------------------------
# EDA AFTER DATA CLEANING:
# UNIVARIENT
#  EDA(EXPLORATORY DATA ANALYSIS):
#  1ST MOMENT BUSINESS DECISION:
#  MEAN:
mean_ICR3_INV1=solar_dataset["ICR-3 - INV1"].mean()
mean_ICR3_INV2=solar_dataset["ICR-3 - INV2"].mean()
mean_ICR3_INV3=solar_dataset["ICR-3 - INV3"].mean()
mean_ICR3_INV4=solar_dataset["ICR-3 - INV4"].mean()
mean_ICR4_INV1=solar_dataset["ICR-4 - INV1"].mean()
mean_ICR4_INV2=solar_dataset["ICR-4 - INV2"].mean()
mean_ICR4_INV3=solar_dataset["ICR-4 - INV3"].mean()
mean_ICR4_INV4=solar_dataset["ICR-4 - INV4"].mean()
mean_Total_Daily_Integrated_Generation_MWh=solar_dataset["Total Daily Integrated Generation MWh"].mean()
mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].mean()
mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].mean()
mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].mean()
mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].mean()
mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].mean()
mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].mean()
mean_Daily_Generation_Plant_end_meter_net_MWh=solar_dataset["Daily Generation Plant end meter (net)MWh"].mean()
mean_Global_Tilted_Irradiation_Irradiance_GTI=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].mean()
mean_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].mean()
mean_Performance_Ratio_PR=solar_dataset["Performance Ratio (PR) %"].mean()

print(f"Mean ICR-3 - INV1: {mean_ICR3_INV1}")
print(f"Mean ICR-3 - INV2: {mean_ICR3_INV2}")
print(f"Mean ICR-3 - INV3: {mean_ICR3_INV3}")
print(f"Mean ICR-3 - INV4: {mean_ICR3_INV4}")
print(f"Mean ICR-4 - INV1: {mean_ICR4_INV1}")
print(f"Mean ICR-4 - INV2: {mean_ICR4_INV2}")
print(f"Mean ICR-4 - INV3: {mean_ICR4_INV3}")
print(f"Mean ICR-4 - INV4: {mean_ICR4_INV4}")
print(f"Mean Total Daily Integrated Generation MWh: {mean_Total_Daily_Integrated_Generation_MWh}")
print(f"Mean PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Mean PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Mean PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Mean PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Mean PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Mean PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Mean Daily Generation Plant end meter (net)MWh: {mean_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Mean Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {mean_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Mean Global horizontal irradiance(GHI)kWh/m2: {mean_Global_horizontal_irradiance_GHI}")
print(f"Mean Performance Ratio (PR) %: {mean_Performance_Ratio_PR}")

# output:
# Mean ICR-3 - INV1: 15.317988505747126
# Mean ICR-3 - INV2: 15.133793103448275
# Mean ICR-3 - INV3: 15.360445402298852
# Mean ICR-3 - INV4: 15.417701149425286
# Mean ICR-4 - INV1: 15.109454022988507
# Mean ICR-4 - INV2: 15.197011494252871
# Mean ICR-4 - INV3: 15.449454022988508
# Mean ICR-4 - INV4: 15.196149425287357
# Mean Total Daily Integrated Generation MWh: 122.16451149425288
# Mean PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 30685.51833333333
# Mean PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 213.03385057471263
# Mean PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 6394.810344827586
# Mean PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 42.422413793103445
# Mean PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 157.63455331412106
# Mean PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.7772910662824207
# Mean Daily Generation Plant end meter (net)MWh: 156.86011527377522
# Mean Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 5.075689655172414
# Mean Global horizontal irradiance(GHI)kWh/m2: 4.794511494252873
# Mean Performance Ratio (PR) %: 78.99709770114943

# Median
median_ICR3_INV1 = solar_dataset["ICR-3 - INV1"].median()
median_ICR3_INV2 = solar_dataset["ICR-3 - INV2"].median()
median_ICR3_INV3 = solar_dataset["ICR-3 - INV3"].median()
median_ICR3_INV4 = solar_dataset["ICR-3 - INV4"].median()
median_ICR4_INV1 = solar_dataset["ICR-4 - INV1"].median()
median_ICR4_INV2 = solar_dataset["ICR-4 - INV2"].median()
median_ICR4_INV3 = solar_dataset["ICR-4 - INV3"].median()
median_ICR4_INV4 = solar_dataset["ICR-4 - INV4"].median()
median_Total_Daily_Integrated_Generation_MWh = solar_dataset["Total Daily Integrated Generation MWh"].median()
median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].median()
median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].median()
median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].median()
median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].median()
median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].median()
median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].median()
median_Daily_Generation_Plant_end_meter_net_MWh = solar_dataset["Daily Generation Plant end meter (net)MWh"].median()
median_Global_Tilted_Irradiation_Irradiance_GTI = solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].median()
median_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].median()
median_Performance_Ratio_PR = solar_dataset["Performance Ratio (PR) %"].median()

print(f"Median ICR-3 - INV1: {median_ICR3_INV1}")
print(f"Median ICR-3 - INV2: {median_ICR3_INV2}")
print(f"Median ICR-3 - INV3: {median_ICR3_INV3}")
print(f"Median ICR-3 - INV4: {median_ICR3_INV4}")
print(f"Median ICR-4 - INV1: {median_ICR4_INV1}")
print(f"Median ICR-4 - INV2: {median_ICR4_INV2}")
print(f"Median ICR-4 - INV3: {median_ICR4_INV3}")
print(f"Median ICR-4 - INV4: {median_ICR4_INV4}")
print(f"Median Total Daily Integrated Generation MWh: {median_Total_Daily_Integrated_Generation_MWh}")
print(f"Median PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Median PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Median PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Median PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Median PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Median PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Median Daily Generation Plant end meter (net)MWh: {median_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Median Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {median_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Median Global horizontal irradiance(GHI)kWh/m2: {median_Global_horizontal_irradiance_GHI}")
print(f"Median Performance Ratio (PR) %: {median_Performance_Ratio_PR}")

# output:
# Median ICR-3 - INV1: 16.12
# Median ICR-3 - INV2: 15.82
# Median ICR-3 - INV3: 16.02
# Median ICR-3 - INV4: 16.12
# Median ICR-4 - INV1: 15.77
# Median ICR-4 - INV2: 15.82
# Median ICR-4 - INV3: 16.12
# Median ICR-4 - INV4: 15.92
# Median Total Daily Integrated Generation MWh: 127.15
# Median PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 28280.695
# Median PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 196.02
# Median PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 5893.5
# Median PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 39.0
# Median PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 146.70999999999998
# Median PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.615
# Median Daily Generation Plant end meter (net)MWh: 146.065
# Median Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 5.35
# Median Global horizontal irradiance(GHI)kWh/m2: 4.855
# Median Performance Ratio (PR) %: 78.4

# MODE
mode_Remarks=solar_dataset["Remarks"].mode()
print(f"Mode Remarks: {mode_Remarks}")
# output:
#     Mode Remarks: 0    Weather was Partially Cloudy
#     Name: Remarks, dtype: object

# ---------------------------------------------------------------------------------
# second moment of bussiness understanding(measure of dispersion):
# variance:
variance_ICR3_INV1 = solar_dataset["ICR-3 - INV1"].var()
variance_ICR3_INV2 = solar_dataset["ICR-3 - INV2"].var()
variance_ICR3_INV3 = solar_dataset["ICR-3 - INV3"].var()
variance_ICR3_INV4 = solar_dataset["ICR-3 - INV4"].var()
variance_ICR4_INV1 = solar_dataset["ICR-4 - INV1"].var()
variance_ICR4_INV2 = solar_dataset["ICR-4 - INV2"].var()
variance_ICR4_INV3 = solar_dataset["ICR-4 - INV3"].var()
variance_ICR4_INV4 = solar_dataset["ICR-4 - INV4"].var()
variance_Total_Daily_Integrated_Generation_MWh = solar_dataset["Total Daily Integrated Generation MWh"].var()
variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].var()
variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].var()
variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].var()
variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].var()
variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].var()
variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].var()
variance_Daily_Generation_Plant_end_meter_net_MWh = solar_dataset["Daily Generation Plant end meter (net)MWh"].var()
variance_Global_Tilted_Irradiation_Irradiance_GTI = solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].var()
variance_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].var()
variance_Performance_Ratio_PR = solar_dataset["Performance Ratio (PR) %"].var()

print(f"Variance ICR-3 - INV1: {variance_ICR3_INV1}")
print(f"Variance ICR-3 - INV2: {variance_ICR3_INV2}")
print(f"Variance ICR-3 - INV3: {variance_ICR3_INV3}")
print(f"Variance ICR-3 - INV4: {variance_ICR3_INV4}")
print(f"Variance ICR-4 - INV1: {variance_ICR4_INV1}")
print(f"Variance ICR-4 - INV2: {variance_ICR4_INV2}")
print(f"Variance ICR-4 - INV3: {variance_ICR4_INV3}")
print(f"Variance ICR-4 - INV4: {variance_ICR4_INV4}")
print(f"Variance Total Daily Integrated Generation MWh: {variance_Total_Daily_Integrated_Generation_MWh}")
print(f"Variance PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Variance PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Variance PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Variance PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Variance PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Variance PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Variance Daily Generation Plant end meter (net)MWh: {variance_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Variance Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {variance_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Variance Global horizontal irradiance(GHI)kWh/m2: {variance_Global_horizontal_irradiance_GHI}")
print(f"Variance Performance Ratio (PR) %: {variance_Performance_Ratio_PR}")

# output:
# Variance ICR-3 - INV1: 15.693576633873251
# Variance ICR-3 - INV2: 14.41289277551428
# Variance ICR-3 - INV3: 15.04510387165028
# Variance ICR-3 - INV4: 15.49025406605055
# Variance ICR-4 - INV1: 13.974968865315168
# Variance ICR-4 - INV2: 16.34634320447845
# Variance ICR-4 - INV3: 15.614713533903084
# Variance ICR-4 - INV4: 15.26810386233397
# Variance Total Daily Integrated Generation MWh: 974.4411504811364
# Variance PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 234632098.35138464
# Variance PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 6251.415223747061
# Variance PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 10185603.312630435
# Variance PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 251.99108118851206
# Variance PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 4424.224007509404
# Variance PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.1407926616781138
# Variance Daily Generation Plant end meter (net)MWh: 4410.367413243195
# Variance Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 2.015425171420054
# Variance Global horizontal irradiance(GHI)kWh/m2: 2.122712440789692
# Variance Performance Ratio (PR) %: 14.17636849763159

# standard Deviation
std_ICR3_INV1 = solar_dataset["ICR-3 - INV1"].std()
std_ICR3_INV2 = solar_dataset["ICR-3 - INV2"].std()
std_ICR3_INV3 = solar_dataset["ICR-3 - INV3"].std()
std_ICR3_INV4 = solar_dataset["ICR-3 - INV4"].std()
std_ICR4_INV1 = solar_dataset["ICR-4 - INV1"].std()
std_ICR4_INV2 = solar_dataset["ICR-4 - INV2"].std()
std_ICR4_INV3 = solar_dataset["ICR-4 - INV3"].std()
std_ICR4_INV4 = solar_dataset["ICR-4 - INV4"].std()
std_Total_Daily_Integrated_Generation_MWh = solar_dataset["Total Daily Integrated Generation MWh"].std()
std_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].std()
std_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].std()
std_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].std()
std_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].std()
std_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].std()
std_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].std()
std_Daily_Generation_Plant_end_meter_net_MWh = solar_dataset["Daily Generation Plant end meter (net)MWh"].std()
std_Global_Tilted_Irradiation_Irradiance_GTI = solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].std()
std_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].std()
std_Performance_Ratio_PR = solar_dataset["Performance Ratio (PR) %"].std()

print(f"Standard Deviation ICR-3 - INV1: {std_ICR3_INV1}")
print(f"Standard Deviation ICR-3 - INV2: {std_ICR3_INV2}")
print(f"Standard Deviation ICR-3 - INV3: {std_ICR3_INV3}")
print(f"Standard Deviation ICR-3 - INV4: {std_ICR3_INV4}")
print(f"Standard Deviation ICR-4 - INV1: {std_ICR4_INV1}")
print(f"Standard Deviation ICR-4 - INV2: {std_ICR4_INV2}")
print(f"Standard Deviation ICR-4 - INV3: {std_ICR4_INV3}")
print(f"Standard Deviation ICR-4 - INV4: {std_ICR4_INV4}")
print(f"Standard Deviation Total Daily Integrated Generation MWh: {std_Total_Daily_Integrated_Generation_MWh}")
print(f"Standard Deviation PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {std_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Standard Deviation PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {std_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Standard Deviation PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {std_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Standard Deviation PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {std_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Standard Deviation PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {std_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Standard Deviation PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {std_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Standard Deviation Daily Generation Plant end meter (net)MWh: {std_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Standard Deviation Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {std_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Standard Deviation Global horizontal irradiance(GHI)kWh/m2: {std_Global_horizontal_irradiance_GHI}")
print(f"Standard Deviation Performance Ratio (PR) %: {std_Performance_Ratio_PR}")
# output:
# Standard Deviation ICR-3 - INV1: 3.9615119126254372
# Standard Deviation ICR-3 - INV2: 3.796431584463795
# Standard Deviation ICR-3 - INV3: 3.878801860323659
# Standard Deviation ICR-3 - INV4: 3.935766007532784
# Standard Deviation ICR-4 - INV1: 3.738310964234405
# Standard Deviation ICR-4 - INV2: 4.043061118073588
# Standard Deviation ICR-4 - INV3: 3.9515457145151545
# Standard Deviation ICR-4 - INV4: 3.907442112473833
# Standard Deviation Total Daily Integrated Generation MWh: 31.216039955143838
# Standard Deviation PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 15317.705387928854
# Standard Deviation PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 79.06589165845827
# Standard Deviation PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 3191.489199829828
# Standard Deviation PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 15.874226947744953
# Standard Deviation PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 66.5148405057804
# Standard Deviation PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.37522348231169356
# Standard Deviation Daily Generation Plant end meter (net)MWh: 66.41059714566039
# Standard Deviation Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 1.419656709003995
# Standard Deviation Global horizontal irradiance(GHI)kWh/m2: 1.4569531360993364
# Standard Deviation Performance Ratio (PR) %: 3.7651518558527743

# RANGE
range_ICR3_INV1 = solar_dataset["ICR-3 - INV1"].max() - solar_dataset["ICR-3 - INV1"].min()
range_ICR3_INV2 = solar_dataset["ICR-3 - INV2"].max() - solar_dataset["ICR-3 - INV2"].min()
range_ICR3_INV3 = solar_dataset["ICR-3 - INV3"].max() - solar_dataset["ICR-3 - INV3"].min()
range_ICR3_INV4 = solar_dataset["ICR-3 - INV4"].max() - solar_dataset["ICR-3 - INV4"].min()
range_ICR4_INV1 = solar_dataset["ICR-4 - INV1"].max() - solar_dataset["ICR-4 - INV1"].min()
range_ICR4_INV2 = solar_dataset["ICR-4 - INV2"].max() - solar_dataset["ICR-4 - INV2"].min()
range_ICR4_INV3 = solar_dataset["ICR-4 - INV3"].max() - solar_dataset["ICR-4 - INV3"].min()
range_ICR4_INV4 = solar_dataset["ICR-4 - INV4"].max() - solar_dataset["ICR-4 - INV4"].min()
range_Total_Daily_Integrated_Generation_MWh = solar_dataset["Total Daily Integrated Generation MWh"].max() - solar_dataset["Total Daily Integrated Generation MWh"].min()
range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].max() - solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].min()
range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].max() - solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].min()
range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].max() - solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].min()
range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].max() - solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].min()
range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].max() - solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].min()
range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].max() - solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].min()
range_Daily_Generation_Plant_end_meter_net_MWh = solar_dataset["Daily Generation Plant end meter (net)MWh"].max() - solar_dataset["Daily Generation Plant end meter (net)MWh"].min()
range_Global_Tilted_Irradiation_Irradiance_GTI = solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].max() - solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].min()
range_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].max()-solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].min()
range_Performance_Ratio_PR = solar_dataset["Performance Ratio (PR) %"].max() - solar_dataset["Performance Ratio (PR) %"].min()

print(f"Range ICR-3 - INV1: {range_ICR3_INV1}")
print(f"Range ICR-3 - INV2: {range_ICR3_INV2}")
print(f"Range ICR-3 - INV3: {range_ICR3_INV3}")
print(f"Range ICR-3 - INV4: {range_ICR3_INV4}")
print(f"Range ICR-4 - INV1: {range_ICR4_INV1}")
print(f"Range ICR-4 - INV2: {range_ICR4_INV2}")
print(f"Range ICR-4 - INV3: {range_ICR4_INV3}")
print(f"Range ICR-4 - INV4: {range_ICR4_INV4}")
print(f"Range Total Daily Integrated Generation MWh: {range_Total_Daily_Integrated_Generation_MWh}")
print(f"Range PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Range PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Range PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Range PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Range PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Range PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Range Daily Generation Plant end meter (net)MWh: {range_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Range Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {range_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Range Global horizontal irradiance(GHI)kWh/m2: {range_Global_horizontal_irradiance_GHI}")
print(f"Range Performance Ratio (PR) %: {range_Performance_Ratio_PR}")
# output:
# Range ICR-3 - INV1: 15.462500000000002
# Range ICR-3 - INV2: 14.899999999999999
# Range ICR-3 - INV3: 15.062500000000005
# Range ICR-3 - INV4: 15.500000000000004
# Range ICR-4 - INV1: 14.999999999999996
# Range ICR-4 - INV2: 16.150000000000002
# Range ICR-4 - INV3: 15.649999999999999
# Range ICR-4 - INV4: 15.800000000000004
# Range Total Daily Integrated Generation MWh: 124.34999999999998
# Range PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 54699.05
# Range PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 269.5
# Range PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 11399.0
# Range PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 54.0
# Range PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 282.77
# Range PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 1.45
# Range Daily Generation Plant end meter (net)MWh: 281.48
# Range Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 5.670000000000002
# Range Global horizontal irradiance(GHI)kWh/m2: 6.609999999999999
# Range Performance Ratio (PR) %: 18.75999999999999

# -----------------------------------------------------------------------------------------
# THIRD MOMENT OF BUSINESS UNDERSTANDING
# skewness
skewness_ICR3_INV1 = solar_dataset["ICR-3 - INV1"].skew()
skewness_ICR3_INV2 = solar_dataset["ICR-3 - INV2"].skew()
skewness_ICR3_INV3 = solar_dataset["ICR-3 - INV3"].skew()
skewness_ICR3_INV4 = solar_dataset["ICR-3 - INV4"].skew()
skewness_ICR4_INV1 = solar_dataset["ICR-4 - INV1"].skew()
skewness_ICR4_INV2 = solar_dataset["ICR-4 - INV2"].skew()
skewness_ICR4_INV3 = solar_dataset["ICR-4 - INV3"].skew()
skewness_ICR4_INV4 = solar_dataset["ICR-4 - INV4"].skew()
skewness_Total_Daily_Integrated_Generation_MWh = solar_dataset["Total Daily Integrated Generation MWh"].skew()
skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].skew()
skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].skew()
skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].skew()
skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].skew()
skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].skew()
skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].skew()
skewness_Daily_Generation_Plant_end_meter_net_MWh = solar_dataset["Daily Generation Plant end meter (net)MWh"].skew()
skewness_Global_Tilted_Irradiation_Irradiance_GTI = solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].skew()
skewness_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].skew()
skewness_Performance_Ratio_PR = solar_dataset["Performance Ratio (PR) %"].skew()

print(f"Skewness ICR-3 - INV1: {skewness_ICR3_INV1}")
print(f"Skewness ICR-3 - INV2: {skewness_ICR3_INV2}")
print(f"Skewness ICR-3 - INV3: {skewness_ICR3_INV3}")
print(f"Skewness ICR-3 - INV4: {skewness_ICR3_INV4}")
print(f"Skewness ICR-4 - INV1: {skewness_ICR4_INV1}")
print(f"Skewness ICR-4 - INV2: {skewness_ICR4_INV2}")
print(f"Skewness ICR-4 - INV3: {skewness_ICR4_INV3}")
print(f"Skewness ICR-4 - INV4: {skewness_ICR4_INV4}")
print(f"Skewness Total Daily Integrated Generation MWh: {skewness_Total_Daily_Integrated_Generation_MWh}")
print(f"Skewness PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Skewness PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Skewness PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Skewness PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Skewness PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Skewness PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Skewness Daily Generation Plant end meter (net)MWh: {skewness_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Skewness Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {skewness_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Skewness Global horizontal irradiance(GHI)kWh/m2: {skewness_Global_horizontal_irradiance_GHI}")
print(f"Skewness Performance Ratio (PR) %: {skewness_Performance_Ratio_PR}")
# output:
# Skewness ICR-3 - INV1: -0.9684143956569035
# Skewness ICR-3 - INV2: -0.9349284236513234
# Skewness ICR-3 - INV3: -0.9311349886116779
# Skewness ICR-3 - INV4: -0.9510523058411517
# Skewness ICR-4 - INV1: -0.9520117081393327
# Skewness ICR-4 - INV2: -0.9309412596126665
# Skewness ICR-4 - INV3: -0.9699201564595624
# Skewness ICR-4 - INV4: -0.9345871112944901
# Skewness Total Daily Integrated Generation MWh: -0.9721268674251434
# Skewness PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 0.4515798370603562
# Skewness PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 0.2789482325752937
# Skewness PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 0.4517092591864534
# Skewness PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 0.297322042826403
# Skewness PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 0.23595595189260155
# Skewness PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: -0.04947028588783892
# Skewness Daily Generation Plant end meter (net)MWh: 0.2354391841874319
# Skewness Global Tilted Irradiation/Irradiance (GTI)kWh/m2: -0.9022839770165361
# Skewness Global horizontal irradiance(GHI)kWh/m2: -0.6270454789921845
# Skewness Performance Ratio (PR) %: 0.49425942420298774

# ----------------------------------------------------------------------------------------
# FORTH MOMENT OF BUSINESS UNDERSTANDING
# kurtosis
kurtosis_ICR3_INV1 = solar_dataset["ICR-3 - INV1"].kurt()
kurtosis_ICR3_INV2 = solar_dataset["ICR-3 - INV2"].kurt()
kurtosis_ICR3_INV3 = solar_dataset["ICR-3 - INV3"].kurt()
kurtosis_ICR3_INV4 = solar_dataset["ICR-3 - INV4"].kurt()
kurtosis_ICR4_INV1 = solar_dataset["ICR-4 - INV1"].kurt()
kurtosis_ICR4_INV2 = solar_dataset["ICR-4 - INV2"].kurt()
kurtosis_ICR4_INV3 = solar_dataset["ICR-4 - INV3"].kurt()
kurtosis_ICR4_INV4 = solar_dataset["ICR-4 - INV4"].kurt()
kurtosis_Total_Daily_Integrated_Generation_MWh = solar_dataset["Total Daily Integrated Generation MWh"].kurt()
kurtosis_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].kurt()
kurtosis_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"].kurt()
kurtosis_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].kurt()
kurtosis_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh = solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"].kurt()
kurtosis_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].kurt()
kurtosis_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh = solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"].kurt()
kurtosis_Daily_Generation_Plant_end_meter_net_MWh = solar_dataset["Daily Generation Plant end meter (net)MWh"].kurt()
kurtosis_Global_Tilted_Irradiation_Irradiance_GTI = solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].kurt()
kurtosis_Global_horizontal_irradiance_GHI=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].kurt()
kurtosis_Performance_Ratio_PR = solar_dataset["Performance Ratio (PR) %"].kurt()

print(f"Kurtosis ICR-3 - INV1: {kurtosis_ICR3_INV1}")
print(f"Kurtosis ICR-3 - INV2: {kurtosis_ICR3_INV2}")
print(f"Kurtosis ICR-3 - INV3: {kurtosis_ICR3_INV3}")
print(f"Kurtosis ICR-3 - INV4: {kurtosis_ICR3_INV4}")
print(f"Kurtosis ICR-4 - INV1: {kurtosis_ICR4_INV1}")
print(f"Kurtosis ICR-4 - INV2: {kurtosis_ICR4_INV2}")
print(f"Kurtosis ICR-4 - INV3: {kurtosis_ICR4_INV3}")
print(f"Kurtosis ICR-4 - INV4: {kurtosis_ICR4_INV4}")
print(f"Kurtosis Total Daily Integrated Generation MWh: {kurtosis_Total_Daily_Integrated_Generation_MWh}")
print(f"Kurtosis PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: {kurtosis_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH}")
print(f"Kurtosis PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: {kurtosis_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Kurtosis PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: {kurtosis_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh}")
print(f"Kurtosis PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: {kurtosis_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh}")
print(f"Kurtosis PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: {kurtosis_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh}")
print(f"Kurtosis PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: {kurtosis_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh}")
print(f"Kurtosis Daily Generation Plant end meter (net)MWh: {kurtosis_Daily_Generation_Plant_end_meter_net_MWh}")
print(f"Kurtosis Global Tilted Irradiation/Irradiance (GTI)kWh/m2: {kurtosis_Global_Tilted_Irradiation_Irradiance_GTI}")
print(f"Kurtosis Global horizontal irradiance(GHI)kWh/m2: {kurtosis_Global_horizontal_irradiance_GHI}")
print(f"Kurtosis Performance Ratio (PR) %: {kurtosis_Performance_Ratio_PR}")
# output:
# Kurtosis ICR-3 - INV1: 0.3183598869834139
# Kurtosis ICR-3 - INV2: 0.2831808436261385
# Kurtosis ICR-3 - INV3: 0.23773199864191552
# Kurtosis ICR-3 - INV4: 0.3048585495905165
# Kurtosis ICR-4 - INV1: 0.3932378307600741
# Kurtosis ICR-4 - INV2: 0.40055411032706134
# Kurtosis ICR-4 - INV3: 0.351339779240631
# Kurtosis ICR-4 - INV4: 0.3890808134197834
# Kurtosis Total Daily Integrated Generation MWh: 0.4101082893292989
# Kurtosis PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: -0.9248607496600534
# Kurtosis PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: -1.250919847762313
# Kurtosis PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: -0.924276902711779
# Kurtosis PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: -1.2438626492070177
# Kurtosis PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: -0.6638093570813668
# Kurtosis PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: -0.7677507823804834
# Kurtosis Daily Generation Plant end meter (net)MWh: -0.6600559805762996
# Kurtosis Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 0.24647920798701373
# Kurtosis Global horizontal irradiance(GHI)kWh/m2: 0.14812394893113678
# Kurtosis Performance Ratio (PR) %: 0.20858542580860195
# --------------------------------------------------------------------------------
# graphical analysis
# boxplot
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["ICR-3 - INV1"])
plt.title("ICR-3 - INV1")

plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["ICR-3 - INV2"])
plt.title("ICR-3 - INV2")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["ICR-3 - INV3"])
plt.title("ICR-3 - INV3")

plt.subplot(2,3,4)
sns.boxplot(y=solar_dataset["ICR-3 - INV4"])
plt.title("ICR-3 - INV4")

plt.subplot(2,3,5)
sns.boxplot(y=solar_dataset["ICR-4 - INV1"])
plt.title("ICR-4 - INV1")

plt.subplot(2,3,6)
sns.boxplot(y=solar_dataset["ICR-4 - INV2"])
plt.title("ICR-4 - INV2")

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------
plt.figure(figsize=(20,12))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["ICR-4 - INV3"])
plt.title("ICR-4 - INV3")

plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["ICR-4 - INV4"])
plt.title("ICR-4 - INV4")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["Total Daily Integrated Generation MWh"])
plt.title("Total Daily Integrated Generation MWh")

plt.subplot(2,3,4)
sns.boxplot(y=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"])
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH")

plt.subplot(2,3,5)
sns.boxplot(y=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"])
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")

plt.subplot(2,3,6)
sns.boxplot(y=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"])
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh")

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
sns.boxplot(y=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"])
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")

plt.subplot(2,2,2)
sns.boxplot(y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh")

plt.subplot(2,2,3)
sns.boxplot(y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")

plt.subplot(2,2,4)
sns.boxplot(y=solar_dataset["Daily Generation Plant end meter (net)MWh"])
plt.title("Daily Generation Plant end meter (net)MWh")

plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(y=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"])
plt.title("Global Tilted Irradiation/Irradiance (GTI)kWh/m2")


plt.subplot(2,3,2)
sns.boxplot(y=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"])
plt.title("Global horizontal irrradiance (GHI)kMh/m2")

plt.subplot(2,3,3)
sns.boxplot(y=solar_dataset["Performance Ratio (PR) %"])
plt.title("Performance Ratio (PR) %")

plt.tight_layout()
plt.show()


# -------------------------------------------------------------------------------------------
# histogram
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.hist(solar_dataset["ICR-3 - INV1"])
plt.title("ICR-3 - INV1")

plt.subplot(2,3,2)
plt.hist(solar_dataset["ICR-3 - INV2"])
plt.title("ICR-3 - INV2")

plt.subplot(2,3,3)
plt.hist(solar_dataset["ICR-3 - INV3"])
plt.title("ICR-3 - INV3")

plt.subplot(2,3,4)
plt.hist(solar_dataset["ICR-3 - INV4"])
plt.title("ICR-3 - INV4")

plt.subplot(2,3,5)
plt.hist(solar_dataset["ICR-4 - INV1"])
plt.title("ICR-4 - INV1")

plt.subplot(2,3,6)
plt.hist(solar_dataset["ICR-4 - INV2"])
plt.title("ICR-4 - INV2")

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------
plt.figure(figsize=(20,8))
plt.subplot(2,3,1)
plt.hist(solar_dataset["ICR-4 - INV3"])
plt.title("ICR-4 - INV3")

plt.subplot(2,3,2)
plt.hist(solar_dataset["ICR-4 - INV4"])
plt.title("ICR-4 - INV4")

plt.subplot(2,3,3)
plt.hist(solar_dataset["Total Daily Integrated Generation MWh"])
plt.title("Total Daily Integrated Generation MWh")

plt.subplot(2,3,4)
plt.hist(solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"])
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH")

plt.subplot(2,3,5)
plt.hist(solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"])
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")

plt.subplot(2,3,6)
plt.hist(solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"])
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh")

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.hist(solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"])
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")

plt.subplot(2,2,2)
plt.hist(solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh")

plt.subplot(2,2,3)
plt.hist(solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"])
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")

plt.subplot(2,2,4)
plt.hist(solar_dataset["Daily Generation Plant end meter (net)MWh"])
plt.title("Daily Generation Plant end meter (net)MWh")

plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.hist(solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"])
plt.title("Global Tilted Irradiation/Irradiance (GTI)kWh/m2")


plt.subplot(2,3,2)
plt.hist(solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"])
plt.title("Global horizontal irrradiance (GHI)kMh/m2")

plt.subplot(2,3,3)
plt.hist(solar_dataset["Performance Ratio (PR) %"])
plt.title("Performance Ratio (PR) %")

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------------------

# BIVARIATE


import matplotlib.pyplot as plt
import seaborn as sns
# Energy Generation vs. Irradiance:
# Global Tilted Irradiation (GTI), kWh/m² vs. Daily Generation Plant end meter (net), MWh
correlation=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].corr(solar_dataset["Daily Generation Plant end meter (net)MWh"])
print("Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Daily Generation Plant end meter (net)MWh:", correlation)
# output:Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Daily Generation Plant end meter (net)MWh: 0.7476810619580432
plt.scatter(x=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"],y=solar_dataset["Daily Generation Plant end meter (net)MWh"],color="green")
plt.xlabel("Global Tilted Irradiation/Irradiance (GTI) in kWh/m2")
plt.ylabel("Daily Generation Plant end meter (net)MWh")
plt.title("Global Tilted Irradiation (GTI), kWh/m² vs. Daily Generation Plant end meter (net), MWh")
plt.show()

# Global Horizontal Irradiance (GHI), kWh/m² vs. Daily Generation Plant end meter (net), MWh
correlation=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].corr(solar_dataset["Daily Generation Plant end meter (net)MWh"])
print("Correlation between Global horizontal irrradiance (GHI)kMh/m2 and Daily Generation Plant end meter (net)MWh:", correlation)
# output: Correlation between Global horizontal irrradiance (GHI)kMh/m2 and Daily Generation Plant end meter (net)MWh: 0.7027309084124154plt.scatter(x=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"],y=solar_dataset["Daily Generation Plant end meter (net)MWh"],color="green")
plt.xlabel("Global horizontal irrradiance (GHI)kMh/m2")
plt.ylabel("Daily Generation Plant end meter (net)MWh")
plt.title("Global horizontal irrradiance (GHI)kMh/m2 vs. Daily Generation Plant end meter (net), MWh")
plt.show()


# Global Tilted Irradiation/Irradiance (GTI)kWh/m2 vs. Global horizontal irrradiance (GHI)kMh/m2
correlation=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].corr(solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"])
print("Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Global horizontal irrradiance (GHI)kMh/m2:", correlation)
# output: Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Global horizontal irrradiance (GHI)kMh/m2: 0.9478420870159251plt.scatter(x=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"],y=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"],color="green")
plt.xlabel("Global Tilted Irradiation/Irradiance (GTI) in kWh/m2")
plt.ylabel("Global horizontal irrradiance (GHI)kMh/m2")
plt.title("Global Tilted Irradiation (GTI), kWh/m² vs. Global horizontal irrradiance (GHI)kMh/m2")
plt.show()


# Energy Export vs. Energy Import:
# PSS Main Meter (Cumulative Plant end meter reading)(Export), MWh vs. PSS Main Meter (Cumulative Plant end meter reading)(Import), MWh
correlation=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].corr(solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"])
print("Correlation between PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH and PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh:", correlation)
# output : Correlation between PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH and PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 0.9931010425324288plt.scatter(x=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"],y=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"],color="green")
plt.xlabel("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH")
plt.ylabel("PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH vs. PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.show()


# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh vs. PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh
correlation=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].corr(solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"])
print("Correlation between PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh and PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh:", correlation)
# output: Correlation between PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh and PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 0.993175247554434plt.figure(figsize=(12,8))
plt.scatter(x=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"],y=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"],color="green")
plt.xlabel("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh")
plt.ylabel("PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh vs. PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.show()


# PSS Main Meter (Daily Generation Plant end meter)(Export), MWh vs. PSS Main Meter (Daily Generation Plant end meter)(Import), MWh
correlation=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].corr(solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"])
print("Correlation between PSS Main Meter (Daily Generation Plant end meter )(Export)MWh and PSS Main Meter (Daily Generation Plant end meter )(Import)MWh:", correlation)
# output: Correlation between PSS Main Meter (Daily Generation Plant end meter )(Export)MWh and PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.2659988358360408plt.figure(figsize=(12,8))
plt.scatter(x=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"],y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"],color="green")
plt.xlabel("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh")
plt.ylabel("PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh vs. PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")
plt.show()


# Performance Ratio vs. Energy Generation:
# Performance Ratio (PR) % vs. Daily Generation Plant end meter (net), MWh
correlation=solar_dataset["Performance Ratio (PR) %"].corr(solar_dataset["Daily Generation Plant end meter (net)MWh"])
print("Correlation between Performance Ratio (PR) % and Daily Generation Plant end meter (net)MWh:", correlation)
# output: Correlation between Performance Ratio (PR) % and Daily Generation Plant end meter (net)MWh: -0.38427791600376965plt.scatter(x=solar_dataset["Performance Ratio (PR) %"],y=solar_dataset["Daily Generation Plant end meter (net)MWh"],color="green")
plt.xlabel("Performance Ratio (PR) %")
plt.ylabel("Daily Generation Plant end meter (net)MWh")
plt.title("Performance Ratio (PR) % vs. Daily Generation Plant end meter (net)MWh")
plt.show()

# ------------------------------------------------------------------------------------------------------------------
# MULTIVARIATE
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
solar_dataset.columns

columns_of_interest = ['ICR-3 - INV1', 'ICR-3 - INV2', 'ICR-3 - INV3', 'ICR-3 - INV4',
       'ICR-4 - INV1', 'ICR-4 - INV2', 'ICR-4 - INV3', 'ICR-4 - INV4']

# Compute the correlation matrix
correlation_matrix=solar_dataset[columns_of_interest].corr()
# Plot heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation heatmap")
plt.show()


# Energy Generation Influenced by Multiple Factors:
# Daily Generation Plant end meter (net), MWh as the dependent variable.
# Independent variables: Global Tilted Irradiation (GTI), kWh/m², Global Horizontal Irradiance (GHI), kWh/m², Performance Ratio (PR) %
# Select columns of interest
columns_of_interest = ['Daily Generation Plant end meter (net)MWh',
                       'Global Tilted Irradiation/Irradiance (GTI)kWh/m2',
                       'Global horizontal irrradiance (GHI)kMh/m2',
                       'Performance Ratio (PR) %']

# Compute the correlation matrix
correlation_matrix=solar_dataset[columns_of_interest].corr()
# Plot heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation heatmap")
plt.show()
# There is very strong positive correlation (around 0.99) between the variables ICR-3 - INV1, ICR-3 - INV2, ICR-3 - INV3, and ICR-3 - INV4, as indicated by the dark red squares along the diagonal.
# Similarly, the variables ICR-4 - INV1, ICR-4 - INV2, ICR-4 - INV3, and ICR-4 - INV4 also exhibit very strong positive correlation among themselves.
# However, there is a relatively lower but still strong positive correlation (around 0.98) between the ICR-3 and ICR-4 groups of variables.
# No significant negative correlations are observed among the variables considered.



# Cumulative Energy Relationships:
# Dependent variable: Daily Generation Plant end meter (net), MWh
# Independent variables: PSS Main Meter (Cumulative Plant end meter reading)(Export), MWh, PSS Main Meter (Cumulative Plant end meter reading)(Import), MWh, 
#                        PSS Check Meter (Cumulative Plant end meter reading)(Export), MWh, PSS Check Meter (Cumulative Plant end meter reading)(Import), MWh
columns_of_interest = ['Daily Generation Plant end meter (net)MWh',
                       'PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH',
                       'PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh',
                       'PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh',
                       'PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh']

# Compute the correlation matrix
correlation_matrix=solar_dataset[columns_of_interest].corr()
# Plot heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation heatmap")
plt.show()
# The Daily Generation Plant end meter (net)MWh has a moderate positive correlation of 0.77 with all the other variables, indicating that higher daily generation is associated with higher export and import readings across the main and check meters.
# The PSS Main Meter readings for Export and Import have a very strong positive correlation of 0.95, suggesting that the export and import values recorded by the main meter are closely related.
# Similarly, the PSS Check Meter readings for Export and Import also exhibit a strong positive correlation of 0.80, indicating consistency between the export and import values recorded by the check meter.
# The Main Meter and Check Meter readings for both Export and Import show moderate positive correlations (around 0.77), implying a reasonable level of agreement between the main and check meter readings.


# Daily Energy Export and Import Analysis:
# Dependent variable: Daily Generation Plant end meter (net), MWh
# Independent variables: PSS Main Meter (Daily Generation Plant end meter)(Export), MWh, PSS Main Meter (Daily Generation Plant end meter)(Import), MWh
columns_of_interest = ['Daily Generation Plant end meter (net)MWh',
                       'PSS Main Meter (Daily Generation Plant end meter )(Export)MWh',
                       'PSS Main Meter (Daily Generation Plant end meter )(Import)MWh']

# Compute the correlation matrix
correlation_matrix=solar_dataset[columns_of_interest].corr()
# Plot heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation heatmap")
plt.show()
# There is a perfect positive correlation (1.0) between the Daily Generation Plant end meter (net)MWh and the PSS Main Meter (Daily Generation Plant end meter)(Export)MWh. This suggests that the net daily generation is entirely accounted for by the export readings on the main meter.
# There is a very low positive correlation (0.26) between the Daily Generation Plant end meter (net)MWh and the PSS Main Meter (Daily Generation Plant end meter)(Import)MWh. This indicates that the import readings on the main meter are largely independent of the net daily generation.
# There is a moderate negative correlation (-0.54) between the PSS Main Meter (Daily Generation Plant end meter)(Export)MWh and the PSS Main Meter (Daily Generation Plant end meter)(Import)MWh. This suggests that as exports increase, imports tend to decrease, or vice versa, which is an expected relationship in a power generation system.

# Overall Performance
# Dependent variable: Performance Ratio (PR) %
# Independent variables: Global Tilted Irradiation (GTI), kWh/m², Global Horizontal Irradiance (GHI), kWh/m²
columns_of_interest = ['Performance Ratio (PR) %',
                       'Global Tilted Irradiation/Irradiance (GTI)kWh/m2',
                       'Global horizontal irrradiance (GHI)kMh/m2']

# Compute the correlation matrix
correlation_matrix=solar_dataset[columns_of_interest].corr()
# Plot heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation heatmap")
plt.show()
# There is a moderate positive correlation (0.42) between the Performance Ratio (PR) and Global Tilted Irradiation/Irradiance (GTI). This suggests that higher solar irradiation on the tilted surface is associated with a higher performance ratio of the solar plant.
# There is a moderate negative correlation (-0.36) between the Performance Ratio (PR) and Global Horizontal Irradiance (GHI). This indicates that as the horizontal irradiance increases, the performance ratio tends to decrease slightly.
# There is a strong positive correlation (0.95) between Global Tilted Irradiation/Irradiance (GTI) and Global Horizontal Irradiance (GHI). This is an expected relationship, as higher horizontal irradiance generally leads to higher irradiation on the tilted surface.
# -------------------------------------------------------------------------------------------------------------------

