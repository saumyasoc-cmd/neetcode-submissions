class Solution {
public:
    string mergeAlternately(string w1, string w2) {
        int i=0;
        int j=0;
        int s1=w1.size();
        int s2=w2.size();
        string res="";
        while(i<s1 and j<s2)
        {
            res+=w1[i];
            res+=w2[j];
            i++;
            j++;
        }
        if(i<s1)
        {
            res+=w1.substr(i);
        }
        if(j<s2)res+=w2.substr(j);
        return res;
    }
};