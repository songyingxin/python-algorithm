#include <stack>

class MyQueue
{
  public:
    /** Initialize your data structure here. */
    std::stack<int> data;
    std::stack<int> help;
    MyQueue()
    {
    }

    /** Push element x to the back of queue. */
    void push(int x)
    {
        data.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop()
    {
        if(help.empty()){
            while(!data.empty()){
                help.push(data.top());
                data.pop();
            }
        }

        int result = help.top();
        help.pop();
        return result;
    }

    /** Get the front element. */
    int peek()
    {
        if (help.empty())
        {
            while (!data.empty())
            {
                help.push(data.top());
                data.pop();
            }
        }

        return help.top();
    }

    /** Returns whether the queue is empty. */
    bool empty()
    {
        if (help.empty() && data.empty()){
            return true;
        }
        return false;
    }
};

class MyQueue
{
  public:
    /** Initialize your data structure here. */
    std::stack<int> data;
    std::stack<int> help;
    MyQueue()
    {
    }

    /** Push element x to the back of queue. */
    void push(int x)
    {
        while(!data.empty()){
            help.push(data.top());
            data.pop();
        }

        help.push(x);

        while(!help.empty()){
            data.push(help.top());
            help.pop();
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop()
    {
        int result = data.top();
        data.pop();
        return result;
    }

    /** Get the front element. */
    int peek()
    {
        return data.top();
    }

    /** Returns whether the queue is empty. */
    bool empty()
    {
        if (data.empty())
        {
            return true;
        }
        return false;
    }
};