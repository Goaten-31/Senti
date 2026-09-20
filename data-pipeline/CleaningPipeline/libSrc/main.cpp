#include <fstream>

class Loc_lib{
    public:
        void remove_titles(){
            std::ifstream infile;
            std::ofstream outfile;
            std::string line;
        
            infile.open("..\\..\\datasets\\silverData\\titledReviews.txt");
            outfile.open("..\\..\\datasets\\silverData\\untitledReviews.txt");
            
            while (std::getline(infile, line)) {
                outfile << line.substr(line.find(':') + 1) << "\n";
            }
        
            infile.close();
            outfile.close();
        }
        
        };

extern "C" {
    Loc_lib* Loc_new(){ return new Loc_lib();}
    void Loc_lib_function(Loc_lib* loc_lib){ loc_lib -> remove_titles(); }
}