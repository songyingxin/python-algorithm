#include <queue>

class MyStack
{
  public:
    std::queue<int> data;
    std::queue<int> help;
    /** Initialize your data structure here. */
    MyStack()
    {
    }

    /** Push element x onto stack. */
    void push(int x)
    {
        data.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop()
    {
        if (data.empty()){
            return -1;
        }

        while(data.size() > 1){
            help.push(data.front());
            data.pop();
        }

        int result = data.front();
        data.pop();
        std::swap(data, help);

        return result;
    }

    /** Get the top element. */
    int top()
    {
        if (data.empty())
        {
            return -1;
        }

        while (data.size() > 1)
        {
            help.push(data.front());
            data.pop();
        }

        int result = data.front();
        help.push(data.front());
        data.pop();
        std::swap(data, help);
        return result;
    }

    /** Returns whether the stack is empty. */
    bool empty()
    {
        return data.empty();
    }
};

class MyStack
{
  public:
    std::queue<int> data;
    std::queue<int> help;
    /** Initialize your data structure here. */
    MyStack()
    {
    }

    /** Push element x onto stack. */
    void push(int x)
    {
        help.push(x);
        while(!data.empty()){
            help.push(data.front());
            data.pop();
        }

        swap(data, help);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop()
    {
       int result = data.front();
       data.pop();
       return result;
    }

    /** Get the top element. */
    int top()
    {
       return data.front();
    }

    /** Returns whether the stack is empty. */
    bool empty()
    {
        return data.empty();
    }
};