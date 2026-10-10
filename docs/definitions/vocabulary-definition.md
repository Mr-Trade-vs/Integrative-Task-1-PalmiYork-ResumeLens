## Vocabulary Definition in ResumeLens

We know **ResumeLens** can get a set of symbols from input user. Under *Integrative-Task-1* context,  we can define:

$$\Sigma =  U $$

**U** : Set of Unicode characters

If user give us any input, must be:

$$x \in \Sigma^*$$

Where **$x$** is the raw resume represented as a string

**Valid User Input Example**

**Mary Jane Watson**

2 years of experience developing predictive models and data-processing pipelines.

**Technical Skills:**

Python, Pandas, NumPy, Scikit-learn, TensorFlow, SQL, Git.

With this definition, we aren't validating that resume, only say that is a finite sequence of characters.

First, we'll use **Regex** to start extracting text values that match our patterns