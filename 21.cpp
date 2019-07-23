#include <iostream>
#include <stdexcept>
#include <stdlib.h> // Or #include <bits/stdc++.h>

using namespace std;

int main(){

    int num1,num2,current,answer = 0; // numbers of algorithms,algorithms for delete, variable for build the answer and answer
    int i,j,h; //variables for
    int p = 0, pp; //variables of mark
    char number[num1],now[num1-num2]; //store of the number and variable

    while(true){
        try{
            cin >> num1 >> num2;
            cin >> number;
            for(i=0; i<num1; i++){ //catch the first number for now
                p++; //mark the next numbers
                now[0] = number[i]; //store the first number of now
                for(j=p; j<num1; j++){ //prepare for the hunt, j always starting for the position 1(now[1])
                    try{
                        pp = 1; //store the numbers in now from position 1(now[1]) and reset for each try
                        for(h=j; h<j+(num1-num2-1); h++){ //start the hunt, h<j+(num1-num2-1) mark the limite of algorithms conted
                            now[pp] = number[h];
                            pp++; //next position
                        }
                        current = atoi(now); //convert in int
                        if (current > answer){
                            answer = current; //comparison in order to get answer
                        }
                    }catch(exception& index){
                        break; //avoid index errors
                    }
                }
            }
            cout << answer << "\n";
        }catch(exception& error){
            break; //for the program end
        }
    }
    return 0;
}
