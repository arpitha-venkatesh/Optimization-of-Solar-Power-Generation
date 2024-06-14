use solar;
select * from solardataset;
-- PRE-PROCESSING
-- HANDLING DUPLICATES
SELECT COUNT(*) AS TOTAL_ROW FROM solardataset;
-- TOTAL_ROW : 366

-- FINDING DUPLICATES RECORDS in solardataset

    round(AVG(), 3) AS mean_PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(AVG(), 3) AS mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh,
    round(AVG(), 3) AS mean_PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh,
    round(AVG(), 3) AS mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh,
    round(AVG(), 3) AS mean_PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh,
    round(AVG(), 3) AS mean_Daily_Generation_Plant_end_meter_net_MWh,
    round(AVG(), 3) AS mean_Global_Tilted_Irradiation_Irradiance_GTI,
    round(AVG(), 3) AS mean_Global_horizontal_irradiance_GHI,
    round(AVG(), 3) AS mean_Performance_Ratio_PR
FROM solardataset;
SELECT
      Date,`ICR-3 - INV1`,`ICR-3 - INV2`,`ICR-3 - INV3`,`ICR-3 - INV4`,
      `ICR-4 - INV1`,`ICR-4 - INV2`,`ICR-4 - INV3`,`ICR-4 - INV4`,
      `Total Daily Integrated Generation MWh`,
      `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`,
      `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`,
      `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`,
      `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`,
      `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`,
      `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`,
      `Daily Generation Plant end meter (net)MWh`,
      `Global Tilted Irradiation/Irradiance (GTI)kWh/m2`,
      `Global horizontal irrradiance (GHI)kMh/m2`,
      `Performance Ratio (PR) %`,`Grid Downtime HH:MM`,`Plant Downtime HH:MM`,
      `Remarks`,count(*) AS TOTAL
FROM solardataset
GROUP BY 
       Date,`ICR-3 - INV1`,`ICR-3 - INV2`,`ICR-3 - INV3`,`ICR-3 - INV4`,
      `ICR-4 - INV1`,`ICR-4 - INV2`,`ICR-4 - INV3`,`ICR-4 - INV4`,
      `Total Daily Integrated Generation MWh`,
      `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH`,
      `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh`,
      `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWH`,
      `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh`,
      `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`,
      `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`,
      `Daily Generation Plant end meter (net)MWh`,
      `Global Tilted Irradiation/Irradiance (GTI)kWh/m2`,
      `Global horizontal irrradiance (GHI)kMh/m2`,
      `Performance Ratio (PR) %`,`Grid Downtime HH:MM`,`Plant Downtime HH:MM`,
      `Remarks`
HAVING TOTAL>1 LIMIT 0,5000;
-- No duplicated records

-- ------------------------------------------------------------------------------
# droping column
# In the dataset, the 'Grid Downtime HH' column contains only 2 non-null values, 
# thus providing limited information for analysis. 
# Similarly, the 'Plant Downtime HH' column, having the same value for all entries, 
# lacks variability and useful information for analysis.
# so we are droping that column
ALTER TABLE solardataset 
DROP COLUMN `Grid Downtime HH:MM`;
ALTER TABLE solardataset 
DROP COLUMN `Plant Downtime HH:MM`;
 
SELECT * FROM solardataset;

