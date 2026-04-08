import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_initial_graph(dataset, ax):
    if dataset == "Binary":
        X, y = make_blobs(n_features=2, centers=2, random_state=6)
        ax.scatter(X.T[0], X.T[1], c=y, cmap='rainbow')
        return X, y
    elif dataset == "Multiclass":
        X, y = make_blobs(n_features=2, centers=3, random_state=2)
        ax.scatter(X.T[0], X.T[1], c=y, cmap='rainbow')
        return X, y

def draw_meshgrid(X):
    a = np.arange(start=X[:, 0].min() - 1, stop=X[:, 0].max() + 1, step=0.01)
    b = np.arange(start=X[:, 1].min() - 1, stop=X[:, 1].max() + 1, step=0.01)
    XX, YY = np.meshgrid(a, b)
    input_array = np.array([XX.ravel(), YY.ravel()]).T
    return XX, YY, input_array

plt.style.use('fivethirtyeight')

st.sidebar.markdown("# Logistic Regression Classifier")

dataset = st.sidebar.selectbox('Select Dataset', ('Binary', 'Multiclass'))

penalty = st.sidebar.selectbox('Regularization', ('l2', 'l1', 'elasticnet', None))

c_input = float(st.sidebar.number_input('C', value=1.0, min_value=0.01))

solver = st.sidebar.selectbox('Solver', ('newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'))

max_iter = int(st.sidebar.number_input('Max Iterations', value=100, min_value=1))

l1_ratio = float(st.sidebar.number_input('l1 Ratio', value=0.0, min_value=0.0, max_value=1.0))

# Load initial graph
fig, ax = plt.subplots()
X, y = load_initial_graph(dataset, ax)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
orig = st.pyplot(fig)

if st.sidebar.button('Run Algorithm'):
    orig.empty()

    # Determine valid solver for chosen penalty
    penalty_solver_map = {
        'l1': ['liblinear', 'saga'],
        'l2': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
        'elasticnet': ['saga'],
        None: ['newton-cg', 'lbfgs', 'sag', 'saga'],
    }
    valid_solvers = penalty_solver_map.get(penalty, ['lbfgs'])
    chosen_solver = solver if solver in valid_solvers else valid_solvers[0]

    if penalty != 'elasticnet':
        clf = LogisticRegression(
            penalty=penalty,
            C=c_input,
            solver=chosen_solver,
            max_iter=max_iter
        )
    else:
        clf = LogisticRegression(
            penalty=penalty,
            C=c_input,
            solver=chosen_solver,
            max_iter=max_iter,
            l1_ratio=l1_ratio
        )

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    XX, YY, input_array = draw_meshgrid(X)
    labels = clf.predict(input_array)

    fig2, ax2 = plt.subplots()
    ax2.scatter(X.T[0], X.T[1], c=y, cmap='rainbow')
    ax2.contourf(XX, YY, labels.reshape(XX.shape), alpha=0.5, cmap='rainbow')
    plt.xlabel("Col1")
    plt.ylabel("Col2")
    st.pyplot(fig2)
    st.subheader("Accuracy for Logistic Regression: " + str(round(accuracy_score(y_test, y_pred), 2)))