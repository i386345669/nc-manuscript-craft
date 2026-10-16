# Synthetic evaluation fixture: complete manuscript

This is invented teaching material, not a real study or a manuscript for submission. Write a complete English teaching manuscript of about 800–1,200 words using only the supplied evidence. Include a title, abstract, Introduction, complete Results, Discussion, Methods, a reference list, both figure legends and a brief Supplementary Methods section. Do not stop at an outline. Do not write Chinese, a cover letter, or generate figures. No browsing or new analysis is allowed in this evaluation. Save the text only to the evaluator's specified output file.

## Supplied study material

Question: how can inconsistent station identifiers and sampling labels be organized so seasonal water-quality observations can be compared at the same stations?

Study design: a descriptive observational resource. Four urban lake monitoring stations were scheduled once each month over one calendar year. There were 48 planned paired temperature/dissolved-oxygen records, four missing records and 44 complete records. Stations, not monthly observations, are the independent spatial units. The study did not perform interventions, causal identification, predictive validation, preregistration or cost-effectiveness analysis.

Construction: records were joined using stable station identifiers and a fixed sampling dictionary. Raw reported measurements were retained. The team checked units and date formats, marked missing records explicitly, and computed descriptive means from complete records without imputation. The calculations in the teaching study used NumPy 1.26.4. No inferential tests or confidence intervals were produced.

Result R-01: the resource contains four station histories and 44 complete monthly paired records, with the four missing slots retained as explicit missing entries.

Result R-02, supplied summary table S-02:

| Period | Planned records | Complete records | Missing records | Mean dissolved oxygen |
|---|---:|---:|---:|---:|
| June–August | 12 | 11 | 1 | 6.1 mg/L |
| Other months | 36 | 33 | 3 | 8.3 mg/L |

The supplied mean difference is −2.2 mg/L. No adjustment or statistical comparison was performed. Temperature, mixing and other factors were not separated as causal contributions.

Result R-03: a local interface retrieves each station's complete and missing slots and exports seasonally summarized observations. This is an implemented teaching prototype. It has no public repository DOI, live alerting deployment, clinical task or usability study.

Figure 1: a complete workflow schematic showing identifier harmonization, dictionary mapping, explicit missingness, station histories and export. It contains no measured effect estimate.

Figure 2: a two-bar descriptive display of the two supplied means, labeled with complete-record counts. No error bars, hypothesis-test marks or causal arrows are present.

Supplementary Methods should specify how stable identifiers, the sampling dictionary, complete-record means and missing slots are represented. Do not invent code, variable names, thresholds or dates not supplied.

Reference R1: Harris, C. R. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI 10.1038/s41586-020-2649-2. Its supplied role is attribution for the numerical software, not evidence for the water-quality findings. Metadata was checked against https://numpy.org/citing-numpy/ when this fixture was prepared. No other literature is supplied.

Use the one supplied reference where appropriate. Do not invent background sources. Clearly identify the document as a teaching draft and state actual unresolved publication items rather than claiming submission readiness.
