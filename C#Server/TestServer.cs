using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace TestServer {
    public class TestServer {
        public static void Main (string[] args) {
            byte[] myReadBuffer = new byte[1024];
            StringBuilder myCompleteMessage = new StringBuilder ();

            try {
                IPAddress IP = IPAddress.Parse ("127.0.0.1");
                TcpListener server = new TcpListener (IP, 5434);
                Console.WriteLine ("Server online...");
                server.Start ();
                TcpClient client = server.AcceptTcpClient ();
                NetworkStream stream = client.GetStream ();
                int numberOfBytesRead = stream.Read (myReadBuffer, 0, myReadBuffer.Length);
                myCompleteMessage.AppendFormat ("{0}", Encoding.ASCII.GetString (myReadBuffer, 0, numberOfBytesRead));
                Console.WriteLine (myCompleteMessage);
                byte[] myWriteBuffer = Encoding.ASCII.GetBytes ("Are you receiving this message?");
                stream.Write (myWriteBuffer, 0, myWriteBuffer.Length);

                stream.Close ();
                server.Stop ();
                client.Close ();
            } catch (Exception e) {
                Console.WriteLine (e.ToString ());
            }
            Console.ReadKey ();
        }
    }
}