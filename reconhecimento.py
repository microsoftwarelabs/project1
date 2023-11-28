import sys
import inspect

def main():
    frame = inspect.currentframe()
    script_file = inspect.getsourcefile(frame)
    print(script_file)

if __name__ == "__main__":
    main()