#include "../../thrift/gen-cpp/ProcessorService.h"

using namespace std;
using namespace example;

class Server : public ProcessorServiceIf
{
  public:
    Server() {}

    void process( ::example::A& _return, const  ::example::B& b)
    {

    }
};

int main()
{

}
