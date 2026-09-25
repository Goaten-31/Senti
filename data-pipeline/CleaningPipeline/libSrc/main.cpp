#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>


#define TITLED_REV "../../datasets/silverData/titledReviews.txt"
#define UNTITLED_REV "../../datasets/goldData/untitledReviews.txt"

#define TITLED_SCORE "../../datasets/silverData/titledScoresPrices.txt"
#define UNTITLED_SOCRE "../../datasets/goldData/untitledScoresPrices.csv"


class Loc_lib{
    public:
        void remove_titles(int choice){
            std::ifstream infile;
            std::ofstream outfile;
            std::string line;

            switch (choice) {
                case 1:
                    infile.open(TITLED_REV);
                    outfile.open(UNTITLED_REV);
                break;
                
                case 2:
                    infile.open(TITLED_SCORE);
                    outfile.open(UNTITLED_SOCRE);
                break;    

                default:
                    std::cout << "This option doesn't exist.";

            }
            
            while (std::getline(infile, line)) {
                outfile << line.substr(line.find(':') + 2) << "\n";
            }
        
            infile.close();
            outfile.close();
        }

        void add_commas(int choice, int reset_index){
            std::ifstream infile;
            std::ofstream outfile;
            std::string line;
            unsigned short int counter = 1;

            switch (choice) {
                case 1:
                    infile.open(TITLED_REV);
                    outfile.open(UNTITLED_REV);
                break;
                
                case 2:
                    infile.open(TITLED_SCORE);
                    outfile.open(UNTITLED_SOCRE);
                break;
                
                default:
                    std::cout << "This option doesn't exist";
                break;
            }
            
            while (std::getline(infile, line)) {
                if(counter == reset_index){
                    line = line.replace(line.end(), line.end(), 1, ',') + '\n';
                    counter = 1;
                } else {
                    line = line.replace(line.end(), line.end(), 1, ',');
                    counter ++;
                }
                
                outfile << line;
            }   
            
            infile.close();
            outfile.close();
            
        }
        };

extern "C" {
    Loc_lib* Loc_new(){ return new Loc_lib();}
    void remove_titles_function(Loc_lib* loc_lib, int choice){ loc_lib -> remove_titles(choice); }
    void add_commas_function(Loc_lib* loc_lib, int choice, int reset_index){ loc_lib -> add_commas(choice, reset_index); }
}