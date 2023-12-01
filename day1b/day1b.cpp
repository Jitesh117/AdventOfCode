#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

#define nline  "\n"
#define pb push_back
#define PI 3.141592653589793238462

bool isprime(int x)
{
    long long n = INT_MAX;
    vector<int> v(n + 1, 1);
    for (int i = 2; i <= n; i++)
    {
        if (v[i])
            continue;
        for (int j = i * 2; j <= n; j += i)
        {
            v[j] = 0;
        }
    }
    return v[x];
}

vector<int> factor(int n)
{
    vector<int> f;
    for (int x = 2; x * x <= n; x++)
    {
        while (n % x == 0)
        {
            f.push_back(x);
            n /= x;
        }
    }
    if (n > 2)
        f.push_back(n);
    return f;
}

ll gcd(ll a, ll b)
{
    if (b > a)
    {
        return gcd(b, a);
    }
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}
int modpow(int x, int n, int m)
{
    if (n == 0)
        return 1 % m;
    long long u = modpow(x, n / 2, m);
    u = (u * u) % m;
    if (n % 2 == 1)
        u = (u * x) % m;
    return u;
}
int max(int a, int b, int c)
{
    return max(a, max(b, c));
}
int min(int a, int b, int c)
{
    return min(a, min(b, c));
}
ll max(ll a, ll b, ll c){
    return max(a, max(b, c));
}
ll min(ll a, ll b, ll c){
    return min(a, min(b, c));
}

void solve()
{
    vector<string> file;
    string line;
    while (getline(cin, line)){
        if (line.empty())
            break;
        file.push_back(line);
    }
    int result = 0;
    unordered_map<string, int> numbers = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9},
        {"zero", 0},
    };
    for(string line : file){
        int n = line.size();
        int i = 0, j = n - 1;
        string first, last;
        bool found_first = false, found_last = false;
        while(i < n){
            if(found_first)
                break;
            if(line[i] < 65){
                first = line[i];
                found_first = true;
                break;
            }
            else{
                for(auto it: numbers){
                    if(i  + it.first.size() - 1 <= n and line.substr(i,it.first.size()) == it.first){
                        first = to_string(it.second);
                        found_first = true;
                        break;
                    }
                }
            }
            i++;
        }
        while(j >= 0){
            if(found_last)
                break;
            if(line[j] < 65){
                last = line[j];
                found_last = true;
                break;
            }
            else{
                for(auto it: numbers){
                    if(j >= it.first.size() - 1 and line.substr(j - it.first.size() + 1, it.first.size()) == it.first){
                        last = to_string(it.second);
                        found_last = true;
                        break;
                    }
                }
            }
            j--;
        }
        // cout << first + last << nline;
        result += stoi(first + last);
    }
    cout << result << nline;
}

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());

    solve();
    return 0;
}