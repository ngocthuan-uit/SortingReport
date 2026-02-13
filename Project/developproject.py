import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

def get_mae(max_leaf_nodes, train_x, test_x, train_y, test_y):
    model=DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_x, train_y)
    preds_val=model.predict(test_x)
    mae=mean_absolute_error(test_y, preds_val)
    return (mae)

melbourne_file_path="C:/Users/Lenovo/Desktop/Thuan/nmlt/melb_data.csv"
melbourne_data=pd.read_csv(melbourne_file_path)
print(melbourne_data.describe())
print(melbourne_data.columns)
melbourne_data=melbourne_data.dropna(axis=0)
y=melbourne_data.Price
melbourne_features=['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
x=melbourne_data[melbourne_features]
## or x=melbourne_data[["Rooms","Bathroom","Landsize","Lattitude","Longtitude"]]
print(x.describe())
print(x.head())
melbourne_model=DecisionTreeRegressor()
train_x, test_x, train_y,test_y=train_test_split(x,y, random_state=0)
melbourne_model.fit(train_x,train_y)
predictions=melbourne_model.predict(test_x)
print(mean_absolute_error(test_y,predictions))
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_x, test_x, train_y, test_y)
    print(f"Max leaf nodes: {max_leaf_nodes}  \t\t Mean Absolute Error:  {my_mae}")