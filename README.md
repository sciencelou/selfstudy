# Selfstudy
Design, execute and evaluate a blinded self-study.

## Why?
If you want to know if some some treatment has the effect that you want, you can do a self-study.
For example, if you think that caffeine might be responsible for your headaches, take some caffeine pills and some sham-condition pills like multivitamin pills, and compare the effects.
You might get placebo effects if you know which pill you took, so you can blind yourself. That's what the label generator is for: you label paper bags with the pills inside, and swallow them without seeing them. Then you only record the label, and only check what the label meant in the end.
Also, you might want to settle for some statistical critera before seing the results, thats what the `evaluation.py` script is for. Otherwise you might bias yourself in the direction of your hypothesis (confirmation bias).
This approach is optimized for sticking close to reality. If, on the other hand, your goal is to get a paper with p<0.05 published, don't use it.
I will explain the details with an example I want to do myself, finding out if thenanine+caffeine is better than caffeine alone.

## Labeling
* I will use ~125 mg theanine (=1/4 pill of 500 mg) and ~50 mg caffeine (1/4 pill of 200 mg) as the test case.
* The control case will be ~50 mg caffeine together with a multivitamin pill.
* The multivitamin pill keeps me from easily recognizing the control case.
* In both cases, the pills will be packaged in a (opaque) labelled paper bag.
* I label the test case with prime numbers, and the control case with
odd non-prime numbers
* I will generate 20 data points for starters, thus 10 of each case.

## Data aquisition
I will fill in a questionnaire after taking a pill, it should be short and contain only questions with a high expected value for distinguishing between hypothesses.
* Questionnaires should be filled in at ingestion time, and 30 min afterwards.
Theanine can take up to 2h to reach maximum level, so a 1h and 2h repetition maight be good.
* Do not take multiple sets at once or change dosage during the experiment.
* Don't drink caffeinated or sugary drinks between taking the pill and filling in questionnaires unless you repeat that every time. This would probably increase noise, making more data points necessary.
* In gereneral, try to do similar things between taking the drugs and answering the questionnaires. Focused desk work should be a good activity

### Choosing your Question(s)
The questions you ask have a stupendously big influence on what you will learn.
More questions mean more effort/cost, but also increase the chance of acutally finding an interesting effect. There are some effects of theanine in the literature:
* Improved memory
* Enhanced focus
* Increased motivation
* Boosted mood
* Reduced anxiety

These are only tested for groups of people, so I don't know if they apply to me presonally. So I created a google form that I fill in when taking the pills, 30, 60 and 90 minutes afterwards.
The goal of the questions is to track the hypotheses as closely as possible, and are probably not optimal.
Also, the times where I answer the questions is rather random. After 30 min, caffeine concentration should peak, and theanine concentration after 1h-2h. If I see interesting temporal effects, I will just run a follow-up experiment with different parameters.
Also, I don't see any obvious and cheap way to test the 'improved memory' hypothesis, so I will skip this in my first trial.

Questionnaire is at [Google Forms](https://goo.gl/forms/VK3WTDPohuMlRkbz1).

## Hypothesis Testing
The questions and the timing constrain the meaningful hypotheses I can test.
Simple hypotheses are:
 

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


## Choosing your question

## Data collection

## Evaluation
