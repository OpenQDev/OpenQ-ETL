import extract
import transform
import extract

def main():
    # Call extract.py
    extract.extract_data()

    # Call transform.py
    transform.transform_data()

    # Call load.py
    extract.load_data()

if __name__ == "__main__":
    main()
