1. **Create a New File of test.java and Run in it VS CODE to get BLUE TEXT**
   
   ```java
      public class test {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
   }
   ```
   
2. **Create a New Item using Freestyle Project in Jenkins**
3. **Go to Build Steps**
4. **Add a Build Step of Windows Command**
5. **Add the code below with updated path of BLUE TEXT**

    ```bash
   pushd `{BLUE TEXT}`
   javac test.java
   java test 
   ```

6. **Save and Click on Build Now**
