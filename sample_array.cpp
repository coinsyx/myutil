#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <stdlib.h>
#include <time.h>
using namespace std;


ostream& operator<<(ostream& out, vector<int>& v)
{
    for(auto &x : v)  
       out << x << " ";
    return out;
}

/* 从一个数组中不重复采样出n个数 */
void random_sample(vector<int>& vec, int n)
{
    size_t vec_size = vec.size();
    for (int i=0; i<n; i++)
    {   
        size_t len = vec_size - i;
        int rand_idx = static_cast<int>(random() / static_cast<double>(RAND_MAX) * len);
    
        int tmp = vec[rand_idx];
        vec[rand_idx] = vec[len-1];
        vec[len-1] = tmp;
    }   
}

int main()
{
    srand(time(NULL));
    vector<int> vec{1,2,3,4,5,6,7,8,9,10};
    random_sample(vec, 3); 
    cout<<vec<<endl;
    return 0;
}
