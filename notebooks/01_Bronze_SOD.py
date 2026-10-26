import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node sod_2023_2024
sod_2023_2024_node1790515593116 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://lab-teste-tech-challenge-6890/data_input/sod_2023_2024/State_of_data_BR_2023_Kaggle - df_survey_2023.csv"], "recurse": True}, transformation_ctx="sod_2023_2024_node1790515593116")

# Script generated for node sod_2024_2025
sod_2024_2025_node1790518019741 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://lab-teste-tech-challenge-6890/data_input/sod_2024_2025/Final Dataset - State of Data 2024 - Kaggle - df_survey_2024.csv"], "recurse": True}, transformation_ctx="sod_2024_2025_node1790518019741")

# Script generated for node sod_2025_2026
sod_2025_2026_node1790625484437 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://lab-teste-tech-challenge-6890/data_input/sod_2025_2026/Final Dataset - State of Data 2025-2026 - Kaggle.csv"], "recurse": True}, transformation_ctx="sod_2025_2026_node1790625484437")

# Script generated for node tb_sod_2023_2024
EvaluateDataQuality().process_rows(frame=sod_2023_2024_node1790515593116, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1790905233046", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
tb_sod_2023_2024_node1790905316853 = glueContext.getSink(path="s3://lab-teste-tech-challenge-6890/Bronze/sod_23-24/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="tb_sod_2023_2024_node1790905316853")
tb_sod_2023_2024_node1790905316853.setCatalogInfo(catalogDatabase="tech-challenge-bronze",catalogTableName="tb_sod_2023_2024")
tb_sod_2023_2024_node1790905316853.setFormat("glueparquet", compression="snappy")
tb_sod_2023_2024_node1790905316853.writeFrame(sod_2023_2024_node1790515593116)
# Script generated for node tb_sod_2024_2025
EvaluateDataQuality().process_rows(frame=sod_2024_2025_node1790518019741, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1790905233046", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
tb_sod_2024_2025_node1790906311607 = glueContext.getSink(path="s3://lab-teste-tech-challenge-6890/Bronze/sod_24-25/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="tb_sod_2024_2025_node1790906311607")
tb_sod_2024_2025_node1790906311607.setCatalogInfo(catalogDatabase="tech-challenge-bronze",catalogTableName="tb_sod_2024_2025")
tb_sod_2024_2025_node1790906311607.setFormat("glueparquet", compression="snappy")
tb_sod_2024_2025_node1790906311607.writeFrame(sod_2024_2025_node1790518019741)
# Script generated for node tb_sod_2025_2026
EvaluateDataQuality().process_rows(frame=sod_2025_2026_node1790625484437, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1790905233046", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
tb_sod_2025_2026_node1790907339876 = glueContext.getSink(path="s3://lab-teste-tech-challenge-6890/Bronze/sod_25-26/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="tb_sod_2025_2026_node1790907339876")
tb_sod_2025_2026_node1790907339876.setCatalogInfo(catalogDatabase="tech-challenge-bronze",catalogTableName="tb_sod_2025_2026")
tb_sod_2025_2026_node1790907339876.setFormat("glueparquet", compression="snappy")
tb_sod_2025_2026_node1790907339876.writeFrame(sod_2025_2026_node1790625484437)
job.commit()