# Python Classes and Functions Tips

## Inner Functions
```python
# nested functions have access to outer variables
def outer(a,b):
    c = 'c'

    def inner():
        return a + b +c
    
    return inner()

print(outer('a', 'b')) #abc

# can modify objects but not reassign unless using 
# nonlocal keyword
def double(arr, val):
    def helper():
        # modifying array works
        for i, n in enumerate(arr):
            arr[i] *=2
        
        # will only modify val in the helper scope:
        val *= 2

        # need to use nonlocal keyword to modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums, val) # [2,4] 6
```

## Classes
```python
class Myclass:
    # constructor:
    def __init__(self, nums):
        

```