# lang_hdfs.py
from sklearn import svm, metrics
import numpy as np
import pandas as pd
import os.path, glob
from hdfs import InsecureClient
import time
client = InsecureClient( "http://master:9870", user="hdfs" )
def load_txt( path ) :
    # files = glob.glob( path )
    files = client.list( path )
    data = []
    label = []
    for filename in files :
        file = os.path.basename( filename )
        lang = file.split( "-" )
        label.append( lang[0] )
        
        # langfile = open( filename, "r", encoding="utf-8" ).read()
        try :
            with client.read( os.path.join( path, file ), encoding="utf-8" ) as reader :
                langfile = reader.read()
                langtext = langfile.lower()
                code_a = ord( "a" )
                code_z = ord( "z" )
                count = [ i for i in range( 0, 26 ) ]
                for char in langtext :
                    charcode = ord( char )
                    if code_a <= charcode and charcode <= code_z :
                        count[ charcode - code_a ] += 1
                total = sum( count )
                count = list( map( lambda n : n/total, count ) )
                data.append( count )
        except :
            time.sleep( 5 )
    return data, label
        
train_data, train_label = load_txt( "/input/lang/train/" )
test_data, test_label = load_txt( "/input/lang/test/" )

svc = svm.SVC()
model = svc.fit( train_data, train_label )
print( model.score( train_data, train_label ) )   # 1.0
print( model.score( test_data, test_label ) )     # 0.75

import matplotlib.pyplot as plt
dict = {}
for i in range( len( train_label ) ) :
    label = train_label[i]
    data = train_data[i]
    if not label in dict :
        dict[ label ] = data
asclist = [ [ chr( i ) for i in range( 97, 97+26 ) ] ]
df = pd.DataFrame( dict, index=asclist[0] )
plt.style.use( "ggplot" )
df.plot( kind="bar", subplots=True )
plt.savefig( "lang-plt.png" )
plt.show()




