# hdfs_pyspark.py
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.python.pyspark.shell import sqlContext
from pyspark.sql.session import SparkSession

# Eclipse / Linux Local #
# iris = sqlContext.read.format( "com.databricks.spark.csv" ).options( header="true", inferSchema="true" )\
#             .load( "iris.csv" ).repartition( 2 ).cache()

# Spark Multi #
# conf = SparkConf().setAppName( "iris" ).setMaster( "spark://master:7077" )
# sc = SparkContext().getOrCreate(conf=conf)
# sqlContext = SQLContext( sc )
# iris = sqlContext.read.format( "com.databricks.spark.csv" ).options( header="true", inferSchema="true" )\
#             .load( "/input/iris.csv" ).repartition( 2 ).cache()

spark = SparkSession.builder\
            .appName('iris')\
            .master( "spark://master:7077" )\
            .getOrCreate()   
iris = spark.read.csv("/input/iris.csv", header=True, inferSchema=True)
            
# print( type( iris ) )               # pyspark.sql.dataframe.DataFrame
# print( iris.show() )            

stridx = StringIndexer( inputCol="Name", outputCol="label" )
#encode = OneHotEncoder( inputCol="name_idx", outputCol="name_encode" )
inputs = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
va = VectorAssembler( inputCols=inputs, outputCol="features" )
pipeline = Pipeline( stages=[va, stridx] )
pipelineModel = pipeline.fit( iris )
datadf = pipelineModel.transform( iris ).drop( "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Name" )
# print( datadf.show() )

(train, test) = datadf.randomSplit( [0.7, 0.3], seed=0 )
lr = LogisticRegression( labelCol="label", featuresCol="features", maxIter=10 )
model = lr.fit( train )
predicts = model.transform( test )
# print( predicts.show() )

# 모델검증
evaluator = MulticlassClassificationEvaluator()
# print( evaluator.getMetricName() )          # f1
evaluator.setPredictionCol( "prediction" )
evaluator.setLabelCol( "label" )
score = evaluator.evaluate( predicts, {evaluator.metricName: "truePositiveRateByLabel", 
                              evaluator.metricLabel: 1.0 } )
# score = evaluator.evaluate( predicts, {evaluator.metricName: "falsePositiveRateByLabel", 
#                               evaluator.metricLabel: 1.0 } )
# score = evaluator.evaluate( predicts, {evaluator.metricName: "precisionByLabel", 
#                               evaluator.metricLabel: 1.0 } )
# score = evaluator.evaluate( predicts, {evaluator.metricName: "recallByLabel", 
#                               evaluator.metricLabel: 1.0 } )
# score = evaluator.evaluate( predicts, {evaluator.metricName: "accuracy", 
#                               evaluator.metricLabel: 1.0 } )
print( score ) 

# 최적화
paramGrid = ParamGridBuilder().addGrid( lr.regParam, [0.01, 0.1] )\
                            .addGrid( lr.elasticNetParam, [0.0, 0.5, 1.0] )\
                            .addGrid( lr.maxIter, [1, 5, 10] )\
                            .build() 
cv = CrossValidator( estimator=lr, estimatorParamMaps=paramGrid, 
                     evaluator=evaluator, numFolds=5 )
models = cv.fit( train )
print( models.bestModel.getMaxIter() )
print( models.bestModel.getRegParam() )
print( models.bestModel.getElasticNetParam() )
predicts = models.bestModel.transform( test )
# print( predicts.show() )
print( ( predicts[ predicts["label"] == predicts["prediction"] ].count() * 100 ) / predicts.count() )




































