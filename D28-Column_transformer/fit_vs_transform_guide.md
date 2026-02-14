# Fit vs Transform in Machine Learning Preprocessing

## 1. What does **fit()** mean?

**fit()** learns the parameters from the training data.

Examples: - Mean and standard deviation in **StandardScaler** -
Categories in **OneHotEncoder** - Min and max values in **MinMaxScaler**

**Important:**\
➡️ `fit()` should be done **ONLY on training data**.

------------------------------------------------------------------------

## 2. What does **transform()** mean?

**transform()** applies the already‑learned parameters to new data.

Examples: - Uses stored mean & std to scale validation/test data - Uses
stored categories to encode test data

**Key idea:**\
➡️ `transform()` **does NOT learn anything new**.

------------------------------------------------------------------------

## 3. What is **fit_transform()**?

`fit_transform()` = **fit() + transform() together**

It: 1. Learns parameters from the data\
2. Immediately applies the transformation

➡️ Used mainly on **training data**.

------------------------------------------------------------------------

## 4. Correct Usage Rule

### Training Data

``` python
X_train_scaled = scaler.fit_transform(X_train)
```

✔ Learns from training data\
✔ Transforms training data

### Test Data

``` python
X_test_scaled = scaler.transform(X_test)
```

✔ Uses same learned parameters\
❌ Does NOT learn from test data

------------------------------------------------------------------------

## 5. What happens if we use **fit() on test data?**

### Problems:

-   **Data leakage** → Model indirectly sees test information\
-   **Wrong evaluation** → Accuracy appears higher than real\
-   **Different scaling/encoding** → Column mismatch or inconsistent
    values

🚫 This makes the ML experiment **invalid**.

------------------------------------------------------------------------

## 6. Golden Interview Rule

> **Always `fit` on TRAIN data and only `transform` on TEST data.**

Remember:

**Train = Learn**\
**Test = Apply only**

------------------------------------------------------------------------

## 7. One‑Hot Encoding Example

``` python
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop='first', sparse_output=False)

# Correct
X_train_ohe = ohe.fit_transform(X_train[['gender', 'city']])
X_test_ohe = ohe.transform(X_test[['gender', 'city']])
```

------------------------------------------------------------------------

## 8. Quick Visual Memory

| Dataset \| Operation \|

\|---------\|-----------\| Train \| fit + transform \| \| Test \|
transform only \|

------------------------------------------------------------------------

### Final Takeaway

**Never use `fit()` or `fit_transform()` on validation/test data in
machine learning.**
