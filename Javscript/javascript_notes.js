Javascript Functions


###

var in javascript creates a variables in current scope, if there is no var, then you create it in the global namespace

Window Object:

setTimeout(func, delay)
	-sets up function on a timer!


Regular Expressions
	-Two ways to define
		1) var x = new RegExp(pattern, modifiers);
		2) var x = /pattern/moddifers
		important modifiers =  g : find all matches rather than stopping after the first match
				       m: performs multi-matching
				       i: Perform -case-insenitive-matching

Methods:
	str.replace(pattern, '')
					


filter = returns called on Array Ojbects, can call a function to return a filter array
	arr = [1,2,,,,4,,,6,,8,,,9,,0,,3]
	arr.filter(function(){ return true});
	//[1,2,3,4,6,,8,9,0]
	

Asynchronous Events:
	When you execute something synchronously, you wait for it to finish before moving on to another task. 
	When you execute something asynchronously, you can move on to another task before it finishes.
	
	Ajax is asyncrhonous, this means if we waiting for a number of ajax calls to return, we must set up a type of counter 

