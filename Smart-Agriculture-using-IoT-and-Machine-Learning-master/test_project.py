import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import subprocess
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
#import plotly.plotly as py

#reading the training data and storing it in pandas dataframe
df = pd.read_csv("test_file1.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])

print (df['output'].unique())
#modifying the dataframe, encoding the categorical variables to integers since the decision_tree classifier takes
#only integer inputs
def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)
    return df_mod, targets
df2, targets = encode_target(df, "output")

df.cumsum()

#plt.show()
#plt.figure()
#plt.show()
df.plot()

features = list(df2.columns[:4])
y = df2["Target"]
X = df2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(X, y) #it is getting trained here
dt_test = pd.read_csv("test_this.csv", names=['humidity', 'temp', 'moisture', 'LDR'])
test_features = []
test_features = dt_test.head(1)
#x_test =['10','20','200','75']
type = dt.predict(test_features)
#print dt.predict(x_test)
if type==0:
    print ("dry")
elif type==1:
    print ("Healthy")

sns.pairplot(df, hue="output", size=3)
plt.show()
plt.andrews_curves(df,"output",ax=None)
#plt.show()
plt.figure()
#plt.show()
def visualize_tree(tree,feature_names):

    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f, feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")

visualize_tree(dt, features)
'''
data_clean = AH_data.dropna()
#data_clean.dtypes
#data_clean.describe()

predictors = [['Humidity','Temp','Moisture','LDR']]
targets = data_clean.output

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)
'''
'''
classifier = DecisionTreeClassifier()
classifier = classifier.fit(pred_train,tar_train)

predictions = classifier.predict(pred_test)
print predictions

sklearn.metrics.accuracy_score(tar_test, predictions)
'''
