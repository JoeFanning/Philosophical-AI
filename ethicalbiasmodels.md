the IBM AI Fairness 360 (AIF360) toolkit uses all three of these metrics and many more. It's a comprehensive library designed to help users identify and mitigate various types of bias.
​Disparate Impact
​The toolkit includes a metric for disparate impact, which measures the ratio of favorable outcomes between an unprivileged and a privileged group. This metric is a key way to check for potential unintentional discrimination in a model's predictions.
​Equal Opportunity Difference
​AIF360 also features a metric called Equal Opportunity Difference. This metric is a more refined measure of fairness. It calculates the difference in the true positive rate between the privileged and unprivileged groups. This helps determine if qualified individuals from all groups are being selected at the same rate.
​Statistical Parity
​The toolkit uses the statistical parity difference metric, also known as the demographic parity difference. This metric compares the overall proportion of positive outcomes (e.g., getting a loan) between different groups. A value of zero indicates that the model is making positive predictions at the same rate for both groups.
