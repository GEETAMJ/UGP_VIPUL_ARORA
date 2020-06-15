This file contains alll the steps required to run the Extractive Summarizer

The tweets required have been already fetched using twitter API  using fetch.py

Step 1:- Install the Tweebo parser (https://github.com/ikekonglp/TweeboParser)
      1) git clone https://github.com/ikekonglp/TweeboParser.git
      2) cd TweeboParser
      3) ./install.sh

Step 2:- install all the dependency packages if not already installed
"pip3 install packagename"
itertools , aspell , numpy , textblob , gzip , networkx , codecs , sklearn , pylab .

Step3:- Install GurobiPy , its a commertial software which requires a local , easy to obtain liscence to run .
https://www.gurobi.com/free-trial/

Now , everything is ready
------>
To test the summarizer on the tweets , do the following steps :-

1) python3 tweet_concept_extraction.py expt/tweets.txt place/nepal_place.txt infrastructure_concept.txt
 This step takes the original bunch of tweets from expt/tweets.txt and does POS tagging on them , and applies other preprocessing procedure .
 The content after this step is stored in infrastructure_concept.txt
 
2) python3 NCOWTS.py infrastructure_concept.txt place/nepal_place.txt infrastructure 20150425 1000
 This step applies the summarization procedure on the file of tweets infrastructure_concept.txt and produces the summary of 1000 words length(summary length is changeable)
 The final summary after this step is stored in infrastructure_ICOWTS_20150425.txt
 
------>
To test the summarizer on a story , do the following steps

1) enter your story in story.txt

2) python3 generator.py story.txt sentence.txt
 This step breaks down the story and stores the sentences in sentence.txt , this will be worked upon

3) python3 tweet_concept_extraction.py sentence.txt place/nepal_place.txt infrastructure_concept.txt
 This step takes the original bunch of sentences from sentence.txt and does POS tagging on them , and applies other preprocessing procedure .
 The content after this step is stored in infrastructure_concept.txt
 
4) python3 NCOWTS.py infrastructure_concept.txt place/nepal_place.txt infrastructure 20150425 200
 This step applies the summarization procedure on the file of sentences infrastructure_concept.txt and produces the summary of 200 words length(summary length is changeable)
 The final summary after this step is stored in infrastructure_ICOWTS_20150425.txt
 
 
------->
A demo for the results has already been prepared by me(on my machine) in the demo folder:-
1:- tweets.txt is the original file containing the tweets and infrastructure_ICOWTS.txt is the final summary of 1000 word length
2:- story.txt is the original file containing the story and summary.txt is the final 200 word summary of the story .