-- ---------------------------------------------------------------------------
-- HANDLING MISSING values
SELECT 
	 SUM(CASE WHEN  `Date` IS NULL THEN 1 ELSE 0 END) AS Date_NULL_COUNT,
     SUM(CASE WHEN `ICR-3 - INV1` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV1_NULL_COOUNT,
     SUM(CASE WHEN  `ICR-3 - INV2` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV2_NULL_COUNT,
     SUM(CASE WHEN  `ICR-3 - INV3` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV3_NULL_COUNT,
     SUM(CASE WHEN  `ICR-3 - INV4` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV4_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV1` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV1_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV2` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV2_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV3` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV3_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV4` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV4_NULL_COUNT,
     SUM(CASE WHEN  `Total Daily Integrated Generation MWh` IS NULL THEN 1 ELSE 0 END) AS Total_Daily_Integrated_Generation_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `Daily Generation Plant end meter (net)MWh` IS NULL THEN 1 ELSE 0 END) AS Daily_Generation_Plant_end_meter_net_MWh_NULL_COUNT,
     SUM(CASE WHEN  `Global Tilted Irradiation/Irradiance (GTI)kWh/m2` IS NULL THEN 1 ELSE 0 END) AS Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT,
     SUM(CASE WHEN  `Global horizontal irrradiance (GHI)kMh/m2` IS NULL THEN 1 ELSE 0 END) AS Global_horizontal_irrradiance_GHI_kMh_m2_NULL_COUNT,
     SUM(CASE WHEN  `Performance Ratio (PR) %` IS NULL THEN 1 ELSE 0 END) AS Performance_Ratio_PR__NULL_COUNT,
     SUM(CASE WHEN  `Remarks` IS NULL THEN 1 ELSE 0 END) AS Remarks_NULL_COUNT
FROM solardataset;
     -- Date_NULL_COUNT :
     -- ICR3_INV1_NULL_COUNT :0
     -- ICR3_INV2_NULL_COUNT :18
     -- ICR3_INV3_NULL_COUNT :18
     -- ICR3_INV4_NULL_COUNT :18
     -- ICR4_INV1_NULL_COUNT :18
     -- ICR4_INV2_NULL_COUNT :18
     -- ICR4_INV3_NULL_COUNT :18
     -- ICR4_INV4_NULL_COUNT :18
     -- Total_Daily_Integrated_Generation_MWh_NULL_COUNT :18
     -- PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH_NULL_COUNT : 18
     -- PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT :18
     -- PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh_NULL_COUNT: 18
     -- PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT : 18
     -- PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh_NULL_COUNT : 19
     -- PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh_NULL_COUNT :19
     -- Daily_Generation_Plant_end_meter_net_MWh_NULL_COUNT :19
     -- Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT :18
     -- Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT:18
     -- Global_horizontal_irrradiance_GHI_kMh_m2_NULL_COUNT :18
     -- Performance_Ratio_PR__NULL_COUNT : 19
     -- Remarks_NULL_COUNT :18
      
# In the dataset, we observed that the bottom 18 rows contain only date values, 
# while all other 19 columns do not contain any values, so we just dropped those rows.
-- droping null value :
SET SQL_SAFE_UPDATES=0;
DELETE FROM solardataset 
WHERE `ICR-3 - INV1` IS NULL;

-- AFTER DROPING NULL values
SELECT 
	 SUM(CASE WHEN  `Date` IS NULL THEN 1 ELSE 0 END) AS Date_NULL_COUNT,
     SUM(CASE WHEN `ICR-3 - INV1` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV1_NULL_COOUNT,
     SUM(CASE WHEN  `ICR-3 - INV2` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV2_NULL_COUNT,
     SUM(CASE WHEN  `ICR-3 - INV3` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV3_NULL_COUNT,
     SUM(CASE WHEN  `ICR-3 - INV4` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV4_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV1` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV1_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV2` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV2_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV3` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV3_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV4` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV4_NULL_COUNT,
     SUM(CASE WHEN  `Total Daily Integrated Generation MWh` IS NULL THEN 1 ELSE 0 END) AS Total_Daily_Integrated_Generation_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `Daily Generation Plant end meter (net)MWh` IS NULL THEN 1 ELSE 0 END) AS Daily_Generation_Plant_end_meter_net_MWh_NULL_COUNT,
     SUM(CASE WHEN  `Global Tilted Irradiation/Irradiance (GTI)kWh/m2` IS NULL THEN 1 ELSE 0 END) AS Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT,
     SUM(CASE WHEN  `Global horizontal irrradiance (GHI)kMh/m2` IS NULL THEN 1 ELSE 0 END) AS Global_horizontal_irrradiance_GHI_kMh_m2_NULL_COUNT,
     SUM(CASE WHEN  `Performance Ratio (PR) %` IS NULL THEN 1 ELSE 0 END) AS Performance_Ratio_PR__NULL_COUNT,
     SUM(CASE WHEN  `Remarks` IS NULL THEN 1 ELSE 0 END) AS Remarks_NULL_COUNT
FROM solardataset;
     -- Date_NULL_COUNT :
     -- ICR3_INV1_NULL_COUNT :0
     -- ICR3_INV2_NULL_COUNT :0
     -- ICR3_INV3_NULL_COUNT :0
     -- ICR3_INV4_NULL_COUNT :0
     -- ICR4_INV1_NULL_COUNT :0
     -- ICR4_INV2_NULL_COUNT :0
     -- ICR4_INV3_NULL_COUNT :0
     -- ICR4_INV4_NULL_COUNT :0
     -- Total_Daily_Integrated_Generation_MWh_NULL_COUNT :0
     -- PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH_NULL_COUNT : 0
     -- PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT :0
     -- PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh_NULL_COUNT: 0
     -- PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT : 0
     -- PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh_NULL_COUNT : 1
     -- PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh_NULL_COUNT :1
     -- Daily_Generation_Plant_end_meter_net_MWh_NULL_COUNT :1
     -- Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT :0
     -- Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT:0
     -- Global_horizontal_irrradiance_GHI_kMh_m2_NULL_COUNT : 0
     -- Performance_Ratio_PR__NULL_COUNT :1
     -- Remarks_NULL_COUNT :0
     
# there are still outliers in 
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh
# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh
# Daily Generation Plant end meter (net)MWh 
# Performance Ratio (PR) %


# imputation 
# first we check for the outliers
# there is not outliers present in 
# here we go for mean imputer 
# PSS Main Meter (Daily Generation Plant end meter )(Export)MWh
UPDATE solardataset 
SET `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` = (
    SELECT avg_val
    FROM (SELECT AVG(`PSS Main Meter (Daily Generation Plant end meter )(Export)MWh`) AS avg_val FROM solardataset) AS avg_table
)
WHERE `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` IS NULL;

# PSS Main Meter (Daily Generation Plant end meter )(Import)MWh
UPDATE solardataset 
SET `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` = (
    SELECT avg_val
    FROM (SELECT AVG(`PSS Main Meter (Daily Generation Plant end meter )(Import)MWh`) AS avg_val FROM solardataset) AS avg_table
)
WHERE `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` IS NULL;

# Daily Generation Plant end meter (net)MWh 
UPDATE solardataset 
SET `Daily Generation Plant end meter (net)MWh` = (
    SELECT avg_val
    FROM (SELECT AVG(`Daily Generation Plant end meter (net)MWh`) AS avg_val FROM solardataset) AS avg_table
)
WHERE `Daily Generation Plant end meter (net)MWh` IS NULL;

# In Performance Ratio (PR) % column there are outlier
# here we go for median imputer 

WITH CTE AS (
    SELECT `Performance Ratio (PR) %`, 
           ROW_NUMBER() OVER (ORDER BY `Performance Ratio (PR) %`) AS row_num,
           COUNT(*) OVER() AS total_count 
    FROM solardataset
)
UPDATE solardataset
SET `Performance Ratio (PR) %`=(
SELECT ROUND(AVG(`Performance Ratio (PR) %`), 3) AS median_Performance_Ratio_PR 
FROM CTE
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2)))
WHERE `Performance Ratio (PR) %` IS NULL;
-- median_Performance_Ratio_PR : 78.25


-- AFTER DROPING NULL values
SELECT 
	 SUM(CASE WHEN  `Date` IS NULL THEN 1 ELSE 0 END) AS Date_NULL_COUNT,
     SUM(CASE WHEN `ICR-3 - INV1` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV1_NULL_COOUNT,
     SUM(CASE WHEN  `ICR-3 - INV2` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV2_NULL_COUNT,
     SUM(CASE WHEN  `ICR-3 - INV3` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV3_NULL_COUNT,
     SUM(CASE WHEN  `ICR-3 - INV4` IS NULL THEN 1 ELSE 0 END) AS ICR3_INV4_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV1` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV1_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV2` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV2_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV3` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV3_NULL_COUNT,
     SUM(CASE WHEN  `ICR-4 - INV4` IS NULL THEN 1 ELSE 0 END) AS ICR4_INV4_NULL_COUNT,
     SUM(CASE WHEN  `Total Daily Integrated Generation MWh` IS NULL THEN 1 ELSE 0 END) AS Total_Daily_Integrated_Generation_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Cumulative Plant end meter reading)(Export)MWH` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Cumulative Plant end meter reading)(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Check Meter (Cumulative Plant end meter reading)(Export)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Check Meter (Cumulative Plant end meter reading)(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Daily Generation Plant end meter )(Export)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh_NULL_COUNT,
     SUM(CASE WHEN  `PSS Main Meter (Daily Generation Plant end meter )(Import)MWh` IS NULL THEN 1 ELSE 0 END) AS PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh_NULL_COUNT,
     SUM(CASE WHEN  `Daily Generation Plant end meter (net)MWh` IS NULL THEN 1 ELSE 0 END) AS Daily_Generation_Plant_end_meter_net_MWh_NULL_COUNT,
     SUM(CASE WHEN  `Global Tilted Irradiation/Irradiance (GTI)kWh/m2` IS NULL THEN 1 ELSE 0 END) AS Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT,
     SUM(CASE WHEN  `Global horizontal irrradiance (GHI)kMh/m2` IS NULL THEN 1 ELSE 0 END) AS Global_horizontal_irrradiance_GHI_kMh_m2_NULL_COUNT,
     SUM(CASE WHEN  `Performance Ratio (PR) %` IS NULL THEN 1 ELSE 0 END) AS Performance_Ratio_PR__NULL_COUNT,
     SUM(CASE WHEN  `Remarks` IS NULL THEN 1 ELSE 0 END) AS Remarks_NULL_COUNT
FROM solardataset;
     -- Date_NULL_COUNT :
     -- ICR3_INV1_NULL_COUNT :0
     -- ICR3_INV2_NULL_COUNT :0
     -- ICR3_INV3_NULL_COUNT :0
     -- ICR3_INV4_NULL_COUNT :0
     -- ICR4_INV1_NULL_COUNT :0
     -- ICR4_INV2_NULL_COUNT :0
     -- ICR4_INV3_NULL_COUNT :0
     -- ICR4_INV4_NULL_COUNT :0
     -- Total_Daily_Integrated_Generation_MWh_NULL_COUNT :0
     -- PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Export_MWH_NULL_COUNT : 0
     -- PSS_Main_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT :0
     -- PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Export_MWh_NULL_COUNT: 0
     -- PSS_Check_Meter_Cumulative_Plant_end_meter_reading_Import_MWh_NULL_COUNT : 0
     -- PSS_Main_Meter_Daily_Generation_Plant_end_meter_Export_MWh_NULL_COUNT : 0
     -- PSS_Main_Meter_Daily_Generation_Plant_end_meter_Import_MWh_NULL_COUNT :0
     -- Daily_Generation_Plant_end_meter_net_MWh_NULL_COUNT :0
     -- Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT :0
     -- Global_Tilted_Irradiation_Irradiance_GTI_kWh_m2_NULL_COUNT:0
     -- Global_horizontal_irrradiance_GHI_kMh_m2_NULL_COUNT : 0
     -- Performance_Ratio_PR__NULL_COUNT :0
     -- Remarks_NULL_COUNT :0
      
-- -----------------------------------------------------------------------------------------------
-- zero variance
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

-- there is no zero variance column
