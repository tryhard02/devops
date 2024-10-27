1. **Create a New Item using Freestyle Project in Jenkins**
2. **Go to Build Steps**
3. **Add a Build Step of Execute Python**
4. **Add the code below **

   ```python
      numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      squares_of_even = [n ** 2 for n in numbers if n % 2 == 0]
      print(squares_of_even)
    ```

5. **Save and Click on Build Now**
