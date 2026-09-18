#include <iostream>
#include <fstream>
#include <string>

typedef std::string string;

class Loc_lib{
    public:
        void remove_title(string input_file_path, string output_file_path){
            std::ifstream infile;
            std::ofstream outfile;
            string line;
        
            infile.open(input_file_path);
            outfile.open(output_file_path);
            
            while (std::getline(infile, line)) {
                outfile << line.substr(line.find(':') + 1) << "\n";
            }
        
            infile.close();
            outfile.close();
        }

        int get_sixth_comma(string text){
            int num_of_comma = 0;
            int index = 0;
            
            for(index = 0; index <= text.length(); ++index){
                if(text[index] == ','){
                    num_of_comma ++;
                }
                if (num_of_comma == 6) {
                    break;
                }
            }
        
            return index;
        }

        string replace_commas(string text, int index){
            for(int i = index; i <= text.length(); ++i){
                if(text[i] == ','){
                    text[i] = '\0';
                }
            }
            return text;
        }

        void remove_commas(string input_file_path, string output_file_path){
            std::ifstream infile;
            std::ofstream outfile;
            string line;

            infile.open(input_file_path);
            outfile.open(output_file_path);

            while (std::getline(infile, line)) {
                int index = get_sixth_comma(line);
                outfile << replace_commas(line,index);   
            }

            infile.close();
            outfile.close();
        }

        string remove_spaces(string line){
            int j = 0;
            for(int i = 0; i < line.length(); ++i){
                if (line[i] != ' ') {
                    line[j++] = line[i];
                }
            }
            line[j] = '\0';
            return line;
        }

        void remove_newlines(){
            std::ifstream infile;
            std::ofstream outfile;
            string line;

            while (std::getline(infile, line)) {
                if () {
                
                }
            }
        }
        
        };

extern "C" {
    void remove_header(const char* input_file_path, const char* output_file_path){
        return remove_header(input_file_path, output_file_path);
    }

    void remove_commas(const char* input_file_path, const char* output_file_path){
        return remove_commas(input_file_path, output_file_path);
    }
}