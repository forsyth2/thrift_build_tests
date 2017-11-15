package example;

public class JavaServer implements example.ProcessorService.Iface
{

  public example.A process(example.B b) throws org.apache.thrift.TException
  {
    return new example.A();
  }

}
