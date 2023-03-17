# cybernetics-lab

The REST endpoint that accepts a numeric type and returns a truncated, "prettified" string version. The prettified version include one number after the decimal when the truncated number is not an integer. If should prettify numbers greater than 6 digits then it support millions, billions and trillions.

Examples:

● input: 500 output 500

● input: 3400 outputs 3.5k

● input: 1000000 output: 1M

● input: 2500000.34 output: 2.5M

● input: 1123456789 output: 1.1B

# To Setup Project

1) Install Python 3.7 Or Higher
2) Create virtual environment and then activate it.
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```
3) Install all dependencies cmd -
    ```sh
    python -m pip install -r requirements.txt
    ```
4) Finally run cmd - 
    ```sh
    python manage.py runserver
    ```
5) To run test cases run cmd - 
    ```sh
    python manage.py test
    ```
6) To test via url please visit that [url](http://127.0.0.1:8000/app/numbers/?q=1000000) change param value to "prettified" string version.
