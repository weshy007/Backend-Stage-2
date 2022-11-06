### Task Description
Using the same server setup from stage one

Create an (POST) api endoint that takes the following sample json: <br>
```python
{ “operation_type”: Enum <addition | subtraction | multiplication> , 
    “x”: Integer, 
    “y”: Integer 
}
```
Operation can either be addition, subtraction or mutiplication <br>
x can be a number and Integer datatype <br>
y can be a number and Integer datatype <br>
Based on the operation sent, perform a simple arithmetic operation on x and y
Return a response with the result of the operation and your slack username
{ “slackUsername”: String, “result”: Integer } <br>
Push to GitHub
Sample Input { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer } <br>e
Sample Response Format { “result”: Integer, “operation_type”: Enum.value }