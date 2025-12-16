
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Correct way to read the CSV file
df = pd.read_csv("C:\Users\lafor\Downloads\TP53_only_expression.csv")

# Optional: check the first few rows
print(df.head())

GSE62944_subsample_log2TPM= "C:\Users\lafor\Downloads\TP53_only_expression.csv"
dataset = GSE62944_subsample_log2TPM(as_frame=True)
print(dataset.data.shape, dataset.target.shape)
print(dataset.feature_names[0:6])

# %%
print(dataset.DESCR)
# %% single feature
feature = "TP53"

X = dataset["data"][feature].values.reshape(-1, 1)
y = dataset.target

reg = LinearRegression().fit(X, y)
print("R^2", reg.score(X, y))
print(reg.coef_, reg.intercept_)

x_test = np.linspace(0, 15, 100).reshape(-1, 1)
y_test = reg.predict(x_test)
plt.scatter(X, y)
plt.plot(x_test, y_test, color="red")
plt.xlabel(feature)
plt.ylabel("Tumor Stage")
plt.annotate(
    "R^2 = {:.2f}".format(reg.score(X, y)),
    xy=(0.5, 0.9),
    xycoords="axes fraction",
    fontsize=14,
    ha="center",
)
plt.show()
