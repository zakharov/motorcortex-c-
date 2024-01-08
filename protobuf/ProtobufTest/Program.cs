
namespace ProtobufTest;
using Motorcortex;
class Program
{

    static void Main(string[] args)
    {
        // testing hash
        Console.WriteLine(Hash.Get<ConsoleCmdMsg>());
        Console.WriteLine(Hash.Get<Error>());
        Console.WriteLine(Hash.Get<ParameterMsg>());
    }
}
