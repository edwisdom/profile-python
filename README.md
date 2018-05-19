# Profiling Python Code

Recently, I implemented a network agent-based model of [political dynamics under conditions of resource shock](https://github.com/edwisdom/regime_model). The social scientist in me wanted to have a clean, non-laggy, interactive simulation amenable to visual interpretation; the data scientist in me wanted to run large parameter sweeps over the model to produce informative 3-D plots.

Both of these aspirations led me to one realization -- my code needs to be **fast**. Ordinarily, elegance and readability are more important than speed to me when coding in Python, as long as the algorithms are the right time complexity and the choice of data structures isn't absurd. However, this large-scale project forced me to think about smaller-scale speed improvements in Python.

Here are just a few things I learned about Python code and speed.

## Averaging Lists

I needed to take averages of lists of numbers fairly often in my simulation. These represented an agent's best guess about an environmental value, given their memory of prior revealed values. 

There are three easy ways of doing this:

### Native Sum/Len

The easiest method is just to use Python's native sum and divide by length.

```python
return sum(lst)/len(lst)
```

### Reduce for Sum

Instead of using Python's sum, use reduce to sum the list and divide by length.

```python
return reduce(lambda a, b: a+b, lst) / len(lst)
```

### Numpy Mean

Or just use Numpy's mean.

```python
import numpy as np

return np.mean(lst)
```

### Bonus: Statistics Mean

There's a statistics library in Python that we could use instead of Numpy.

```python
from statistics import mean

return mean(lst)
```

### Results

I didn't graph the statistics mean because it was so awfully slow that it obscured the difference between the other methods. Unsurprisingly, reduce didn't do too well because function calls are expensive in Python (see next section). Surprisingly, Numpy didn't fare better than native Python averaging, even for long lists. 

![alt-text](https://github.com/edwisdom/python-prof/blob/master/means.png)

This was because each Python list had to be broadcasted into a Numpy array. If we do this conversion before calling the mean function, Numpy is much faster as expected.

![alt-text](https://github.com/edwisdom/python-prof/blob/master/means2.png)


