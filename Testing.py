# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:46:46 2020

@author: jonas
"""
from  spacingmodel_categoricalfacts import *
m = SpacingModel()

# Add some study facts to the model (you could also read them from a CSV file)
facts = [Fact(1, "hello", "bonjour", "other"),
		Fact(2, "dog", "chien", "animal"),
		Fact(3, "cat", "chat", "animal"),
		Fact(4, "computer", "ordinateur", "object"),
		Fact(5, "house", "maison", "object"),
		Fact(6, "car", "voiture", "object"),
		Fact(7, "fish", "poisson", "animal"),
		Fact(8, "bottle", "bouteille", "object")]

for fact in facts:
	m.add_fact(fact)
#%%
print(m.facts)
#%%
def estimate_category_alpha(fact):
     #facts = pd.DataFrame(m.facts)
     #facts_category = facts[facts["category"] == category]
     
     facts_category = [f for f in m.facts if f.category == fact.category]
     time = float(np.inf)
     x = np.mean([m.get_rate_of_forgetting(time, f) for f in facts_category])
     
     return(x)

ex_fact = m.facts[1]     
print(estimate_category_alpha(ex_fact))        
