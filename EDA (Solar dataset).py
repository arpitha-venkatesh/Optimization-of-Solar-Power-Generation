# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:11:14 2024

@author: Admin
"""
# loading data to sql
import pandas as pd
from sqlalchemy import create_engine
solar_dataset=pd.read_csv("Solar Dataset.csv",encoding="latin")
engine=create_engine("mysql+pymysql://root:123456@localhost/solar")
solar_dataset.to_sql("solardataset",con=engine,if_exists="replace",index=False)

import pandas as pd
solar_dataset=pd.read_csv("Solar Dataset.csv",encoding="latin")
solar_dataset
solar_dataset.columns
solar_dataset.describe()
solar_dataset.info()
solar_dataset.count()


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
# Mean ICR-3 - INV1: 15.215114942528738
# Mean ICR-3 - INV2: 15.018850574712642
# Mean ICR-3 - INV3: 15.238965517241379
# Mean ICR-3 - INV4: 15.308793103448275
# Mean ICR-4 - INV1: 14.99307471264368
# Mean ICR-4 - INV2: 15.119425287356323
# Mean ICR-4 - INV3: 15.347586206896551
# Mean ICR-4 - INV4: 15.093563218390804
# Mean Total Daily Integrated Generation MWh: 121.37528735632186
# Mean PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 30685.51833333333
# Mean PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 213.03385057471263
# Mean PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 6394.810344827586
# Mean PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 42.422413793103445
# Mean PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 157.63455331412104
# Mean PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.7772910662824208
# Mean Daily Generation Plant end meter (net)MWh: 156.86011527377522
# Mean Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 5.0537068965517244
# Mean Global horizontal irradiance(GHI)kWh/m2: 4.790258620689656
# Mean Performance Ratio (PR) %: 78.8257060518732

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
# Median PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 146.6
# Median PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.61
# Median Daily Generation Plant end meter (net)MWh: 145.97
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
# Variance ICR-3 - INV1: 18.03112880519397
# Variance ICR-3 - INV2: 16.94708801218987
# Variance ICR-3 - INV3: 17.74816953194871
# Variance ICR-3 - INV4: 17.96174724237304
# Variance ICR-4 - INV1: 16.53503345837888
# Variance ICR-4 - INV2: 18.165820994401926
# Variance ICR-4 - INV3: 17.95577859485243
# Variance ICR-4 - INV4: 17.596244327404033
# Variance Total Daily Integrated Generation MWh: 1118.3592146145938
# Variance PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 234632098.35138464
# Variance PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 6251.415223747061
# Variance PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 10185603.312630435
# Variance PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 251.99108118851206
# Variance PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 4437.010782097582
# Variance PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.14119957688527598
# Variance Daily Generation Plant end meter (net)MWh: 4423.114139871065
# Variance Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 2.188774403756334
# Variance Global horizontal irradiance(GHI)kWh/m2: 2.1572192412799365
# Variance Performance Ratio (PR) %: 33.95755752028121


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
# Standard Deviation ICR-3 - INV1: 4.246307667279182
# Standard Deviation ICR-3 - INV2: 4.116684104007723
# Standard Deviation ICR-3 - INV3: 4.212857644396344
# Standard Deviation ICR-3 - INV4: 4.238130158734278
# Standard Deviation ICR-4 - INV1: 4.066329236348046
# Standard Deviation ICR-4 - INV2: 4.262138077819855
# Standard Deviation ICR-4 - INV3: 4.237425939748379
# Standard Deviation ICR-4 - INV4: 4.194787757134327
# Standard Deviation Total Daily Integrated Generation MWh: 33.44187815620698
# Standard Deviation PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 15317.705387928854
# Standard Deviation PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 79.06589165845827
# Standard Deviation PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 3191.489199829828
# Standard Deviation PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 15.874226947744953
# Standard Deviation PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 66.6108908670165
# Standard Deviation PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.37576532155758596
# Standard Deviation Daily Generation Plant end meter (net)MWh: 66.5064969748901
# Standard Deviation Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 1.4794507101476324
# Standard Deviation Global horizontal irradiance(GHI)kWh/m2: 1.468747507667651
# Standard Deviation Performance Ratio (PR) %: 5.827311345747815

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
# Range ICR-3 - INV1: 20.8
# Range ICR-3 - INV2: 20.5
# Range ICR-3 - INV3: 20.8
# Range ICR-3 - INV4: 21.0
# Range ICR-4 - INV1: 20.599999999999998
# Range ICR-4 - INV2: 20.8
# Range ICR-4 - INV3: 21.0
# Range ICR-4 - INV4: 21.0
# Range Total Daily Integrated Generation MWh: 166.1
# Range PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 54699.05
# Range PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 269.5
# Range PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 11399.0
# Range PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 54.0
# Range PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 282.77
# Range PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 1.45
# Range Daily Generation Plant end meter (net)MWh: 281.48
# Range Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 6.68
# Range Global horizontal irradiance(GHI)kWh/m2: 6.99
# Range Performance Ratio (PR) %: 96.39 

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
# Skewness ICR-3 - INV1: -1.24509189698312
# Skewness ICR-3 - INV2: -1.2648080585373485
# Skewness ICR-3 - INV3: -1.2587331281527696
# Skewness ICR-3 - INV4: -1.2495958636718116
# Skewness ICR-4 - INV1: -1.297631203652476
# Skewness ICR-4 - INV2: -1.160202741508104
# Skewness ICR-4 - INV3: -1.2559571356814343
# Skewness ICR-4 - INV4: -1.2300424993374335
# Skewness Total Daily Integrated Generation MWh: -1.256960872398465
# Skewness PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: 0.4515798370603561
# Skewness PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 0.2789482325752936
# Skewness PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: 0.45170925918645344
# Skewness PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 0.297322042826403
# Skewness PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: 0.23561963738550362
# Skewness PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: -0.04939977452891457
# Skewness Daily Generation Plant end meter (net)MWh: 0.23510360624355417
# Skewness Global Tilted Irradiation/Irradiance (GTI)kWh/m2: -1.0729819343139249
# Skewness Global horizontal irradiance(GHI)kWh/m2: -0.6699031762163137
# Skewness Performance Ratio (PR) %: -6.959567200378571


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
# Kurtosis ICR-3 - INV1: 1.3446340618568873
# Kurtosis ICR-3 - INV2: 1.5030851871291335
# Kurtosis ICR-3 - INV3: 1.4328471527914917
# Kurtosis ICR-3 - INV4: 1.4083068317680083
# Kurtosis ICR-4 - INV1: 1.6756292026060104
# Kurtosis ICR-4 - INV2: 1.2469905521030396
# Kurtosis ICR-4 - INV3: 1.4286702557301445
# Kurtosis ICR-4 - INV4: 1.4636462202642249
# Kurtosis Total Daily Integrated Generation MWh: 1.4783686869217942
# Kurtosis PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH: -0.9248607496600543
# Kurtosis PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: -1.2509198477623127
# Kurtosis PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh: -0.9242769027117781
# Kurtosis PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: -1.2438626492070177
# Kurtosis PSS Main Meter (Daily Generation Plant end meter )(Export)MWh: -0.6705754064132812
# Kurtosis PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: -0.7742224683769399
# Kurtosis Daily Generation Plant end meter (net)MWh: -0.6668326595144953
# Kurtosis Global Tilted Irradiation/Irradiance (GTI)kWh/m2: 0.844353740029077
# Kurtosis Global horizontal irradiance(GHI)kWh/m2: 0.28727514478129024
# Kurtosis Performance Ratio (PR) %: 96.55036499954561
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
# output: Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Daily Generation Plant end meter (net)MWh: 0.7488357462339688
plt.scatter(x=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"],y=solar_dataset["Daily Generation Plant end meter (net)MWh"],color="green")
plt.xlabel("Global Tilted Irradiation/Irradiance (GTI) in kWh/m2")
plt.ylabel("Daily Generation Plant end meter (net)MWh")
plt.title("Global Tilted Irradiation (GTI), kWh/m² vs. Daily Generation Plant end meter (net), MWh")
plt.show()
# The correlation coefficient is approximately 0.75. This indicates a strong positive correlation between GTI (kWh/m²) and the Daily Generation Plant's net meter readings (MWh). 
# As the GTI increases, the daily generation tends to increase as well.
# Overall, the data indicates that GTI is a significant factor in determining the plant's daily energy generation, 
# and efforts to maximize GTI capture could directly enhance energy output.


# Global Horizontal Irradiance (GHI), kWh/m² vs. Daily Generation Plant end meter (net), MWh
correlation=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"].corr(solar_dataset["Daily Generation Plant end meter (net)MWh"])
print("Correlation between Global horizontal irrradiance (GHI)kMh/m2 and Daily Generation Plant end meter (net)MWh:", correlation)
# output: Correlation between Global horizontal irrradiance (GHI)kMh/m2 and Daily Generation Plant end meter (net)MWh: 0.7067005546698554
plt.scatter(x=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"],y=solar_dataset["Daily Generation Plant end meter (net)MWh"],color="green")
plt.xlabel("Global horizontal irrradiance (GHI)kMh/m2")
plt.ylabel("Daily Generation Plant end meter (net)MWh")
plt.title("Global horizontal irrradiance (GHI)kMh/m2 vs. Daily Generation Plant end meter (net), MWh")
plt.show()
# The scatter plot shows a positive correlation between global horizontal irradiance (GHI) and daily generation at the power plant. 
# As the GHI increases, the daily generation also tends to increase. 
# This makes sense because higher solar irradiance means more energy is available to be converted into electricity by the solar power plant.
# The correlation coefficient of around 0.71 indicates a fairly strong positive linear relationship between the two variables. However,
# there is still some scatter in the data points, suggesting that other factors besides just GHI also influence the daily generation output.


# Global Tilted Irradiation/Irradiance (GTI)kWh/m2 vs. Global horizontal irrradiance (GHI)kMh/m2
correlation=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"].corr(solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"])
print("Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Global horizontal irrradiance (GHI)kMh/m2:", correlation)
# output: Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Global horizontal irrradiance (GHI)kMh/m2: 0.9498249969521289
plt.scatter(x=solar_dataset["Global Tilted Irradiation/Irradiance (GTI)kWh/m2"],y=solar_dataset["Global horizontal irrradiance (GHI)kMh/m2"],color="green")
plt.xlabel("Global Tilted Irradiation/Irradiance (GTI) in kWh/m2")
plt.ylabel("Global horizontal irrradiance (GHI)kMh/m2")
plt.title("Global Tilted Irradiation (GTI), kWh/m² vs. Global horizontal irrradiance (GHI)kMh/m2")
plt.show()
# The scatter plot shows a strong positive correlation between Global Tilted Irradiation (GTI) in kWh/m2 and 
# Global Horizontal Irradiance (GHI) in kMh/m2. The data points closely follow a linear trend, indicating that as GHI increases, 
# GTI also tends to increase proportionally. The calculated correlation coefficient of approximately 0.95 confirms this strong linear 
# relationship between the two variables.


# Energy Export vs. Energy Import:
# PSS Main Meter (Cumulative Plant end meter reading)(Export), MWh vs. PSS Main Meter (Cumulative Plant end meter reading)(Import), MWh
correlation=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"].corr(solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"])
print("Correlation between PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH and PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh:", correlation)
# output : Correlation between PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH and PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 0.9931010425324288
plt.figure(figsize=(12,8))
plt.scatter(x=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH"],y=solar_dataset["PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh"],color="green")
plt.xlabel("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH")
plt.ylabel("PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.title("PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH vs. PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.show()
# The scatter plot shows an extremely strong positive correlation (correlation coefficient of 0.993) between the cumulative energy exported 
# from the power plant and the cumulative energy imported into the plant.
# This near perfect linear relationship suggests that the amount of energy imported is directly proportional to the amount exported over time, 
# likely due to the need to import some energy from the grid to support plant operations and energy losses, even as the plant is exporting energy 
# generated from solar. The tight clustering of data points along the line indicates this relationship holds consistently across the observed period.


# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh vs. PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh
correlation=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"].corr(solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"])
print("Correlation between PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh and PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh:", correlation)
# output: Correlation between PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh and PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 0.993175247554434
plt.figure(figsize=(12,8))
plt.scatter(x=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh"],y=solar_dataset["PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh"],color="green")
plt.xlabel("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh")
plt.ylabel("PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.title("PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh vs. PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh")
plt.show()
# The scatter plot shows an extremely strong positive correlation (correlation coefficient of around 0.993) between the cumulative energy 
# exported from the plant according to the PSS Check Meter and the cumulative energy imported into the plant according to the same meter. 
# The data points align almost perfectly along a straight line, indicating that the amount of energy imported is directly proportional to 
# the amount exported over time. This near 1:1 linear relationship suggests that the Check Meter readings for import and export are consistent 
# and reliable measures of the actual energy flows in and out of the plant. The tight clustering of points confirms this relationship holds 
# robustly across the observed period.


# PSS Main Meter (Daily Generation Plant end meter)(Export), MWh vs. PSS Main Meter (Daily Generation Plant end meter)(Import), MWh
correlation=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"].corr(solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"])
print("Correlation between PSS Main Meter (Daily Generation Plant end meter )(Export)MWh and PSS Main Meter (Daily Generation Plant end meter )(Import)MWh:", correlation)
# output: Correlation between PSS Main Meter (Daily Generation Plant end meter )(Export)MWh and PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.26599883583604084
plt.figure(figsize=(12,8))
plt.scatter(x=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Export)MWh"],y=solar_dataset["PSS Main Meter (Daily Generation Plant end meter )(Import)MWh"],color="green")
plt.xlabel("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh")
plt.ylabel("PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")
plt.title("PSS Main Meter (Daily Generation Plant end meter )(Export)MWh vs. PSS Main Meter (Daily Generation Plant end meter )(Import)MWh")
plt.show()
# The scatter plot shows a weak positive correlation (correlation coefficient of around 0.266) between the daily energy exported from the plant 
# and the daily energy imported into the plant, as measured by the PSS Main Meter. While there is an overall positive trend, the data points are 
# scattered and do not align closely to a straight line. This suggests that the daily import and export values do not have a consistent linear 
# relationship like the cumulative values did.



# Performance Ratio vs. Energy Generation:
# Performance Ratio (PR) % vs. Daily Generation Plant end meter (net), MWh
correlation=solar_dataset["Performance Ratio (PR) %"].corr(solar_dataset["Daily Generation Plant end meter (net)MWh"])
print("Correlation between Performance Ratio (PR) % and Daily Generation Plant end meter (net)MWh:", correlation)
# output: Correlation between Performance Ratio (PR) % and Daily Generation Plant end meter (net)MWh: -0.17921610115237563
plt.scatter(x=solar_dataset["Performance Ratio (PR) %"],y=solar_dataset["Daily Generation Plant end meter (net)MWh"],color="green")
plt.xlabel("Performance Ratio (PR) %")
plt.ylabel("Daily Generation Plant end meter (net)MWh")
plt.title("Performance Ratio (PR) % vs. Daily Generation Plant end meter (net)MWh")
plt.show()
# the scatter plot shows a weak negative correlation (around -0.18) between the Performance Ratio percentage and 
# the Daily Generation Plant end meter net output. While there is an overall downward trend, the data points are quite scattered, 
# suggesting other factors beyond just the Performance Ratio significantly influence the daily net generation. 
# The relationship is modest and inconsistent across all data points.

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
