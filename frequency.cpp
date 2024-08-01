#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <cctype>
using namespace std;

void toLowercase(string &str) {
    transform(str.begin(), str.end(), str.begin(), [](unsigned char c) { return tolower(c); });
}


int main()
{
    string paragraph;
    map<string, int> wordCount;
    cout << "Enter a paragraph:\n";
    getline(cin, paragraph);

    toLowercase(paragraph);

    istringstream stream(paragraph);
    string word;
    while (stream >> word) {
        word.erase(remove_if(word.begin(), word.end(), [](unsigned char c) { return ispunct(c); }), word.end());
        if (!word.empty()) {
            wordCount[word]++;
        }
    }

    cout << "Word Frequencies:\n";
    for (const auto &pair : wordCount) {
        cout << pair.first << ": " << pair.second << '\n';
    }

    return 0;
}
