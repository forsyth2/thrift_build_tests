using System;

namespace example
{
  public class Server : ProcessorService.ISync
  {
    public example.A process(example.B b)
    {
      return new example.A();
    }

    static int Main()
    {
      return 0;
    }
  }
}
