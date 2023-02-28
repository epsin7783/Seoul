# bank_pyspark.py
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql.context import SQLContext
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.classification import RandomForestClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

spark = SparkSession.builder.appName( "bank" ).master( "spark://master:7077" ).getOrCreate()
bank = spark.read.csv( "/input/bank.csv", header=True, inferSchema=True )

# conf = SparkConf().setAppName( "bank" )
# sc = SparkContext.getOrCreate( conf=conf )
# sqlContext = SQLContext( sc )
# bank = sqlContext.read.format( "com.databricks.spark.csv" )\
#         .options( header="true", inferSchema="true" )\
#         .load( "bank.csv" ).repartition( 2 ).cache()
# print( bank.printSchema() )
# print( bank.show() )

df = bank.select( "age", "job", "marital", "education", "balance", 
                  "housing", "loan", "duration", "campaign", "pdays", "previous", "poutcome", "y" )
# age 연령 job 직업 marital 결혼여부 education 교육 default 기본값 
# balance housing 주택 loan 대출(yes/no) contact 통신유형 day month 최종연락일 
# duration 잔고 0이면 y no가 된다. campaign 캠페인중 연락 수
# pdays 이전 캠페인 경과 일수 previous 이전 캠페인 수 
# poutcome 이전 마케팅 결과(성공, 실패)
# y 정기예금 신청 여부(yes/no)

cols = df.columns
# print( cols )
categories = ["job", "marital", "education", "housing", "loan", "poutcome"]
stages = []
for category in categories :
    stridx = StringIndexer( inputCol=category, outputCol=category+"Index" )
    encoder = OneHotEncoder( inputCols=[stridx.getOutputCol()], outputCols=[category+"classVec"] )
    stages += [stridx, encoder]
label = StringIndexer( inputCol="y", outputCol="label" )
stages += [label]

numerics = ["age", "balance", "duration", "pdays", "previous"]
inputs = [ c + "classVec" for c in categories ] + numerics
va = VectorAssembler( inputCols=inputs, outputCol="features" )
stages += [va]

pipline = Pipeline( stages = stages )
piplineModel = pipline.fit( df )
df = piplineModel.transform( df )
# print( df.show() )
selectedCol = ["label", "features"] + cols
df = df.select( selectedCol )
# print( df.show() )

( train, test ) = df.randomSplit( [0.7, 0.3], seed=0 )
forest = RandomForestClassifier( featuresCol="features", labelCol="label" )
model = forest.fit( train )
predicts = model.transform( test )
# print( predicts.select( "label", "prediction" ).show() )

evaluator = BinaryClassificationEvaluator()
score = evaluator.evaluate( predicts, {evaluator.metricName:"areaUnderROC"} )
print( score )

gbt = GBTClassifier( maxIter=10 )
model = gbt.fit( train )
predicts = model.transform( test )

evaluator = BinaryClassificationEvaluator()
score = evaluator.evaluate( predicts, {evaluator.metricName:"areaUnderROC"} )
# print( score )
# print( gbt.explainParams() )

paramGrid = ParamGridBuilder().addGrid( gbt.maxDepth, [2, 4, 6] )\
                            .addGrid( gbt.maxBins, [10, 20, 40] )\
                            .addGrid( gbt.maxIter, [10, 20] )\
                            .build()
cv = CrossValidator( estimator=gbt, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5 )
models = cv.fit( train )
predicts = models.bestModel.transform( test )
                            
evaluator = BinaryClassificationEvaluator()
score = evaluator.evaluate( predicts, {evaluator.metricName:"areaUnderROC"} )
print( score )                    






    


































