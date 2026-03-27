## Classical ML Learning Summary

This file gives a complete flow of learning in this Classical ML journey, from data collection to Feature Engineering.

## 1. Foundation and Data Understanding

- **<span style="color:orange">D11</span>**: Tensor basics and core tensor concepts.
- **<span style="color:orange">D13</span>**: End-to-end ML pipeline overview.
- **<span style="color:orange">D15 to D18</span>**: Data collection methods for training.
  - CSV
  - JSON
  - API
  - Web Scraping
- **<span style="color:orange">D19 to D22</span>**: Exploratory Data Analysis (EDA).
  - Bivariate analysis
  - Multivariate analysis
  - Pandas profiling

At this stage, we learned how to collect data and perform basic EDA before moving to Feature Engineering.

## 2. Feature Engineering Overview

- **<span style="color:orange">D23</span>**: Introduction to Feature Engineering.
  1. Feature Transformation
  2. Feature Construction
  3. Feature Selection
  4. Feature Extraction

This summary currently covers the **Feature Transformation** part in detail.

## 3. Feature Transformation (Detailed Flow)

### 3.1 Feature Scaling

- **<span style="color:orange">D24</span>**: Standardization
- **<span style="color:orange">D25</span>**: Normalization

### 3.2 Handling Categorical Features

- **<span style="color:orange">D26</span>**: Ordinal Encoding and Label Encoding
- **<span style="color:orange">D27</span>**: One Hot Encoding
- **<span style="color:orange">D28</span>**: Column Transformer to make transformations efficient and easier to manage

### 3.3 Building Reusable Transformation Workflows

- **<span style="color:orange">D29</span>**: Sklearn Pipelines

### 3.4 Mathematical Transformation of Features

- **<span style="color:orange">D30</span>**: Function Transformer
  - Log Transformation
  - Reciprocal Transformation
  - Power Transformation
- **<span style="color:orange">D31</span>**: Power Transformer
  - Box-Cox Transformation
  - Yeo-Johnson Transformation

## <span style="color:green">Tip</span>

- If you are working with a model that relies on normally distributed data, first check whether columns are normally distributed.
- If they are not, apply transformation techniques to make them closer to normal distribution.
- You can try Function Transformation, but in many cases Power Transformation gives better results.
- Best practice: try both and compare model performance.

### 3.5 Encoding Numerical Features

- **<span style="color:orange">D32</span>**: Binning and Binarization

### 3.6 Handling Mixed Variables and Time Features

- **<span style="color:orange">D33</span>**: Handling mixed variables (numerical and categorical data in the same column)
- **<span style="color:orange">D34</span>**: Handling date and time features

### 3.7 Handling Missing Values

#### 3.7.1 Univariate Missing Value Methods

- **<span style="color:orange">D35</span>**: Complete Case Analysis (dropping missing values)
- **<span style="color:orange">D36</span>**: Imputing numerical data
- **<span style="color:orange">D37</span>**: Handling missing categorical data
- **<span style="color:orange">D38</span>**: Imputation for both numerical and categorical data
  - Random Sample Imputation (works for both numerical and categorical features)
  - Missing Indicator
  - Automatic imputation selection using **GridSearchCV**

#### 3.7.2 Multivariate Missing Value Methods

- **<span style="color:orange">D39</span>**: KNN Imputation
- **<span style="color:orange">D40</span>**: Iterative Imputation

### 3.8 Outlier Detection and Handling

- **<span style="color:orange">D41</span>**: Outlier Theory
- **<span style="color:orange">D42</span>**: Outlier detection and removal using Z-score
- **<span style="color:orange">D43</span>**: Outlier detection and removal using IQR
- **<span style="color:orange">D44</span>**: Outlier detection and removal using Percentile Capping

---

With Outlier Detection completed, the **Feature Transformation** part is now complete.

## 4. Next Part of Feature Engineering

### 4.1 Feature Construction and Feature Splitting

- **<span style="color:orange">D45</span>**: Feature Construction and Feature Splitting
  - Feature Construction: creating new features from existing ones manually (e.g., combining date features into a single datetime feature)
  - Feature Splitting: breaking down complex features into simpler components (e.g., splitting a datetime feature into year, month, day, etc.)

### 4.2 Progress Status

Feature construction and feature splitting are done.

Now Feature Selection and Feature Extraction are left to be covered in the next part of this journey, which is based on Curse of Dimensionality.

Feature Selection will be covered later after ML models, because it is often model-dependent.

## 5. Curse of Dimensionality and Feature Extraction

- **<span style="color:orange">D46</span>**: Curse of Dimensionality
- **<span style="color:orange">D47</span>**: Feature Extraction using PCA

## 6. Machine Learning Alogorithms

- **<span style="color:orange">D48</span>**: Simple Linear Regression
- **<span style="color:orange">D49</span>**: Regression Metrics
- **<span style="color:orange">D50</span>**: Multiple Linear Regression
- **<span style="color:orange">D50.2</span>**: Assumptions of Linear Regression
- **<span style="color:orange">D51</span>**: Gradient Descent
- **<span style="color:orange">D52</span>**: Types of Gradient Descent
  - Batch Gradient Descent
  - Stochastic Gradient Descent
  - Mini-batch Gradient Descent
- **<span style="color:orange">D53</span>**: Polynomial Regression
- **<span style="color:orange">D54</span>**: Bias-Variance Tradeoff


