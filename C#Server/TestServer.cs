using System;
using System.Net.Sockets;
using System.Text;
using System.IO;

namespace TestServer
{
    public class TestServer
    {
        public static void Main(string[] args)
        {
            Int32 port = 5434;
            IPAddress localAddr = IPAddress.Parse("127.0.0.1");
            TcpListener server = new TcpListener(localAddr, port);
            
        }
    }
}