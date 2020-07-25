
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

y_true = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
y_pred = [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0]

mat = confusion_matrix(y_true, y_pred)
sns.heatmap(mat, square=True, annot=True, cbar=False)
plt.xlabel('Previsão do modelo')
plt.ylabel('Valor verdadeiro');

print(classification_report(y_true, y_pred))

#MAE

# Perform the intial fitting to get the LinearRegression object
from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(X, sales)

mae_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mae_sum += abs(sale - prediction)
mae = mae_sum / len(sales)

print(mae)

#MSE

mse_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mse_sum += (sale - prediction)**2
mse = mse_sum / len(sales)

print(mse)

#MAPE

mape_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mape_sum += (abs((sale - prediction))/sale)
mape = mape_sum/len(sales)

print(mape)

#MPE (equal to Mape, except for the ABS)

mpe_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mpe_sum += ((sale - prediction)/sale)
mpe = mpe_sum/len(sales)

print(mpe)