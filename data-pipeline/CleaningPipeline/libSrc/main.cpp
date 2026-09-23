#include <fstream>
#include <string>
#include <algorithm>

class Loc_lib{
    public:
        void remove_titles(){
            std::ifstream infile;
            std::ofstream outfile;
            std::string line;
        
            infile.open("../../datasets/silverData/titledReviews.txt");
            outfile.open("../../datasets/silverData/untitledReviews.txt");
            
            while (std::getline(infile, line)) {
                outfile << line.substr(line.find(':') + 2) << "\n";
            }
        
            infile.close();
            outfile.close();
        }

        void add_commas(){
            std::ifstream infile;
            std::ofstream outfile;
            std::string line;
            unsigned short int counter = 1;
        
            infile.open("../../datasets/silverData/titledScoresPrices.txt");
            outfile.open("../../datasets/goldData/titledScoresPrices.csv");
            
            while (std::getline(infile, line)) {
                
                switch (counter) {
                    case 3:
                        line = line.replace(line.end(), line.end(), 1, ',') + '\n';
                        counter = 1;
                        break;
                    default:
                        line = line.replace(line.end(), line.end(), 1, ',');
                        counter ++;
                        break;
                        
                }
                
                outfile << line;
            }   
            
            infile.close();
            outfile.close();
            
        }
        };

extern "C" {
    Loc_lib* Loc_new(){ return new Loc_lib();}
    void remove_titles_function(Loc_lib* loc_lib){ loc_lib -> remove_titles(); }
    void add_commas_function(Loc_lib* loc_lib){ loc_lib -> add_commas(); }
}