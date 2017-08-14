# CodeFights - Password Strength

###Determine Password Strength based on repetition_factor and password_length

___

> ####Algorithm to evaluate Password Strength

> 1.  Calculate the number of unique characters in the password, and split them into the following groups:
> > * lowercase English letters
> > * uppercase English letters
> > * digits
> > * other characters

> 2. Next, store the repetition factor for each group using the formula  `  rep_factor = 1 - (1 - growth_factor) `^group_size^. The group_size is determined on the previous step, and the growth_factor for each group is given below (respectively):
> > * 0.25
> > * 0.4
> > * 0.4
> > * 0.5 

> 3. At this step, calculate the digit strength of the password using the formula ` (sum(repetition_factor * max_group_size)) `^password.length^. Here, the repetition_factor is the value found on the previous step, password.length is the size of the password, and max_group_size is the maximum size of the group as given below (respectively):
> > * 26
> > * 26
> > * 10
> > * 32

> 4. Finally, calculate the resulting strength as log2strength, where strength is the value obtained on the previous step.

> ____

> ####Example
> For password = "**abcc73?**", the output should be 
**passwordStrength(password) = 36.5832**.

> Here are the values obtained on each step:

> 1. For each group:
> > * `3`
> > * `0`
> > * `2`
> > * `1`

> 2. For each group:
> > * `0.578125`
> > * `0`
> > * `0.64`
> > * `0.5`

> 3. `102953309771.56915`

>  **`36.5832`** is the answer. 
