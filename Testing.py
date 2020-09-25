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