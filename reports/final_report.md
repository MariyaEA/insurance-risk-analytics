# End-to-End Insurance Risk Analytics & Predictive Modeling

## Executive Summary

This project analyzed historical auto-insurance data for AlphaCare Insurance Solutions (ACIS) to identify key risk drivers, improve pricing strategies, and support data-driven marketing decisions.

The analysis combined exploratory data analysis, statistical hypothesis testing, and predictive modeling to uncover geographic, demographic, and vehicle-related insurance risk patterns. Machine learning models including Linear Regression, Random Forest, and XGBoost were developed to predict claim severity and support a risk-based pricing framework.

The results demonstrate that insurance risk varies across customer and geographic segments, and predictive modeling can provide measurable support for portfolio profitability optimization.

---

# 1. Business Problem

AlphaCare Insurance Solutions (ACIS) aims to expand competitively within the South African auto-insurance market while maintaining portfolio profitability.

Traditional pricing approaches often fail to fully capture differences in customer risk exposure. As a result, ACIS seeks to adopt analytics-driven pricing and segmentation strategies based on historical insurance claims data.

The project objectives include:

- Identifying low-risk customer segments
- Understanding drivers of insurance losses
- Statistically validating regional and demographic risk differences
- Developing predictive models for claim severity
- Supporting explainable and risk-based pricing decisions

---

# 2. Dataset Overview

The dataset contains historical insurance policy and claims data covering:

- Customer demographics
- Vehicle characteristics
- Geographic information
- Insurance plan details
- Premium and claim information

Key business metrics derived during analysis include:

## Loss Ratio

```python
LossRatio = TotalClaims / TotalPremium
```

Measures insurance portfolio profitability and risk exposure.

## Margin

```python
Margin = TotalPremium - TotalClaims
```

Measures per-policy profitability contribution.

---

# 3. Exploratory Data Analysis

## Data Quality Assessment

The dataset was assessed for:

- Missing values
- Data types
- Duplicate records
- Outliers
- Distributional characteristics

Missing numerical values were handled using median imputation, while categorical variables were filled using an `"Unknown"` category.

## Financial Distributions

Key financial variables including:

- TotalPremium
- TotalClaims
- CustomValueEstimate

showed significant skewness and the presence of extreme outliers, which is common in insurance claims data.

## Geographic Trends

Province-level analysis revealed substantial variation in:

- Loss ratio
- Premium volume
- Claim severity

Some provinces demonstrated considerably higher risk exposure compared to others.

## Vehicle Risk Profiles

Certain vehicle makes and models exhibited consistently higher average claim severity, suggesting strong associations between vehicle characteristics and insurance risk.

## Temporal Trends

Monthly claim analysis indicated fluctuations in claim frequency and severity across the observation period, suggesting possible seasonality or operational influences.

---

# 4. Hypothesis Testing Results

Four business hypotheses were evaluated using statistical testing.

## Hypothesis 1 — Risk Differences Across Provinces

A chi-square test was used to evaluate claim frequency differences between provinces.

The results indicated statistically significant regional differences in insurance risk exposure.

## Hypothesis 2 — Risk Differences Between Postal Codes

Claim frequency differences across postal codes were evaluated using chi-square testing.

The analysis demonstrated that geographic micro-regions influence insurance risk.

## Hypothesis 3 — Margin Differences Between Postal Codes

Welch’s t-test was applied to compare profitability margins between postal code groups.

The findings showed meaningful profitability variation across regions.

## Hypothesis 4 — Gender-Based Risk Differences

Gender-based claim frequency differences were evaluated using chi-square testing.

The results suggested that gender alone is not a sufficiently strong standalone pricing factor compared to geographic and vehicle-related variables.

---

# 5. Predictive Modeling

## Modeling Objective

The primary modeling objective was to predict claim severity for policies with recorded claims.

Target variable:

```python
TotalClaims
```

## Models Implemented

Three regression models were developed:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

## Model Evaluation

Models were evaluated using:

- RMSE (Root Mean Squared Error)
- R² (Coefficient of Determination)

XGBoost achieved the strongest predictive performance among the evaluated models.

---

# 6. SHAP Interpretability Findings

SHAP analysis was applied to improve model interpretability and identify the most influential risk drivers.

The most important predictive factors included:

- Vehicle value
- Vehicle type
- Geographic region
- Vehicle age
- Vehicle make/model

The interpretability analysis provides transparency into how different variables influence claim severity predictions and supports explainable underwriting decisions.

---

# 7. Risk-Based Pricing Recommendations

Based on the analytical findings, the following recommendations are proposed for ACIS:

## Geographic Pricing Adjustments

Implement province-level and postal-code-level premium adjustments for high-risk regions.

## Vehicle-Based Risk Segmentation

Introduce pricing differentiation for high-risk vehicle categories and models.

## Low-Risk Customer Targeting

Develop marketing campaigns targeting profitable and low-loss customer segments.

## Explainable Pricing

Incorporate SHAP-based interpretability outputs into underwriting workflows to improve transparency and support regulatory compliance.

---

# 8. Limitations

Several limitations should be acknowledged:

- Limited behavioral driver information
- Potential reporting inconsistencies in historical claims
- Absence of telematics and driving history data
- Possible imbalance in claims frequency across regions

These limitations may affect model generalizability.

---

# 9. Future Work

Future improvements may include:

- Incorporating telematics and driver behavior data
- Developing claim probability classification models
- Real-time premium adjustment systems
- Advanced ensemble and deep learning approaches
- Customer lifetime value modeling

---

# 10. Conclusion

This project demonstrates how data analytics and machine learning can support insurance pricing optimization and risk management.

The combination of exploratory analysis, statistical testing, predictive modeling, and interpretability techniques provides ACIS with a strong foundation for implementing evidence-driven pricing strategies and improving portfolio profitability.