textcorpus.far: textcorpus.grm covid_symptoms.far
	thraxcompiler --input_grammar=$< --output_far=$@

covid_symptoms.far: covid_symptoms.grm example.far exclamation.far numbers.far chinesefirstnames.txt chineselastnames.txt symptom.txt businesses_and_places.txt dates.txt time.txt countries.txt roads_and_streets.txt venues-filtered.txt regions.txt
	thraxcompiler --input_grammar=$< --output_far=$@

example.far: example.grm byte.far numbers.far
	thraxcompiler --input_grammar=$< --output_far=$@

byte.far: byte.grm 
	thraxcompiler --input_grammar=$< --output_far=$@

numbers.far: numbers.grm byte.far
	thraxcompiler --input_grammar=$< --output_far=$@

exclamation.far: exclamation.grm 
	thraxcompiler --input_grammar=$< --output_far=$@

clean:
	rm -f covid_symptoms.far example.far exclamation.far numbers.far byte.far
