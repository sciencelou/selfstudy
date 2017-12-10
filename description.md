# Single-Participant Theanine Effects

This is an experiment designed to test hypotheses of theanine effects on a single person.

## Labeling
Theanine and control pills are labeled in a pseudo-blind way.
The simplest way is to print prime numbers for theanine and non-prime numbers for control pills.
* I will use ~125 mg theanine (=1/4 pill of 500 mg) and ~50 mg caffeine (1/4 pill of 200 mg) as the test case
* the control case will be ~50 mg caffeine together with a multivitamin pill
* in both cases, the pills will be packaged in a (opaque) labelled paper bag

## Data aquisition
I will fill in a questionnaire after taking a pill, it should be short and contain only questions with a high expected value for distinguishing between hypothesses.
*Questionnaires should be filled in at ingestion time, and 30 min afterwards.
Theanine can take up to 2h to reach maximum level, so a 1h and 2h repetition maight be good.
* Do not take multiple sets at once or change dosage during the experiment.
* Don't drink caffeinated or sugary drinks between taking the pill and filling in questionnaires unless you repeat that every time. This would probably increase noise, making more data points necessary.
* In gereneral, try to do similar things between taking the drugs and answering the questionnaires. Focused desk work should be a good activity

### Questions
* Narrowness of focus/attention
* Motivation
* Stress/Anxiety
* Calmness?
* Mood

## Hypotheses
* Improved memory
* Enhanced focus
* Increased motivation
* Boosted mood
* Reduced anxiety

## Open Problems
### Hypothesis Formalization
Effects are (discrete?) Gaussians around mean, mean&var change due to drugs?
### Model specification
* Bayesian Parameter Estimation with pymc3
### Data Pipeline
* Data in csv sheet
* Google questionnaire
* Handwritten
* Alarms for timing, syc with pomos
