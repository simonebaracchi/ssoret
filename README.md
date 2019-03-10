# ssoret

Command-line tool similar to 'sort', but sorts by sentence similarity

Currently using the Spaghetti Distance algorithm to compute sentence similarity (see https://github.com/simonebaracchi/SpaghettiDistance)

Currently using an algorithm similar to A* to compute the best "path" to go through all input sentences and order them by similarity. In addition to A*, the algorithm will also search for the best sentence to start from. The total computational cost is O(n^2).

# Example

Feed it some tweets:

`cat tweets.txt | ./ssoret.py`

it will produce a response where each tweet has a high similarity with the previous and following tweet.

