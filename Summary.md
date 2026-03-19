## This File contains a Summary of learning of Classical ML

- **<span style="color:orange">D11 </span>**: Has all info about tensor
- **<span style="color:orange">D13</span>**: Shows how an end to end ML pipeline looks like
- **<span style="color:orange">D15 to D18</span>**: Different ways to collect data for training
    - From csv
    - JSON
    - API
    - Web Scraping 
- **<span style="color:orange">D19 to D22</span>**: How to analyse the collected data(EDA)
    - Bi-variate analysis
    - Multi-variate analysis
    - Pandas profiling

So avhi tk hum data ko apne paas laake basic level ka EDA karna seekh chuke hain.
- **<span style="color:orange">D23</span>**: Feature Engineering Intro
    1. Feature Transformation
        - Feature Scaling
        - Handling Categorical Features
        - Handling Missing Values
        - Outlier Detection and Handling
    2. Feature Construction
    3. Feature Selection
    4. Feature Extraction

- 1.1 Feature Scaling
    - **<span style="color:orange">D24</span>**: Standardization
    - **<span style="color:orange">D25</span>**: Normalization

- 1.2 Handling Categorical Features(How to encode categorical data)
    - **<span style="color:orange">D26</span>**: Ordinal Encoding & Label Encoding
    - **<span style="color:orange">D27</span>**: One Hot Encoding
- **D28**: Column Transformer to make the transformation process more efficient and easy to manage

- **<span style="color:orange">D29</span>**: Sklearn Pipelines

- **Mathematical Transformation of features**
    - **<span style="color:orange">D30</span>**: Function Transformer
        - Log Transformation
        - Reciprocal Transformation
        - Power Transformation
    - **<span style="color:orange">D31</span>**: Power Transformer
        - Box-Cox Transformation
        - Yeo-Johnson Transformation

## <span style="color:green">TIP</span>

- When you are working with an model - that rely on normally diributed data
- then check if the columns are normally distributed or not, if not then apply power transformation to make it normally distributed
- you can also apply function transformation to make the data normally distributed, but power transformation in general gives better results than function transformation. So, try both and see which one gives better results.

---

**<span style="color:orange">D32</span>**: Binning and Binarization (Encoding of numerical features)

---
**<span style="color:orange">D33</span>**: Handling mixed variables (numerical and categorical features in the same column)
**<span style="color:orange">D34</span>**: Handling date and time features

---

- 1.3 Handling Missing Values

    - 1.3.1 Univariate Analysis of Missing Values
        - **<span style="color:orange">D35</span>**: Complete Case Analysis (Dropping missing values)
        - **<span style="color:orange">D36</span>**: Imputing Numerical Data
        - **<span style="color:orange">D37</span>**: Handling Missing Categorical Data
        - **<span style="color:orange">D38</span>**: 
            - Random Sample Imputation (used for both numerical and categorical data)
            - Missing Indicator
            - Automatic Imputation with sklearn
            
    - 1.3.2 Multivariate Analysis of Missing Values


