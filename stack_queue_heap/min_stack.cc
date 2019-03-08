#include <stack>

class MinStack
{
  private:
    std::stack<int> _data;
    std::stack<int> _help;

  public:
    /** initialize your data structure here. */
    MinStack()
    {
    }

    void push(int x)
    {
        if (_data.empty() || x < _help.top()){
            _help.push(x);
        }
        else{
             _help.push(_help.top());
        }
        _data.push(x);
    }

    void pop()
    {
        _data.pop();
        _help.pop();
    }

    int top()
    {
        return _data.top();
    }

    int getMin()
    {
        return _help.top();
    }
};
