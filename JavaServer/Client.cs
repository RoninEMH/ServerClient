using System;
using System.IO;
using System.Net.Sockets;
using System.Text;

namespace client {
    public class Client {
        public static void Main (string[] args) {
            Console.WriteLine ("Hello world");
            //Console.ReadKey();

            try {
                byte[] myReadBuffer = new byte[1024];
                StringBuilder myCompleteMessage = new StringBuilder ();

                TcpClient client = new TcpClient ("127.0.0.1", 5434);
                NetworkStream stream = client.GetStream ();
                int numberOfBytesRead = stream.Read (myReadBuffer, 0, myReadBuffer.Length);
                myCompleteMessage.AppendFormat ("{0}", Encoding.ASCII.GetString (myReadBuffer, 0, numberOfBytesRead));
                Console.WriteLine (myCompleteMessage);
                byte[] myWriteBuffer = Encoding.ASCII.GetBytes ("Are you receiving this message?");
                stream.Write (myWriteBuffer, 0, myWriteBuffer.Length);
                stream.Close ();
                client.Close ();
            } catch (Exception e) {
                Console.WriteLine ("ERROR");
            }
        }
    }
}