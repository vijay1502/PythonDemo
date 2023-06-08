def Example():
    a=5;
    b=0;
    try:
        print(a/b);
        return a/b;
    except ZeroDivisionError as e:
        print("Cannot divide by zero:" , e)
    except FileNotFoundError as f:
        print("This is file error",f)
    except ValueError as v:
        print("Value error:",v)
    finally:
        print( "I am still in final")
    print("This is sure")

Example();
