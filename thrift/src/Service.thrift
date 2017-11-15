namespace cpp example
namespace csharp example
namespace java example
namespace py example

include "Tools.thrift"

service ProcessorService
{
  Tools.A process(1: Tools.B b);
}
