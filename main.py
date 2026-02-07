# hosam.alafandi@gmail.com
from analyzer import SalesAnalyser

def main():
    analyzer = SalesAnalyser()
    analyzer.load_data()
    analyzer.clean_data()
    analyzer.analytics()
    analyzer.create_visualizations()
    


if __name__ == "__main__":
    main()