def Age_Guessing():
    anton : int = 21  
    beth : int = 6 + anton  
    chen : int = 20 + beth  
    drew  : int= chen + anton  
    ethan : int = chen  

   # This shows all the ages
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))



if __name__ == '__main__':
    Age_Guessing()

""" pseudocode for your Age Guessing program:
FUNCTION Age_Guessing():
    // Define ages of five people
    anton ← 21  
    beth ← 6 + anton  
    chen ← 20 + beth  
    drew ← chen + anton  
    ethan ← chen  

    // Display all the ages
    DISPLAY "Anton is ", anton
    DISPLAY "Beth is ", beth
    DISPLAY "Chen is ", chen
    DISPLAY "Drew is ", drew
    DISPLAY "Ethan is ", ethan
END FUNCTION

// Main program execution
IF main program is running THEN
    CALL Age_Guessing()
END IF
"""
