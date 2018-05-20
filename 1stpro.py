#!/usr/bin/python3

from sklearn import tree

#apple& orange -- texture 0-bumpy 1-smooth and weight
feature=[[110,1],[120,1],[130,0],[140,0]]
output=["apple","apple","orange","orange"]
#sikit-learning

#now loading Decision tree Clasifier

algo=tree.DecisionTreeClassifier()
#now train the feature and output

trained=algo.fit(feature,output)    		#genrally looking for 1core --[gpu]

#testing trained model for questions ANd answers
res=trained.predict([[1000,1]])

#predicted output
print(res)
