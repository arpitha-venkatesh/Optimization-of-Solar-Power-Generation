create database solar;
use solar;
select * from solardataset;

describe solardataset;

-- EDA(EXPLORATORY DATA ANALYSIS):
-- 1ST MOMENT BUSINESS DECISION:
-- MEAN:
SELECT 
    round(AVG(`ICR-3 - INV1`), 3) AS mean_ICR3_INV1,
    round(AVG(`ICR-3 - INV2`), 3) AS mean_ICR3_INV2,
    round(AVG(`ICR-3 - INV3`), 3) AS mean_ICR3_INV3,
    round(AVG(`ICR-3 - INV4`), 3) AS mean_ICR3_INV4,
    round(AVG(`ICR-4 - INV1`), 3) AS mean_ICR4_INV1,
    round(AVG(`ICR-4 - INV2`), 3) AS mean_ICR4_INV2,
    round(AVG(`ICR-4 - INV3`), 3) AS mean_ICR4_INV3,
    round(AVG(`ICR-4 - INV4`), 3) AS mean_ICR4_INV4,
    round(AVG(`Total Daily Integrated Generation MWh`), 3) AS mean_Total_Daily_Integrated_Generation_MWh,
    round(AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh,
    round(AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(AVG(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`), 3) AS mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(AVG(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`), 3) AS mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(AVG(`Daily Generation Plant end meter (net)MWh`), 3) AS mean_Daily_Generation_Plant_end_meter_net_MWh,
    round(AVG(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`), 3) AS mean_Global_Tilted_Irradiation_Irradiance_GTI,
    round(AVG(`Global horizontal irrradiance (GHI)kMh/m2`), 3) AS mean_Global_horizontal_irradiance_GHI,
    round(AVG(`Performance Ratio (PR) %`), 3) AS mean_Performance_Ratio_PR
FROM solardataset;
-- output
-- mean_ICR3_INV1 :15.215
-- mean_ICR3_INV2 :15.019
-- mean_ICR3_INV3 :15.239
-- mean_ICR3_INV4 :15.309
-- mean_ICR4_INV1 :14.993
-- mean_ICR4_INV2 :15.119
-- mean_ICR4_INV3 :15.348
-- mean_ICR4_INV4 :15.094
-- mean_Total_Daily_Integrated_Generation_MWh :121.375
-- mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH :30685.518
-- mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh :213.034
-- mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh :6394.81
-- mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh :42.422
-- mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh :157.635
-- mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh :0.777
-- mean_Daily_Generation_Plant_end_meter_net_MWh :156.86
-- mean_Global_Tilted_Irradiation_Irradiance_GTI :5.054
-- mean_Global_horizontal_irradiance_GHI :4.79
-- mean_Performance_Ratio_PR : 78.826

-- -------------------------------------------------------------------------------------------
-- MEDIAN:
WITH CTE AS (
    SELECT `ICR-3 - INV1`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-3 - INV1`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-3 - INV1`), 3) AS median_ICR3_INV1 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR3_INV1 : 15.72

WITH CTE AS (
    SELECT `ICR-3 - INV2`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-3 - INV2`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-3 - INV2`), 3) AS median_ICR3_INV2 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR3_INV2 : 15.52

WITH CTE AS (
    SELECT `ICR-3 - INV3`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-3 - INV3`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-3 - INV3`), 3) AS median_ICR3_INV3 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR3_INV3 : 15.77

WITH CTE AS (
    SELECT `ICR-3 - INV4`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-3 - INV4`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-3 - INV4`), 3) AS median_ICR3_INV4 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR3_INV4 : 15.92

WITH CTE AS (
    SELECT `ICR-4 - INV1`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-4 - INV1`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-4 - INV1`), 3) AS median_ICR4_INV1 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR4_INV1:15.62

WITH CTE AS (
    SELECT `ICR-4 - INV2`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-4 - INV2`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-4 - INV2`), 3) AS median_ICR4_INV2 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR4_INV2 : 15.62

WITH CTE AS (
    SELECT `ICR-4 - INV3`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-4 - INV3`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-4 - INV3`), 3) AS median_ICR4_INV3 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR4_INV3 : 15.92

WITH CTE AS (
    SELECT `ICR-4 - INV4`, 
           ROW_NUMBER() OVER (ORDER BY `ICR-4 - INV4`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`ICR-4 - INV4`), 3) AS median_ICR4_INV4 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_ICR4_INV4 : 15.67

WITH CTE AS (
    SELECT `Total Daily Integrated Generation MWh`, 
           ROW_NUMBER() OVER (ORDER BY `Total Daily Integrated Generation MWh`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`Total Daily Integrated Generation MWh`), 3) AS median_Total_Daily_Integrated_Generation_MWh 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_Total_Daily_Integrated_Generation_MWh : 125.7

WITH CTE AS (
    SELECT `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`, 
           ROW_NUMBER() OVER (ORDER BY `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : 27231.67

WITH CTE AS (
    SELECT `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`, 
           ROW_NUMBER() OVER (ORDER BY `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh  : 189.895

WITH CTE AS (
    SELECT `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`, 
           ROW_NUMBER() OVER (ORDER BY `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWH 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWH  : 5675

WITH CTE AS (
    SELECT `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`, 
           ROW_NUMBER() OVER (ORDER BY `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 38

WITH CTE AS (
    SELECT `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`, 
           ROW_NUMBER() OVER (ORDER BY `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`), 3) AS median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
--  median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh : 145.06

WITH CTE AS (
    SELECT `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`, 
           ROW_NUMBER() OVER (ORDER BY `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`), 3) AS median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh : 0.61

WITH CTE AS (
    SELECT `Daily Generation Plant end meter (net)MWh`, 
           ROW_NUMBER() OVER (ORDER BY `Daily Generation Plant end meter (net)MWh`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`Daily Generation Plant end meter (net)MWh`), 3) AS median_Daily_Generation_Plant_end_meter_net_MWh 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_Daily_Generation_Plant_end_meter_net_MWh : 144.485

WITH CTE AS (
    SELECT `Global Tilted Irradiation/Irradiance (GTI)kWh/m2`, 
           ROW_NUMBER() OVER (ORDER BY `Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`), 3) AS median_Global_Tilted_Irradiation_Irradiance_GTI 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_Global_Tilted_Irradiation_Irradiance_GTI : 5.265

WITH CTE AS (
    SELECT `Global horizontal irrradiance (GHI)kMh/m2`, 
           ROW_NUMBER() OVER (ORDER BY `Global horizontal irrradiance (GHI)kMh/m2`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`Global horizontal irrradiance (GHI)kMh/m2`), 3) AS median_Global_horizontal_irradiance_GHI 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_Global_horizontal_irradiance_GHI : 4.77

WITH CTE AS (
    SELECT `Performance Ratio (PR) %`, 
           ROW_NUMBER() OVER (ORDER BY `Performance Ratio (PR) %`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
SELECT ROUND(AVG(`Performance Ratio (PR) %`), 3) AS median_Performance_Ratio_PR 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));
-- median_Performance_Ratio_PR : 78.25

-- ---------------------------------------------------------------------------------------------
-- MODE:
WITH CTE AS(
SELECT *,COUNT(`Remarks`) OVER (PARTITION BY `Remarks`) AS ranked
FROM solardataset )
SELECT DISTINCT(`Remarks`) AS mode_Remarks
FROM CTE 
WHERE ranked = (SELECT MAX(ranked) FROM CTE);
-- mode_Remarks : Weather was Partially Cloudy

-- ---------------------------------------------------------------------------------------------
-- SECOND MOMENT BUSSINESS UNDERSTANDING 
-- VARIANCE 
SELECT 
    round(VAR_SAMP(`ICR-3 - INV1`), 3) AS variance_ICR3_INV1,
    round(VAR_SAMP(`ICR-3 - INV2`), 3) AS variance_ICR3_INV2,
    round(VAR_SAMP(`ICR-3 - INV3`), 3) AS variance_ICR3_INV3,
    round(VAR_SAMP(`ICR-3 - INV4`), 3) AS variance_ICR3_INV4,
    round(VAR_SAMP(`ICR-4 - INV1`), 3) AS variance_ICR4_INV1,
    round(VAR_SAMP(`ICR-4 - INV2`), 3) AS variance_ICR4_INV2,
    round(VAR_SAMP(`ICR-4 - INV3`), 3) AS variance_ICR4_INV3,
    round(VAR_SAMP(`ICR-4 - INV4`), 3) AS variance_ICR4_INV4,
    round(VAR_SAMP(`Total Daily Integrated Generation MWh`), 3) AS variance_Total_Daily_Integrated_Generation_MWh,
    round(VAR_SAMP(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(VAR_SAMP(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(VAR_SAMP(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh,
    round(VAR_SAMP(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(VAR_SAMP(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`), 3) AS variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(VAR_SAMP(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`), 3) AS variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(VAR_SAMP(`Daily Generation Plant end meter (net)MWh`), 3) AS variance_Daily_Generation_Plant_end_meter_net_MWh,
    round(VAR_SAMP(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`), 3) AS variance_Global_Tilted_Irradiation_Irradiance_GTI,
    round(VAR_SAMP(`Global horizontal irrradiance (GHI)kMh/m2`), 3) AS variance_Global_horizontal_irradiance_GHI,
    round(VAR_SAMP(`Performance Ratio (PR) %`), 3) AS variance_Performance_Ratio_PR
FROM solardataset;
-- output 																		
-- variance_ICR3_INV1 : 18.031
-- variance_ICR3_INV2 : 16.947
-- variance_ICR3_INV3 : 17.748
-- variance_ICR3_INV4 : 17.962
-- variance_ICR4_INV1 : 16.535
-- variance_ICR4_INV2 : 18.166
-- variance_ICR4_INV3 : 17.956
-- variance_ICR4_INV4 : 17.596
-- variance_Total_Daily_Integrated_Generation_MWh : 1118.359
-- variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : 234632098.351
-- variance_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 6251.415
-- variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh : 10185603.313
-- variance_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 251.991
-- variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh : 4437.011
-- variance_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh : 0.141
-- variance_Daily_Generation_Plant_end_meter_net_MWh : 4423.114
-- variance_Global_Tilted_Irradiation_Irradiance_GTI : 2.189
-- variance_Global_horizontal_irradiance_GHI : 2.157
-- variance_Performance_Ratio_PR : 33.958

-- ---------------------------------------------------------------------------------
-- STANDARD DEVIATION
SELECT 
    round(STDDEV_SAMP(`ICR-3 - INV1`), 3) AS stddev_ICR3_INV1,
    round(STDDEV_SAMP(`ICR-3 - INV2`), 3) AS stddev_ICR3_INV2,
    round(STDDEV_SAMP(`ICR-3 - INV3`), 3) AS stddev_ICR3_INV3,
    round(STDDEV_SAMP(`ICR-3 - INV4`), 3) AS stddev_ICR3_INV4,
    round(STDDEV_SAMP(`ICR-4 - INV1`), 3) AS stddev_ICR4_INV1,
    round(STDDEV_SAMP(`ICR-4 - INV2`), 3) AS stddev_ICR4_INV2,
    round(STDDEV_SAMP(`ICR-4 - INV3`), 3) AS stddev_ICR4_INV3,
    round(STDDEV_SAMP(`ICR-4 - INV4`), 3) AS stddev_ICR4_INV4,
    round(STDDEV_SAMP(`Total Daily Integrated Generation MWh`), 3) AS stddev_Total_Daily_Integrated_Generation_MWh,
    round(STDDEV_SAMP(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS stddev_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(STDDEV_SAMP(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS stddev_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(STDDEV_SAMP(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS stddev_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh,
    round(STDDEV_SAMP(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS stddev_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(STDDEV_SAMP(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`), 3) AS stddev_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(STDDEV_SAMP(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`), 3) AS stddev_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(STDDEV_SAMP(`Daily Generation Plant end meter (net)MWh`), 3) AS stddev_Daily_Generation_Plant_end_meter_net_MWh,
    round(STDDEV_SAMP(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`), 3) AS stddev_Global_Tilted_Irradiation_Irradiance_GTI,
    round(STDDEV_SAMP(`Global horizontal irrradiance (GHI)kMh/m2`), 3) AS stddev_Global_horizontal_irradiance_GHI,
    round(STDDEV_SAMP(`Performance Ratio (PR) %`), 3) AS stddev_Performance_Ratio_PR
FROM solardataset;
-- output 																		
-- stddev_ICR3_INV1 : 4.246
-- stddev_ICR3_INV2 : 4.117
-- stddev_ICR3_INV3 : 4.213
-- stddev_ICR3_INV4 : 4.238
-- stddev_ICR4_INV1 : 4.066
-- stddev_ICR4_INV2 : 4.262
-- stddev_ICR4_INV3 : 4.237
-- stddev_ICR4_INV4 : 4.195
-- stddev_Total_Daily_Integrated_Generation_MWh : 33.442
-- stddev_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : 15317.705
-- stddev_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 79.066
-- stddev_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh : 3191.489
-- stddev_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 15.874
-- stddev_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh : 66.611
-- stddev_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh : 0.376
-- stddev_Daily_Generation_Plant_end_meter_net_MWh : 66.506
-- stddev_Global_Tilted_Irradiation_Irradiance_GTI : 1.479
-- stddev_Global_horizontal_irradiance_GHI : 1.469
-- stddev_Performance_Ratio_PR : 5.827

-- --------------------------------------------------------------------------
-- RANGE
SELECT 
    round(MAX(`ICR-3 - INV1`) - MIN(`ICR-3 - INV1`), 3) AS range_ICR3_INV1,
    round(MAX(`ICR-3 - INV2`) - MIN(`ICR-3 - INV2`), 3) AS range_ICR3_INV2,
    round(MAX(`ICR-3 - INV3`) - MIN(`ICR-3 - INV3`), 3) AS range_ICR3_INV3,
    round(MAX(`ICR-3 - INV4`) - MIN(`ICR-3 - INV4`), 3) AS range_ICR3_INV4,
    round(MAX(`ICR-4 - INV1`) - MIN(`ICR-4 - INV1`), 3) AS range_ICR4_INV1,
    round(MAX(`ICR-4 - INV2`) - MIN(`ICR-4 - INV2`), 3) AS range_ICR4_INV2,
    round(MAX(`ICR-4 - INV3`) - MIN(`ICR-4 - INV3`), 3) AS range_ICR4_INV3,
    round(MAX(`ICR-4 - INV4`) - MIN(`ICR-4 - INV4`), 3) AS range_ICR4_INV4,
    round(MAX(`Total Daily Integrated Generation MWh`) - MIN(`Total Daily Integrated Generation MWh`), 3) AS range_Total_Daily_Integrated_Generation_MWh,
    round(MAX(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) - MIN(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(MAX(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) - MIN(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(MAX(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) - MIN(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`), 3) AS range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh,
    round(MAX(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) - MIN(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`), 3) AS range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(MAX(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) - MIN(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`), 3) AS range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(MAX(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) - MIN(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`), 3) AS range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(MAX(`Daily Generation Plant end meter (net)MWh`) - MIN(`Daily Generation Plant end meter (net)MWh`), 3) AS range_Daily_Generation_Plant_end_meter_net_MWh,
    round(MAX(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) - MIN(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`), 3) AS range_Global_Tilted_Irradiation_Irradiance_GTI,
    round(MAX(`Global horizontal irrradiance (GHI)kMh/m2`) - MIN(`Global horizontal irrradiance (GHI)kMh/m2`), 3) AS range_Global_horizontal_irradiance_GHI,
    round(MAX(`Performance Ratio (PR) %`) - MIN(`Performance Ratio (PR) %`), 3) AS range_Performance_Ratio_PR
FROM solardataset;
-- output 																		
-- range_ICR3_INV1 : 20.8
-- range_ICR3_INV2 : 20.5
-- range_ICR3_INV3 : 20.8
-- range_ICR3_INV4 : 21
-- range_ICR4_INV1 : 20.6
-- range_ICR4_INV2 : 20.8
-- range_ICR4_INV3 : 21
-- range_ICR4_INV4 : 21
-- range_Total_Daily_Integrated_Generation_MWh : 166.1
-- range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : 54699.05
-- range_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 269.5
-- range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh : 11399
-- range_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 54
-- range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh : 282.77
-- range_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh : 1.45
-- range_Daily_Generation_Plant_end_meter_net_MWh : 281.48
-- range_Global_Tilted_Irradiation_Irradiance_GTI : 6.68
-- range_Global_horizontal_irradiance_GHI : 6.99
-- range_Performance_Ratio_PR : 96.39

-- -------------------------------------------------------------------------------------
-- THIRD MOMENT BUSINESS UNDERSTANDING
-- SKEWNESS
SELECT 
    round(SUM(POWER(`ICR-3 - INV1` - (SELECT AVG(`ICR-3 - INV1`) FROM solardataset), 3)) / COUNT(`ICR-3 - INV1`) / POWER((SELECT STD(`ICR-3 - INV1`) FROM solardataset), 3), 3) AS skewness_ICR3_INV1,
    round(SUM(POWER(`ICR-3 - INV2` - (SELECT AVG(`ICR-3 - INV2`) FROM solardataset), 3)) / COUNT(`ICR-3 - INV2`) / POWER((SELECT STD(`ICR-3 - INV2`) FROM solardataset), 3), 3) AS skewness_ICR3_INV2,
    round(SUM(POWER(`ICR-3 - INV3` - (SELECT AVG(`ICR-3 - INV3`) FROM solardataset), 3)) / COUNT(`ICR-3 - INV3`) / POWER((SELECT STD(`ICR-3 - INV3`) FROM solardataset), 3), 3) AS skewness_ICR3_INV3,
    round(SUM(POWER(`ICR-3 - INV4` - (SELECT AVG(`ICR-3 - INV4`) FROM solardataset), 3)) / COUNT(`ICR-3 - INV4`) / POWER((SELECT STD(`ICR-3 - INV4`) FROM solardataset), 3), 3) AS skewness_ICR3_INV4,
    round(SUM(POWER(`ICR-4 - INV1` - (SELECT AVG(`ICR-4 - INV1`) FROM solardataset), 3)) / COUNT(`ICR-4 - INV1`) / POWER((SELECT STD(`ICR-4 - INV1`) FROM solardataset), 3), 3) AS skewness_ICR4_INV1,
    round(SUM(POWER(`ICR-4 - INV2` - (SELECT AVG(`ICR-4 - INV2`) FROM solardataset), 3)) / COUNT(`ICR-4 - INV2`) / POWER((SELECT STD(`ICR-4 - INV2`) FROM solardataset), 3), 3) AS skewness_ICR4_INV2,
    round(SUM(POWER(`ICR-4 - INV3` - (SELECT AVG(`ICR-4 - INV3`) FROM solardataset), 3)) / COUNT(`ICR-4 - INV3`) / POWER((SELECT STD(`ICR-4 - INV3`) FROM solardataset), 3), 3) AS skewness_ICR4_INV3,
    round(SUM(POWER(`ICR-4 - INV4` - (SELECT AVG(`ICR-4 - INV4`) FROM solardataset), 3)) / COUNT(`ICR-4 - INV4`) / POWER((SELECT STD(`ICR-4 - INV4`) FROM solardataset), 3), 3) AS skewness_ICR4_INV4,
    round(SUM(POWER(`Total Daily Integrated Generation MWh` - (SELECT AVG(`Total Daily Integrated Generation MWh`) FROM solardataset), 3)) / COUNT(`Total Daily Integrated Generation MWh`) / POWER((SELECT STD(`Total Daily Integrated Generation MWh`) FROM solardataset), 3), 3) AS skewness_Total_Daily_Integrated_Generation_MWh,
    round(SUM(POWER(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` - (SELECT AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 3)) / COUNT(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) / POWER((SELECT STD(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 3), 3) AS skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(SUM(POWER(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` - (SELECT AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 3)) / COUNT(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) / POWER((SELECT STD(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 3), 3) AS skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(SUM(POWER(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH` - (SELECT AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 3)) / COUNT(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) / POWER((SELECT STD(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 3), 3) AS skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh,
    round(SUM(POWER(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` - (SELECT AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 3)) / COUNT(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) / POWER((SELECT STD(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 3), 3) AS skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(SUM(POWER(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` - (SELECT AVG(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) FROM solardataset), 3)) / COUNT(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) / POWER((SELECT STD(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) FROM solardataset), 3), 3) AS skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(SUM(POWER(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` - (SELECT AVG(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) FROM solardataset), 3)) / COUNT(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) / POWER((SELECT STD(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) FROM solardataset), 3), 3) AS skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(SUM(POWER(`Daily Generation Plant end meter (net)MWh` - (SELECT AVG(`Daily Generation Plant end meter (net)MWh`) FROM solardataset), 3)) / COUNT(`Daily Generation Plant end meter (net)MWh`) / POWER((SELECT STD(`Daily Generation Plant end meter (net)MWh`) FROM solardataset), 3), 3) AS skewness_Daily_Generation_Plant_end_meter_net_MWh,
    round(SUM(POWER(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` - (SELECT AVG(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) FROM solardataset), 3)) / COUNT(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) / POWER((SELECT STD(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) FROM solardataset), 3), 3) AS skewness_Global_Tilted_Irradiation_Irradiance_GTI,
    round(SUM(POWER(`Global horizontal irrradiance (GHI)kMh/m2` - (SELECT AVG(`Global horizontal irrradiance (GHI)kMh/m2`) FROM solardataset), 3)) / COUNT(`Global horizontal irrradiance (GHI)kMh/m2`) / POWER((SELECT STD(`Global horizontal irrradiance (GHI)kMh/m2`) FROM solardataset), 3), 3) AS skewness_Global_horizontal_irradiance_GHI,
    round(SUM(POWER(`Performance Ratio (PR) %` - (SELECT AVG(`Performance Ratio (PR) %`) FROM solardataset), 3)) / COUNT(`Performance Ratio (PR) %`) / POWER((SELECT STD(`Performance Ratio (PR) %`) FROM solardataset), 3), 3) AS skewness_Performance_Ratio_PR
FROM solardataset;
-- output 																		
-- skewness_ICR3_INV1 : -1.24
-- skewness_ICR3_INV2 : -1.259
-- skewness_ICR3_INV3 : -1.253
-- skewness_ICR3_INV4 : -1.244
-- skewness_ICR4_INV1 : -1.292
-- skewness_ICR4_INV2 : -1.155
-- skewness_ICR4_INV3 : -1.251
-- skewness_ICR4_INV4 : -1.225
-- skewness_Total_Daily_Integrated_Generation_MWh : -1.252
-- skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : 0.45
-- skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 0.278
-- skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : 0.45
-- skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : 0.296
-- skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh : 0.235
-- skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh : -0.049
-- skewness_Daily_Generation_Plant_end_meter_net_MWh : 0.234
-- skewness_Global_Tilted_Irradiation_Irradiance_GTI : -1.068
-- skewness_Global_horizontal_irradiance_GHI : -0.667
-- skewness_Performance_Ratio_PR : -6.929

-- ----------------------------------------------------------------------------------------------------------
-- FOURTH MOMENT BUSINESSS UNDERSTANDING 
-- KURTOSIS
SELECT 
    round(SUM(POWER(`ICR-3 - INV1` - (SELECT AVG(`ICR-3 - INV1`) FROM solardataset), 4)) / COUNT(`ICR-3 - INV1`) / POWER((SELECT STD(`ICR-3 - INV1`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR3_INV1,
    round(SUM(POWER(`ICR-3 - INV2` - (SELECT AVG(`ICR-3 - INV2`) FROM solardataset), 4)) / COUNT(`ICR-3 - INV2`) / POWER((SELECT STD(`ICR-3 - INV2`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR3_INV2,
    round(SUM(POWER(`ICR-3 - INV3` - (SELECT AVG(`ICR-3 - INV3`) FROM solardataset), 4)) / COUNT(`ICR-3 - INV3`) / POWER((SELECT STD(`ICR-3 - INV3`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR3_INV3,
    round(SUM(POWER(`ICR-3 - INV4` - (SELECT AVG(`ICR-3 - INV4`) FROM solardataset), 4)) / COUNT(`ICR-3 - INV4`) / POWER((SELECT STD(`ICR-3 - INV4`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR3_INV4,
    round(SUM(POWER(`ICR-4 - INV1` - (SELECT AVG(`ICR-4 - INV1`) FROM solardataset), 4)) / COUNT(`ICR-4 - INV1`) / POWER((SELECT STD(`ICR-4 - INV1`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR4_INV1,
    round(SUM(POWER(`ICR-4 - INV2` - (SELECT AVG(`ICR-4 - INV2`) FROM solardataset), 4)) / COUNT(`ICR-4 - INV2`) / POWER((SELECT STD(`ICR-4 - INV2`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR4_INV2,
    round(SUM(POWER(`ICR-4 - INV3` - (SELECT AVG(`ICR-4 - INV3`) FROM solardataset), 4)) / COUNT(`ICR-4 - INV3`) / POWER((SELECT STD(`ICR-4 - INV3`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR4_INV3,
    round(SUM(POWER(`ICR-4 - INV4` - (SELECT AVG(`ICR-4 - INV4`) FROM solardataset), 4)) / COUNT(`ICR-4 - INV4`) / POWER((SELECT STD(`ICR-4 - INV4`) FROM solardataset), 4) - 3, 3) AS kurtosis_ICR4_INV4,
    round(SUM(POWER(`Total Daily Integrated Generation MWh` - (SELECT AVG(`Total Daily Integrated Generation MWh`) FROM solardataset), 4)) / COUNT(`Total Daily Integrated Generation MWh`) / POWER((SELECT STD(`Total Daily Integrated Generation MWh`) FROM solardataset), 4) - 3, 3) AS kurtosis_Total_Daily_Integrated_Generation_MWh,
    round(SUM(POWER(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` - (SELECT AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 4)) / COUNT(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) / POWER((SELECT STD(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 4) - 3, 3) AS kurtosis_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(SUM(POWER(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` - (SELECT AVG(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 4)) / COUNT(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) / POWER((SELECT STD(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 4) - 3, 3) AS kurtosis_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(SUM(POWER(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH` - (SELECT AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 4)) / COUNT(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) / POWER((SELECT STD(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`) FROM solardataset), 4) - 3, 3) AS kurtosis_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWH,
    round(SUM(POWER(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` - (SELECT AVG(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 4)) / COUNT(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) / POWER((SELECT STD(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) FROM solardataset), 4) - 3, 3) AS kurtosis_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWH,
    round(SUM(POWER(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` - (SELECT AVG(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) FROM solardataset), 4)) / COUNT(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) / POWER((SELECT STD(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) FROM solardataset), 4) - 3, 3) AS kurtosis_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(SUM(POWER(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` - (SELECT AVG(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) FROM solardataset), 4)) / COUNT(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) / POWER((SELECT STD(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) FROM solardataset), 4) - 3, 3) AS kurtosis_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(SUM(POWER(`Daily Generation Plant end meter (net)MWh` - (SELECT AVG(`Daily Generation Plant end meter (net)MWh`) FROM solardataset), 4)) / COUNT(`Daily Generation Plant end meter (net)MWh`) / POWER((SELECT STD(`Daily Generation Plant end meter (net)MWh`) FROM solardataset), 4) - 3, 3) AS kurtosis_Daily_Generation_Plant_end_meter_net_MWh,
    round(SUM(POWER(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` - (SELECT AVG(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) FROM solardataset), 4)) / COUNT(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) / POWER((SELECT STD(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) FROM solardataset), 4) - 3, 3) AS kurtosis_Global_Tilted_Irradiation_Irradiance_GTI,
    round(SUM(POWER(`Global horizontal irrradiance (GHI)kMh/m2` - (SELECT AVG(`Global horizontal irrradiance (GHI)kMh/m2`) FROM solardataset), 4)) / COUNT(`Global horizontal irrradiance (GHI)kMh/m2`) / POWER((SELECT STD(`Global horizontal irrradiance (GHI)kMh/m2`) FROM solardataset), 4) - 3, 3) AS kurtosis_Global_horizontal_irradiance_GHI,
    round(SUM(POWER(`Performance Ratio (PR) %` - (SELECT AVG(`Performance Ratio (PR) %`) FROM solardataset), 4)) / COUNT(`Performance Ratio (PR) %`) / POWER((SELECT STD(`Performance Ratio (PR) %`) FROM solardataset), 4) - 3, 3) AS kurtosis_Performance_Ratio_PR
FROM solardataset;
-- output: 																		
-- skewness_ICR3_INV1 : 1.308
-- skewness_ICR3_INV2 : 1.464
-- skewness_ICR3_INV3 : 1.395
-- skewness_ICR3_INV4 : 1.371
-- skewness_ICR4_INV1 : 1.634
-- skewness_ICR4_INV2 : 1.212
-- skewness_ICR4_INV3 : 1.391
-- skewness_ICR4_INV4 : 1.426
-- skewness_Total_Daily_Integrated_Generation_MWh : 1.44
-- skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : -0.929
-- skewness_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : -1.25
-- skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWH : -0.928
-- skewness_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh : -1.243
-- skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh : -0.678
-- skewness_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh : -0.78
-- skewness_Daily_Generation_Plant_end_meter_net_MWh : -0.675
-- skewness_Global_Tilted_Irradiation_Irradiance_GTI : 0.815
-- skewness_Global_horizontal_irradiance_GHI : 0.266
-- skewness_Performance_Ratio_PR : 95.148

-- --------------------------------------------------------------------------
-- BIVARIATE 
# Energy Generation vs. Irradiance:
# Global Tilted Irradiation (GTI), kWh/m² vs. Daily Generation Plant end meter (net), MWh
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) AS sum_x,
        SUM(`Daily Generation Plant end meter (net)MWh`) AS sum_y,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` * `Daily Generation Plant end meter (net)MWh`) AS sum_xy,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` * `Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) AS sum_xx,
        SUM(`Daily Generation Plant end meter (net)MWh` * `Daily Generation Plant end meter (net)MWh`) AS sum_yy
    FROM solardataset
    WHERE
        `Global Tilted Irradiation/Irradiance (GTI)kWh/m2` IS NOT NULL
        AND `Daily Generation Plant end meter (net)MWh` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
-- output: Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Daily Generation Plant end meter (net)MWh: 0.7488357462339578

-- -------------------------------------------------------------------------------------------------------------------
# Global Horizontal Irradiance (GHI), kWh/m² vs. Daily Generation Plant end meter (net), MWh
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`Global horizontal irrradiance (GHI)kMh/m2`) AS sum_x,
        SUM(`Daily Generation Plant end meter (net)MWh`) AS sum_y,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` * `Daily Generation Plant end meter (net)MWh`) AS sum_xy,
        SUM(`Global horizontal irrradiance (GHI)kMh/m2` * `Global horizontal irrradiance (GHI)kMh/m2`) AS sum_xx,
        SUM(`Daily Generation Plant end meter (net)MWh` * `Daily Generation Plant end meter (net)MWh`) AS sum_yy
    FROM solardataset
    WHERE
        `Global horizontal irrradiance (GHI)kMh/m2` IS NOT NULL
        AND `Daily Generation Plant end meter (net)MWh` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
# output: Correlation between Global horizontal irrradiance (GHI)kMh/m2 and Daily Generation Plant end meter (net)MWh: 1.1865235402762502

# Global Tilted Irradiation/Irradiance (GTI)kWh/m2 vs. Global horizontal irrradiance (GHI)kMh/m2
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) AS sum_x,
        SUM(`Global horizontal irrradiance (GHI)kMh/m2`) AS sum_y,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` * `Global horizontal irrradiance (GHI)kMh/m2`) AS sum_xy,
        SUM(`Global Tilted Irradiation/Irradiance (GTI)kWh/m2` * `Global Tilted Irradiation/Irradiance (GTI)kWh/m2`) AS sum_xx,
        SUM(`Global horizontal irrradiance (GHI)kMh/m2` * `Global horizontal irrradiance (GHI)kMh/m2`) AS sum_yy
    FROM solardataset
    WHERE
        `Global Tilted Irradiation/Irradiance (GTI)kWh/m2` IS NOT NULL
        AND `Global horizontal irrradiance (GHI)kMh/m2` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
# output: Correlation between Global Tilted Irradiation/Irradiance (GTI)kWh/m2 and Global horizontal irrradiance (GHI)kMh/m2: 0.9498249969521428


# Energy Export vs. Energy Import:
# PSS Main Meter (Cumulative Plant end meter reading)(Export), MWh vs. PSS Main Meter (Cumulative Plant end meter reading)(Import), MWh
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) AS sum_x,
        SUM(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) AS sum_y,
        SUM(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` * `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) AS sum_xy,
        SUM(`PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` * `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`) AS sum_xx,
        SUM(`PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` * `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`) AS sum_yy
    FROM solardataset
    WHERE
        `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` IS NOT NULL
        AND `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
# output : Correlation between PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH and PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh: 0.9931010425324288

# PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh vs. PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh`) AS sum_x,
        SUM(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) AS sum_y,
        SUM(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh` * `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) AS sum_xy,
        SUM(`PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh` * `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh`) AS sum_xx,
        SUM(`PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` * `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`) AS sum_yy
    FROM solardataset
    WHERE
        `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh` IS NOT NULL
        AND `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
# output: Correlation between PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh and PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh: 0.9931752475544339

# PSS Main Meter (Daily Generation Plant end meter)(Export), MWh vs. PSS Main Meter (Daily Generation Plant end meter)(Import), MWh
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) AS sum_x,
        SUM(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) AS sum_y,
        SUM(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` * `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) AS sum_xy,
        SUM(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` * `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) AS sum_xx,
        SUM(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` * `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) AS sum_yy
    FROM solardataset
    WHERE
        `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` IS NOT NULL
        AND `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
# output: Correlation between PSS Main Meter (Daily Generation Plant end meter )(Export)MWh and PSS Main Meter (Daily Generation Plant end meter )(Import)MWh: 0.2659988358360428

# Performance Ratio vs. Energy Generation:
# Performance Ratio (PR) % vs. Daily Generation Plant end meter (net), MWh
WITH stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(`Performance Ratio (PR) %`) AS sum_x,
        SUM(`Daily Generation Plant end meter (net)MWh`) AS sum_y,
        SUM(`Performance Ratio (PR) %` * `Daily Generation Plant end meter (net)MWh`) AS sum_xy,
        SUM(`Performance Ratio (PR) %` * `Performance Ratio (PR) %`) AS sum_xx,
        SUM(`Daily Generation Plant end meter (net)MWh` * `Daily Generation Plant end meter (net)MWh`) AS sum_yy
    FROM solardataset
    WHERE
        `Performance Ratio (PR) %` IS NOT NULL
        AND `Daily Generation Plant end meter (net)MWh` IS NOT NULL
),
correlation AS (
    SELECT (n * sum_xy - sum_x * sum_y) /
        SQRT((n * sum_xx - sum_x * sum_x) * (n * sum_yy - sum_y * sum_y)) AS pearson_correlation
    FROM stats )
SELECT pearson_correlation FROM correlation;
# output: Correlation between Performance Ratio (PR) % and Daily Generation Plant end meter (net)MWh: -0.17921610115242767

-- ----------------------------------------------------------------------------------------------------------------
