import logging

# Configure logging
logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

def calculate_division(a, b):
    try:
        logging.debug("Starting division operation.")

        result = a / b

        logging.info(f"Division successful: {a} / {b} = {result}")
        return result

    except ZeroDivisionError:
        logging.exception("Error occurred: Division by zero is not allowed.")

    except Exception:
        logging.exception("An unexpected error occurred.")

def main():
    logging.info("Application started.")

    try:
        num1 = 20
        num2 = 5

        logging.debug(f"Input values: num1={num1}, num2={num2}")

        result = calculate_division(num1, num2)
        print("Division Result:", result)

        # Test exception handling
        logging.info("Testing division by zero.")
        calculate_division(10, 0)

    except Exception:
        logging.exception("Error in main function.")

    finally:
        logging.info("Application execution completed.")

if __name__ == "__main__":
    main()